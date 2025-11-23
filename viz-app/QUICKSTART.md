# Quick Start Guide - React Visualization App

## ✅ Data is Ready!

Verity's cozy fantasy trajectory has been prepared and is waiting at:
```
viz-app/public/data/verity_data.json
```

**Story:** Verity's Cozy Fantasy
**Genre:** Fantasy (Cozy Fantasy)
**Chapters:** 26
**Data Format:** NPE axes (IA, RA, EA, TA) + Dimensions

## 🚀 Run on Your Local Machine

### Option 1: One-Command Launch (Recommended)

```bash
# Clone/pull the repository to your Mac
cd /Volumes/home/github/narrative-dimensions-analysis

# Pull latest changes
git pull origin claude/review-skill-repo-015x8cJNrtTWp5miiS2B6Ah5

# Launch visualization (auto-installs dependencies if needed)
python scripts/launch_viz_app.py examples/verity_cozy_fantasy_trajectory.json \
  --genre fantasy \
  --mode npe \
  --title "Verity's Cozy Fantasy"
```

The launcher will:
1. Check for Node.js/npm (install from https://nodejs.org/ if needed)
2. Install React app dependencies (first time only, ~2-3 minutes)
3. Prepare Verity's data
4. Start the development server
5. Open your browser automatically

### Option 2: Manual Setup

```bash
# Navigate to viz-app
cd viz-app

# Install dependencies (first time only)
npm install

# Start development server
npm run dev
```

Then open browser to:
```
http://localhost:3000/?data=/data/verity_data.json&mode=npe&genre=fantasy
```

## 🎮 Using the Visualization App

### 1. Analysis Mode Toggle

Switch between two modes at the top:

- **Dimensions Mode**: See self-worth, trust, vulnerability, stakes, goal_alignment
- **NPE Mode**: See IA, RA, EA, TA axes (polarity flip, dark night, etc.)

### 2. Layer Controls

Toggle these layers on/off:

- **✓ Ideal** (dashed lines): Genre-typical cozy fantasy arc
- **✓ Actual** (solid lines): Verity's actual story data
- **☐ Difference** (yellow): Gap between ideal and actual
- **☐ Correction** (green): Suggested target path

### 3. Dimension/Axis Controls

At the bottom, check/uncheck individual dimensions or NPE axes to show/hide them on the chart.

### 4. Interactive Chart

- **Hover** over data points to see exact values
- **Zoom** using mouse wheel (if enabled)
- **Pan** by dragging (if enabled)

## 📊 What to Look For

### In NPE Mode:

1. **IA (Internal Axis) - Purple Line**
   - Starts at -0.85 (deeply wounded)
   - Watch for **polarity flip** where it crosses zero
   - Should end positive (healed)

2. **RA (Relational Axis) - Pink Line**
   - Starts at 160° (distant/strangers)
   - Normalized to -1 to +1 scale for chart
   - Should close to ~60° (close/intimate) for cozy fantasy

3. **EA (Environmental Axis) - Orange Line**
   - External pressure throughout story
   - Cozy fantasy: should stay relatively low

4. **TA (Task Axis) - Green Line**
   - Quest completion: 0 → 1
   - Should reach 0.9-1.0 by end

### In Dimensions Mode:

1. **Self-Worth** (purple): Character's internal growth (2 → 9)
2. **Trust** (green): Building trust in magic/friends (3 → 9)
3. **Vulnerability** (blue): Emotional openness
4. **Stakes** (red): What's at risk
5. **Goal Alignment** (green): Progress on quest

### Multi-Layer Analysis:

**Enable Difference Layer (yellow):**
- Shows where Verity's arc deviates from cozy fantasy ideal
- Positive values = exceeds ideal (might be too intense)
- Negative values = below ideal (might feel flat)

**Enable Correction Layer (green):**
- Shows target trajectory to better align with genre
- Blends from current arc toward ideal
- Use this to plan revision strategy

## 🔧 Troubleshooting

### "npm not found"
Install Node.js from https://nodejs.org/

### Port 3000 already in use
Edit `viz-app/vite.config.js` and change port to 3001

### Data not loading
- Ensure you're accessing via `localhost:3000/?data=/data/verity_data.json`
- Check browser console (F12) for errors
- Verify `viz-app/public/data/verity_data.json` exists

### Chart not displaying
- Ensure all dependencies installed: `npm install` in viz-app directory
- Check for JavaScript errors in browser console
- Try refreshing the page

## 📁 Files in This Package

```
viz-app/
├── public/data/verity_data.json   ← Verity's story data (READY!)
├── src/App.jsx                    ← Main visualization component
├── package.json                   ← Dependencies
└── README.md                      ← Full documentation

scripts/
└── launch_viz_app.py              ← Python launcher script

examples/
└── verity_cozy_fantasy_trajectory.json  ← Source data
```

## 🎯 Next Steps

1. **Run the app** using Option 1 or 2 above
2. **Toggle to NPE mode** to see IA, RA, EA, TA axes
3. **Enable Difference layer** to see gaps from ideal
4. **Enable Correction layer** to see revision targets
5. **Switch to Dimensions mode** to see detailed chapter analysis
6. **Take screenshots** or export findings for your writing

## 💡 Tips

- Start with **NPE mode** to validate overall arc structure
- Switch to **Dimensions mode** to diagnose specific chapters
- Use **Difference layer** to identify problem areas
- Use **Correction layer** to plan revisions
- **Hover tooltips** show exact values for each chapter

Enjoy exploring your story's narrative physics! 🚀
