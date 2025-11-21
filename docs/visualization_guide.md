# Dimensional Trajectory Visualization Guide

## Overview

The visualization tools provide ASCII/text-based plotting for analyzing dimensional trajectories in terminal displays. These tools help writers visualize their story's emotional and narrative dynamics without requiring external graphing software.

## Location

- **Main Script**: `/scripts/visualize_trajectory.py`
- **Integration**: Available in `generate_report.py` via `include_visualizations=True`

## Features

### 1. Single Dimension ASCII Plot

Plot a single dimension over time to see its trajectory clearly.

```bash
python3 scripts/visualize_trajectory.py examples/sample_trajectory.json --dimension intimacy
```

**Output Example:**
```
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

Range: 2.0 to 9.0
Change: +7.0 points
```

**Use Cases:**
- Track a single dimension's progression
- Identify growth or decline patterns
- Verify expected arcs (e.g., trust should rebuild after betrayal)

### 2. Multi-Dimension Plot

Plot multiple dimensions on the same graph with different symbols.

```bash
python3 scripts/visualize_trajectory.py examples/sample_trajectory.json --multi intimacy trust desire vulnerability
```

**Output Example:**
```
Multiple Dimensions

  10 |         ●              ★
   9 |      ●     ★        ★
   8 |   ●  ◆  ★        ★
   7 | ●  ◆  ★        ★  ◆
   6 | ◆ ★          ★   ◆
   5 | ★          ★    ◆
     |___________________________
     ★=Intimacy ◆=Trust ●=Desire
```

**Symbols:**
- ★ = First dimension
- ◆ = Second dimension
- ● = Third dimension
- ■ = Fourth dimension
- ▲, ◇, ○, □, △, ▼ = Additional dimensions

**Use Cases:**
- Compare relationship dimensions
- See how dimensions correlate or diverge
- Identify key moments where multiple dimensions shift

### 3. Tension Over Time

Calculate and plot tension at each beat using genre-specific weights.

```bash
python3 scripts/visualize_trajectory.py examples/sample_trajectory.json --tension --genre romance --subgenre dark
```

**Output Example:**
```
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

Average Tension: 6.5/10
Peak Tension: 8.2/10 at Beat 9
Lowest Tension: 3.1/10 at Beat 7
```

**Use Cases:**
- Verify tension arc matches genre expectations
- Identify flat spots (low tension)
- Ensure peak tension at climax
- Plan relief scenes

### 4. Tension Heatmap

Create heat map showing tension intensity across the story using ASCII shading.

```bash
python3 scripts/visualize_trajectory.py examples/sample_trajectory.json --heatmap
```

**Output Example:**
```
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

Legend: ░=Low ▒=Medium ▓=High █=Extreme
```

**Shading Characters:**
- `░` = Low tension (0-2.5)
- `▒` = Medium tension (2.5-5.0)
- `▓` = High tension (5.0-7.5)
- `█` = Extreme tension (7.5-10)

**Use Cases:**
- Visualize overall story pacing
- Spot pacing issues (too much high tension)
- Ensure proper placement of relief scenes
- Verify genre-appropriate tension patterns

### 5. Velocity/Pacing Graph

Show the rate of dimensional change to identify stuck or rushed scenes.

```bash
python3 scripts/visualize_trajectory.py examples/sample_trajectory.json --velocity
```

**Output Example:**
```
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
```

**Interpretation:**
- **High velocity (>3.0)**: Rapid changes, may feel rushed
- **Good velocity (1.5-3.0)**: Steady progression
- **Low velocity (<1.0)**: Minimal change, possible stuck scene

**Use Cases:**
- Identify stagnant scenes that need more movement
- Spot rushed pacing that needs slowing
- Ensure consistent progression

### 6. Trajectory Comparison

Compare two trajectories (planned vs actual, draft 1 vs draft 2, etc.)

```python
from visualize_trajectory import compare_trajectories

result = compare_trajectories(
    planned_trajectory,
    actual_trajectory,
    'trust',
    ('Planned', 'Actual')
)
```

**Output Example:**
```
Trajectory Comparison: Trust

  10 |                    ★
   9 |                 ★
   8 |              ★
   7 |           ★
   6 |        ★     ◆
   5 |     ★     ◆
   4 |  ★    ◆
   3 |★   ◆
   2 | ◆
     |___________________
     ★=Planned ◆=Actual ◈=Same

Average Divergence: 2.3 points
Maximum Divergence: 3.0 points at beat 5
⚠ Significant drift from plan - consider revision
```

**Use Cases:**
- Compare outline to draft
- Track revisions between drafts
- Identify where story diverged from plan
- Verify intentional changes vs drift

### 7. Full Visual Report

Generate comprehensive report with all visualizations.

```bash
python3 scripts/visualize_trajectory.py examples/sample_trajectory.json --full-report
```

Includes:
1. Core relationship dimensions plot
2. Tension trajectory
3. Tension heatmap
4. Pacing velocity
5. Individual dimension trajectories
6. Pattern analysis with diagnostics

Save to file:
```bash
python3 scripts/visualize_trajectory.py examples/sample_trajectory.json --full-report --output report.txt
```

## Integration with Report Generator

The standard report generator can now include visualizations:

```python
from generate_report import DimensionalReport

reporter = DimensionalReport(
    title="My Story - Chapter 5",
    genre="romance",
    content_level="chapter",
    include_visualizations=True  # Enable visualizations
)

report = reporter.generate_full_report(
    current_state=current_state,
    trajectory=trajectory
)
```

## Input Format

### JSON Structure

```json
{
  "title": "Story Title",
  "genre": "romance",
  "subgenre": "dark",
  "trajectory": [
    {
      "beat": 1,
      "label": "Meet Cute",
      "intimacy": 2,
      "trust": 3,
      "desire": 5,
      "vulnerability": 2,
      "goal_alignment": 4,
      "power_differential": -3,
      "stakes": 6
    },
    {
      "beat": 2,
      "label": "Forced Proximity",
      "intimacy": 3,
      "trust": 2,
      "desire": 6,
      ...
    }
  ]
}
```

### Supported Formats

The script accepts:
- List of states directly
- Dict with `trajectory` key
- Dict with `states` key

### Dimension Scales

- **Standard dimensions**: 0-10 scale (intimacy, trust, desire, etc.)
- **Power differential**: -5 to +5 scale (negative = Character A has more power)

## Command-Line Usage

### Basic Commands

```bash
# Single dimension
python3 scripts/visualize_trajectory.py FILE.json --dimension DIMENSION_NAME

# Multiple dimensions
python3 scripts/visualize_trajectory.py FILE.json --multi dim1 dim2 dim3

# Tension analysis
python3 scripts/visualize_trajectory.py FILE.json --tension

# Heatmap
python3 scripts/visualize_trajectory.py FILE.json --heatmap

# Velocity
python3 scripts/visualize_trajectory.py FILE.json --velocity

# Full report
python3 scripts/visualize_trajectory.py FILE.json --full-report
```

### Options

- `--genre GENRE`: Specify genre for tension calculation (default: romance)
- `--subgenre SUBGENRE`: Specify subgenre
- `--output FILE`: Save to file instead of stdout

### Examples

```bash
# Intimacy plot for dark romance
python3 scripts/visualize_trajectory.py story.json --dimension intimacy --genre romance --subgenre dark

# Compare three core dimensions
python3 scripts/visualize_trajectory.py story.json --multi intimacy trust desire

# Full analysis saved to file
python3 scripts/visualize_trajectory.py story.json --full-report --output analysis.txt
```

## Color Support

The tool automatically detects terminal color support:
- If supported, uses ANSI color codes for enhanced readability
- Falls back to plain ASCII if not supported
- Colors highlight different data types and warnings

## Tips and Best Practices

### For Writers

1. **Check velocity regularly**: Low velocity (<1.0) often indicates scenes that drag
2. **Use heatmap for pacing**: Ensure tension rises and falls appropriately
3. **Compare planned vs actual**: Catch unintentional story drift early
4. **Monitor tension patterns**: Different genres have different tension expectations

### For Editors/Beta Readers

1. **Full report gives overview**: Start with `--full-report` for comprehensive view
2. **Heatmap reveals structure**: Quickly spot pacing issues
3. **Dimension plots show arcs**: Verify character/relationship development

### For Series Writers

1. **Track across books**: Compare trajectories between books for consistency
2. **Velocity across series**: Maintain consistent pacing feel
3. **Dimension continuity**: Ensure relationship dimensions continue logically

## Troubleshooting

### "Dimension not found" Error

Ensure the dimension name matches exactly (case-sensitive):
- Correct: `intimacy`
- Incorrect: `Intimacy`, `INTIMACY`

### Empty or Flat Graph

Check that:
1. Trajectory has at least 2 states
2. Dimension values are numeric (not strings)
3. Values actually change between states

### Tension Calculation Fails

Verify:
1. `calculate_tension` module is available
2. Genre weights file exists at `references/genre-weights.json`
3. All required dimensions are present in states

## Advanced Features

### Pattern Analysis

The full report includes automatic pattern detection:
- Intimacy growth/decline
- Trust-vulnerability gaps
- Desire-proximity gaps
- Overall pacing assessment

### Auto-Scaling

All plots automatically scale to data range:
- Standard dimensions: 0-10
- Power differential: -5 to +5
- Custom ranges adapt to actual values

### Annotations

Heatmap automatically annotates significant moments:
- Relief scenes (low tension after high)
- Black moments (very high tension near end)
- Climax (high tension in final act)
- Resolution (tension drop at end)

## Examples

See `/examples/` directory:
- `sample_trajectory.json` - Full story trajectory
- `visualization_demo.py` - All visualization types
- `compare_test.py` - Trajectory comparison demo
- `test_report_with_viz.py` - Integrated report demo
- `full_visual_report.txt` - Sample output

## API Reference

### Python Functions

```python
from visualize_trajectory import (
    plot_dimension_ascii,
    plot_multi_dimension,
    plot_tension_over_time,
    plot_tension_heatmap,
    plot_velocity_graph,
    compare_trajectories,
    create_trajectory_report
)

# Single dimension
plot_dimension_ascii(trajectory, 'intimacy', height=10, width=50)

# Multiple dimensions
plot_multi_dimension(trajectory, ['intimacy', 'trust', 'desire'])

# Tension
plot_tension_over_time(trajectory, genre='romance', subgenre='dark')

# Heatmap
plot_tension_heatmap(trajectory, genre='romance')

# Velocity
plot_velocity_graph(trajectory)

# Compare
compare_trajectories(traj1, traj2, 'trust', ('Draft 1', 'Draft 2'))

# Full report
report = create_trajectory_report(trajectory, 'romance', output_file=Path('report.txt'))
```

## Future Enhancements

Potential additions:
- Interactive mode for exploring trajectory
- Export to image formats (PNG, SVG)
- Statistical correlation analysis
- Predictive suggestions based on patterns
- Multi-story comparison
- Genre template overlays

---

**Version**: 1.0
**Last Updated**: 2025-11-21
**Author**: Narrative Dimensions Analysis Project
