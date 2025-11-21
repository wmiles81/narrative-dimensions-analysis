#!/usr/bin/env python3
"""
Demo of report generation with visualizations.
"""

import sys
import json
from pathlib import Path

# Add scripts directory to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / 'scripts'))

from generate_report import DimensionalReport

# Load sample trajectory
with open(PROJECT_ROOT / 'examples' / 'sample_trajectory.json') as f:
    data = json.load(f)

trajectory = data['trajectory']
current_state = trajectory[-1]  # Last state

# Generate report WITHOUT visualizations
print("=" * 70)
print("STANDARD REPORT (No Visualizations)")
print("=" * 70)
reporter = DimensionalReport(
    title="Dark Redemption - Chapter 12",
    genre="romance",
    content_level="chapter",
    include_visualizations=False
)

report = reporter.generate_full_report(
    current_state=current_state,
    trajectory=trajectory[:5],  # Just first 5 beats for brevity
    analysis_notes="Resolution chapter with HEA."
)

# Show only first 50 lines
lines = report.split('\n')
for line in lines[:50]:
    print(line)

print("\n[... truncated for brevity ...]\n")

# Generate report WITH visualizations
print("=" * 70)
print("ENHANCED REPORT (With Visualizations)")
print("=" * 70)
reporter_viz = DimensionalReport(
    title="Dark Redemption - Chapter 12",
    genre="romance",
    content_level="chapter",
    include_visualizations=True
)

report_viz = reporter_viz.generate_full_report(
    current_state=current_state,
    trajectory=trajectory[:5],  # Just first 5 beats
    analysis_notes="Resolution chapter with HEA."
)

# Find and show the visualization section
lines_viz = report_viz.split('\n')
viz_section_start = None
for i, line in enumerate(lines_viz):
    if 'VISUAL TRAJECTORY PLOTS' in line:
        viz_section_start = i
        break

if viz_section_start:
    print("Found VISUAL TRAJECTORY PLOTS section:")
    print()
    for line in lines_viz[viz_section_start:viz_section_start + 80]:
        print(line)
else:
    print("Visualization section not found")
