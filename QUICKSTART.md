# Dimension Worksheet - Quick Start

## 30-Second Start

```bash
cd /home/user/narrative-dimensions-analysis
python3 scripts/dimension_worksheet.py --title "My Story" --genre romance --interactive
```

Follow the prompts. Type `?` for help on any dimension scoring.

## Common Commands

```bash
# Start fresh
python3 scripts/dimension_worksheet.py --title "Title" --genre romance --interactive

# Resume work
python3 scripts/dimension_worksheet.py --load sessions/my_story.json --interactive

# Quick analysis
python3 scripts/dimension_worksheet.py --load sessions/my_story.json --analyze

# Export for validation
python3 scripts/dimension_worksheet.py --load sessions/my_story.json --export-json trajectory.json
python3 scripts/validate_trajectory.py trajectory.json
```

## Key Dimensions (Romance)

- **intimacy** (0-10): How close they are emotionally
- **trust** (0-10): How much they rely on each other
- **desire** (0-10): How much they want to be together
- **vulnerability** (0-10): How open they are emotionally
- **stakes** (0-10): What's at risk

## Quick Scoring Guide

| Score | Intimacy | Trust | Desire |
|-------|----------|-------|--------|
| 0 | Strangers | Complete distrust | Repulsion |
| 2 | Acquaintances | Suspicious | Minimal attraction |
| 4 | Friends | Cautious trust | Noticeable interest |
| 6 | Close friends | Working trust | Strong attraction |
| 8 | Deep connection | Strong trust | Intense desire |
| 10 | Total unity | Absolute trust | All-consuming |

## Tips

1. **Type `?`** during interactive mode for dimension guides
2. **Type `help`** for beat name examples
3. **Load templates** - They're pre-filled with good examples
4. **Save often** - Choose option 5 or 6 after adding beats
5. **Watch for warnings** - Large jumps need catalyst events

## What Gets Created

- `exports/YourStory_*.json` - For validate_trajectory.py
- `exports/YourStory_*.csv` - For Excel/Google Sheets
- `sessions/YourStory_session_*.json` - Resume your work

## Full Documentation

- `docs/dimension-worksheet-guide.md` - Complete user guide
- `docs/worksheet-sample-output.md` - Example outputs
- `examples/interactive_demo.md` - Session walkthrough
