#!/usr/bin/env python3
"""
NPE-specific visualization of 4-axis progression.
"""

import json
import sys
from pathlib import Path

def load_trajectory(filepath: Path):
    """Load trajectory JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def visualize_four_axes(trajectory, height=20, width=70):
    """Visualize IA, RA, EA, TA progression."""

    lines = [""] * (height + 3)

    # Extract axis values
    ia_values = [s.get('IA', 0) for s in trajectory]
    ra_orbits = [s.get('RA_orbit', 180) for s in trajectory]
    ea_values = [s.get('EA', 0) for s in trajectory]
    ta_values = [s.get('TA', 0) for s in trajectory]

    # Normalize RA orbits to -1/+1 scale (180° = -1, 0° = +1)
    ra_normalized = [(180 - orbit) / 180 * 2 - 1 for orbit in ra_orbits]

    # Scale values to fit height
    def scale_value(val, min_val=-1, max_val=1):
        normalized = (val - min_val) / (max_val - min_val)
        return int(normalized * (height - 1))

    # Plot points
    symbols = {'IA': '●', 'RA': '◆', 'EA': '■', 'TA': '★'}

    for i, (ia, ra, ea, ta) in enumerate(zip(ia_values, ra_normalized, ea_values, ta_values)):
        x = int((i / (len(trajectory) - 1)) * (width - 1)) if len(trajectory) > 1 else 0

        # Plot each axis
        for axis_name, value, symbol in [('IA', ia, symbols['IA']),
                                          ('RA', ra, symbols['RA']),
                                          ('EA', ea, symbols['EA']),
                                          ('TA', ta, symbols['TA'])]:
            y = scale_value(value)
            y_inverted = height - 1 - y  # Invert for top-to-bottom display

            if 0 <= y_inverted < height:
                if not lines[y_inverted]:
                    lines[y_inverted] = " " * width

                line_list = list(lines[y_inverted])
                if x < len(line_list):
                    line_list[x] = symbol
                lines[y_inverted] = "".join(line_list)

    # Add axis labels
    result = []
    result.append("Four-Axis NPE Progression")
    result.append("")

    for i, line in enumerate(lines):
        if i == 0:
            label = " +1.0 |"
        elif i == height // 2:
            label = "  0.0 |"
        elif i == height - 1:
            label = " -1.0 |"
        else:
            label = "      |"

        result.append(label + (line if line else " " * width))

    # Bottom axis
    result.append("      +" + "_" * width)
    result.append("       Ch1" + " " * (width - 20) + "Ch13" + " " * 10 + "Ch26")
    result.append("")
    result.append("       ●=IA (Internal)  ◆=RA (Relational)  ■=EA (Environmental)  ★=TA (Task)")

    return "\n".join(result)

def visualize_orbital_distance(trajectory, height=15, width=70):
    """Visualize orbital distance progression."""

    orbits = [s.get('RA_orbit', 180) for s in trajectory]

    lines = []
    lines.append("Orbital Distance (Verity ↔ Roric)")
    lines.append("")

    # Scale orbits to display height
    max_orbit = 180
    min_orbit = 0

    for i in range(height):
        orbit_level = max_orbit - (i * (max_orbit - min_orbit) / (height - 1))
        line_chars = [" "] * width

        # Plot orbit values
        for j, orbit in enumerate(orbits):
            x = int((j / (len(orbits) - 1)) * (width - 1)) if len(orbits) > 1 else 0

            if abs(orbit - orbit_level) < 8:  # Within range
                line_chars[x] = "●"

        # Add labels
        if i == 0:
            label = f"180° |"
        elif i == height // 2:
            label = f" 90° |"
        elif i == height - 1:
            label = f"  0° |"
        else:
            label = "     |"

        lines.append(label + "".join(line_chars))

    lines.append("     +" + "_" * width)
    lines.append("      Ch1" + " " * (width - 20) + "Ch13" + " " * 10 + "Ch26")
    lines.append("")
    lines.append("      180° = Distant/Strangers")
    lines.append("       90° = Friends/Warming")
    lines.append("       60° = Close/Intimate")

    return "\n".join(lines)

def create_entropy_graph(trajectory, height=10, width=70):
    """Visualize entropy progression."""

    # Calculate entropy
    entropy_values = []
    for state in trajectory:
        stakes = state.get('stakes', 0)
        info_asym = state.get('info_asymmetry', 0)
        goal_misalign = 10 - state.get('goal_alignment', 5)

        entropy = (stakes + info_asym + goal_misalign) / 30
        entropy_values.append(entropy)

    lines = []
    lines.append("Narrative Entropy (Cozy Fantasy Constraint: <0.5)")
    lines.append("")

    max_entropy = max(entropy_values) if entropy_values else 1

    for i in range(height):
        level = max_entropy - (i * max_entropy / (height - 1))
        line_chars = [" "] * width

        for j, entropy in enumerate(entropy_values):
            x = int((j / (len(entropy_values) - 1)) * (width - 1)) if len(entropy_values) > 1 else 0

            if abs(entropy - level) < max_entropy / (height * 2):
                line_chars[x] = "█"

        # Labels
        if i == 0:
            label = f"{max_entropy:.2f} |"
        elif i == height - 1:
            label = " 0.00 |"
        else:
            label = "      |"

        lines.append(label + "".join(line_chars))

    lines.append("      +" + "_" * width)
    lines.append("       Ch1" + " " * (width - 20) + "Ch13" + " " * 10 + "Ch26")
    lines.append("")
    lines.append(f"       Peak: {max(entropy_values):.2f} at Ch{entropy_values.index(max(entropy_values))+1}")
    lines.append(f"       Cozy compliance: {'✓ Yes' if max(entropy_values) <= 0.5 else '✗ Exceeds (dark night expected)'}")

    return "\n".join(lines)

# Main execution
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python npe_visualizer.py <trajectory_file>")
        sys.exit(1)

    filepath = Path(sys.argv[1])

    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    trajectory = load_trajectory(filepath)

    print("=" * 70)
    print("NPE PHYSICS VISUALIZATIONS")
    print("=" * 70)
    print()

    # Four axes
    print(visualize_four_axes(trajectory))
    print()
    print("=" * 70)
    print()

    # Orbital distance
    print(visualize_orbital_distance(trajectory))
    print()
    print("=" * 70)
    print()

    # Entropy
    print(create_entropy_graph(trajectory))
