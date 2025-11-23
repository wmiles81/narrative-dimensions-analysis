#!/usr/bin/env python3
"""
Technical Dimensional Analysis Report Generator
Generates detailed numerical analysis with formulas and statistics.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional
import math
import statistics


def load_trajectory(filepath: Path) -> List[Dict]:
    """Load trajectory JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def calculate_tension_technical(state: Dict, weights: Dict) -> float:
    """
    Calculate tension using weighted formula.

    Formula:
    T = Σ(w_i × d_i) / Σ(w_i × d_max)

    Where:
    - w_i = weight for dimension i
    - d_i = current value of dimension i
    - d_max = maximum possible value for dimension i
    """
    misalignment = 10 - state.get('goal_alignment', 5)
    vuln_trust_gap = state.get('vulnerability', 0) * (10 - state.get('trust', 5)) / 10
    desire_intimacy_gap = state.get('desire', 0) * (10 - state.get('intimacy', 0)) / 10
    proximity_trust_gap = state.get('proximity', 0) * (10 - state.get('trust', 5)) / 10

    numerator = (
        weights.get('info_asymmetry', 0.6) * state.get('info_asymmetry', 0) +
        weights.get('stakes', 0.8) * state.get('stakes', 0) +
        weights.get('misalignment', 1.0) * misalignment +
        weights.get('power_differential', 0.4) * abs(state.get('power_differential', 0)) +
        weights.get('vulnerability_trust', 1.2) * vuln_trust_gap +
        weights.get('desire_intimacy', 1.0) * desire_intimacy_gap +
        weights.get('proximity_trust', 0.5) * proximity_trust_gap +
        weights.get('danger', 0.3) * state.get('danger', 0) +
        weights.get('mystery', 0.4) * state.get('mystery', 0)
    )

    denominator = (
        weights.get('info_asymmetry', 0.6) * 10 +
        weights.get('stakes', 0.8) * 10 +
        weights.get('misalignment', 1.0) * 10 +
        weights.get('power_differential', 0.4) * 5 +
        weights.get('vulnerability_trust', 1.2) * 10 +
        weights.get('desire_intimacy', 1.0) * 10 +
        weights.get('proximity_trust', 0.5) * 10 +
        weights.get('danger', 0.3) * 10 +
        weights.get('mystery', 0.4) * 10
    )

    return (numerator / denominator) * 10 if denominator > 0 else 0


def calculate_gradients(trajectory: List[Dict], dimension: str) -> List[float]:
    """
    Calculate rate of change (gradient) for a dimension.

    Formula: ∇d = (d_{t+1} - d_t) / Δt
    """
    values = [state.get(dimension, 0) for state in trajectory]
    gradients = []

    for i in range(len(values) - 1):
        gradient = values[i + 1] - values[i]
        gradients.append(gradient)

    return gradients


def calculate_correlation(dim1_values: List[float], dim2_values: List[float]) -> float:
    """
    Calculate Pearson correlation coefficient between two dimensions.

    Formula: r = Σ((x - x̄)(y - ȳ)) / √(Σ(x - x̄)² × Σ(y - ȳ)²)
    """
    if len(dim1_values) != len(dim2_values) or len(dim1_values) < 2:
        return 0.0

    try:
        mean1 = statistics.mean(dim1_values)
        mean2 = statistics.mean(dim2_values)

        numerator = sum((x - mean1) * (y - mean2) for x, y in zip(dim1_values, dim2_values))

        sum_sq1 = sum((x - mean1) ** 2 for x in dim1_values)
        sum_sq2 = sum((y - mean2) ** 2 for y in dim2_values)

        denominator = math.sqrt(sum_sq1 * sum_sq2)

        return numerator / denominator if denominator > 0 else 0.0
    except:
        return 0.0


def analyze_dimensional_gaps(trajectory: List[Dict]) -> List[Dict]:
    """
    Identify significant dimensional gaps that create tension.

    Key gaps:
    - High vulnerability + Low trust = Emotional risk
    - High desire + Low intimacy = Yearning
    - High stakes + Low goal alignment = External conflict
    - High proximity + Low trust = Forced proximity tension
    """
    gaps = []

    for i, state in enumerate(trajectory):
        chapter = state.get('chapter', i + 1)

        # Vulnerability-Trust gap
        vuln = state.get('vulnerability', 0)
        trust = state.get('trust', 0)
        vt_gap = vuln - trust
        if vt_gap >= 3.0:
            gaps.append({
                'chapter': chapter,
                'type': 'Vulnerability-Trust Gap',
                'magnitude': vt_gap,
                'values': f"V={vuln:.1f}, T={trust:.1f}",
                'tension_contribution': vt_gap * 1.2
            })

        # Desire-Intimacy gap
        desire = state.get('desire', 0)
        intimacy = state.get('intimacy', 0)
        di_gap = desire - intimacy
        if di_gap >= 3.0:
            gaps.append({
                'chapter': chapter,
                'type': 'Desire-Intimacy Gap',
                'magnitude': di_gap,
                'values': f"D={desire:.1f}, I={intimacy:.1f}",
                'tension_contribution': di_gap * 1.0
            })

        # Stakes-Goal Alignment gap
        stakes = state.get('stakes', 0)
        alignment = state.get('goal_alignment', 5)
        misalignment = 10 - alignment
        if stakes >= 7.0 and misalignment >= 4.0:
            gaps.append({
                'chapter': chapter,
                'type': 'Stakes-Misalignment',
                'magnitude': stakes + misalignment,
                'values': f"Stakes={stakes:.1f}, Align={alignment:.1f}",
                'tension_contribution': stakes * misalignment / 10
            })

        # Proximity-Trust gap
        proximity = state.get('proximity', 0)
        if proximity >= 7.0 and trust <= 4.0:
            pt_gap = proximity - trust
            gaps.append({
                'chapter': chapter,
                'type': 'Proximity-Trust Gap (Forced Proximity)',
                'magnitude': pt_gap,
                'values': f"P={proximity:.1f}, T={trust:.1f}",
                'tension_contribution': pt_gap * 0.5
            })

    return gaps


def calculate_statistics(values: List[float]) -> Dict:
    """Calculate statistical measures for a dimension."""
    if not values:
        return {}

    return {
        'mean': statistics.mean(values),
        'median': statistics.median(values),
        'stdev': statistics.stdev(values) if len(values) > 1 else 0.0,
        'min': min(values),
        'max': max(values),
        'range': max(values) - min(values),
        'variance': statistics.variance(values) if len(values) > 1 else 0.0
    }


def generate_technical_report(trajectory: List[Dict], genre: str) -> str:
    """Generate comprehensive technical dimensional analysis report."""
    lines = []

    lines.append("=" * 70)
    lines.append("TECHNICAL DIMENSIONAL ANALYSIS")
    lines.append("=" * 70)
    lines.append("")
    lines.append(f"Genre: {genre.replace('_', ' ').title()}")
    lines.append(f"Chapters: {len(trajectory)}")
    lines.append("")

    # Extract all dimensions
    dimensions = [
        'intimacy', 'trust', 'vulnerability', 'desire', 'stakes',
        'self_worth', 'goal_alignment', 'info_asymmetry',
        'proximity', 'power_differential', 'danger', 'mystery'
    ]

    dimension_data = {}
    for dim in dimensions:
        values = [state.get(dim, 0) for state in trajectory]
        if any(v != 0 for v in values):  # Only include if dimension is used
            dimension_data[dim] = values

    # 1. DIMENSIONAL PROGRESSION
    lines.append("1. DIMENSIONAL PROGRESSION")
    lines.append("-" * 70)
    lines.append("Dimension         | Start | End   | Δ     | Mean  | StdDev | Range")
    lines.append("------------------|-------|-------|-------|-------|--------|-------")

    for dim, values in dimension_data.items():
        stats = calculate_statistics(values)
        delta = values[-1] - values[0]
        lines.append(
            f"{dim:17s} | {values[0]:5.1f} | {values[-1]:5.1f} | "
            f"{delta:+5.1f} | {stats['mean']:5.1f} | {stats['stdev']:6.2f} | "
            f"[{stats['min']:.1f}, {stats['max']:.1f}]"
        )
    lines.append("")

    # 2. TENSION ANALYSIS
    lines.append("2. TENSION ANALYSIS")
    lines.append("-" * 70)

    # Calculate tension with genre-specific weights
    weights = {
        'info_asymmetry': 0.6,
        'stakes': 0.8,
        'misalignment': 1.0,
        'power_differential': 0.4,
        'vulnerability_trust': 1.2,
        'desire_intimacy': 1.0,
        'proximity_trust': 0.5,
        'danger': 0.3,
        'mystery': 0.4
    }

    tension_values = [calculate_tension_technical(state, weights) for state in trajectory]
    tension_stats = calculate_statistics(tension_values)

    lines.append("Tension Formula:")
    lines.append("  T = Σ(w_i × d_i) / Σ(w_i × d_max) × 10")
    lines.append("")
    lines.append("Weight Configuration:")
    for key, weight in sorted(weights.items()):
        lines.append(f"  w_{key:20s} = {weight:.2f}")
    lines.append("")
    lines.append(f"Tension Statistics:")
    lines.append(f"  Mean:     {tension_stats['mean']:.2f}")
    lines.append(f"  Median:   {tension_stats['median']:.2f}")
    lines.append(f"  Std Dev:  {tension_stats['stdev']:.2f}")
    lines.append(f"  Range:    [{tension_stats['min']:.2f}, {tension_stats['max']:.2f}]")
    lines.append(f"  Peak:     {tension_stats['max']:.2f} at Chapter {tension_values.index(max(tension_values)) + 1}")
    lines.append("")

    # 3. GRADIENT ANALYSIS
    lines.append("3. GRADIENT ANALYSIS (Rate of Change)")
    lines.append("-" * 70)
    lines.append("Dimension         | Max Δ+ | Max Δ- | Avg |Δ| | Volatile Chapters")
    lines.append("------------------|--------|--------|---------|------------------")

    for dim, values in dimension_data.items():
        gradients = calculate_gradients(trajectory, dim)
        if not gradients:
            continue

        max_increase = max(gradients)
        max_decrease = min(gradients)
        avg_abs_change = sum(abs(g) for g in gradients) / len(gradients)

        # Find chapters with high volatility (|Δ| > 2.0)
        volatile = [i + 1 for i, g in enumerate(gradients) if abs(g) > 2.0]
        volatile_str = ", ".join(str(c) for c in volatile[:5]) if volatile else "None"

        lines.append(
            f"{dim:17s} | {max_increase:+6.2f} | {max_decrease:+6.2f} | "
            f"{avg_abs_change:7.2f} | {volatile_str}"
        )
    lines.append("")

    # 4. CORRELATION MATRIX
    lines.append("4. CORRELATION MATRIX")
    lines.append("-" * 70)
    lines.append("Pearson correlation coefficient r ∈ [-1, 1]")
    lines.append("  r > +0.7:  Strong positive correlation")
    lines.append("  r < -0.7:  Strong negative correlation")
    lines.append("")

    # Calculate key correlations
    correlations = []
    dim_names = list(dimension_data.keys())

    for i, dim1 in enumerate(dim_names):
        for dim2 in dim_names[i+1:]:
            r = calculate_correlation(dimension_data[dim1], dimension_data[dim2])
            if abs(r) >= 0.5:  # Only show significant correlations
                correlations.append((dim1, dim2, r))

    correlations.sort(key=lambda x: abs(x[2]), reverse=True)

    if correlations:
        lines.append("Significant Correlations (|r| ≥ 0.5):")
        for dim1, dim2, r in correlations[:10]:
            direction = "↑↑" if r > 0 else "↑↓"
            lines.append(f"  {dim1:15s} ⟷ {dim2:15s}: r = {r:+.3f} {direction}")
    else:
        lines.append("No strong correlations detected (all |r| < 0.5)")
    lines.append("")

    # 5. DIMENSIONAL GAP ANALYSIS
    lines.append("5. DIMENSIONAL GAP ANALYSIS")
    lines.append("-" * 70)
    lines.append("Gaps that create narrative tension:")
    lines.append("")

    gaps = analyze_dimensional_gaps(trajectory)

    if gaps:
        # Sort by tension contribution
        gaps.sort(key=lambda x: x['tension_contribution'], reverse=True)

        lines.append("Ch  | Gap Type                      | Magnitude | Values          | T_contrib")
        lines.append("----|-------------------------------|-----------|-----------------|----------")

        for gap in gaps[:20]:  # Top 20 gaps
            lines.append(
                f"{gap['chapter']:3d} | {gap['type']:29s} | "
                f"{gap['magnitude']:9.2f} | {gap['values']:15s} | {gap['tension_contribution']:9.2f}"
            )
    else:
        lines.append("No significant dimensional gaps detected.")
    lines.append("")

    # 6. CHAPTER-BY-CHAPTER BREAKDOWN
    lines.append("6. CHAPTER-BY-CHAPTER DIMENSIONAL VALUES")
    lines.append("-" * 70)

    # Show first 5 and last 5 chapters in detail
    display_chapters = list(range(min(5, len(trajectory)))) + \
                      list(range(max(5, len(trajectory) - 5), len(trajectory)))
    display_chapters = sorted(set(display_chapters))

    for idx in display_chapters:
        if idx >= len(trajectory):
            continue

        state = trajectory[idx]
        chapter = state.get('chapter', idx + 1)
        title = state.get('title', '')

        lines.append(f"\nChapter {chapter}: {title}")
        lines.append("-" * 70)

        for dim in sorted(dimension_data.keys()):
            value = state.get(dim, 0)
            lines.append(f"  {dim:20s}: {value:6.2f}")

        tension = calculate_tension_technical(state, weights)
        lines.append(f"  {'TENSION':20s}: {tension:6.2f}")

    if len(trajectory) > 10:
        lines.append(f"\n... ({len(trajectory) - 10} chapters omitted for brevity) ...")

    lines.append("")
    lines.append("=" * 70)
    lines.append("END DIMENSIONAL ANALYSIS")
    lines.append("=" * 70)

    return "\n".join(lines)


# Main execution
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python dimensional_analyzer.py <trajectory_file> [genre]")
        print("\nGenerates technical dimensional analysis with formulas and statistics.")
        print("\nGenre options: romance, cozy_fantasy, thriller, dark_romance, etc.")
        sys.exit(1)

    filepath = Path(sys.argv[1])
    genre = sys.argv[2] if len(sys.argv) > 2 else 'romance'

    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    trajectory = load_trajectory(filepath)
    report = generate_technical_report(trajectory, genre)

    print(report)
