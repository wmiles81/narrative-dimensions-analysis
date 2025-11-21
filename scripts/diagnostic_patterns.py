#!/usr/bin/env python3
"""
Advanced diagnostic patterns for detecting story problems.
Analyzes trajectories for common issues and provides specific fixes.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import statistics

PROJECT_ROOT = Path(__file__).parent.parent

# Import existing functions
sys.path.append(str(PROJECT_ROOT / 'scripts'))
from calculate_tension import calculate_tension, load_genre_weights
from validate_trajectory import TrajectoryValidator


class NarrativeDiagnostics:
    """
    Advanced pattern detection for story problems.
    """

    def __init__(self, trajectory: List[Dict], genre: str,
                 catalysts: Optional[List[Dict]] = None):
        """
        Initialize diagnostics.

        Args:
            trajectory: Story dimensional trajectory
            genre: Genre for context-aware diagnostics
            catalysts: Optional list of catalyst events with locations
                      Format: [{'beat': 3, 'type': 'revelation', 'dimensions': ['info_asymmetry']}]
        """
        self.trajectory = trajectory
        self.genre = genre
        self.catalysts = catalysts or []
        self.validator = TrajectoryValidator(genre=genre)

    def detect_melodrama(self) -> Optional[Dict]:
        """
        Detect if too many dimensions at extremes (0-1 or 9-10).

        Returns diagnostic if found:
        {
            'issue': 'melodrama',
            'severity': 'warning',
            'description': 'Too many extreme dimensional values',
            'locations': [3, 7, 9],  # Beat indices
            'fix': 'Consider moderating some values to 2-8 range for realism'
        }
        """
        extreme_beats = []
        total_dimension_values = 0
        extreme_count = 0

        # Metadata fields to skip
        skip_fields = {'beat', 'chapter', 'description', 'act', 'scene', 'notes'}

        for i, state in enumerate(self.trajectory):
            beat_extremes = 0
            for dimension, value in state.items():
                # Skip non-dimensional metadata fields
                if dimension in skip_fields or not isinstance(value, (int, float)):
                    continue

                total_dimension_values += 1
                # Check if value is extreme (0-1 or 9-10)
                # Power_differential can be negative, so handle specially
                if dimension == 'power_differential':
                    if abs(value) >= 4:  # -5 to -4 or 4 to 5
                        extreme_count += 1
                        beat_extremes += 1
                else:
                    if value <= 1 or value >= 9:
                        extreme_count += 1
                        beat_extremes += 1

            # Flag beat if more than half its dimensions are extreme
            if beat_extremes > len(state) / 2:
                extreme_beats.append(i)

        # Flag if > 30% of all dimension-beats are extreme
        if total_dimension_values > 0:
            extreme_ratio = extreme_count / total_dimension_values
            if extreme_ratio > 0.30:
                return {
                    'issue': 'melodrama',
                    'severity': 'warning',
                    'description': f'{extreme_ratio:.1%} of dimensional values are at extremes (0-1 or 9-10)',
                    'locations': extreme_beats,
                    'affected_beats': len(extreme_beats),
                    'fix': 'Consider moderating values to 2-8 range for emotional realism. '
                           'Extremes lose impact when overused. Reserve 0-1 and 9-10 for '
                           'truly critical moments.',
                    'examples': self._get_extreme_examples(extreme_beats[:3])
                }

        return None

    def _get_extreme_examples(self, beat_indices: List[int]) -> List[str]:
        """Get specific examples of extreme values."""
        skip_fields = {'beat', 'chapter', 'description', 'act', 'scene', 'notes'}
        examples = []
        for i in beat_indices:
            if i < len(self.trajectory):
                state = self.trajectory[i]
                extremes = []
                for dim, val in state.items():
                    if dim in skip_fields or not isinstance(val, (int, float)):
                        continue
                    if dim == 'power_differential':
                        if abs(val) >= 4:
                            extremes.append(f"{dim}={val}")
                    elif val <= 1 or val >= 9:
                        extremes.append(f"{dim}={val}")
                if extremes:
                    examples.append(f"Beat {i}: {', '.join(extremes)}")
        return examples

    def detect_one_note_tension(self) -> Optional[Dict]:
        """
        Check if one component dominates tension (> 70% of total).

        Example: If stakes drive 80% of all tension, story may feel one-dimensional.
        """
        # Analyze component breakdown across entire story
        component_totals = {}
        total_tension_sum = 0

        for state in self.trajectory:
            tension_data = calculate_tension(state, genre=self.genre)
            total_tension_sum += tension_data['total_tension']

            for component, value in tension_data['components'].items():
                if component not in component_totals:
                    component_totals[component] = 0
                component_totals[component] += value

        if total_tension_sum == 0:
            return None

        # Calculate percentages
        component_percentages = {
            comp: (total / total_tension_sum) * 100
            for comp, total in component_totals.items()
        }

        # Find dominant component
        dominant_component = max(component_percentages.items(), key=lambda x: x[1])

        if dominant_component[1] > 70:
            return {
                'issue': 'one_note_tension',
                'severity': 'warning',
                'description': f'Single component ({dominant_component[0]}) drives {dominant_component[1]:.1f}% of total tension',
                'dominant_component': dominant_component[0],
                'percentage': round(dominant_component[1], 1),
                'breakdown': {k: round(v, 1) for k, v in component_percentages.items()},
                'fix': f'Diversify tension sources. Currently over-relying on {dominant_component[0]}. '
                       f'Try increasing other dimensions to create multi-layered tension. '
                       f'Consider adding conflict through goal_misalignment, info_asymmetry, '
                       f'or vulnerability_trust_gap.'
            }

        return None

    def detect_flatline(self) -> List[Dict]:
        """
        Detect scenes/chapters where nothing moves (velocity ≈ 0).

        Returns list of flat scenes with context.
        """
        flat_scenes = []

        for i in range(1, len(self.trajectory)):
            velocity = self.validator.calculate_velocity(
                self.trajectory[i-1],
                self.trajectory[i]
            )

            if velocity < 0.5:  # Very low movement
                flat_scenes.append({
                    'issue': 'flatline',
                    'severity': 'warning',
                    'beat': i,
                    'velocity': round(velocity, 2),
                    'description': f'Beat {i} has minimal dimensional movement (velocity: {velocity:.2f})',
                    'fix': f'Beat {i}: Add character development or relationship shift. '
                           f'At least 2-3 dimensions should move by 1+ points per scene.'
                })

        return flat_scenes

    def detect_teleportation(self) -> List[Dict]:
        """
        Find dimensional jumps ≥ 3 without matching catalyst events.

        Cross-references jumps with provided catalyst list.
        """
        teleportations = []
        max_jump = 3
        skip_fields = {'beat', 'chapter', 'description', 'act', 'scene', 'notes'}

        for i in range(1, len(self.trajectory)):
            prev_state = self.trajectory[i-1]
            curr_state = self.trajectory[i]

            for dimension in curr_state:
                if dimension in skip_fields or not isinstance(curr_state[dimension], (int, float)):
                    continue
                if dimension in prev_state and isinstance(prev_state[dimension], (int, float)):
                    jump = abs(curr_state[dimension] - prev_state[dimension])

                    if jump >= max_jump:
                        # Check if there's a matching catalyst
                        has_catalyst = self._has_matching_catalyst(i, dimension)

                        if not has_catalyst:
                            teleportations.append({
                                'issue': 'teleportation',
                                'severity': 'critical',
                                'beat': i,
                                'dimension': dimension,
                                'jump': round(jump, 1),
                                'from': round(prev_state[dimension], 1),
                                'to': round(curr_state[dimension], 1),
                                'description': f'Beat {i}: {dimension} jumped {jump:.1f} points without catalyst event',
                                'fix': f'Add a catalyst event at beat {i} to justify {dimension} changing '
                                       f'from {prev_state[dimension]:.1f} to {curr_state[dimension]:.1f}. '
                                       f'Examples: revelation, betrayal, sacrifice, confrontation.'
                            })

        return teleportations

    def _has_matching_catalyst(self, beat: int, dimension: str) -> bool:
        """Check if there's a catalyst event for this beat/dimension."""
        for catalyst in self.catalysts:
            if catalyst.get('beat') == beat:
                affected_dims = catalyst.get('dimensions', [])
                if dimension in affected_dims or not affected_dims:
                    return True
        return False

    def detect_sawtooth_overuse(self, dimension: str) -> Optional[Dict]:
        """
        Detect if a dimension oscillates too frequently (artificial drama).

        Some sawtooth is good (trust build-break-rebuild), but too much is tiring.
        """
        if len(self.trajectory) < 3:
            return None

        # Track direction changes
        direction_changes = 0
        prev_direction = None

        values = []
        for state in self.trajectory:
            if dimension in state and isinstance(state[dimension], (int, float)):
                values.append(state[dimension])

        if len(values) < 3:
            return None

        for i in range(1, len(values)):
            diff = values[i] - values[i-1]
            if abs(diff) > 0.5:  # Ignore tiny fluctuations
                current_direction = 'up' if diff > 0 else 'down'

                if prev_direction and current_direction != prev_direction:
                    direction_changes += 1

                prev_direction = current_direction

        # Flag if changes direction > 4 times
        if direction_changes > 4:
            return {
                'issue': 'sawtooth_overuse',
                'severity': 'warning',
                'dimension': dimension,
                'changes': direction_changes,
                'description': f'{dimension} oscillates {direction_changes} times (pattern: {values})',
                'fix': f'Too much back-and-forth in {dimension} can feel exhausting. '
                       f'Consider a smoother progression with 1-2 major setbacks instead of '
                       f'constant oscillation. Build momentum in one direction before reversing.'
            }

        return None

    def detect_stuck_arc(self) -> List[Dict]:
        """
        Detect dimensions that should move but don't (genre-specific).

        E.g., in romance, if intimacy stays at 3 for 60% of the story.
        """
        stuck_arcs = []

        # Genre-specific expectations
        genre_critical_dims = {
            'romance': ['intimacy', 'trust', 'vulnerability'],
            'dark': ['intimacy', 'trust', 'power_differential'],
            'thriller': ['danger', 'stakes'],
            'mystery': ['info_asymmetry']
        }

        critical_dims = genre_critical_dims.get(self.genre, [])

        for dimension in critical_dims:
            # Check if dimension exists in trajectory
            values = []
            for state in self.trajectory:
                if dimension in state and isinstance(state[dimension], (int, float)):
                    values.append(state[dimension])

            if len(values) < 3:
                continue

            # Calculate how long dimension stays in same range
            plateau_count = 0
            for i in range(1, len(values)):
                if abs(values[i] - values[i-1]) < 1:  # Minimal change
                    plateau_count += 1

            plateau_ratio = plateau_count / (len(values) - 1)

            # Also check total arc progression
            total_arc = abs(values[-1] - values[0])

            if plateau_ratio > 0.6 or total_arc < 2:
                stuck_arcs.append({
                    'issue': 'stuck_arc',
                    'severity': 'warning',
                    'dimension': dimension,
                    'plateau_ratio': round(plateau_ratio, 2),
                    'total_movement': round(total_arc, 1),
                    'description': f'{dimension} barely moves ({plateau_ratio:.0%} plateau, total change: {total_arc:.1f})',
                    'fix': f'{dimension} is critical for {self.genre} but shows minimal progression. '
                           f'Plan a clear arc: start at {values[0]:.0f}, have setbacks/growth, '
                           f'end significantly higher (7-9 range). Current endpoint: {values[-1]:.0f}.'
                })

        return stuck_arcs

    def detect_rushed_ending(self) -> Optional[Dict]:
        """
        Check if too many dimensions shift in final 10% of story.

        Suggests rushing to tie up loose ends.
        """
        if len(self.trajectory) < 5:
            return None

        # Define final 10% (at least last 2 beats)
        final_section_size = max(2, int(len(self.trajectory) * 0.1))
        final_section_start = len(self.trajectory) - final_section_size

        # Calculate average velocity for final section
        final_velocities = []
        for i in range(final_section_start, len(self.trajectory)):
            if i > 0:
                vel = self.validator.calculate_velocity(
                    self.trajectory[i-1],
                    self.trajectory[i]
                )
                final_velocities.append(vel)

        if not final_velocities:
            return None

        # Calculate average velocity for rest of story
        earlier_velocities = []
        for i in range(1, final_section_start):
            vel = self.validator.calculate_velocity(
                self.trajectory[i-1],
                self.trajectory[i]
            )
            earlier_velocities.append(vel)

        if not earlier_velocities:
            return None

        avg_final = statistics.mean(final_velocities)
        avg_earlier = statistics.mean(earlier_velocities)

        # Flag if final section is more than 2x faster
        if avg_final > avg_earlier * 2 and avg_final > 3:
            return {
                'issue': 'rushed_ending',
                'severity': 'warning',
                'final_velocity': round(avg_final, 2),
                'earlier_velocity': round(avg_earlier, 2),
                'ratio': round(avg_final / avg_earlier, 2),
                'description': f'Final {final_section_size} beats move {avg_final/avg_earlier:.1f}x faster than earlier story',
                'fix': f'Ending feels rushed. Final velocity ({avg_final:.1f}) is much higher '
                       f'than earlier pacing ({avg_earlier:.1f}). Either: '
                       f'(1) Slow down - give resolutions more space, or '
                       f'(2) Increase earlier pacing - move faster in middle acts.'
            }

        return None

    def detect_missing_black_moment(self) -> Optional[Dict]:
        """
        For genres that need a crisis, check if one exists.

        Romance should have trust/alignment crash around 75-80%.
        """
        if self.genre not in ['romance', 'dark']:
            return None

        if len(self.trajectory) < 5:
            return None

        # Check 70-85% range for black moment
        story_length = len(self.trajectory)
        check_start = int(story_length * 0.70)
        check_end = int(story_length * 0.85)

        # Look for trust or alignment crash
        has_black_moment = False

        for i in range(check_start, min(check_end + 1, story_length)):
            state = self.trajectory[i]
            trust = state.get('trust', 5)
            alignment = state.get('goal_alignment', 5)

            # Black moment: trust ≤ 3 or alignment ≤ 3
            if trust <= 3 or alignment <= 3:
                has_black_moment = True
                break

        if not has_black_moment:
            return {
                'issue': 'missing_black_moment',
                'severity': 'critical',
                'expected_range': f'beats {check_start}-{check_end}',
                'description': f'No crisis/black moment detected in expected range (beats {check_start}-{check_end})',
                'fix': f'Romance needs a dark moment around 75-80% where trust/alignment crashes. '
                       f'This is where everything seems lost. Add a major betrayal, misunderstanding, '
                       f'or sacrifice that drops trust or goal_alignment to ≤3. '
                       f'Current trust/alignment in range: ' +
                       ', '.join([f"beat {i}: trust={self.trajectory[i].get('trust', 'N/A')}, "
                                  f"align={self.trajectory[i].get('goal_alignment', 'N/A')}"
                                  for i in range(check_start, min(check_end + 1, story_length))])
            }

        return None

    def detect_weak_chemistry(self) -> Optional[Dict]:
        """
        For romance: check chemistry indicators.

        Chemistry = desire + vulnerability + productive info_asymmetry
        """
        if self.genre not in ['romance', 'dark', 'contemporary', 'paranormal']:
            return None

        # Analyze first 40% of story (chemistry building phase)
        chemistry_section = int(len(self.trajectory) * 0.4)
        if chemistry_section < 2:
            chemistry_section = len(self.trajectory)

        chemistry_scores = []

        for i in range(chemistry_section):
            state = self.trajectory[i]
            desire = state.get('desire', 0)
            vulnerability = state.get('vulnerability', 0)
            info_asym = state.get('info_asymmetry', 0)

            # Good chemistry: desire rising, vulnerability present, some mystery
            chemistry_score = (desire * 0.4 + vulnerability * 0.4 +
                             min(info_asym, 5) * 0.2)
            chemistry_scores.append(chemistry_score)

        if chemistry_scores:
            avg_chemistry = statistics.mean(chemistry_scores)

            if avg_chemistry < 3:
                return {
                    'issue': 'weak_chemistry',
                    'severity': 'warning',
                    'chemistry_score': round(avg_chemistry, 2),
                    'description': f'Low chemistry in early story (score: {avg_chemistry:.1f}/10)',
                    'fix': 'Chemistry = desire + vulnerability + mystery. In first 40% of story: '
                           '(1) Build desire - attraction, longing, charged moments, '
                           '(2) Show vulnerability - characters revealing themselves, '
                           '(3) Maintain mystery - some info_asymmetry keeps intrigue. '
                           f'Current avg: desire={statistics.mean([s.get("desire", 0) for s in self.trajectory[:chemistry_section]]):.1f}, '
                           f'vulnerability={statistics.mean([s.get("vulnerability", 0) for s in self.trajectory[:chemistry_section]]):.1f}'
                }

        return None

    def detect_info_dump(self) -> List[Dict]:
        """
        Detect info_asymmetry dropping > 3 points in single beat.

        Suggests exposition dump rather than gradual revelation.
        """
        info_dumps = []

        for i in range(1, len(self.trajectory)):
            prev_state = self.trajectory[i-1]
            curr_state = self.trajectory[i]

            if 'info_asymmetry' in prev_state and 'info_asymmetry' in curr_state:
                drop = prev_state['info_asymmetry'] - curr_state['info_asymmetry']

                if drop > 3:  # Major drop suggests dump
                    info_dumps.append({
                        'issue': 'info_dump',
                        'severity': 'warning',
                        'beat': i,
                        'drop': round(drop, 1),
                        'from': round(prev_state['info_asymmetry'], 1),
                        'to': round(curr_state['info_asymmetry'], 1),
                        'description': f'Beat {i}: info_asymmetry drops {drop:.1f} points ({prev_state["info_asymmetry"]:.1f} → {curr_state["info_asymmetry"]:.1f})',
                        'fix': f'Beat {i}: Spread revelations across multiple scenes. '
                               f'Instead of explaining everything at once, reveal gradually '
                               f'through action, dialogue, and discovery. '
                               f'Drop info_asymmetry by 1-2 points per scene, not {drop:.0f}.'
                    })

        return info_dumps

    def detect_power_imbalance_plateau(self) -> Optional[Dict]:
        """
        Check if power_differential stays extreme for too long.

        Even in dark romance, power should shift or exchange at times.
        """
        if len(self.trajectory) < 5:
            return None

        # Count how many beats have extreme power imbalance (|diff| >= 4)
        extreme_count = 0
        extreme_beats = []

        for i, state in enumerate(self.trajectory):
            power_diff = state.get('power_differential', 0)
            if abs(power_diff) >= 4:
                extreme_count += 1
                extreme_beats.append(i)

        extreme_ratio = extreme_count / len(self.trajectory)

        if extreme_ratio > 0.5:
            return {
                'issue': 'power_imbalance_plateau',
                'severity': 'warning',
                'extreme_ratio': round(extreme_ratio, 2),
                'affected_beats': extreme_beats,
                'description': f'Power differential stays extreme (±4 or ±5) for {extreme_ratio:.0%} of story',
                'fix': f'Even in dark/captive romance, power should shift. Show: '
                       f'(1) Moments where lower-power character gains leverage, '
                       f'(2) Vulnerability from higher-power character, '
                       f'(3) Gradual equalization as relationship deepens. '
                       f'Current pattern: extreme in beats {extreme_beats[:5]}...'
            }

        return None

    def detect_positive_patterns(self) -> List[Dict]:
        """
        Identify what's working well.

        Examples:
        - Well-paced tension waves
        - Properly earned major moments
        - Effective genre beat alignment
        """
        strengths = []

        # Check for good tension pacing (waves not flatlines)
        tension_values = []
        for state in self.trajectory:
            tension = calculate_tension(state, genre=self.genre)
            tension_values.append(tension['total_tension'])

        if len(tension_values) >= 3:
            # Look for variance (good) vs flatline (bad)
            variance = statistics.variance(tension_values)
            if variance > 2:  # Good variation
                strengths.append({
                    'pattern': 'tension_waves',
                    'description': f'Good tension variation (variance: {variance:.1f})',
                    'why_good': 'Tension rises and falls naturally, creating rhythm and preventing fatigue'
                })

        # Check for earned climax (velocity spike near end)
        if len(self.trajectory) >= 5:
            final_third = len(self.trajectory) * 2 // 3
            velocities = []
            for i in range(final_third, len(self.trajectory)):
                if i > 0:
                    vel = self.validator.calculate_velocity(
                        self.trajectory[i-1],
                        self.trajectory[i]
                    )
                    velocities.append(vel)

            if velocities and max(velocities) > 3:
                strengths.append({
                    'pattern': 'strong_climax',
                    'description': f'Strong climax with high velocity ({max(velocities):.1f})',
                    'why_good': 'Final act has significant movement - story building to powerful conclusion'
                })

        # Check for character growth
        if len(self.trajectory) >= 2:
            first = self.trajectory[0]
            last = self.trajectory[-1]
            skip_fields = {'beat', 'chapter', 'description', 'act', 'scene', 'notes'}

            growth_dims = []
            for dim in first:
                if dim in skip_fields or not isinstance(first[dim], (int, float)):
                    continue
                if dim in last and isinstance(last[dim], (int, float)):
                    growth = last[dim] - first[dim]
                    if growth >= 3:
                        growth_dims.append((dim, growth))

            if growth_dims:
                strengths.append({
                    'pattern': 'character_growth',
                    'description': f'Strong character development: {", ".join([f"{d}(+{g:.0f})" for d, g in growth_dims])}',
                    'why_good': 'Characters show clear progression and transformation'
                })

        # Check for proper black moment (if genre requires)
        if self.genre in ['romance', 'dark'] and len(self.trajectory) >= 5:
            story_length = len(self.trajectory)
            check_start = int(story_length * 0.70)
            check_end = int(story_length * 0.85)

            for i in range(check_start, min(check_end + 1, story_length)):
                state = self.trajectory[i]
                trust = state.get('trust', 5)
                if trust <= 3:
                    strengths.append({
                        'pattern': 'proper_black_moment',
                        'description': f'Black moment at beat {i} ({i/story_length:.0%} through story)',
                        'why_good': 'Crisis moment properly positioned in 75-85% range for maximum impact'
                    })
                    break

        return strengths

    def run_full_diagnostic(self) -> Dict:
        """
        Run all diagnostics and compile report.

        Returns:
        {
            'critical': [...],  # Must fix
            'warnings': [...],  # Should address
            'suggestions': [...],  # Consider
            'strengths': [...]  # What's working well
        }
        """
        results = {
            'critical': [],
            'warnings': [],
            'suggestions': [],
            'strengths': []
        }

        # Run all detect_* methods

        # Melodrama
        melodrama = self.detect_melodrama()
        if melodrama:
            results['warnings'].append(melodrama)

        # One-note tension
        one_note = self.detect_one_note_tension()
        if one_note:
            results['warnings'].append(one_note)

        # Flatlines
        flatlines = self.detect_flatline()
        for flatline in flatlines:
            if flatline['velocity'] < 0.2:
                results['critical'].append(flatline)
            else:
                results['warnings'].append(flatline)

        # Teleportation
        teleports = self.detect_teleportation()
        results['critical'].extend(teleports)

        # Sawtooth overuse (check key dimensions)
        key_dimensions = ['trust', 'intimacy', 'desire', 'stakes']
        for dim in key_dimensions:
            sawtooth = self.detect_sawtooth_overuse(dim)
            if sawtooth:
                results['warnings'].append(sawtooth)

        # Stuck arcs
        stuck = self.detect_stuck_arc()
        results['warnings'].extend(stuck)

        # Rushed ending
        rushed = self.detect_rushed_ending()
        if rushed:
            results['warnings'].append(rushed)

        # Missing black moment
        black_moment = self.detect_missing_black_moment()
        if black_moment:
            results['critical'].append(black_moment)

        # Weak chemistry
        chemistry = self.detect_weak_chemistry()
        if chemistry:
            results['warnings'].append(chemistry)

        # Info dumps
        dumps = self.detect_info_dump()
        results['warnings'].extend(dumps)

        # Power plateau
        power_plateau = self.detect_power_imbalance_plateau()
        if power_plateau:
            results['warnings'].append(power_plateau)

        # Positive patterns
        positive = self.detect_positive_patterns()
        results['strengths'].extend(positive)

        return results

    def generate_diagnostic_report(self) -> str:
        """
        Generate human-readable diagnostic report.
        """
        results = self.run_full_diagnostic()

        report = []
        report.append("=" * 70)
        report.append("NARRATIVE DIAGNOSTIC REPORT")
        report.append("=" * 70)
        report.append(f"Genre: {self.genre}")
        report.append(f"Trajectory Length: {len(self.trajectory)} beats")
        report.append(f"Catalysts Provided: {len(self.catalysts)}")
        report.append("")

        # Critical Issues
        if results['critical']:
            report.append("🚨 CRITICAL ISSUES (Must Fix)")
            report.append("-" * 70)
            for i, issue in enumerate(results['critical'], 1):
                report.append(f"\n{i}. {issue['issue'].upper()}")
                report.append(f"   {issue['description']}")
                report.append(f"   FIX: {issue['fix']}")
        else:
            report.append("✓ No critical issues detected")

        report.append("\n")

        # Warnings
        if results['warnings']:
            report.append("⚠️  WARNINGS (Should Address)")
            report.append("-" * 70)
            for i, warning in enumerate(results['warnings'], 1):
                report.append(f"\n{i}. {warning['issue'].upper()}")
                report.append(f"   {warning['description']}")
                report.append(f"   FIX: {warning['fix']}")
        else:
            report.append("✓ No warnings")

        report.append("\n")

        # Strengths
        if results['strengths']:
            report.append("💪 STRENGTHS (What's Working)")
            report.append("-" * 70)
            for i, strength in enumerate(results['strengths'], 1):
                report.append(f"\n{i}. {strength['pattern'].upper()}")
                report.append(f"   {strength['description']}")
                report.append(f"   Why it works: {strength['why_good']}")

        report.append("\n")
        report.append("=" * 70)

        # Summary
        total_issues = len(results['critical']) + len(results['warnings'])
        if total_issues == 0:
            report.append("OVERALL: Excellent trajectory! No major issues detected.")
        elif len(results['critical']) > 0:
            report.append(f"OVERALL: {len(results['critical'])} critical issues require immediate attention.")
        else:
            report.append(f"OVERALL: {len(results['warnings'])} warnings to consider addressing.")

        report.append("=" * 70)

        return "\n".join(report)


# Specialized diagnostic functions
def diagnose_genre_compliance(trajectory: List[Dict], genre: str) -> Dict:
    """Check if trajectory meets genre-specific requirements."""
    validator = TrajectoryValidator(genre=genre)
    report = validator.validate_trajectory(trajectory)

    compliance_report = {
        'genre': genre,
        'compliant': report['valid'],
        'failed_checks': [],
        'passed_checks': [],
        'recommendations': []
    }

    for check in report['checks']:
        if check['passed']:
            compliance_report['passed_checks'].append(check['name'])
        else:
            compliance_report['failed_checks'].append({
                'check': check['name'],
                'issues': check['issues']
            })

    # Add recommendations
    if not report['valid']:
        compliance_report['recommendations'] = validator.suggest_fixes(report)

    return compliance_report


def diagnose_pacing_issues(trajectory: List[Dict]) -> Dict:
    """Analyze pacing across the trajectory."""
    validator = TrajectoryValidator()

    pacing_analysis = {
        'velocities': [],
        'act_breakdown': {},
        'problem_chapters': [],
        'recommendations': []
    }

    # Calculate velocities
    velocities = []
    for i in range(1, len(trajectory)):
        vel = validator.calculate_velocity(trajectory[i-1], trajectory[i])
        velocities.append({
            'beat': i,
            'velocity': round(vel, 2)
        })
        pacing_analysis['velocities'].append(velocities[-1])

    if not velocities:
        return pacing_analysis

    # Act breakdown (3-act structure)
    act1_end = len(trajectory) // 3
    act2_end = 2 * len(trajectory) // 3

    act1_vels = [v['velocity'] for v in velocities[:act1_end] if v['velocity'] > 0]
    act2_vels = [v['velocity'] for v in velocities[act1_end:act2_end] if v['velocity'] > 0]
    act3_vels = [v['velocity'] for v in velocities[act2_end:] if v['velocity'] > 0]

    pacing_analysis['act_breakdown'] = {
        'act1_avg': round(statistics.mean(act1_vels), 2) if act1_vels else 0,
        'act2_avg': round(statistics.mean(act2_vels), 2) if act2_vels else 0,
        'act3_avg': round(statistics.mean(act3_vels), 2) if act3_vels else 0
    }

    # Identify problem chapters
    avg_vel = statistics.mean([v['velocity'] for v in velocities])
    for v in velocities:
        if v['velocity'] < 0.5:
            pacing_analysis['problem_chapters'].append({
                'beat': v['beat'],
                'issue': 'too_slow',
                'velocity': v['velocity']
            })
        elif v['velocity'] > avg_vel * 2.5:
            pacing_analysis['problem_chapters'].append({
                'beat': v['beat'],
                'issue': 'too_fast',
                'velocity': v['velocity']
            })

    # Recommendations
    act_breakdown = pacing_analysis['act_breakdown']
    if act_breakdown['act2_avg'] < act_breakdown['act1_avg'] * 0.6:
        pacing_analysis['recommendations'].append(
            "Act 2 drags - add complications or raise stakes to maintain momentum"
        )

    if act_breakdown['act3_avg'] > act_breakdown['act1_avg'] * 2.5:
        pacing_analysis['recommendations'].append(
            "Act 3 feels rushed - spread resolution across more beats"
        )

    return pacing_analysis


def suggest_fixes(diagnostic_results: Dict, trajectory: List[Dict]) -> List[str]:
    """
    Generate specific, actionable fix suggestions.

    Not just "increase tension" but "increase stakes in chapter 5 by..."
    """
    fixes = []

    # Process critical issues
    for issue in diagnostic_results.get('critical', []):
        if issue['issue'] == 'teleportation':
            fixes.append(
                f"Beat {issue['beat']}: Add catalyst event for {issue['dimension']}. "
                f"Examples: if trust jumped, add a sacrifice or vulnerability moment. "
                f"If stakes jumped, introduce new threat or raise consequences."
            )

        elif issue['issue'] == 'missing_black_moment':
            expected_beat = int(len(trajectory) * 0.75)
            fixes.append(
                f"Beat {expected_beat}: Create black moment. Drop trust to ≤3 through "
                f"betrayal, misunderstanding, or forced separation. This crisis makes "
                f"the eventual resolution meaningful."
            )

        elif issue['issue'] == 'flatline':
            fixes.append(
                f"Beat {issue['beat']}: Scene is static. Add: (1) emotional revelation "
                f"(+vulnerability), (2) desire spike (charged moment), or "
                f"(3) new obstacle (+stakes or info_asymmetry)."
            )

    # Process warnings with specific context
    for warning in diagnostic_results.get('warnings', []):
        if warning['issue'] == 'one_note_tension':
            dominant = warning['dominant_component']
            fixes.append(
                f"Over-reliance on {dominant}. Add variety: increase info_asymmetry "
                f"(secrets/mysteries), widen desire-proximity gap (longing), or "
                f"create goal conflict."
            )

        elif warning['issue'] == 'stuck_arc':
            dim = warning['dimension']
            fixes.append(
                f"{dim} needs clear progression. Map arc: start low, build through "
                f"middle, crash at black moment (beat ~75%), resolve high. "
                f"Currently stuck at same level."
            )

        elif warning['issue'] == 'weak_chemistry':
            fixes.append(
                f"First 40% needs more chemistry. Add: (1) desire moments - attraction, "
                f"tension, longing, (2) vulnerability - characters opening up, "
                f"(3) mystery - info_asymmetry to maintain intrigue."
            )

    return fixes


# CLI interface
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Run narrative diagnostics on a trajectory"
    )
    parser.add_argument("trajectory_file", help="JSON file with trajectory data")
    parser.add_argument("--genre", required=True, help="Story genre")
    parser.add_argument("--catalysts", help="JSON file with catalyst events")
    parser.add_argument("--report", help="Output report to file")

    args = parser.parse_args()

    # Load trajectory
    try:
        with open(args.trajectory_file, 'r') as f:
            data = json.load(f)
            # Support both direct list and {'trajectory': [...]} format
            if isinstance(data, list):
                trajectory = data
            elif 'trajectory' in data:
                trajectory = data['trajectory']
            else:
                print("Error: JSON must be a list or contain 'trajectory' key")
                sys.exit(1)
    except FileNotFoundError:
        print(f"Error: Trajectory file not found: {args.trajectory_file}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in trajectory file: {e}")
        sys.exit(1)

    # Load catalysts if provided
    catalysts = []
    if args.catalysts:
        try:
            with open(args.catalysts, 'r') as f:
                catalysts = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Warning: Could not load catalysts: {e}")

    # Run diagnostics
    diagnostics = NarrativeDiagnostics(trajectory, args.genre, catalysts)
    report_text = diagnostics.generate_diagnostic_report()

    # Output report
    if args.report:
        with open(args.report, 'w') as f:
            f.write(report_text)
        print(f"Report written to: {args.report}")
    else:
        print(report_text)

    # Also output structured results as JSON
    results = diagnostics.run_full_diagnostic()
    print("\n\nSTRUCTURED RESULTS (JSON):")
    print("=" * 70)
    print(json.dumps(results, indent=2))
