# Interactive Demo Script

This document shows what an interactive session looks like when using the Dimension Worksheet tool.

## Example Session: Creating a Romance Trajectory

```bash
$ python3 scripts/dimension_worksheet.py --title "Coffee Shop Romance" --genre romance --interactive
```

### Session Output:

```
======================================================================
  DIMENSIONAL WORKSHEET: Coffee Shop Romance
  Genre: romance
  Target Beats: 12
======================================================================

This tool will guide you through scoring your story beat-by-beat.
You can track as many or as few dimensions as you like.

Load template beats for this genre? (y/n): y

✓ Loaded 14 template beats from romance-beat-template.csv

Which dimensions do you want to track?

PRIMARY DIMENSIONS (romance/relationship):
  - intimacy
  - trust
  - desire
  - vulnerability
  - goal_alignment
  - power_differential
  - info_asymmetry
  - stakes
  - proximity

SECONDARY DIMENSIONS (genre-specific):
  - danger
  - fear_dread
  - mystery
  - moral_ambiguity
  - acceptance

Enter dimension names separated by commas
(or press Enter to track all primary dimensions):
> intimacy, trust, desire, vulnerability, stakes

Tracking: intimacy, trust, desire, vulnerability, stakes

──────────────────────────────────────────────────────────────────────
  BEAT 1 of 12
──────────────────────────────────────────────────────────────────────
Beat name (or 'done' to finish, 'help' for examples): Meet Cute

Story position % (default: 8%): 5

Enter scores for each dimension:
  intimacy (0 to 10, '?' for guide): ?

  INTIMACY scoring guide:
    0: Complete strangers
    2: Acquaintances
    4: Friends / developing connection
    6: Close friends / strong romantic interest
    8: Deep connection
    10: Complete emotional unity

  intimacy (0 to 10, '?' for guide): 0
    ⚠ Extreme value! Make sure this is intentional.

  trust (0 to 10, '?' for guide): 3

  desire (0 to 10, '?' for guide): 2

  vulnerability (0 to 10, '?' for guide): 1

  stakes (0 to 10, '?' for guide): 4

Notes (what happens in this beat?): They meet when he spills coffee on her laptop. Initial attraction despite awkward start.

✓ Beat 'Meet Cute' added!

──────────────────────────────────────────────────────────────────────
  BEAT 2 of 12
──────────────────────────────────────────────────────────────────────
Beat name (or 'done' to finish, 'help' for examples): Forced Together

Story position % (default: 17%): 20

Enter scores for each dimension:
  intimacy (0 to 10, '?' for guide): 2

  trust (0 to 10, '?' for guide): 4

  desire (0 to 10, '?' for guide): 5

  vulnerability (0 to 10, '?' for guide): 2

  stakes (0 to 10, '?' for guide): 5

Notes (what happens in this beat?): Boss assigns them to same project. Sparks fly but both trying to stay professional.

✓ Beat 'Forced Together' added!

──────────────────────────────────────────────────────────────────────
  BEAT 3 of 12
──────────────────────────────────────────────────────────────────────
Beat name (or 'done' to finish, 'help' for examples): done

======================================================================
  WORKSHEET COMPLETE
======================================================================

Total beats recorded: 2

Would you like to:
  1. View analysis summary
  2. View ASCII visualization
  3. Export to JSON
  4. Export to CSV
  5. Save session
  6. All of the above
  0. Exit

Choice: 6

======================================================================
  TRAJECTORY ANALYSIS: Coffee Shop Romance
  Genre: romance
======================================================================

Total Beats: 2
Story Coverage: 5% to 20%
Average Velocity: 1.20 points/beat
Max Velocity: 1.20 points/beat
Min Velocity: 1.20 points/beat

DIMENSIONAL CHANGES:
  desire               ↑ +3.0 (2.0 → 5.0)
  intimacy             ↑ +2.0 (0.0 → 2.0)
  trust                ↑ +1.0 (3.0 → 4.0)
  stakes               ↑ +1.0 (4.0 → 5.0)
  vulnerability        ↑ +1.0 (1.0 → 2.0)

✓ No major issues detected

======================================================================
  Coffee Shop Romance - Dimensional Trajectory
======================================================================

INTIMACY
  Range: 0 to 10
    10 |
       |
       |
       | *
       |
       |
       |
       |
       |
     0 |*
       +--

TRUST
  Range: 0 to 10
    10 |
       |
       | *
       |
       |
       |
       |
       |
       |*
     0 |
       +--

DESIRE
  Range: 0 to 10
    10 |
       |
       | *
       |
       |
       |
       |
       |
       |*
     0 |
       +--

VULNERABILITY
  Range: 0 to 10
    10 |
       |
       | *
       |
       |
       |
       |
       |
       |*
     0 |
       +--

BEATS:
  1. Meet Cute (5%)
  2. Forced Together (20%)

✓ Exported to JSON: /home/user/narrative-dimensions-analysis/exports/Coffee_Shop_Romance_20251121_150000.json
✓ Exported to CSV: /home/user/narrative-dimensions-analysis/exports/Coffee_Shop_Romance_20251121_150000.csv
✓ Session saved: /home/user/narrative-dimensions-analysis/sessions/Coffee_Shop_Romance_session_20251121_150000.json
```

## Example: Getting Help During Session

```
──────────────────────────────────────────────────────────────────────
  BEAT 1 of 12
──────────────────────────────────────────────────────────────────────
Beat name (or 'done' to finish, 'help' for examples): help

Example beats:
  - Meet Cute (5%)
  - First Connection (15%)
  - Growing Closer (25%)
  - First Conflict (35%)
  - Deepening Bond (45%)
  - False Victory (55%)
  - Major Setback (65%)
  - Black Moment (75%)
  - Grand Gesture (85%)
  - Resolution (95%)
  - HEA (100%)

Beat name (or 'done' to finish, 'help' for examples): Black Moment
```

## Example: Dimension Scoring Help

```
Enter scores for each dimension:
  trust (0 to 10, '?' for guide): ?

  TRUST scoring guide:
    0: Complete distrust / active betrayal
    2: Suspicious / guarded
    4: Cautious trust
    6: Working trust
    8: Strong trust
    10: Absolute unwavering trust

  trust (0 to 10, '?' for guide): 1
```

## Example: Warning Messages

```
  intimacy (0 to 10, '?' for guide): 8
    ⚠ Large jump (6.0 points) - catalyst event needed!

  power_differential (-5 to 5, '?' for guide): 6
    ⚠ Must be -5 to 5

  power_differential (-5 to 5, '?' for guide): 3
```

## Example: Resuming a Session

```bash
$ python3 scripts/dimension_worksheet.py --load sessions/Coffee_Shop_Romance_session_20251121_150000.json --interactive

✓ Loaded session: Coffee Shop Romance

======================================================================
  DIMENSIONAL WORKSHEET: Coffee Shop Romance
  Genre: romance
  Target Beats: 12
======================================================================

This tool will guide you through scoring your story beat-by-beat.
You can track as many or as few dimensions as you like.

Load template beats for this genre? (y/n): n

[... continue adding beats ...]
```

## Example: Quick Analysis Without Interaction

```bash
$ python3 scripts/dimension_worksheet.py --load sessions/my_story.json --analyze

✓ Loaded session: Coffee Shop Romance

======================================================================
  TRAJECTORY ANALYSIS: Coffee Shop Romance
  Genre: romance
======================================================================

Total Beats: 7
Story Coverage: 5% to 100%
Average Velocity: 2.14 points/beat
...
```

## Example: Programmatic Usage

```python
#!/usr/bin/env python3
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from dimension_worksheet import DimensionalWorksheet

# Create worksheet
ws = DimensionalWorksheet(
    story_title="My Quick Story",
    genre="romance",
    num_beats=5
)

# Add beats programmatically (no interaction)
beats = [
    ("Meet", 10, {'intimacy': 1, 'trust': 3, 'desire': 2}),
    ("Connect", 30, {'intimacy': 3, 'trust': 4, 'desire': 5}),
    ("Conflict", 60, {'intimacy': 4, 'trust': 2, 'desire': 6}),
    ("Reconcile", 85, {'intimacy': 7, 'trust': 6, 'desire': 8}),
    ("HEA", 100, {'intimacy': 9, 'trust': 8, 'desire': 9})
]

for name, percent, dims in beats:
    ws.add_beat(name, percent, dims)

# Export everything
ws.export_to_json("my_trajectory.json")
ws.export_to_csv("my_trajectory.csv")
ws.save_session("sessions/my_session.json")

print(ws.get_analysis_summary())
print(ws.visualize_ascii())
```

## Tips for Interactive Sessions

1. **Use '?' liberally** - The scoring guides are very helpful
2. **Press Enter to skip dimensions** - You don't need to score every dimension for every beat
3. **Type 'help' for beat examples** - Get genre-appropriate beat names
4. **Use descriptive notes** - Future you will thank you
5. **Save sessions frequently** - Use option 5 or 6 after adding several beats
6. **Review analysis** - The summary report catches issues early
7. **Export multiple formats** - JSON for validation, CSV for spreadsheets
