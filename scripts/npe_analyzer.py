#!/usr/bin/env python3
"""
Narrative Physics Engine (NPE) Analyzer
Tracks axis progressions, orbital mechanics, and waveform analysis.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional
import math

# Import genre profiles
sys.path.insert(0, str(Path(__file__).parent.parent / 'references'))
try:
    from npe_genre_profiles import NPE_GENRE_PROFILES
except ImportError:
    NPE_GENRE_PROFILES = {}

def load_trajectory(filepath: Path) -> List[Dict]:
    """Load trajectory JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def calculate_axis_from_dimensions(state: Dict) -> Dict:
    """Convert 0-10 dimensions back to -1/+1 NPE axes."""
    # IA: Internal Axis (wound → growth)
    # Based on self_worth, vulnerability, trust
    IA = (state.get('self_worth', 5) / 5) - 1  # Normalize to -1/+1

    # RA: Relational Axis (intimacy + trust - power_diff)
    RA = ((state.get('intimacy', 5) + state.get('trust', 5)) / 10) - 1

    # EA: Environmental Axis (stakes + danger + pressure)
    EA = ((state.get('stakes', 5)) / 10) * 2 - 1

    # TA: Task/Plot Axis (goal_alignment - info_asymmetry)
    TA = ((state.get('goal_alignment', 5) - state.get('info_asymmetry', 5)) / 10)

    return {'IA': IA, 'RA': RA, 'EA': EA, 'TA': TA}

def analyze_orbital_progression(trajectory: List[Dict]) -> List[Dict]:
    """Track orbital distance changes across trajectory."""
    orbits = []

    for state in trajectory:
        orbit_data = {
            'chapter': state.get('chapter', 0),
            'title': state.get('title', ''),
            'orbital_distance': state.get('RA_orbit', 180),
            'intimacy_level': categorize_intimacy(state.get('RA_orbit', 180))
        }
        orbits.append(orbit_data)

    return orbits

def categorize_intimacy(orbit_degrees: float) -> str:
    """Categorize relationship intimacy by orbital distance."""
    if orbit_degrees >= 160:
        return "Distant/Strangers"
    elif orbit_degrees >= 120:
        return "Acquaintances"
    elif orbit_degrees >= 90:
        return "Friends/Warming"
    elif orbit_degrees >= 60:
        return "Close/Intimate"
    else:
        return "Deep Bond"

def analyze_waveform(values: List[float]) -> Dict:
    """Analyze emotional waveform characteristics."""
    if not values:
        return {}

    amplitude = max(values) - min(values)
    mean = sum(values) / len(values)

    # Calculate "frequency" - how often values cross the mean
    crossings = 0
    for i in range(1, len(values)):
        if (values[i-1] < mean and values[i] > mean) or \
           (values[i-1] > mean and values[i] < mean):
            crossings += 1

    frequency = crossings / len(values) if len(values) > 0 else 0

    # Detect phase (current position in cycle)
    last_value = values[-1]
    if last_value > mean:
        phase = "Rising/Peak"
    else:
        phase = "Falling/Trough"

    return {
        'amplitude': round(amplitude, 2),
        'mean': round(mean, 2),
        'frequency': round(frequency, 3),
        'phase': phase,
        'range': (min(values), max(values))
    }

def detect_thresholds(trajectory: List[Dict]) -> List[Dict]:
    """Detect major threshold moments (polarity shifts, turning points)."""
    thresholds = []

    for i in range(1, len(trajectory)):
        prev = trajectory[i-1]
        curr = trajectory[i]

        # Detect IA polarity crossing
        prev_IA = prev.get('IA', 0)
        curr_IA = curr.get('IA', 0)

        if prev_IA < 0 and curr_IA >= 0:
            thresholds.append({
                'chapter': curr.get('chapter'),
                'type': 'IA Polarity Flip',
                'description': 'Internal Axis crosses from wound to growth',
                'significance': 'MAJOR'
            })

        # Detect dramatic drops (dark night)
        ia_change = curr_IA - prev_IA
        if ia_change < -0.3:
            thresholds.append({
                'chapter': curr.get('chapter'),
                'type': 'Crisis/Dark Night',
                'description': f'IA drops {abs(ia_change):.2f} points',
                'significance': 'CRITICAL'
            })

        # Detect major orbital shifts
        prev_orbit = prev.get('RA_orbit', 180)
        curr_orbit = curr.get('RA_orbit', 180)
        orbit_change = prev_orbit - curr_orbit  # Positive = closer

        if orbit_change >= 30:
            thresholds.append({
                'chapter': curr.get('chapter'),
                'type': 'Relational Breakthrough',
                'description': f'Orbit closes {orbit_change}° (now {curr_orbit}°)',
                'significance': 'MAJOR'
            })

    return thresholds

def calculate_entropy(trajectory: List[Dict]) -> List[float]:
    """Calculate narrative entropy (disorder/tension) over time."""
    entropy_values = []

    for state in trajectory:
        # Entropy = environmental pressure + goal misalignment + instability
        stakes = state.get('stakes', 0)
        info_asym = state.get('info_asymmetry', 0)
        goal_misalign = 10 - state.get('goal_alignment', 5)

        entropy = (stakes + info_asym + goal_misalign) / 30
        entropy_values.append(entropy)

    return entropy_values

def generate_npe_report(trajectory: List[Dict]) -> str:
    """Generate comprehensive NPE analysis report."""
    lines = []

    lines.append("=" * 70)
    lines.append("NARRATIVE PHYSICS ENGINE ANALYSIS")
    lines.append("=" * 70)
    lines.append("")

    # Extract key data
    ia_values = [s.get('IA', 0) for s in trajectory]
    ra_orbits = [s.get('RA_orbit', 180) for s in trajectory]
    ea_values = [s.get('EA', 0) for s in trajectory]
    ta_values = [s.get('TA', 0) for s in trajectory]
    self_worth = [s.get('self_worth', 5) for s in trajectory]

    # 1. AXIS PROGRESSION SUMMARY
    lines.append("1. AXIS PROGRESSION")
    lines.append("-" * 70)
    lines.append(f"Internal Axis (IA):  {ia_values[0]:+.2f} → {ia_values[-1]:+.2f}  (Δ {ia_values[-1]-ia_values[0]:+.2f})")
    lines.append(f"  Status: {categorize_ia_state(ia_values[-1])}")
    lines.append(f"  Lowest point: {min(ia_values):+.2f} at Chapter {ia_values.index(min(ia_values))+1}")
    lines.append("")

    lines.append(f"Relational Axis (RA): {ra_orbits[0]}° → {ra_orbits[-1]}°  (Δ {ra_orbits[0]-ra_orbits[-1]}° closer)")
    lines.append(f"  Status: {categorize_intimacy(ra_orbits[-1])}")
    lines.append(f"  Closest approach: {min(ra_orbits)}° at Chapter {ra_orbits.index(min(ra_orbits))+1}")
    lines.append("")

    lines.append(f"Environmental Axis (EA): {ea_values[0]:+.2f} → {ea_values[-1]:+.2f}")
    lines.append(f"  Peak pressure: {max(ea_values):+.2f} at Chapter {ea_values.index(max(ea_values))+1}")
    lines.append("")

    lines.append(f"Task Axis (TA): {ta_values[0]:+.2f} → {ta_values[-1]:+.2f}")
    lines.append(f"  Completion achieved: {ta_values[-1] >= 0.9}")
    lines.append("")

    # 2. WAVEFORM ANALYSIS
    lines.append("2. EMOTIONAL WAVEFORM ANALYSIS")
    lines.append("-" * 70)
    ia_waveform = analyze_waveform(ia_values)
    lines.append(f"IA Waveform:")
    lines.append(f"  Amplitude: {ia_waveform.get('amplitude', 0):.2f} (cozy constraint: <1.5)")
    lines.append(f"  Frequency: {ia_waveform.get('frequency', 0):.3f} (oscillations per chapter)")
    lines.append(f"  Phase: {ia_waveform.get('phase', 'Unknown')}")
    lines.append(f"  Range: {ia_waveform.get('range', (0,0))}")
    lines.append("")

    # 3. THRESHOLD MOMENTS
    lines.append("3. CRITICAL THRESHOLDS")
    lines.append("-" * 70)
    thresholds = detect_thresholds(trajectory)

    if thresholds:
        for threshold in thresholds:
            sig_marker = "🔴" if threshold['significance'] == 'CRITICAL' else "🟡"
            lines.append(f"{sig_marker} Chapter {threshold['chapter']}: {threshold['type']}")
            lines.append(f"   {threshold['description']}")
            lines.append("")
    else:
        lines.append("No major thresholds detected.")
        lines.append("")

    # 4. ENTROPY CURVE
    lines.append("4. ENTROPY (Narrative Disorder)")
    lines.append("-" * 70)
    entropy_vals = calculate_entropy(trajectory)
    lines.append(f"Starting entropy: {entropy_vals[0]:.2f}")
    lines.append(f"Peak entropy: {max(entropy_vals):.2f} at Chapter {entropy_vals.index(max(entropy_vals))+1}")
    lines.append(f"Ending entropy: {entropy_vals[-1]:.2f}")
    lines.append(f"Genre compliance: {'✓ Cozy' if max(entropy_vals) < 0.5 else '✗ Too intense for cozy'}")
    lines.append("")

    # 5. ORBITAL MECHANICS
    lines.append("5. ORBITAL RELATIONSHIP PROGRESSION")
    lines.append("-" * 70)
    lines.append("Chapter | Orbit  | Intimacy Level")
    lines.append("--------|--------|-------------------")

    milestones = [0, 5, 11, 16, 19, 25]  # Key chapters
    for i in milestones:
        if i < len(trajectory):
            state = trajectory[i]
            orbit = state.get('RA_orbit', 180)
            lines.append(f"  {state.get('chapter', i+1):2d}    | {orbit:3.0f}°   | {categorize_intimacy(orbit)}")

    lines.append("")

    # 6. ACT STRUCTURE ANALYSIS
    lines.append("6. THREE-ACT STRUCTURE")
    lines.append("-" * 70)

    act1_end = len(trajectory) // 4
    act2_end = 3 * len(trajectory) // 4

    act1_ia = ia_values[:act1_end]
    act2_ia = ia_values[act1_end:act2_end]
    act3_ia = ia_values[act2_end:]

    lines.append(f"Act 1 (Ch 1-{act1_end}):   IA {min(act1_ia):+.2f} → {max(act1_ia):+.2f}")
    lines.append(f"Act 2 (Ch {act1_end+1}-{act2_end}): IA {min(act2_ia):+.2f} → {max(act2_ia):+.2f} (includes dark night)")
    lines.append(f"Act 3 (Ch {act2_end+1}-26): IA {min(act3_ia):+.2f} → {max(act3_ia):+.2f}")
    lines.append("")

    # 7. CHAPTER-BY-CHAPTER AXIS VALUES
    lines.append("7. DETAILED AXIS TRACKING")
    lines.append("-" * 70)
    lines.append("Ch | Title                           | IA    | RA_Orbit | EA    | TA   ")
    lines.append("---|--------------------------------|-------|----------|-------|------")

    for state in trajectory:
        ch = state.get('chapter', 0)
        title = state.get('title', '')[:30].ljust(30)
        ia = state.get('IA', 0)
        orbit = state.get('RA_orbit', 180)
        ea = state.get('EA', 0)
        ta = state.get('TA', 0)

        lines.append(f"{ch:2d} | {title} | {ia:+.2f} | {orbit:4.0f}°    | {ea:+.2f} | {ta:.2f}")

    lines.append("")
    lines.append("=" * 70)
    lines.append("END NPE ANALYSIS")
    lines.append("=" * 70)

    return "\n".join(lines)

def categorize_ia_state(ia_value: float) -> str:
    """Categorize IA state."""
    if ia_value < -0.7:
        return "Deep Wound"
    elif ia_value < -0.3:
        return "Wounded"
    elif ia_value < 0:
        return "Healing"
    elif ia_value < 0.5:
        return "Growing"
    else:
        return "Transformed/Whole"

def validate_genre_constraints(trajectory: List[Dict], genre: str = 'cozy_fantasy') -> Dict:
    """Validate trajectory against genre-specific NPE constraints."""

    if genre not in NPE_GENRE_PROFILES:
        return {
            'valid': False,
            'error': f'Unknown genre: {genre}. Available: {list(NPE_GENRE_PROFILES.keys())}'
        }

    profile = NPE_GENRE_PROFILES[genre]
    violations = []
    warnings = []

    # Extract data
    ia_values = [s.get('IA', 0) for s in trajectory]
    entropy_vals = calculate_entropy(trajectory)
    waveform = analyze_waveform(ia_values)

    # Check waveform constraints
    wf_constraints = profile['waveform_constraints']
    if waveform.get('amplitude', 0) > wf_constraints['amplitude']['max']:
        violations.append(
            f"Waveform amplitude {waveform['amplitude']:.2f} exceeds {genre} max "
            f"({wf_constraints['amplitude']['max']:.2f}). "
            f"{wf_constraints['amplitude']['note']}"
        )

    if waveform.get('frequency', 0) > wf_constraints['frequency']['max']:
        violations.append(
            f"Waveform frequency {waveform['frequency']:.3f} exceeds {genre} max "
            f"({wf_constraints['frequency']['max']:.3f}). "
            f"{wf_constraints['frequency']['note']}"
        )

    # Check entropy constraints
    ent_constraints = profile['entropy_constraints']
    max_entropy = max(entropy_vals)
    avg_entropy = sum(entropy_vals) / len(entropy_vals)

    if max_entropy > ent_constraints['peak_allowed']:
        violations.append(
            f"Peak entropy {max_entropy:.2f} exceeds {genre} peak "
            f"({ent_constraints['peak_allowed']:.2f}). "
            f"{ent_constraints['note']}"
        )

    if avg_entropy > ent_constraints['max_sustained']:
        warnings.append(
            f"Average entropy {avg_entropy:.2f} exceeds {genre} sustained max "
            f"({ent_constraints['max_sustained']:.2f})"
        )

    # Check IA axis profile
    ia_profile = profile['axis_profiles']['IA']

    if ia_profile.get('must_cross_zero'):
        crosses_zero = any(ia_values[i] < 0 and ia_values[i+1] >= 0
                          for i in range(len(ia_values)-1))
        if not crosses_zero:
            violations.append(
                f"{genre} requires IA polarity flip (crossing 0). "
                f"{ia_profile.get('note', '')}"
            )

    # Check final IA value
    final_ia = ia_values[-1]
    final_range = ia_profile.get('final_range', (-1, 1))
    if not (final_range[0] <= final_ia <= final_range[1]):
        violations.append(
            f"Final IA value {final_ia:.2f} outside {genre} range "
            f"({final_range[0]:.2f} to {final_range[1]:.2f})"
        )

    # Check threshold requirements
    thresh_reqs = profile.get('threshold_requirements', {})
    thresholds = detect_thresholds(trajectory)

    if thresh_reqs.get('dark_night_required'):
        has_dark_night = any(t['type'] == 'Crisis/Dark Night' for t in thresholds)
        if not has_dark_night:
            violations.append(f"{genre} requires a dark night moment")

    return {
        'valid': len(violations) == 0,
        'genre': genre,
        'violations': violations,
        'warnings': warnings,
        'profile_notes': {
            'waveform': wf_constraints,
            'entropy': ent_constraints,
            'description': profile.get('description', '')
        }
    }

# Main execution
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python npe_analyzer.py <trajectory_file> [--genre GENRE]")
        print("\nAvailable genres:")
        for genre in NPE_GENRE_PROFILES.keys():
            print(f"  - {genre}")
        sys.exit(1)

    filepath = Path(sys.argv[1])

    # Parse genre argument
    genre = 'cozy_fantasy'  # default
    if '--genre' in sys.argv:
        genre_idx = sys.argv.index('--genre')
        if genre_idx + 1 < len(sys.argv):
            genre = sys.argv[genre_idx + 1]

    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    trajectory = load_trajectory(filepath)
    report = generate_npe_report(trajectory)

    print(report)

    # Add genre validation section
    if NPE_GENRE_PROFILES:
        print("\n" + "=" * 70)
        print("GENRE CONSTRAINT VALIDATION")
        print("=" * 70)

        validation = validate_genre_constraints(trajectory, genre)

        print(f"\nGenre: {validation['genre']}")
        print(f"Description: {validation['profile_notes'].get('description', '')}")
        print(f"\nValid: {'✓ YES' if validation['valid'] else '✗ NO'}")

        if validation.get('violations'):
            print(f"\n🚨 VIOLATIONS ({len(validation['violations'])}):")
            for v in validation['violations']:
                print(f"  - {v}")

        if validation.get('warnings'):
            print(f"\n⚠️  WARNINGS ({len(validation['warnings'])}):")
            for w in validation['warnings']:
                print(f"  - {w}")

        if validation['valid']:
            print(f"\n✓ Trajectory complies with {genre} physics constraints")

        print("\n" + "=" * 70)
