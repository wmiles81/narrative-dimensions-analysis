#!/usr/bin/env python3
"""Quick demonstration of all visualization capabilities."""

import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent / 'scripts'))

from visualize_trajectory import compare_trajectories, plot_multi_dimension
from subplot_tracker import SubplotTracker

print("=" * 70)
print("DEMONSTRATION: Comparing Multiple Story Arcs")
print("=" * 70)
print()

# Create a romantic comedy with two intersecting arcs
main_romance = [
    {'intimacy': 2, 'trust': 3, 'desire': 6, 'stakes': 4},
    {'intimacy': 3, 'trust': 4, 'desire': 7, 'stakes': 5},
    {'intimacy': 5, 'trust': 5, 'desire': 8, 'stakes': 6},
    {'intimacy': 4, 'trust': 2, 'desire': 8, 'stakes': 8},  # Misunderstanding
    {'intimacy': 7, 'trust': 7, 'desire': 9, 'stakes': 7},
    {'intimacy': 9, 'trust': 9, 'desire': 10, 'stakes': 3},  # HEA
]

career_subplot = [
    {'stakes': 7, 'goal_alignment': 8, 'vulnerability': 3},
    {'stakes': 7, 'goal_alignment': 7, 'vulnerability': 4},
    {'stakes': 8, 'goal_alignment': 6, 'vulnerability': 5},
    {'stakes': 9, 'goal_alignment': 4, 'vulnerability': 7},  # Career vs love conflict
    {'stakes': 6, 'goal_alignment': 8, 'vulnerability': 6},
    {'stakes': 4, 'goal_alignment': 9, 'vulnerability': 5},  # Balanced
]

print("SCENARIO: Rom-Com with Career/Love Conflict")
print("-" * 70)
print("Main Romance Arc: Protagonist and love interest")
print("Career Subplot: Dream job vs. relationship")
print()

# Show multi-dimensional view of main romance
print("MAIN ROMANCE ARC: Multiple Dimensions")
print("-" * 70)

romance_viz = plot_multi_dimension(
    main_romance,
    ['intimacy', 'trust', 'desire'],
    height=12,
    width=60
)
print(romance_viz)
print()

# Subplot tracker analysis
print("=" * 70)
print("SUBPLOT TRACKER ANALYSIS")
print("=" * 70)
print()

tracker = SubplotTracker()

tracker.add_plot(
    'romance',
    main_romance,
    genre='romance',
    subgenre='contemporary',
    description='Enemies-to-lovers office romance'
)

tracker.add_plot(
    'career',
    career_subplot,
    genre='romance',
    subgenre='contemporary',
    description='Career ambitions and compromises'
)

# Generate comparison report
comparison = tracker.compare_plots(['romance', 'career'])

print("Synchronized Moments:")
if comparison['synchronized_peaks']:
    for sync in comparison['synchronized_peaks']:
        print(f"  • {' & '.join(sync['plots'])} both peak at beats {sync['beat_range']}")
else:
    print("  No synchronized peaks detected")

print()
print("Tension Intersections:")
if comparison['intersections']:
    for inter in comparison['intersections'][:3]:
        print(f"  • Beat {inter['beat']}: {inter['plots'][0]} and {inter['plots'][1]} cross")
        print(f"    Tensions: {inter['tensions']}")
else:
    print("  No tension crossovers detected")

print()
print("Combined Tension Timeline (50% romance, 50% career):")
print("-" * 70)

combined = tracker.calculate_combined_tension({'romance': 0.5, 'career': 0.5})

# Create simple bar chart
max_tension = max(combined)
for i, tension in enumerate(combined):
    bars = int((tension / max_tension) * 40) if max_tension > 0 else 0
    bar = "█" * bars
    print(f"Beat {i+1:2d}: {bar} {tension:.2f}")

print()
print(f"Average Combined Tension: {sum(combined) / len(combined):.2f}/10")
print(f"Peak Combined: {max(combined):.2f} at Beat {combined.index(max(combined)) + 1}")

print()
print("=" * 70)
print("KEY INSIGHT:")
print("=" * 70)
print("Beat 4 shows synchronized peaks - this is the 'dark moment' where")
print("both romance (misunderstanding) and career (difficult choice) hit")
print("maximum tension simultaneously. Perfect for a climactic scene!")
print()
