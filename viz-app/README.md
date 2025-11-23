# Narrative Dimensions Visualization App

Interactive React-based visualization tool for narrative analysis.

## Features

- **Dual Analysis Modes**
  - **Dimensions Mode**: Visualize 10+ narrative dimensions (intimacy, trust, stakes, etc.)
  - **NPE Mode**: Plot 4 NPE axes (IA, RA, EA, TA)

- **Multi-Layer Visualization**
  - **Ideal Layer**: Genre-typical trajectory (reference curve)
  - **Actual Layer**: Your story data (what you wrote)
  - **Difference Layer**: Gap analysis (Δ between ideal and actual)
  - **Correction Layer**: Suggested path to align with genre expectations

- **Dynamic Data Loading**
  - Load trajectory JSON files
  - Supports chapter-by-chapter analysis
  - Auto-detects NPE vs dimensional data

- **Genre-Aware Analysis**
  - Romance (Romancing the Beat structure)
  - Fantasy (Hero's Journey structure)
  - Cozy Fantasy (Custom cozy arc)
  - Mystery/Thriller
  - And more...

## Quick Start

### Option 1: Launch from Python Skill (Recommended)

```bash
# Launch with dimensional analysis
python scripts/launch_viz_app.py examples/verity_cozy_fantasy_trajectory.json --genre fantasy --mode dimensions

# Launch with NPE analysis
python scripts/launch_viz_app.py examples/verity_cozy_fantasy_trajectory.json --genre fantasy --mode npe

# With custom title
python scripts/launch_viz_app.py your_story.json --genre romance --mode dimensions --title "My Amazing Story"
```

The Python launcher will:
1. Install dependencies (first run only)
2. Prepare your data
3. Start the development server
4. Open your browser automatically

### Option 2: Manual Setup

```bash
cd viz-app

# Install dependencies (first time only)
npm install

# Start development server
npm run dev

# App opens at http://localhost:3000
```

Then load data via URL parameter:
```
http://localhost:3000/?data=/data/story_data.json&mode=npe&genre=fantasy
```

## Data Format

### Dimensions Mode

```json
{
  "trajectory": [
    {
      "chapter": 1,
      "title": "Chapter Title",
      "intimacy": 2,
      "trust": 3,
      "vulnerability": 2,
      "stakes": 5,
      "desire": 1,
      "proximity": 4,
      "goal_alignment": 6,
      "info_asymmetry": 2
    },
    ...
  ],
  "metadata": {
    "title": "Your Story Title",
    "genre": "romance",
    "totalChapters": 26
  }
}
```

### NPE Mode

```json
{
  "trajectory": [
    {
      "chapter": 1,
      "title": "Chapter Title",
      "IA": -0.85,
      "RA": 160,
      "EA": 0.0,
      "TA": 0.1
    },
    ...
  ],
  "metadata": {
    "title": "Your Story Title",
    "genre": "fantasy",
    "totalChapters": 26
  }
}
```

## Layer Controls

### Ideal Layer (Dashed Lines)
Shows the typical trajectory for the selected genre. This is your reference curve based on genre conventions.

### Actual Layer (Solid Lines)
Your story's actual trajectory data. This shows what you've written.

### Difference Layer (Yellow)
Calculates the gap between ideal and actual at each point. Helps identify where your story deviates from genre expectations.

### Correction Layer (Green)
Suggests a target trajectory that blends from your current story toward the genre ideal. Use this to plan revisions.

## NPE Mode

When in NPE mode, the app displays the four composite axes:

- **IA (Internal Axis)**: Character's wound-to-healing journey (-1 to +1)
- **RA (Relational Axis)**: Relationship orbital distance (0° to 180°, normalized to -1 to +1 for chart)
- **EA (Environmental Axis)**: External pressure (-1 to +1)
- **TA (Task Axis)**: Quest/goal completion (0 to 1)

The zero line (IA = 0) is prominently displayed as the polarity flip point.

## Development

### Tech Stack
- React 18
- Vite (fast build tool)
- Recharts (charting library)
- Inline Tailwind-style CSS

### Build for Production

```bash
npm run build
```

Output goes to `dist/` directory.

### Project Structure

```
viz-app/
├── package.json          # Dependencies
├── vite.config.js        # Vite configuration
├── index.html            # HTML entry point
├── src/
│   ├── main.jsx          # React entry point
│   ├── App.jsx           # Main application component
│   └── index.css         # Global styles
└── public/
    └── data/             # Data files loaded by app
        └── story_data.json
```

## Troubleshooting

### npm not found
Install Node.js from https://nodejs.org/

### Port 3000 already in use
Change port in `vite.config.js`:
```js
server: {
  port: 3001,  // Change this
  open: true
}
```

### Data not loading
- Ensure data file is in `public/data/`
- Check browser console for errors
- Verify JSON format is valid

## Integration with Skill

The visualization app integrates seamlessly with the narrative-dimensions-analysis skill:

```bash
# From skill scripts directory
python scripts/launch_viz_app.py examples/verity_cozy_fantasy_trajectory.json \
  --genre fantasy \
  --mode npe \
  --title "Verity's Cozy Fantasy"
```

The launcher script handles:
- Data format conversion
- Server startup
- Browser opening
- URL parameter construction

## License

Part of the Narrative Dimensions Analysis skill package.
