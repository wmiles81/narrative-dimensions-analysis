#!/usr/bin/env python3
"""
Calculate narrative tension from dimensional state vectors.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Optional

# Get the project root directory (parent of scripts/)
PROJECT_ROOT = Path(__file__).parent.parent
WEIGHTS_FILE = PROJECT_ROOT / 'references' / 'genre-weights.json'

def load_genre_weights(genre: str, subgenre: Optional[str] = None) -> Dict[str, float]:
    """Load tension weights for specific genre/subgenre."""
    try:
        with open(WEIGHTS_FILE, 'r') as f:
            weights = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Genre weights file not found at {WEIGHTS_FILE}. "
            f"Please ensure references/genre-weights.json exists."
        )
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in genre weights file: {e}")
    
    # Navigate to specific genre/subgenre
    if genre in weights:
        genre_weights = weights[genre]
        if subgenre and subgenre in genre_weights:
            return genre_weights[subgenre]
        elif 'default' in genre_weights:
            return genre_weights['default']
        elif isinstance(genre_weights, dict) and len(genre_weights) > 0:
            # Return first subgenre if no default
            return list(genre_weights.values())[0]
    
    # Fallback weights if genre not found
    return {
        "stakes": 0.20,
        "info_asymmetry": 0.15,
        "goal_misalignment": 0.15,
        "vulnerability_trust_gap": 0.20,
        "desire_proximity_gap": 0.20,
        "power_differential": 0.10
    }

def calculate_tension(state: Dict[str, float], genre: str = "romance", 
                     subgenre: Optional[str] = None, 
                     modifiers: Optional[list] = None) -> Dict:
    """
    Calculate tension and component breakdown from dimensional state.
    
    Args:
        state: Dictionary of dimension values (0-10 scale except power_diff)
        genre: Primary genre
        subgenre: Specific subgenre
        modifiers: List of modifiers (e.g., ['mafia', 'captive'])
    
    Returns:
        Dictionary with total tension and component breakdown
    """
    weights = load_genre_weights(genre, subgenre)
    
    # Calculate base components
    components = {}
    
    # Direct dimensions
    if 'stakes' in weights and 'stakes' in state:
        components['stakes'] = state['stakes'] * weights['stakes']
    
    if 'info_asymmetry' in weights and 'info_asymmetry' in state:
        components['info_asymmetry'] = state['info_asymmetry'] * weights['info_asymmetry']
    
    # Calculate goal misalignment (10 - alignment)
    if 'goal_misalignment' in weights and 'goal_alignment' in state:
        misalignment = 10 - state['goal_alignment']
        components['goal_misalignment'] = misalignment * weights['goal_misalignment']
    
    # Calculate vulnerability-trust gap
    if 'vulnerability_trust_gap' in weights:
        vulnerability = state.get('vulnerability', 5)
        trust = state.get('trust', 5)
        gap = max(0, vulnerability - trust)
        components['vulnerability_trust_gap'] = gap * weights['vulnerability_trust_gap']
    
    # Calculate desire-proximity gap  
    if 'desire_proximity_gap' in weights:
        desire = state.get('desire', 5)
        proximity = state.get('proximity', 5)
        gap = max(0, desire - proximity)
        components['desire_proximity_gap'] = gap * weights['desire_proximity_gap']
    
    # Power differential (absolute value)
    if 'power_differential' in weights and 'power_differential' in state:
        components['power_differential'] = abs(state['power_differential']) * weights['power_differential']
    
    # Genre-specific dimensions
    if 'danger' in weights and 'danger' in state:
        components['danger'] = state['danger'] * weights['danger']
    
    if 'moral_ambiguity' in weights and 'moral_ambiguity' in state:
        components['moral_ambiguity'] = state['moral_ambiguity'] * weights['moral_ambiguity']
    
    # Apply modifiers
    if modifiers:
        try:
            with open(WEIGHTS_FILE, 'r') as f:
                all_weights = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Warning: Could not load modifiers: {e}", file=sys.stderr)
            all_weights = {}

        if 'modifiers' in all_weights:
            for modifier in modifiers:
                if modifier in all_weights['modifiers']:
                    mod_factors = all_weights['modifiers'][modifier]
                    for key, factor in mod_factors.items():
                        if key in components:
                            components[key] *= factor
    
    # Calculate total tension (0-10 scale)
    total_tension = sum(components.values())
    total_tension = min(10, total_tension)  # Cap at 10
    
    return {
        'total_tension': round(total_tension, 2),
        'components': {k: round(v, 2) for k, v in components.items()},
        'primary_driver': max(components.items(), key=lambda x: x[1])[0] if components else None,
        'configuration': {
            'genre': genre,
            'subgenre': subgenre,
            'modifiers': modifiers or []
        }
    }

def diagnose_tension(tension_data: Dict) -> Dict:
    """Provide diagnostic feedback on tension levels."""
    total = tension_data['total_tension']
    diagnosis = {
        'level': '',
        'assessment': '',
        'suggestions': []
    }
    
    if total < 3:
        diagnosis['level'] = 'LOW'
        diagnosis['assessment'] = 'Scene lacks tension - reader may disengage'
        diagnosis['suggestions'] = [
            'Increase stakes or consequences',
            'Create information asymmetry',
            'Introduce goal conflict',
            'Widen desire-proximity gap'
        ]
    elif total < 5:
        diagnosis['level'] = 'MODERATE'
        diagnosis['assessment'] = 'Adequate tension for quieter scenes'
        diagnosis['suggestions'] = [
            'Consider if this is intentional pacing',
            'Could increase one dimension for more engagement'
        ]
    elif total < 7:
        diagnosis['level'] = 'GOOD'
        diagnosis['assessment'] = 'Strong tension - reader engaged'
        diagnosis['suggestions'] = [
            'Maintain this level for key scenes',
            'Monitor pacing to avoid fatigue'
        ]
    elif total < 9:
        diagnosis['level'] = 'HIGH'
        diagnosis['assessment'] = 'Peak tension - use sparingly'
        diagnosis['suggestions'] = [
            'Perfect for climax/black moment',
            'Cannot sustain for multiple chapters',
            'Plan relief/resolution soon'
        ]
    else:
        diagnosis['level'] = 'EXTREME'
        diagnosis['assessment'] = 'Maximum tension - reader exhaustion risk'
        diagnosis['suggestions'] = [
            'Only for crisis moments',
            'Must provide relief immediately after',
            'Risk numbing reader if overused'
        ]
    
    return diagnosis

# Example usage
if __name__ == "__main__":
    # Example state - dark romance at black moment
    example_state = {
        'intimacy': 7,
        'power_differential': -3,
        'info_asymmetry': 2,
        'goal_alignment': 3,
        'proximity': 8,
        'vulnerability': 9,
        'desire': 9,
        'stakes': 9,
        'trust': 2,
        'danger': 7,
        'moral_ambiguity': 8
    }
    
    tension = calculate_tension(
        example_state, 
        genre='romance',
        subgenre='dark',
        modifiers=['captive']
    )
    
    print("TENSION ANALYSIS")
    print("=" * 50)
    print(f"Total Tension: {tension['total_tension']}/10")
    print(f"\nComponents:")
    for component, value in tension['components'].items():
        print(f"  {component}: {value}")
    print(f"\nPrimary Driver: {tension['primary_driver']}")
    
    diagnosis = diagnose_tension(tension)
    print(f"\nDiagnosis: {diagnosis['level']}")
    print(f"Assessment: {diagnosis['assessment']}")
    print("Suggestions:")
    for suggestion in diagnosis['suggestions']:
        print(f"  - {suggestion}")
