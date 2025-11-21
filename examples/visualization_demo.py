#!/usr/bin/env python3
"""
Comprehensive demonstration of all visualization features.
"""

import sys
import json
from pathlib import Path

# Add scripts directory to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / 'scripts'))

from visualize_trajectory import (
    plot_dimension_ascii,
    plot_multi_dimension,
    plot_tension_over_time,
    plot_tension_heatmap,
    plot_velocity_graph,
    compare_trajectories
)

# Load sample trajectory
with open(PROJECT_ROOT / 'examples' / 'sample_trajectory.json') as f:
    data = json.load(f)

trajectory = data['trajectory']

print("=" * 80)
print("VISUALIZATION TOOLS DEMONSTRATION")
print("Story: Dark Redemption (Dark Romance)")
print("=" * 80)
print()

# 1. Single Dimension Plot
print("1. SINGLE DIMENSION PLOT - Intimacy")
print("-" * 80)
print(plot_dimension_ascii(trajectory, 'intimacy', height=10, width=60))
print()
print()

# 2. Multi-Dimension Plot
print("2. MULTI-DIMENSION PLOT - Core Relationship Dimensions")
print("-" * 80)
print(plot_multi_dimension(trajectory, ['intimacy', 'trust', 'desire', 'vulnerability']))
print()
print()

# 3. Tension Over Time
print("3. TENSION TRAJECTORY")
print("-" * 80)
print(plot_tension_over_time(trajectory, genre='romance', subgenre='dark'))
print()
print()

# 4. Tension Heatmap
print("4. TENSION HEATMAP")
print("-" * 80)
print(plot_tension_heatmap(trajectory, genre='romance'))
print()
print()

# 5. Velocity/Pacing Graph
print("5. PACING VELOCITY ANALYSIS")
print("-" * 80)
print(plot_velocity_graph(trajectory))
print()
print()

# 6. Power Differential Plot (demonstrates negative values)
print("6. POWER DIFFERENTIAL PLOT (Demonstrates Negative Scale)")
print("-" * 80)
print(plot_dimension_ascii(trajectory, 'power_differential', height=10, width=60))
print()
print()

# 7. Trajectory Comparison
print("7. TRAJECTORY COMPARISON - Planned vs Actual")
print("-" * 80)

# Create a "planned" version where trust was supposed to stay higher
planned_trajectory = []
for state in trajectory:
    planned_state = state.copy()
    # In the plan, trust was supposed to remain higher
    if planned_state.get('trust', 0) < 5:
        planned_state['trust'] = planned_state.get('trust', 0) + 2
    planned_trajectory.append(planned_state)

print(compare_trajectories(
    planned_trajectory,
    trajectory,
    'trust',
    ('Planned (Higher Trust)', 'Actual (Betrayal Arc)')
))
print()
print()

print("=" * 80)
print("END OF DEMONSTRATION")
print("=" * 80)
print()
print("Usage Examples:")
print("  # Generate full report")
print("  python3 scripts/visualize_trajectory.py examples/sample_trajectory.json --full-report")
print()
print("  # Plot specific dimension")
print("  python3 scripts/visualize_trajectory.py examples/sample_trajectory.json --dimension intimacy")
print()
print("  # Plot multiple dimensions")
print("  python3 scripts/visualize_trajectory.json --multi intimacy trust desire")
print()
print("  # Save output to file")
print("  python3 scripts/visualize_trajectory.json --full-report --output report.txt")
