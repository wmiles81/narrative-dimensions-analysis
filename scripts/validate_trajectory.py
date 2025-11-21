#!/usr/bin/env python3
"""
Validate narrative trajectories for proper story progression.
"""

import json
import sys
from typing import Dict, List, Tuple, Optional

class TrajectoryValidator:
    def __init__(self, genre: str = "romance", subgenre: Optional[str] = None,
                 ending_type: Optional[str] = None):
        self.genre = genre
        self.subgenre = subgenre
        self.ending_type = ending_type  # 'HEA', 'HFN', 'tragic', 'bittersweet', etc.
        self.load_genre_requirements()
        self.load_ending_types()
        
    def load_genre_requirements(self):
        """Load genre-specific requirements."""
        # Default requirements - would load from genre-configs.json in practice
        self.requirements = {
            'romance': {
                'ending': {'intimacy': 8, 'trust': 7, 'goal_alignment': 8},
                'max_jump': 3,
                'min_dimensions_moving': 2
            },
            'dark-romance': {
                'ending': {'intimacy': 7, 'trust': 6, 'power_differential': (-2, 2)},
                'sustained': {'stakes': 5},
                'max_jump': 4
            },
            'thriller': {
                'sustained': {'danger': 7, 'stakes': 8},
                'max_jump': 4
            },
            'mystery': {
                'ending': {'info_asymmetry': 2},
                'progression': 'info_asymmetry_decreasing'
            }
        }

    def load_ending_types(self):
        """Load ending type definitions for different genres and outcomes."""
        self.ending_types = {
            'romance': {
                'HEA': {  # Happily Ever After
                    'intimacy': 8,
                    'trust': 7,
                    'goal_alignment': 8,
                    'description': 'Committed relationship, high intimacy and trust'
                },
                'HFN': {  # Happy For Now
                    'intimacy': 7,
                    'trust': 6,
                    'goal_alignment': 7,
                    'description': 'Together but not fully committed'
                },
                'tragic': {
                    'description': 'Intentional failure to unite',
                    'note': 'No minimum requirements - validates narrative justification for separation'
                },
                'bittersweet': {
                    'intimacy': (4, 7),
                    'trust': (4, 6),
                    'description': 'Together but with significant cost or limitation'
                }
            },
            'dark-romance': {
                'HEA': {
                    'intimacy': 7,
                    'trust': 6,
                    'power_differential': (-2, 2),
                    'description': 'Together with balanced power'
                },
                'HFN': {
                    'intimacy': 6,
                    'trust': 5,
                    'power_differential': (-3, 3),
                    'description': 'Together but power or trust issues remain'
                },
                'tragic': {
                    'description': 'Separation or death despite connection',
                    'note': 'Validates dark romance elements maintained throughout'
                },
                'dark_hea': {
                    'intimacy': 7,
                    'trust': 5,
                    'power_differential': (-4, -2),  # Intentional power imbalance
                    'description': 'Together in morally ambiguous dynamic'
                }
            },
            'mystery': {
                'solved': {
                    'info_asymmetry': (0, 2),
                    'description': 'Mystery fully resolved'
                },
                'noir_open': {
                    'info_asymmetry': (4, 6),
                    'moral_ambiguity': (6, 10),
                    'description': 'Some answers, but morally complex'
                },
                'unsolved': {
                    'info_asymmetry': (7, 10),
                    'acceptance': (7, 10),
                    'description': 'Intentionally unresolved, character accepts uncertainty'
                }
            },
            'thriller': {
                'victory': {
                    'danger': (0, 2),
                    'stakes': (0, 4),
                    'description': 'Threat eliminated, safety restored'
                },
                'pyrrhic_victory': {
                    'danger': (0, 3),
                    'stakes': (3, 6),
                    'description': 'Threat stopped but at great cost'
                },
                'ongoing_threat': {
                    'danger': (5, 8),
                    'acceptance': (7, 10),
                    'description': 'Threat remains, character adapts to new reality'
                }
            }
        }
    
    def validate_trajectory(self, trajectory: List[Dict]) -> Dict:
        """
        Validate a complete story trajectory.

        Args:
            trajectory: List of dimensional states in chronological order

        Returns:
            Validation report with passed/failed checks and issues
        """
        # Input validation
        if not isinstance(trajectory, list):
            raise TypeError(f"Trajectory must be a list, got {type(trajectory)}")

        if not trajectory:
            raise ValueError("Trajectory cannot be empty")

        for i, state in enumerate(trajectory):
            if not isinstance(state, dict):
                raise TypeError(f"State at index {i} must be a dict, got {type(state)}")

        report = {
            'valid': True,
            'checks': [],
            'warnings': [],
            'errors': []
        }

        # Check 1: Minimum trajectory length
        if len(trajectory) < 3:
            report['errors'].append("Trajectory too short for analysis")
            report['valid'] = False
            return report
        
        # Check 2: Jump validation (no teleportation)
        jump_check = self.check_jumps(trajectory)
        report['checks'].append(jump_check)
        if not jump_check['passed']:
            report['errors'].extend(jump_check['issues'])
            report['valid'] = False
        
        # Check 3: Movement validation (not stuck)
        movement_check = self.check_movement(trajectory)
        report['checks'].append(movement_check)
        if not movement_check['passed']:
            report['warnings'].extend(movement_check['issues'])
        
        # Check 4: Genre requirements
        genre_check = self.check_genre_requirements(trajectory)
        report['checks'].append(genre_check)
        if not genre_check['passed']:
            report['errors'].extend(genre_check['issues'])
            report['valid'] = False
        
        # Check 5: Pacing consistency
        pacing_check = self.check_pacing(trajectory)
        report['checks'].append(pacing_check)
        if not pacing_check['passed']:
            report['warnings'].extend(pacing_check['issues'])
        
        # Check 6: Arc completion
        arc_check = self.check_character_arcs(trajectory)
        report['checks'].append(arc_check)
        if not arc_check['passed']:
            report['warnings'].extend(arc_check['issues'])
        
        return report
    
    def check_jumps(self, trajectory: List[Dict]) -> Dict:
        """Check for unrealistic jumps between states."""
        max_jump = self.requirements.get(self.genre, {}).get('max_jump', 3)
        issues = []
        skip_fields = {'beat', 'chapter', 'description', 'act', 'scene', 'notes'}

        for i in range(1, len(trajectory)):
            prev_state = trajectory[i-1]
            curr_state = trajectory[i]

            for dimension in curr_state:
                if dimension in skip_fields or not isinstance(curr_state[dimension], (int, float)):
                    continue
                if dimension in prev_state and isinstance(prev_state[dimension], (int, float)):
                    jump = abs(curr_state[dimension] - prev_state[dimension])
                    if jump > max_jump:
                        issues.append(
                            f"Chapter {i}: {dimension} jumped {jump} points "
                            f"(max allowed: {max_jump}). Needs catalyst event."
                        )

        return {
            'name': 'Jump Validation',
            'passed': len(issues) == 0,
            'issues': issues
        }
    
    def check_movement(self, trajectory: List[Dict]) -> Dict:
        """Check for sufficient dimensional movement."""
        issues = []
        min_moving = self.requirements.get(self.genre, {}).get('min_dimensions_moving', 2)
        skip_fields = {'beat', 'chapter', 'description', 'act', 'scene', 'notes'}

        for i in range(1, len(trajectory)):
            prev_state = trajectory[i-1]
            curr_state = trajectory[i]

            dimensions_moved = 0
            for dimension in curr_state:
                if dimension in skip_fields or not isinstance(curr_state[dimension], (int, float)):
                    continue
                if dimension in prev_state and isinstance(prev_state[dimension], (int, float)):
                    if abs(curr_state[dimension] - prev_state[dimension]) >= 0.5:
                        dimensions_moved += 1

            if dimensions_moved < min_moving:
                issues.append(
                    f"Chapter {i}: Only {dimensions_moved} dimensions moving "
                    f"(minimum: {min_moving}). Scene may feel static."
                )

        return {
            'name': 'Movement Validation',
            'passed': len(issues) < len(trajectory) * 0.2,  # Allow 20% static scenes
            'issues': issues
        }
    
    def check_genre_requirements(self, trajectory: List[Dict]) -> Dict:
        """Check if story meets genre-specific requirements."""
        issues = []
        reqs = self.requirements.get(self.genre, {})

        # Check ending requirements
        if len(trajectory) > 0:
            final_state = trajectory[-1]

            # If ending_type is specified, use ending type requirements
            if self.ending_type:
                ending_reqs = self.ending_types.get(self.genre, {}).get(self.ending_type, {})

                # Special handling for tragic endings - minimal validation
                if self.ending_type == 'tragic':
                    # For tragic endings, we just add an informational note
                    # No strict requirements - allows narrative flexibility
                    pass
                else:
                    # Validate against ending type requirements
                    for dimension, required_value in ending_reqs.items():
                        # Skip non-dimensional fields
                        if dimension in ['description', 'note']:
                            continue

                        if dimension in final_state:
                            if isinstance(required_value, tuple):
                                # Range requirement
                                if not (required_value[0] <= final_state[dimension] <= required_value[1]):
                                    issues.append(
                                        f"Ending ({self.ending_type}): {dimension} = {final_state[dimension]} "
                                        f"(required: {required_value[0]} to {required_value[1]})"
                                    )
                            else:
                                # Minimum requirement
                                if final_state[dimension] < required_value:
                                    issues.append(
                                        f"Ending ({self.ending_type}): {dimension} = {final_state[dimension]} "
                                        f"(required: >= {required_value})"
                                    )

            # Otherwise use default genre ending requirements
            elif 'ending' in reqs:
                for dimension, required_value in reqs['ending'].items():
                    if dimension in final_state:
                        if isinstance(required_value, tuple):
                            # Range requirement
                            if not (required_value[0] <= final_state[dimension] <= required_value[1]):
                                issues.append(
                                    f"Ending: {dimension} = {final_state[dimension]} "
                                    f"(required: {required_value[0]} to {required_value[1]})"
                                )
                        else:
                            # Minimum requirement
                            if final_state[dimension] < required_value:
                                issues.append(
                                    f"Ending: {dimension} = {final_state[dimension]} "
                                    f"(required: >= {required_value})"
                                )

        # Check sustained requirements (applies regardless of ending type)
        if 'sustained' in reqs:
            for dimension, min_value in reqs['sustained'].items():
                violations = []
                for i, state in enumerate(trajectory):
                    if dimension in state and state[dimension] < min_value:
                        violations.append(i)

                if violations:
                    issues.append(
                        f"{dimension} dropped below {min_value} in chapters: {violations}"
                    )

        return {
            'name': 'Genre Requirements',
            'passed': len(issues) == 0,
            'issues': issues
        }
    
    def check_pacing(self, trajectory: List[Dict]) -> Dict:
        """Check pacing consistency."""
        issues = []
        velocities = []
        
        for i in range(1, len(trajectory)):
            velocity = self.calculate_velocity(trajectory[i-1], trajectory[i])
            velocities.append(velocity)
        
        if velocities:
            avg_velocity = sum(velocities) / len(velocities)
            
            # Check for extreme variations
            for i, v in enumerate(velocities):
                if v > avg_velocity * 3:
                    issues.append(f"Chapter {i+1}: Pacing spike (velocity: {v:.2f})")
                elif v < avg_velocity * 0.2 and avg_velocity > 1:
                    issues.append(f"Chapter {i+1}: Pacing drop (velocity: {v:.2f})")
        
        # Check acts
        if len(trajectory) >= 9:
            act1_vel = sum(velocities[:len(velocities)//3]) / (len(velocities)//3)
            act2_vel = sum(velocities[len(velocities)//3:2*len(velocities)//3]) / (len(velocities)//3)
            act3_vel = sum(velocities[2*len(velocities)//3:]) / (len(velocities)//3 or 1)
            
            if act2_vel < act1_vel * 0.5:
                issues.append("Act 2 pacing significantly slower than Act 1")
            if act3_vel > act1_vel * 2:
                issues.append("Act 3 pacing may feel rushed compared to setup")
        
        return {
            'name': 'Pacing Consistency',
            'passed': len(issues) < 3,
            'issues': issues
        }
    
    def check_character_arcs(self, trajectory: List[Dict]) -> Dict:
        """Check if character arcs show growth."""
        issues = []
        skip_fields = {'beat', 'chapter', 'description', 'act', 'scene', 'notes'}

        if len(trajectory) < 2:
            return {'name': 'Character Arcs', 'passed': True, 'issues': []}

        first_state = trajectory[0]
        final_state = trajectory[-1]

        # Check for dimensions that haven't changed
        static_dimensions = []
        for dimension in first_state:
            if dimension in skip_fields or not isinstance(first_state[dimension], (int, float)):
                continue
            if dimension in final_state and isinstance(final_state[dimension], (int, float)):
                if abs(final_state[dimension] - first_state[dimension]) < 1:
                    static_dimensions.append(dimension)

        # Count total dimensional fields
        total_dims = sum(1 for d in first_state if d not in skip_fields and isinstance(first_state[d], (int, float)))

        if total_dims > 0 and len(static_dimensions) > total_dims * 0.5:
            issues.append(
                f"Limited character growth: {', '.join(static_dimensions)} "
                "remained largely static"
            )

        # Check for regression (unless intentional for tragic ending)
        if self.genre == 'romance' and self.ending_type != 'tragic':
            key_dimensions = ['intimacy', 'trust', 'vulnerability']
            for dim in key_dimensions:
                if dim in first_state and dim in final_state:
                    if isinstance(first_state[dim], (int, float)) and isinstance(final_state[dim], (int, float)):
                        if final_state[dim] < first_state[dim]:
                            issues.append(f"Character regression: {dim} ended lower than started")

        return {
            'name': 'Character Arcs',
            'passed': len(issues) == 0,
            'issues': issues
        }
    
    def calculate_velocity(self, state1: Dict, state2: Dict) -> float:
        """Calculate velocity between two states."""
        total_movement = 0
        dimensions_counted = 0

        # Skip metadata fields
        skip_fields = {'beat', 'chapter', 'description', 'act', 'scene', 'notes'}

        for dimension in state1:
            if dimension in skip_fields or not isinstance(state1[dimension], (int, float)):
                continue
            if dimension in state2 and isinstance(state2[dimension], (int, float)):
                movement = abs(state2[dimension] - state1[dimension])
                total_movement += movement
                dimensions_counted += 1

        if dimensions_counted > 0:
            return total_movement / dimensions_counted
        return 0
    
    def suggest_fixes(self, report: Dict) -> List[str]:
        """Suggest fixes for validation issues."""
        suggestions = []
        
        for error in report['errors']:
            if 'jumped' in error:
                suggestions.append("Add catalyst event to justify large dimensional jump")
            elif 'Ending:' in error:
                suggestions.append("Adjust final chapters to meet genre requirements")
            elif 'dropped below' in error:
                suggestions.append("Maintain genre-critical dimensions above minimum")
        
        for warning in report['warnings']:
            if 'static' in warning.lower():
                suggestions.append("Add dimensional movement to static scenes")
            elif 'pacing' in warning.lower():
                suggestions.append("Redistribute dimensional changes for consistent pacing")
        
        return list(set(suggestions))  # Remove duplicates

# Example usage
if __name__ == "__main__":
    # Example trajectory - romance novel key points
    example_trajectory = [
        # Chapter 1 - Meet
        {'intimacy': 0, 'trust': 3, 'desire': 2, 'power_differential': 3, 
         'goal_alignment': 2, 'vulnerability': 1, 'stakes': 4},
        
        # Chapter 3 - First connection
        {'intimacy': 2, 'trust': 3, 'desire': 5, 'power_differential': 2,
         'goal_alignment': 3, 'vulnerability': 2, 'stakes': 5},
        
        # Chapter 5 - Growing closer
        {'intimacy': 4, 'trust': 4, 'desire': 7, 'power_differential': 1,
         'goal_alignment': 5, 'vulnerability': 4, 'stakes': 6},
        
        # Chapter 7 - First conflict
        {'intimacy': 3, 'trust': 3, 'desire': 7, 'power_differential': 2,
         'goal_alignment': 3, 'vulnerability': 2, 'stakes': 7},
        
        # Chapter 9 - Reconciliation
        {'intimacy': 5, 'trust': 5, 'desire': 8, 'power_differential': 0,
         'goal_alignment': 6, 'vulnerability': 6, 'stakes': 6},
        
        # Chapter 11 - Black moment
        {'intimacy': 6, 'trust': 1, 'desire': 8, 'power_differential': 0,
         'goal_alignment': 2, 'vulnerability': 8, 'stakes': 9},
        
        # Chapter 12 - Resolution
        {'intimacy': 8, 'trust': 7, 'desire': 9, 'power_differential': 0,
         'goal_alignment': 9, 'vulnerability': 8, 'stakes': 5}
    ]
    
    validator = TrajectoryValidator(genre='romance')
    report = validator.validate_trajectory(example_trajectory)
    
    print("TRAJECTORY VALIDATION REPORT")
    print("=" * 50)
    print(f"Valid: {report['valid']}")
    
    print("\nChecks Performed:")
    for check in report['checks']:
        status = "✓ PASSED" if check['passed'] else "✗ FAILED"
        print(f"  {check['name']}: {status}")
        if not check['passed']:
            for issue in check['issues'][:3]:  # Show first 3 issues
                print(f"    - {issue}")
    
    if report['errors']:
        print("\nERRORS (must fix):")
        for error in report['errors']:
            print(f"  - {error}")
    
    if report['warnings']:
        print("\nWARNINGS (should address):")
        for warning in report['warnings'][:5]:
            print(f"  - {warning}")
    
    suggestions = validator.suggest_fixes(report)
    if suggestions:
        print("\nSuggested Fixes:")
        for suggestion in suggestions:
            print(f"  → {suggestion}")
