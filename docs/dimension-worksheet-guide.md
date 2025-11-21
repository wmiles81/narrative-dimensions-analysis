# Dimension Worksheet Tool - User Guide

## Overview

The Dimension Worksheet (`dimension_worksheet.py`) is an interactive Python tool that helps authors systematically score their story dimensions beat-by-beat. It provides validation, visualization, and export capabilities to track emotional and narrative progression throughout your story.

## Quick Start

### Interactive Mode (Recommended for Beginners)

Start a new worksheet interactively:

```bash
cd /home/user/narrative-dimensions-analysis
python3 scripts/dimension_worksheet.py --title "My Story" --genre romance --interactive
```

The tool will guide you through:
1. Choosing which dimensions to track
2. Adding each story beat
3. Scoring dimensions with helpful prompts
4. Viewing analysis and exporting results

### Command-Line Mode

For quick operations on existing worksheets:

```bash
# Analyze a saved session
python3 scripts/dimension_worksheet.py --load sessions/my_story.json --analyze

# Visualize trajectories
python3 scripts/dimension_worksheet.py --load sessions/my_story.json --visualize

# Export to different formats
python3 scripts/dimension_worksheet.py --load sessions/my_story.json --export-json output.json
python3 scripts/dimension_worksheet.py --load sessions/my_story.json --export-csv output.csv
```

### Programmatic Mode

Use the DimensionalWorksheet class in your own scripts:

```python
from dimension_worksheet import DimensionalWorksheet

# Create worksheet
ws = DimensionalWorksheet("My Story", "romance", num_beats=10)

# Add beats
ws.add_beat(
    beat_name="Meet Cute",
    beat_percent=5,
    dimensions={'intimacy': 0, 'trust': 3, 'desire': 2},
    notes="They meet in a coffee shop"
)

# Analyze
print(ws.get_analysis_summary())

# Export
ws.export_to_json()
ws.export_to_csv()
ws.save_session()
```

## Features

### 1. Dimension Tracking

Track any combination of dimensions:

**Primary Dimensions (Romance/Relationship):**
- `intimacy` (0-10): Emotional closeness
- `trust` (0-10): Belief in reliability
- `desire` (0-10): Attraction and wanting
- `vulnerability` (0-10): Emotional openness
- `goal_alignment` (0-10): Shared objectives
- `power_differential` (-5 to +5): Balance of power
- `info_asymmetry` (0-10): Knowledge gaps
- `stakes` (0-10): What's at risk
- `proximity` (0-10): Physical closeness

**Secondary Dimensions (Genre-Specific):**
- `danger` (0-10): Physical threat level
- `fear_dread` (0-10): Psychological terror
- `mystery` (0-10): Unknown elements
- `moral_ambiguity` (0-10): Ethical grayness
- `acceptance` (0-10): Psychological peace

### 2. Input Validation

The tool automatically validates:
- Dimension values are in valid ranges
- Large jumps (>3 points) are flagged
- Extreme values trigger warnings
- Unknown dimensions are rejected

### 3. Analysis Features

**Velocity Calculation:**
```
Average dimensional change between beats
Helps identify pacing issues
```

**Issue Detection:**
- Large jumps requiring catalyst events
- Flatlined dimensions (no change)
- Pacing spikes and drops

**Trajectory Analysis:**
- Which dimensions changed most
- Overall story progression
- Potential problems and warnings

### 4. Visualization

ASCII art graphs show dimensional changes over time:

```
INTIMACY
  Range: 0 to 10
    10 |
       |             *
       |            *
       |      *    *
       |     * *
       |    *     *
```

Visualize any dimensions:
```python
ws.visualize_ascii(['intimacy', 'trust', 'desire', 'vulnerability'])
```

### 5. Export Formats

**JSON Export** (for use with validate_trajectory.py):
```json
{
  "story_title": "My Story",
  "genre": "romance",
  "beats": [...],
  "trajectory": [
    {"intimacy": 1, "trust": 3, "desire": 2},
    {"intimacy": 3, "trust": 4, "desire": 5},
    ...
  ]
}
```

**CSV Export** (for Excel/Google Sheets):
```csv
Beat Name,Story %,intimacy,trust,desire,Notes
Meet Cute,5,0,3,2,They meet in coffee shop
...
```

**Session Export** (for resuming later):
Saves complete worksheet state including metadata

### 6. Genre Templates

Pre-populated templates for common genres:

```bash
# Available templates:
templates/romance-beat-template.csv
templates/thriller-beat-template.csv
templates/mystery-beat-template.csv
```

Load in interactive mode when prompted, or programmatically:
```python
ws = DimensionalWorksheet("My Romance", "romance")
ws._load_genre_template()
```

## Usage Examples

### Example 1: Romance Novel

```python
from dimension_worksheet import DimensionalWorksheet

ws = DimensionalWorksheet("Enemies to Lovers", "romance", num_beats=7)

ws.add_beat("First Meeting", 5, {
    'intimacy': 0, 'trust': 2, 'desire': 3,
    'goal_alignment': 1, 'power_differential': 0
})

ws.add_beat("Forced Proximity", 20, {
    'intimacy': 2, 'trust': 3, 'desire': 5,
    'goal_alignment': 3, 'power_differential': 0
})

ws.add_beat("Black Moment", 75, {
    'intimacy': 3, 'trust': 1, 'desire': 8,
    'goal_alignment': 2, 'power_differential': 0
})

ws.add_beat("HEA", 100, {
    'intimacy': 9, 'trust': 8, 'desire': 9,
    'goal_alignment': 10, 'power_differential': 0
})

# Analyze
print(ws.get_analysis_summary())

# Export
ws.export_to_json("my_romance_trajectory.json")
```

### Example 2: Thriller

```python
ws = DimensionalWorksheet("Spy Thriller", "thriller", num_beats=5)

ws.add_beat("Normal World", 5, {
    'danger': 0, 'stakes': 2, 'trust': 5, 'info_asymmetry': 3
})

ws.add_beat("Inciting Incident", 15, {
    'danger': 5, 'stakes': 7, 'trust': 4, 'info_asymmetry': 6
})

ws.add_beat("Midpoint", 50, {
    'danger': 7, 'stakes': 9, 'trust': 2, 'info_asymmetry': 8
})

ws.add_beat("Climax", 90, {
    'danger': 10, 'stakes': 10, 'trust': 3, 'info_asymmetry': 2
})

ws.add_beat("Resolution", 100, {
    'danger': 1, 'stakes': 4, 'trust': 6, 'info_asymmetry': 0
})

# Visualize danger progression
print(ws.visualize_ascii(['danger', 'stakes']))
```

### Example 3: Using with Validator

```python
from dimension_worksheet import DimensionalWorksheet
from validate_trajectory import TrajectoryValidator

# Create worksheet
ws = DimensionalWorksheet("My Story", "romance")
ws.add_beat("Start", 0, {'intimacy': 1, 'trust': 3})
ws.add_beat("End", 100, {'intimacy': 9, 'trust': 8})

# Generate trajectory
trajectory = ws.generate_trajectory()

# Validate
validator = TrajectoryValidator(genre='romance')
report = validator.validate_trajectory(trajectory)

print(f"Valid: {report['valid']}")
for check in report['checks']:
    print(f"{check['name']}: {'PASSED' if check['passed'] else 'FAILED'}")
```

## Interactive Mode Guide

When running in interactive mode, you'll be prompted for:

### 1. Template Loading
```
Load template beats for this genre? (y/n):
```
Choose 'y' to start with pre-populated beats for your genre.

### 2. Dimension Selection
```
Which dimensions do you want to track?
Enter dimension names separated by commas:
> intimacy, trust, desire, vulnerability
```

### 3. Beat Entry

For each beat:

```
BEAT 1 of 12
─────────────────────────────────────────
Beat name (or 'done' to finish, 'help' for examples): Meet Cute
Story position % (default: 8%): 5
```

### 4. Dimension Scoring

For each dimension:
```
Enter scores for each dimension:
  intimacy (0 to 10, '?' for guide): ?

  INTIMACY scoring guide:
    0: Complete strangers
    2: Acquaintances
    4: Friends / developing connection
    6: Close friends / strong romantic interest
    8: Deep connection
    10: Complete emotional unity

  intimacy (0 to 10, '?' for guide): 2
```

The tool will warn you about:
- Extreme values (0 or 10)
- Large jumps from previous beat (>3 points)

### 5. Beat Notes
```
Notes (what happens in this beat?): They meet in a coffee shop
```

### 6. Export Options

After adding all beats:
```
Would you like to:
  1. View analysis summary
  2. View ASCII visualization
  3. Export to JSON
  4. Export to CSV
  5. Save session
  6. All of the above
  0. Exit
```

## Tips and Best Practices

### 1. Start with Templates

Genre templates provide a solid foundation:
```bash
python3 scripts/dimension_worksheet.py --title "My Story" --genre romance --interactive
# When prompted: Load template beats for this genre? y
```

Then modify the template to fit your specific story.

### 2. Track Core Dimensions

For romance, focus on:
- intimacy, trust, desire (the core three)
- vulnerability, goal_alignment
- stakes, proximity

For thriller:
- danger, stakes
- trust, info_asymmetry
- proximity

### 3. Use Descriptive Beat Names

Good beat names help you remember the story:
- ✓ "Coffee Shop Meet Cute"
- ✓ "Secret Identity Revealed"
- ✗ "Beat 1"
- ✗ "Chapter 5"

### 4. Add Detailed Notes

Notes help when revising:
```python
ws.add_beat(
    "Black Moment", 75,
    {'intimacy': 3, 'trust': 1, 'desire': 8},
    notes="Sarah discovers Jake was hired to spy on her company. "
          "Confrontation in the rain. She walks away."
)
```

### 5. Check for Large Jumps

Large jumps (>3 points) need catalyst events:

```
⚠ Large jump in trust at 'Black Moment' (5.0 points) - needs catalyst event
```

This means you need a significant plot event to justify that change.

### 6. Watch for Flatlines

If a dimension doesn't change, readers won't feel progression:

```
⚠ power_differential shows minimal change (flatline)
```

Consider if this is intentional or if the dimension needs more variation.

### 7. Save Regularly

Use session files to save your progress:
```python
session_path = ws.save_session()
print(f"Saved to {session_path}")

# Later...
ws = DimensionalWorksheet.load_session(session_path)
```

### 8. Validate Your Trajectory

Always validate before considering your trajectory complete:

```bash
# Export from worksheet
python3 scripts/dimension_worksheet.py --load sessions/my_story.json --export-json trajectory.json

# Validate
python3 scripts/validate_trajectory.py trajectory.json
```

## Troubleshooting

### "Validation errors: unknown dimension"

Check spelling and use lowercase with underscores:
- ✓ `info_asymmetry`
- ✗ `information_asymmetry`
- ✗ `InfoAsymmetry`

### "Value out of range"

Check dimension ranges:
- Most dimensions: 0-10
- `power_differential`: -5 to +5

### "Large jump" warnings

This is intentional! Large jumps need catalyst events:
1. Add a note explaining what causes the jump
2. Consider adding an intermediate beat
3. Or accept the warning if you have a strong catalyst

### Session file not found

Use absolute or relative paths:
```bash
# Absolute
python3 scripts/dimension_worksheet.py --load /home/user/narrative-dimensions-analysis/sessions/my_story.json

# Relative from project root
python3 scripts/dimension_worksheet.py --load sessions/my_story.json
```

## File Locations

```
narrative-dimensions-analysis/
├── scripts/
│   └── dimension_worksheet.py     # Main script
├── templates/
│   ├── romance-beat-template.csv
│   ├── thriller-beat-template.csv
│   └── mystery-beat-template.csv
├── exports/                        # Auto-created
│   ├── *.json                      # JSON exports
│   └── *.csv                       # CSV exports
└── sessions/                       # Auto-created
    └── *.json                      # Saved sessions
```

## Integration with Other Tools

### With validate_trajectory.py

```python
# Create and validate
ws = DimensionalWorksheet("My Story", "romance")
# ... add beats ...

trajectory = ws.generate_trajectory()
from validate_trajectory import TrajectoryValidator
validator = TrajectoryValidator(genre='romance')
report = validator.validate_trajectory(trajectory)
```

### With calculate_tension.py

```python
# Export trajectory
json_path = ws.export_to_json()

# Use with tension calculator
# (Assuming calculate_tension.py can read JSON)
import subprocess
subprocess.run(['python3', 'scripts/calculate_tension.py', str(json_path)])
```

### With generate_report.py

Export your worksheet and use the trajectory with the report generator to get comprehensive analysis of your story's dimensional progression.

## Advanced Usage

### Custom Dimension Ranges

While not recommended, you can track custom metrics by validating manually:

```python
custom_dimensions = {'romance_level': 7, 'action_intensity': 9}
errors = ws.validate_dimensions(custom_dimensions)
# Will show errors for unknown dimensions, but you can ignore
```

### Batch Processing

Process multiple stories:

```python
import glob
from dimension_worksheet import DimensionalWorksheet

for session_file in glob.glob('sessions/*.json'):
    ws = DimensionalWorksheet.load_session(session_file)
    print(f"\n{ws.story_title}")
    print(ws.get_analysis_summary())
```

### Custom Visualization

Access raw data for custom plots:

```python
sorted_beats = sorted(ws.beats, key=lambda b: b['percent'])

intimacy_values = [b['dimensions'].get('intimacy', 0) for b in sorted_beats]
trust_values = [b['dimensions'].get('trust', 0) for b in sorted_beats]

# Use with matplotlib, plotly, etc.
```

## Support and Resources

- See `dimension-scoring-guide.md` for detailed scoring rubrics
- See `genre-configs.md` for genre-specific guidance
- See `examples/worksheet_example.py` for code examples
- See `examples/test_integration.py` for integration patterns

## Quick Reference

```bash
# Start new interactive session
python3 scripts/dimension_worksheet.py --title "Title" --genre romance --interactive

# Load and analyze
python3 scripts/dimension_worksheet.py --load sessions/file.json --analyze

# Load and visualize
python3 scripts/dimension_worksheet.py --load sessions/file.json --visualize

# Export formats
python3 scripts/dimension_worksheet.py --load sessions/file.json --export-json out.json
python3 scripts/dimension_worksheet.py --load sessions/file.json --export-csv out.csv

# Help
python3 scripts/dimension_worksheet.py --help
```
