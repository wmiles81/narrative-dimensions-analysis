#!/usr/bin/env python3
"""
Calculate narrative tension from dimensional state vectors.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Optional, List, Tuple

# Get the project root directory (parent of scripts/)
PROJECT_ROOT = Path(__file__).parent.parent
WEIGHTS_FILE = PROJECT_ROOT / 'references' / 'genre-weights.json'
CUSTOM_WEIGHTS_DIR = PROJECT_ROOT / 'custom-weights'

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

def blend_genre_weights(genre_blends: List[Tuple[str, Optional[str], float]]) -> Dict[str, float]:
    """
    Blend multiple genre formulas with specified proportions.

    Args:
        genre_blends: List of (genre, subgenre, weight) tuples
                     Example: [('romance', 'contemporary', 0.7), ('thriller', 'psychological', 0.3)]

    Returns:
        Blended weights dictionary
    """
    if not genre_blends:
        raise ValueError("Must provide at least one genre blend")

    # Normalize weights to sum to 1.0
    total_weight = sum(weight for _, _, weight in genre_blends)
    if total_weight == 0:
        raise ValueError("Total blend weights cannot be zero")

    blended = {}

    for genre, subgenre, weight in genre_blends:
        genre_weights = load_genre_weights(genre, subgenre)
        normalized_weight = weight / total_weight

        for dimension, dim_weight in genre_weights.items():
            if dimension not in blended:
                blended[dimension] = 0
            blended[dimension] += dim_weight * normalized_weight

    return blended


def save_custom_weights(weights: Dict[str, float], name: str) -> Path:
    """
    Save custom weights configuration to file.

    Args:
        weights: Dictionary of dimension weights
        name: Name for this custom configuration

    Returns:
        Path to saved file
    """
    CUSTOM_WEIGHTS_DIR.mkdir(exist_ok=True)

    filepath = CUSTOM_WEIGHTS_DIR / f"{name}.json"

    with open(filepath, 'w') as f:
        json.dump({
            'name': name,
            'weights': weights,
            'note': 'Custom tension formula weights'
        }, f, indent=2)

    return filepath


def load_custom_weights(name: str) -> Dict[str, float]:
    """
    Load custom weights configuration from file.

    Args:
        name: Name of custom configuration

    Returns:
        Dictionary of dimension weights
    """
    filepath = CUSTOM_WEIGHTS_DIR / f"{name}.json"

    if not filepath.exists():
        raise FileNotFoundError(f"Custom weights '{name}' not found at {filepath}")

    with open(filepath, 'r') as f:
        data = json.load(f)

    return data.get('weights', {})


def calculate_tension(state: Dict[str, float], genre: str = "romance",
                     subgenre: Optional[str] = None,
                     modifiers: Optional[list] = None,
                     custom_weights: Optional[Dict[str, float]] = None,
                     genre_blend: Optional[List[Tuple[str, Optional[str], float]]] = None) -> Dict:
    """
    Calculate tension and component breakdown from dimensional state.

    Args:
        state: Dictionary of dimension values (0-10 scale except power_diff)
        genre: Primary genre (ignored if custom_weights or genre_blend provided)
        subgenre: Specific subgenre (ignored if custom_weights or genre_blend provided)
        modifiers: List of modifiers (e.g., ['mafia', 'captive'])
        custom_weights: Optional custom weights dictionary (overrides genre/subgenre)
        genre_blend: Optional list of (genre, subgenre, weight) tuples for blending
                    Example: [('romance', 'contemporary', 0.7), ('thriller', 'psychological', 0.3)]

    Returns:
        Dictionary with total tension and component breakdown
    """
    # Determine which weights to use (priority: custom > blend > genre)
    if custom_weights:
        weights = custom_weights
        config_type = 'custom'
    elif genre_blend:
        weights = blend_genre_weights(genre_blend)
        config_type = 'blend'
    else:
        weights = load_genre_weights(genre, subgenre)
        config_type = 'genre'
    
    # Calculate base components
    components = {}
    
    # Direct dimensions
    if 'stakes' in weights and 'stakes' in state:
        components['stakes'] = state['stakes'] * weights['stakes']
    
    if 'info_asymmetry' in weights and 'info_asymmetry' in state:
        components['info_asymmetry'] = state['info_asymmetry'] * weights['info_asymmetry']
    
    # Calculate goal misalignment (inverse of alignment)
    # Note: goal_misalignment = 10 - goal_alignment
    # This converts alignment (how much they want the same thing)
    # into misalignment (how much they're in conflict)
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
    
    # Build configuration info
    config_info = {
        'type': config_type,
        'modifiers': modifiers or []
    }

    if config_type == 'genre':
        config_info['genre'] = genre
        config_info['subgenre'] = subgenre
    elif config_type == 'blend':
        config_info['genre_blend'] = genre_blend
    elif config_type == 'custom':
        config_info['note'] = 'Using custom weights'

    return {
        'total_tension': round(total_tension, 2),
        'components': {k: round(v, 2) for k, v in components.items()},
        'primary_driver': max(components.items(), key=lambda x: x[1])[0] if components else None,
        'configuration': config_info,
        'weights_used': {k: round(v, 3) for k, v in weights.items()}
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

    print("=" * 70)
    print("EXAMPLE 1: Standard Genre Formula (Dark Romance)")
    print("=" * 70)

    tension = calculate_tension(
        example_state,
        genre='romance',
        subgenre='dark',
        modifiers=['captive']
    )

    print(f"Total Tension: {tension['total_tension']}/10")
    print(f"Configuration: {tension['configuration']['type']}")
    print(f"\nComponents:")
    for component, value in tension['components'].items():
        print(f"  {component}: {value}")
    print(f"\nPrimary Driver: {tension['primary_driver']}")

    diagnosis = diagnose_tension(tension)
    print(f"\nDiagnosis: {diagnosis['level']} - {diagnosis['assessment']}")

    print("\n" + "=" * 70)
    print("EXAMPLE 2: Blended Genre (70% Romance + 30% Thriller)")
    print("=" * 70)

    blend_tension = calculate_tension(
        example_state,
        genre_blend=[
            ('romance', 'contemporary', 0.7),
            ('thriller', 'psychological', 0.3)
        ]
    )

    print(f"Total Tension: {blend_tension['total_tension']}/10")
    print(f"Configuration: {blend_tension['configuration']['type']}")
    print(f"\nWeights Used:")
    for dim, weight in blend_tension['weights_used'].items():
        print(f"  {dim}: {weight}")
    print(f"\nPrimary Driver: {blend_tension['primary_driver']}")

    print("\n" + "=" * 70)
    print("EXAMPLE 3: Custom Weights")
    print("=" * 70)

    # Create custom weights emphasizing danger and stakes
    custom = {
        'stakes': 0.30,
        'danger': 0.25,
        'info_asymmetry': 0.15,
        'goal_misalignment': 0.10,
        'vulnerability_trust_gap': 0.10,
        'power_differential': 0.10
    }

    custom_tension = calculate_tension(
        example_state,
        custom_weights=custom
    )

    print(f"Total Tension: {custom_tension['total_tension']}/10")
    print(f"Configuration: {custom_tension['configuration']['type']}")
    print(f"\nWeights Used:")
    for dim, weight in custom_tension['weights_used'].items():
        print(f"  {dim}: {weight}")
    print(f"\nPrimary Driver: {custom_tension['primary_driver']}")

    # Save custom weights for later use
    save_path = save_custom_weights(custom, 'high-stakes-action')
    print(f"\nCustom weights saved to: {save_path}")

    print("\n" + "=" * 70)
    print("EXAMPLE 4: Loading Saved Custom Weights")
    print("=" * 70)

    loaded_weights = load_custom_weights('high-stakes-action')
    loaded_tension = calculate_tension(
        example_state,
        custom_weights=loaded_weights
    )

    print(f"Total Tension: {loaded_tension['total_tension']}/10")
    print(f"Loaded weights match saved: {loaded_tension['total_tension'] == custom_tension['total_tension']}")
    print("\nAll examples completed successfully!")
