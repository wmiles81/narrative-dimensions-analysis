# Sample Output from Dimension Worksheet Tool

This document shows real output examples from the dimension_worksheet.py tool.

## Sample Analysis Summary

```
======================================================================
  TRAJECTORY ANALYSIS: Love in the Time of Deadlines
  Genre: romance
======================================================================

Total Beats: 7
Story Coverage: 5% to 100%
Average Velocity: 2.19 points/beat
Max Velocity: 2.56 points/beat
Min Velocity: 1.89 points/beat

DIMENSIONAL CHANGES:
  intimacy             ↑ +9.0 (0.0 → 9.0)
  goal_alignment       ↑ +8.0 (2.0 → 10.0)
  proximity            ↑ +8.0 (2.0 → 10.0)
  desire               ↑ +7.0 (2.0 → 9.0)
  vulnerability        ↑ +7.0 (1.0 → 8.0)

POTENTIAL ISSUES:
  ⚠ Large jump in proximity at 'Forced Proximity' (6.0 points) - needs catalyst event
  ⚠ Large jump in vulnerability at 'First Kiss' (4.0 points) - needs catalyst event
  ⚠ Large jump in info_asymmetry at 'Secret Revealed' (6.0 points) - needs catalyst event
  ⚠ Large jump in proximity at 'Secret Revealed' (5.0 points) - needs catalyst event
  ⚠ Large jump in info_asymmetry at 'Black Moment' (7.0 points) - needs catalyst event
  ⚠ Large jump in proximity at 'Black Moment' (4.0 points) - needs catalyst event
  ⚠ Large jump in trust at 'Grand Gesture' (4.0 points) - needs catalyst event
  ⚠ Large jump in goal_alignment at 'Grand Gesture' (5.0 points) - needs catalyst event
  ⚠ Large jump in proximity at 'Grand Gesture' (7.0 points) - needs catalyst event
  ⚠ Large jump in stakes at 'HEA' (5.0 points) - needs catalyst event
  ⚠ power_differential shows minimal change (flatline)
  ⚠ stakes shows minimal change (flatline)
```

## Sample ASCII Visualization

```
======================================================================
  Love in the Time of Deadlines - Dimensional Trajectory
======================================================================

INTIMACY
  Range: 0 to 10
    10 |
       |      *
       |
       |
       |   * *
       |  *
       |
       |    *
       | *
     0 |*
       +-------

TRUST
  Range: 0 to 10
    10 |
       |
       |      *
       |
       |
       |  *  *
       | *
       |*
       |   *
     0 |    *
       +-------

DESIRE
  Range: 0 to 10
    10 |
       |     **
       |  ***
       |
       |
       | *
       |
       |
       |*
     0 |
       +-------

VULNERABILITY
  Range: 0 to 10
    10 |     *
       |
       |    * *
       |   *
       |  *
       |
       |
       |
       | *
     0 |*
       +-------

BEATS:
  1. Meet Cute (5%)
  2. Forced Proximity (20%)
  3. First Kiss (40%)
  4. Secret Revealed (60%)
  5. Black Moment (75%)
  6. Grand Gesture (90%)
  7. HEA (100%)
```

## Sample Velocity Analysis

```
VELOCITY ANALYSIS:
Beat-to-beat velocity (average dimensional change):
  Meet Cute → Forced Proximity: 1.89 points/dimension
  Forced Proximity → First Kiss: 1.89 points/dimension
  First Kiss → Secret Revealed: 2.56 points/dimension
  Secret Revealed → Black Moment: 2.22 points/dimension
  Black Moment → Grand Gesture: 2.56 points/dimension
  Grand Gesture → HEA: 2.00 points/dimension
```

## Sample JSON Export

```json
{
  "story_title": "Love in the Time of Deadlines",
  "genre": "romance",
  "metadata": {
    "created": "2025-11-21T23:30:12.738373",
    "last_modified": "2025-11-21T23:30:12.738419"
  },
  "beats": [
    {
      "name": "Meet Cute",
      "percent": 5,
      "dimensions": {
        "intimacy": 0,
        "trust": 3,
        "desire": 2,
        "vulnerability": 1,
        "goal_alignment": 2,
        "power_differential": 0,
        "info_asymmetry": 4,
        "stakes": 4,
        "proximity": 2
      },
      "notes": "They meet at a coffee shop - he spills coffee on her laptop"
    },
    {
      "name": "Forced Proximity",
      "percent": 20,
      "dimensions": {
        "intimacy": 2,
        "trust": 4,
        "desire": 5,
        "vulnerability": 2,
        "goal_alignment": 4,
        "power_differential": 0,
        "info_asymmetry": 3,
        "stakes": 5,
        "proximity": 8
      },
      "notes": "Boss assigns them to same project - must work together"
    }
  ],
  "trajectory": [
    {
      "intimacy": 0,
      "trust": 3,
      "desire": 2,
      "vulnerability": 1,
      "goal_alignment": 2,
      "power_differential": 0,
      "info_asymmetry": 4,
      "stakes": 4,
      "proximity": 2
    },
    {
      "intimacy": 2,
      "trust": 4,
      "desire": 5,
      "vulnerability": 2,
      "goal_alignment": 4,
      "power_differential": 0,
      "info_asymmetry": 3,
      "stakes": 5,
      "proximity": 8
    }
  ]
}
```

## Sample CSV Export

```csv
Beat Name,Story %,desire,goal_alignment,info_asymmetry,intimacy,power_differential,proximity,stakes,trust,vulnerability,Notes
Meet Cute,5,2,2,4,0,0,2,4,3,1,They meet at a coffee shop - he spills coffee on her laptop
Forced Proximity,20,5,4,3,2,0,8,5,4,2,Boss assigns them to same project - must work together
First Kiss,40,8,6,2,5,0,10,6,5,6,Late night working - tension breaks into passionate kiss
Secret Revealed,60,8,3,8,6,-2,5,8,2,7,She discovers he was assigned to evaluate her for promotion
Black Moment,75,8,2,1,3,0,1,9,1,8,She quits and prepares to move to another city
Grand Gesture,90,9,7,0,6,0,8,9,5,10,He quits his job and follows her - full confession
HEA,100,9,10,0,9,0,10,4,8,8,They start their own business together - partnership in life and work
```

## Sample Validation Report

```
VALIDATION REPORT
──────────────────────────────────────────────────────────────────────

Valid: ✓ YES

Checks:
  Jump Validation           ✓ PASSED
  Movement Validation       ✓ PASSED
  Genre Requirements        ✓ PASSED
  Pacing Consistency        ✓ PASSED
  Character Arcs            ✓ PASSED
```

## Sample Error Messages

### Input Validation

```
⚠ Error: Validation errors: intimacy = 15 (valid range: 0 to 10)

⚠ Error: Validation errors: power_differential = -10 (valid range: -5 to 5)

⚠ Validation errors: ['Unknown dimension: fake_dimension']
```

### Interactive Warnings

```
  intimacy (0 to 10, '?' for guide): 0
    ⚠ Extreme value! Make sure this is intentional.

  intimacy (0 to 10, '?' for guide): 8
    ⚠ Large jump (6.0 points) - catalyst event needed!
```

## Sample Session File

```json
{
  "story_title": "Session Test",
  "genre": "thriller",
  "num_beats": 3,
  "beats": [
    {
      "name": "Start",
      "percent": 10,
      "dimensions": {
        "stakes": 3,
        "danger": 2,
        "trust": 5
      },
      "notes": "Normal world"
    },
    {
      "name": "Crisis",
      "percent": 50,
      "dimensions": {
        "stakes": 8,
        "danger": 7,
        "trust": 3
      },
      "notes": "Danger escalates"
    },
    {
      "name": "End",
      "percent": 100,
      "dimensions": {
        "stakes": 4,
        "danger": 1,
        "trust": 6
      },
      "notes": "Resolution"
    }
  ],
  "metadata": {
    "created": "2025-11-21T23:31:11.123456",
    "last_modified": "2025-11-21T23:31:11.123456"
  }
}
```

## Sample Template (Romance)

First few rows of romance-beat-template.csv:

```csv
Beat Name,Story %,intimacy,trust,desire,vulnerability,goal_alignment,power_differential,info_asymmetry,stakes,proximity,Notes
Meet Cute,5,0,3,2,1,2,0,4,4,2,First encounter - initial chemistry but strangers
Forced Proximity,10,1,3,4,1,3,0,4,5,8,Circumstances force them together
First Real Conversation,15,2,4,5,2,4,0,3,5,7,Opening up slightly - discovering common ground
Growing Attraction,25,4,4,6,3,5,0,3,6,7,Spending more time together - attraction building
First Kiss,35,5,5,7,5,6,0,2,6,10,Major romantic milestone - vulnerability increases
```

## Sample Integration Test Results

```
######################################################################
#  INTEGRATION TEST SUITE
######################################################################

======================================================================
  INTEGRATION TEST: Worksheet → Validator
======================================================================

✓ Created worksheet with 5 beats
✓ Generated trajectory: 5 states

Trajectory format preview:
  {'intimacy': 1, 'trust': 3, 'desire': 3, 'goal_alignment': 4, 'stakes': 5}

──────────────────────────────────────────────────────────────────────
VALIDATION REPORT
──────────────────────────────────────────────────────────────────────

Valid: ✓ YES

Checks:
  Jump Validation           ✓ PASSED
  Movement Validation       ✓ PASSED
  Genre Requirements        ✓ PASSED
  Pacing Consistency        ✓ PASSED
  Character Arcs            ✓ PASSED

──────────────────────────────────────────────────────────────────────
JSON EXPORT TEST
──────────────────────────────────────────────────────────────────────

✓ Exported to: /home/user/narrative-dimensions-analysis/exports/Test_Story_20251121_233148.json
✓ Loaded trajectory from JSON: 5 states
✓ Re-validation: PASSED
✓ Generated and exported trajectories match perfectly


======================================================================
  SESSION PERSISTENCE TEST
======================================================================

✓ Created original worksheet: 3 beats
✓ Saved session to: /home/user/narrative-dimensions-analysis/sessions/Session_Test_session_20251121_233148.json
✓ Loaded session: 3 beats

Data integrity checks:
  ✓ Title
  ✓ Genre
  ✓ Beat count
  ✓ First beat name
  ✓ Last beat notes


######################################################################
#  TEST RESULTS
######################################################################

  ✓ PASSED  Worksheet → Validator Integration
  ✓ PASSED  Session Persistence

Overall: ✓ ALL TESTS PASSED
```

## Command Line Usage Examples

### Help Output

```bash
$ python3 scripts/dimension_worksheet.py --help

usage: dimension_worksheet.py [-h] [--title TITLE] [--genre GENRE]
                              [--beats BEATS] [--load LOAD] [--interactive]
                              [--analyze] [--visualize]
                              [--export-json EXPORT_JSON]
                              [--export-csv EXPORT_CSV]

Interactive dimensional analysis worksheet

options:
  -h, --help            show this help message and exit
  --title TITLE         Story title
  --genre GENRE         Genre (romance, thriller, mystery, etc.)
  --beats BEATS         Number of beats to track (default: 12)
  --load LOAD           Load saved session file
  --interactive         Run interactive mode
  --analyze             Show analysis summary
  --visualize           Show ASCII visualization
  --export-json EXPORT_JSON
                        Export to JSON file
  --export-csv EXPORT_CSV
                        Export to CSV file

Examples:
  # Start new interactive session
  dimension_worksheet.py --title "My Romance Novel" --genre romance --interactive

  # Resume saved session
  dimension_worksheet.py --load sessions/my_story_session.json --interactive

  # Quick export of session to JSON
  dimension_worksheet.py --load sessions/my_story_session.json --export-json

  # Show analysis of saved session
  dimension_worksheet.py --load sessions/my_story_session.json --analyze
```

### Quick Analysis

```bash
$ python3 scripts/dimension_worksheet.py --load sessions/my_story.json --analyze

✓ Loaded session: Love in the Time of Deadlines

======================================================================
  TRAJECTORY ANALYSIS: Love in the Time of Deadlines
  Genre: romance
======================================================================

Total Beats: 7
Story Coverage: 5% to 100%
...
```

### Quick Visualization

```bash
$ python3 scripts/dimension_worksheet.py --load sessions/my_story.json --visualize

✓ Loaded session: Love in the Time of Deadlines

======================================================================
  Love in the Time of Deadlines - Dimensional Trajectory
======================================================================

INTIMACY
  Range: 0 to 10
...
```

### Export Commands

```bash
$ python3 scripts/dimension_worksheet.py --load sessions/my_story.json --export-json output.json
✓ Loaded session: Love in the Time of Deadlines
✓ Exported to JSON: output.json

$ python3 scripts/dimension_worksheet.py --load sessions/my_story.json --export-csv output.csv
✓ Loaded session: Love in the Time of Deadlines
✓ Exported to CSV: output.csv
```
