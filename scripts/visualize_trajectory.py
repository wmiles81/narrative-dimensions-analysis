#!/usr/bin/env python3
"""
Generate visual representations of dimensional trajectories.
ASCII/text-based plotting for terminal display.
"""

import sys
import json
import math
from pathlib import Path
from typing import Dict, List, Optional, Tuple

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / 'scripts'))

# Import tension calculation module
try:
    from calculate_tension import calculate_tension, diagnose_tension
except ImportError:
    print("Warning: Could not import calculate_tension module", file=sys.stderr)
    calculate_tension = None
    diagnose_tension = None

# ASCII symbols for different dimensions
SYMBOLS = ['★', '◆', '●', '■', '▲', '◇', '○', '□', '△', '▼']

# Shading characters for heatmap (low to high intensity)
SHADING = ['░', '▒', '▓', '█']

# ANSI color codes (if terminal supports)
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'reset': '\033[0m'
}

def supports_color() -> bool:
    """Check if terminal supports ANSI color codes."""
    import os
    return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty() and os.getenv('TERM') != 'dumb'

def colorize(text: str, color: str) -> str:
    """Apply color to text if terminal supports it."""
    if supports_color():
        return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"
    return text

def plot_dimension_ascii(trajectory: List[Dict], dimension_name: str,
                        height: int = 10, width: int = 50) -> str:
    """
    Plot single dimension over time as ASCII graph.

    Args:
        trajectory: List of dimensional states
        dimension_name: Which dimension to plot
        height: Graph height in lines
        width: Graph width in characters

    Returns:
        ASCII art string representation

    Example output:
    Intimacy Trajectory
    10 |                              ★
     9 |                           ★
     8 |                        ★
     7 |                     ★
     6 |                  ★
     5 |               ★
     4 |            ★
     3 |         ★
     2 |      ★
     1 |   ★
     0 | ★___________________________
       Beat 1    Beat 5    Beat 9
    """
    if not trajectory:
        return "Error: Empty trajectory"

    # Extract values for the specified dimension
    values = []
    for state in trajectory:
        if dimension_name in state:
            values.append(state[dimension_name])
        else:
            values.append(None)

    if not any(v is not None for v in values):
        return f"Error: Dimension '{dimension_name}' not found in trajectory"

    # Determine scale
    valid_values = [v for v in values if v is not None]
    if not valid_values:
        return f"Error: No valid values for dimension '{dimension_name}'"

    min_val = min(valid_values)
    max_val = max(valid_values)

    # For power_differential, handle negative values
    if dimension_name == 'power_differential':
        scale_min = -5
        scale_max = 5
    else:
        scale_min = 0
        scale_max = 10

    # Build graph
    lines = []
    title = f"{dimension_name.replace('_', ' ').title()} Trajectory"
    lines.append(title)
    lines.append("")

    # Create plot grid
    for row in range(height, -1, -1):
        y_val = scale_min + (row / height) * (scale_max - scale_min)
        line = f"{y_val:4.0f} |"

        # Plot points
        for i, value in enumerate(values):
            if value is None:
                continue

            # Calculate x position
            x_pos = int((i / max(len(values) - 1, 1)) * (width - 1))

            # Calculate if this value should be plotted at this row
            value_row = int(((value - scale_min) / (scale_max - scale_min)) * height)

            if value_row == row:
                # Extend line to this position and place symbol
                while len(line) - 6 < x_pos:  # 6 = length of "YYYY |"
                    line += " "
                line = line[:6 + x_pos] + "★" + line[6 + x_pos + 1:]

        # Fill rest of line
        while len(line) < width + 7:
            line += " " if row > 0 else "_"

        lines.append(line)

    # Add x-axis labels
    x_labels = "       "
    num_labels = min(3, len(values))
    for i in range(num_labels):
        beat_num = int(i * (len(values) - 1) / max(num_labels - 1, 1)) + 1
        label = f"Beat {beat_num}"
        pos = int((i / max(num_labels - 1, 1)) * (width - len(label)))
        while len(x_labels) < 7 + pos:
            x_labels += " "
        x_labels += label

    lines.append(x_labels)

    # Add statistics
    lines.append("")
    lines.append(f"Range: {min_val:.1f} to {max_val:.1f}")
    lines.append(f"Change: {valid_values[-1] - valid_values[0]:+.1f} points")

    return "\n".join(lines)

def plot_multi_dimension(trajectory: List[Dict], dimensions: List[str],
                        height: int = 15, width: int = 60) -> str:
    """
    Plot multiple dimensions on same graph with different symbols.

    Uses symbols: ★ (dimension 1), ◆ (dimension 2), ● (dimension 3), etc.

    Example:
    Multiple Dimensions
    10 |         ●              ★
     9 |      ●     ★        ★
     8 |   ●  ◆  ★        ★
     7 | ●  ◆  ★        ★  ◆
     6 | ◆ ★          ★   ◆
     5 | ★          ★    ◆
       |___________________________
       ★=Intimacy ◆=Trust ●=Desire
    """
    if not trajectory or not dimensions:
        return "Error: Empty trajectory or dimensions list"

    lines = []
    lines.append("Multiple Dimensions")
    lines.append("")

    # Create plot grid
    grid = {}
    for row in range(height + 1):
        grid[row] = [' '] * width

    # Plot each dimension with its symbol
    for dim_idx, dim_name in enumerate(dimensions):
        if dim_idx >= len(SYMBOLS):
            break

        symbol = SYMBOLS[dim_idx]

        # Extract values
        values = []
        for state in trajectory:
            values.append(state.get(dim_name))

        if not any(v is not None for v in values):
            continue

        # Plot points
        for i, value in enumerate(values):
            if value is None:
                continue

            # Handle power_differential differently
            if dim_name == 'power_differential':
                scale_min, scale_max = -5, 5
            else:
                scale_min, scale_max = 0, 10

            # Calculate position
            x_pos = int((i / max(len(values) - 1, 1)) * (width - 1))
            y_pos = int(((value - scale_min) / (scale_max - scale_min)) * height)

            # Place symbol on grid
            if 0 <= y_pos <= height and 0 <= x_pos < width:
                grid[y_pos][x_pos] = symbol

    # Render grid
    for row in range(height, -1, -1):
        y_val = row
        line = f"{y_val:4.0f} |"
        for col in range(width):
            char = grid[row][col] if grid[row][col] != ' ' else (' ' if row > 0 else '_')
            line += char
        lines.append(line)

    # Add legend
    legend = "       "
    for dim_idx, dim_name in enumerate(dimensions):
        if dim_idx >= len(SYMBOLS):
            break
        symbol = SYMBOLS[dim_idx]
        legend += f"{symbol}={dim_name.replace('_', ' ').title()} "
    lines.append(legend)

    return "\n".join(lines)

def plot_tension_over_time(trajectory: List[Dict], genre: str = "romance",
                          subgenre: Optional[str] = None) -> str:
    """
    Calculate and plot tension at each beat.

    Uses calculate_tension module to compute tension values.
    Shows as bar chart.

    Example:
    Tension Trajectory
    10 |                    ████
     9 |                    ████
     8 |                    ████ ████
     7 |          ████      ████ ████
     6 |          ████ ████ ████ ████
     5 |     ████ ████ ████ ████ ████
     4 | ████ ████ ████ ████ ████ ████
       |________________________________
       Beat 1  3   5   7   9   11  13
    """
    if not trajectory:
        return "Error: Empty trajectory"

    if calculate_tension is None:
        return "Error: calculate_tension module not available"

    # Calculate tension for each beat
    tension_values = []
    for state in trajectory:
        try:
            tension_result = calculate_tension(state, genre=genre, subgenre=subgenre)
            tension_values.append(tension_result['total_tension'])
        except Exception as e:
            tension_values.append(0)

    if not tension_values:
        return "Error: Could not calculate tension values"

    # Build graph
    lines = []
    lines.append("Tension Trajectory")
    lines.append("")

    height = 10
    width = len(tension_values) * 5

    # Create bar chart
    for row in range(height, -1, -1):
        y_val = row
        line = f"{y_val:4.0f} |"

        for tension in tension_values:
            bar_height = int((tension / 10) * height)

            if bar_height >= row and row > 0:
                line += "████ "
            else:
                line += ("     " if row > 0 else "_____")

        lines.append(line)

    # Add x-axis labels
    x_labels = "       "
    for i in range(len(tension_values)):
        beat_label = str(i + 1)
        x_labels += f"{beat_label:>4} "
    lines.append(x_labels)

    # Add statistics
    lines.append("")
    avg_tension = sum(tension_values) / len(tension_values)
    max_tension = max(tension_values)
    min_tension = min(tension_values)
    max_idx = tension_values.index(max_tension)
    min_idx = tension_values.index(min_tension)

    lines.append(f"Average Tension: {avg_tension:.1f}/10")
    lines.append(f"Peak Tension: {max_tension:.1f}/10 at Beat {max_idx + 1}")
    lines.append(f"Lowest Tension: {min_tension:.1f}/10 at Beat {min_idx + 1}")

    return "\n".join(lines)

def plot_tension_heatmap(trajectory: List[Dict], genre: str = "romance") -> str:
    """
    Create heat map showing tension intensity across story.

    Uses ASCII shading: ░ (low), ▒ (medium), ▓ (high), █ (extreme)

    Example:
    Tension Heatmap (by chapter)
    Ch  1 ▒░░░
    Ch  2 ░░▒▒
    Ch  3 ▒▒▒▓
    Ch  4 ▓▓▓▓
    Ch  5 ▓▓▓█
    Ch  6 ▓▓▓▓
    Ch  7 ░░░▒  ← Relief scene
    Ch  8 ▒▓▓▓
    Ch  9 ▓▓██  ← Black moment
    Ch 10 ░▒▓▓
    Ch 11 ▓▓██  ← Climax
    Ch 12 ▒▒▓░  ← Resolution
    """
    if not trajectory:
        return "Error: Empty trajectory"

    if calculate_tension is None:
        return "Error: calculate_tension module not available"

    # Calculate tension for each beat
    tension_values = []
    for state in trajectory:
        try:
            tension_result = calculate_tension(state, genre=genre)
            tension_values.append(tension_result['total_tension'])
        except Exception as e:
            tension_values.append(0)

    lines = []
    lines.append("Tension Heatmap")
    lines.append("")

    # Group into chapters (assume 4 beats per chapter if many beats)
    beats_per_chapter = 4 if len(trajectory) > 12 else 1
    chapters = []

    for i in range(0, len(tension_values), beats_per_chapter):
        chapter_tensions = tension_values[i:i + beats_per_chapter]
        chapters.append(chapter_tensions)

    # Render heatmap
    for ch_idx, chapter_tensions in enumerate(chapters):
        ch_num = ch_idx + 1
        line = f"Ch {ch_num:2d} "

        for tension in chapter_tensions:
            # Map tension to shading character
            if tension < 2.5:
                shade = SHADING[0]  # ░
            elif tension < 5.0:
                shade = SHADING[1]  # ▒
            elif tension < 7.5:
                shade = SHADING[2]  # ▓
            else:
                shade = SHADING[3]  # █

            line += shade

        # Add annotations for significant moments
        avg_tension = sum(chapter_tensions) / len(chapter_tensions)
        annotation = ""

        if avg_tension < 2.5 and ch_idx > 0:
            annotation = "  ← Relief scene"
        elif avg_tension > 8.5:
            if ch_idx > len(chapters) * 0.6 and ch_idx < len(chapters) * 0.8:
                annotation = "  ← Black moment"
            elif ch_idx >= len(chapters) * 0.8:
                annotation = "  ← Climax"
        elif ch_idx == len(chapters) - 1 and avg_tension < 6:
            annotation = "  ← Resolution"

        line += annotation
        lines.append(line)

    # Add legend
    lines.append("")
    lines.append(f"Legend: {SHADING[0]}=Low {SHADING[1]}=Medium {SHADING[2]}=High {SHADING[3]}=Extreme")

    return "\n".join(lines)

def plot_velocity_graph(trajectory: List[Dict]) -> str:
    """
    Show pacing/velocity (rate of dimensional change).

    Helps identify stuck scenes (low velocity) or rushed scenes (high velocity).

    Example:
    Pacing Velocity
    5.0 |      ★
    4.5 |      ★
    4.0 |    ★   ★
    3.5 |  ★   ★   ★
    3.0 |★       ★   ★
    2.5 |          ★   ★
    2.0 |               ★
    1.5 |                 ★
    1.0 |                   ★
    0.5 |                     ★ ← Stuck?
    0.0 |_________________________
       Ch 1 2 3 4 5 6 7 8 9 10 11

    Velocity: Avg 2.8 points/chapter
    Issues: Ch 10 low velocity (0.5) - possible flat scene
    """
    if len(trajectory) < 2:
        return "Error: Need at least 2 trajectory points to calculate velocity"

    # Calculate velocity between each pair of beats
    velocities = []
    for i in range(1, len(trajectory)):
        prev_state = trajectory[i - 1]
        curr_state = trajectory[i]

        # Calculate total change across all dimensions
        total_change = 0
        dims_counted = 0

        for dim in prev_state:
            if dim in curr_state:
                # Skip non-numeric fields
                if not isinstance(prev_state[dim], (int, float)) or not isinstance(curr_state[dim], (int, float)):
                    continue
                change = abs(curr_state[dim] - prev_state[dim])
                total_change += change
                dims_counted += 1

        velocity = total_change / dims_counted if dims_counted > 0 else 0
        velocities.append(velocity)

    # Build graph
    lines = []
    lines.append("Pacing Velocity")
    lines.append("")

    height = 10
    width = len(velocities) * 3
    max_velocity = max(velocities) if velocities else 5

    # Create plot
    for row in range(height, -1, -1):
        y_val = (row / height) * max(max_velocity, 1)
        line = f"{y_val:4.1f} |"

        for i, velocity in enumerate(velocities):
            x_pos = i * 3
            velocity_row = int((velocity / max(max_velocity, 1)) * height)

            while len(line) - 6 < x_pos:
                line += " "

            if velocity_row == row:
                line = line[:6 + x_pos] + "★" + line[6 + x_pos + 1:]

        # Fill rest of line
        while len(line) < width + 7:
            line += " " if row > 0 else "_"

        lines.append(line)

    # Add x-axis labels
    x_labels = "       "
    for i in range(len(velocities)):
        x_labels += f"{i + 1:2d} "
    lines.append(x_labels)

    # Add statistics and diagnostics
    lines.append("")
    avg_velocity = sum(velocities) / len(velocities)
    lines.append(f"Velocity: Avg {avg_velocity:.1f} points/chapter")

    # Identify issues
    issues = []
    for i, vel in enumerate(velocities):
        if vel < 0.5:
            issues.append(f"Ch {i + 1} low velocity ({vel:.1f}) - possible flat scene")
        elif vel > avg_velocity * 2 and vel > 3:
            issues.append(f"Ch {i + 1} high velocity ({vel:.1f}) - possible rushed pacing")

    if issues:
        lines.append("Issues:")
        for issue in issues:
            lines.append(f"  - {issue}")

    return "\n".join(lines)

def create_trajectory_report(trajectory: List[Dict], genre: str,
                            output_file: Optional[Path] = None) -> str:
    """
    Generate comprehensive visual report with multiple graphs.

    Combines all visualization types into one report.
    """
    report = []
    report.append("=" * 70)
    report.append("DIMENSIONAL TRAJECTORY VISUAL ANALYSIS")
    report.append("=" * 70)
    report.append("")

    # Extract all dimensions present in trajectory
    all_dimensions = set()
    for state in trajectory:
        all_dimensions.update(state.keys())

    # Core relationship dimensions to plot
    core_dims = ['intimacy', 'trust', 'desire', 'vulnerability']
    plot_dims = [d for d in core_dims if d in all_dimensions]

    # 1. Multi-dimension plot
    if len(plot_dims) >= 2:
        report.append("1. CORE RELATIONSHIP DIMENSIONS")
        report.append("-" * 70)
        report.append(plot_multi_dimension(trajectory, plot_dims[:4]))
        report.append("")
        report.append("")

    # 2. Tension over time
    report.append("2. TENSION TRAJECTORY")
    report.append("-" * 70)
    report.append(plot_tension_over_time(trajectory, genre=genre))
    report.append("")
    report.append("")

    # 3. Tension heatmap
    report.append("3. TENSION HEATMAP")
    report.append("-" * 70)
    report.append(plot_tension_heatmap(trajectory, genre=genre))
    report.append("")
    report.append("")

    # 4. Velocity graph
    if len(trajectory) >= 2:
        report.append("4. PACING VELOCITY")
        report.append("-" * 70)
        report.append(plot_velocity_graph(trajectory))
        report.append("")
        report.append("")

    # 5. Individual dimension plots for key dimensions
    report.append("5. INDIVIDUAL DIMENSION TRAJECTORIES")
    report.append("-" * 70)
    for dim in plot_dims[:3]:  # Plot top 3
        report.append(plot_dimension_ascii(trajectory, dim, height=8, width=50))
        report.append("")

    # 6. Commentary on patterns
    report.append("6. PATTERN ANALYSIS")
    report.append("-" * 70)
    report.extend(_analyze_patterns(trajectory))
    report.append("")

    report.append("=" * 70)
    report.append("END OF VISUAL ANALYSIS")
    report.append("=" * 70)

    full_report = "\n".join(report)

    # Save to file if requested
    if output_file:
        output_file.write_text(full_report)
        print(f"Report saved to {output_file}")

    return full_report

def _analyze_patterns(trajectory: List[Dict]) -> List[str]:
    """Analyze and comment on trajectory patterns."""
    lines = []

    if len(trajectory) < 2:
        lines.append("Insufficient data for pattern analysis")
        return lines

    # Analyze intimacy progression
    if all('intimacy' in state for state in trajectory):
        intimacy_vals = [state['intimacy'] for state in trajectory]
        intimacy_change = intimacy_vals[-1] - intimacy_vals[0]

        if intimacy_change > 3:
            lines.append("✓ Strong intimacy growth - relationship deepening")
        elif intimacy_change < -3:
            lines.append("⚠ Intimacy declining - possible relationship crisis")
        else:
            lines.append("→ Intimacy relatively stable")

    # Analyze trust vs vulnerability gap
    if all('trust' in state and 'vulnerability' in state for state in trajectory):
        gaps = [state['vulnerability'] - state['trust'] for state in trajectory]
        avg_gap = sum(gaps) / len(gaps)

        if avg_gap > 3:
            lines.append("⚠ High vulnerability-trust gap - significant tension source")
        elif avg_gap < 1:
            lines.append("✓ Balanced trust and vulnerability - emotionally safe")

    # Analyze desire-proximity gap
    if all('desire' in state and 'proximity' in state for state in trajectory):
        gaps = [state['desire'] - state['proximity'] for state in trajectory]
        avg_gap = sum(gaps) / len(gaps)

        if avg_gap > 3:
            lines.append("→ Strong yearning (desire exceeds proximity) - good for tension")
        elif avg_gap < -2:
            lines.append("→ Forced proximity (proximity exceeds desire) - possible conflict")

    # Overall movement
    total_movement = 0
    for i in range(1, len(trajectory)):
        for dim in trajectory[i]:
            if dim in trajectory[i-1]:
                # Skip non-numeric fields
                if not isinstance(trajectory[i][dim], (int, float)) or not isinstance(trajectory[i-1][dim], (int, float)):
                    continue
                total_movement += abs(trajectory[i][dim] - trajectory[i-1][dim])

    avg_movement = total_movement / (len(trajectory) - 1)

    if avg_movement < 5:
        lines.append("⚠ Low overall movement - story may feel static")
    elif avg_movement > 15:
        lines.append("⚠ High overall movement - pacing may feel rushed")
    else:
        lines.append("✓ Good pacing - steady dimensional progression")

    return lines

def compare_trajectories(trajectory1: List[Dict], trajectory2: List[Dict],
                        dimension: str, labels: Tuple[str, str]) -> str:
    """
    Compare two trajectories on same graph (e.g., planned vs actual).

    Useful for revision - see where story drifted from outline.
    """
    if not trajectory1 or not trajectory2:
        return "Error: Empty trajectory"

    lines = []
    lines.append(f"Trajectory Comparison: {dimension.replace('_', ' ').title()}")
    lines.append("")

    height = 10
    width = 60

    # Extract values
    values1 = [state.get(dimension) for state in trajectory1]
    values2 = [state.get(dimension) for state in trajectory2]

    # Handle power_differential scale
    if dimension == 'power_differential':
        scale_min, scale_max = -5, 5
    else:
        scale_min, scale_max = 0, 10

    # Create grid
    grid = {}
    for row in range(height + 1):
        grid[row] = [' '] * width

    # Plot trajectory 1 with symbol ★
    symbol1 = '★'
    max_len = max(len(values1), len(values2))
    for i, value in enumerate(values1):
        if value is None:
            continue
        x_pos = int((i / max(max_len - 1, 1)) * (width - 1))
        y_pos = int(((value - scale_min) / (scale_max - scale_min)) * height)
        if 0 <= y_pos <= height and 0 <= x_pos < width:
            grid[y_pos][x_pos] = symbol1

    # Plot trajectory 2 with symbol ◆
    symbol2 = '◆'
    for i, value in enumerate(values2):
        if value is None:
            continue
        x_pos = int((i / max(max_len - 1, 1)) * (width - 1))
        y_pos = int(((value - scale_min) / (scale_max - scale_min)) * height)
        if 0 <= y_pos <= height and 0 <= x_pos < width:
            # If both trajectories have point at same position, use special symbol
            if grid[y_pos][x_pos] == symbol1:
                grid[y_pos][x_pos] = '◈'  # Combined symbol
            else:
                grid[y_pos][x_pos] = symbol2

    # Render grid
    for row in range(height, -1, -1):
        y_val = scale_min + (row / height) * (scale_max - scale_min)
        line = f"{y_val:4.0f} |"
        for col in range(width):
            char = grid[row][col] if grid[row][col] != ' ' else (' ' if row > 0 else '_')
            line += char
        lines.append(line)

    # Add legend
    lines.append(f"       {symbol1}={labels[0]} {symbol2}={labels[1]} ◈=Same")

    # Calculate divergence
    lines.append("")
    valid_pairs = [(v1, v2) for v1, v2 in zip(values1, values2) if v1 is not None and v2 is not None]
    if valid_pairs:
        differences = [abs(v1 - v2) for v1, v2 in valid_pairs]
        avg_divergence = sum(differences) / len(differences)
        max_divergence = max(differences)
        max_idx = differences.index(max_divergence)

        lines.append(f"Average Divergence: {avg_divergence:.1f} points")
        lines.append(f"Maximum Divergence: {max_divergence:.1f} points at beat {max_idx + 1}")

        if avg_divergence > 2:
            lines.append("⚠ Significant drift from plan - consider revision")
        else:
            lines.append("✓ Trajectories closely aligned")

    return "\n".join(lines)

# CLI interface
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Visualize dimensional trajectories",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s trajectory.json --full-report
  %(prog)s trajectory.json --dimension intimacy
  %(prog)s trajectory.json --multi intimacy trust desire
  %(prog)s trajectory.json --tension --output tension_plot.txt
        """
    )
    parser.add_argument("trajectory_file", help="JSON file with trajectory data")
    parser.add_argument("--dimension", help="Specific dimension to plot")
    parser.add_argument("--multi", nargs="+", help="Multiple dimensions to plot together")
    parser.add_argument("--tension", action="store_true", help="Plot tension over time")
    parser.add_argument("--heatmap", action="store_true", help="Generate tension heatmap")
    parser.add_argument("--velocity", action="store_true", help="Plot pacing velocity")
    parser.add_argument("--full-report", action="store_true", help="Generate full visual report")
    parser.add_argument("--genre", default="romance", help="Genre for tension calculation")
    parser.add_argument("--subgenre", help="Subgenre for tension calculation")
    parser.add_argument("--output", help="Save to file instead of stdout")

    args = parser.parse_args()

    # Load trajectory from JSON
    try:
        with open(args.trajectory_file, 'r') as f:
            data = json.load(f)

        # Handle different JSON structures
        if isinstance(data, list):
            trajectory = data
        elif isinstance(data, dict) and 'trajectory' in data:
            trajectory = data['trajectory']
        elif isinstance(data, dict) and 'states' in data:
            trajectory = data['states']
        else:
            print("Error: Unable to find trajectory data in JSON file", file=sys.stderr)
            print("Expected a list of states or a dict with 'trajectory' or 'states' key", file=sys.stderr)
            sys.exit(1)

        if not trajectory:
            print("Error: Trajectory is empty", file=sys.stderr)
            sys.exit(1)

    except FileNotFoundError:
        print(f"Error: File '{args.trajectory_file}' not found", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file: {e}", file=sys.stderr)
        sys.exit(1)

    # Generate requested visualization
    output = ""

    if args.full_report:
        output = create_trajectory_report(trajectory, args.genre,
                                        Path(args.output) if args.output else None)
    elif args.dimension:
        output = plot_dimension_ascii(trajectory, args.dimension)
    elif args.multi:
        output = plot_multi_dimension(trajectory, args.multi)
    elif args.tension:
        output = plot_tension_over_time(trajectory, args.genre, args.subgenre)
    elif args.heatmap:
        output = plot_tension_heatmap(trajectory, args.genre)
    elif args.velocity:
        output = plot_velocity_graph(trajectory)
    else:
        print("Error: Please specify a visualization type", file=sys.stderr)
        print("Use --help for options", file=sys.stderr)
        sys.exit(1)

    # Output to stdout or file
    if args.output and not args.full_report:  # full_report handles its own file output
        Path(args.output).write_text(output)
        print(f"Output saved to {args.output}")
    else:
        print(output)
