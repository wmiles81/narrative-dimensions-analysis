# Visualization Guide

How to visualize your story analysis with author-friendly charts and graphs.

---

## Choose Your Visualization Type

You have three visualization options:

1. **HTML Dimensional Report** - Static HTML showing 6 dimensions (quick, easy to share)
2. **HTML NPE Report** - Static HTML showing 4 NPE axes (big-picture arc validation)
3. **Interactive React App** - Full-featured interactive visualization with multi-layer plotting ⭐ **NEW**

---

## 🚀 OPTION 1: Interactive React App (Recommended for Advanced Analysis)

The React app provides the most powerful visualization with **multi-layer analysis**:

- **Layer 1 (Ideal)**: Genre-typical trajectory - what readers expect
- **Layer 2 (Actual)**: Your story data - what you wrote
- **Layer 3 (Difference)**: Gap analysis - where you deviate
- **Layer 4 (Correction)**: Suggested target path - how to fix it

### Quick Start

```bash
# Launch with your story data
python scripts/launch_viz_app.py examples/verity_cozy_fantasy_trajectory.json --genre fantasy --mode npe

# For dimensional analysis
python scripts/launch_viz_app.py your_story.json --genre romance --mode dimensions

# With custom title
python scripts/launch_viz_app.py your_story.json --genre fantasy --mode npe --title "My Epic Tale"
```

The launcher will:
1. ✅ Install dependencies automatically (first run only)
2. ✅ Prepare your data
3. ✅ Start the server
4. ✅ Open your browser

### Features

- **Dual Analysis Modes**: Toggle between Dimensions and NPE axes
- **Multi-Layer Plotting**: Compare ideal vs. actual, see gaps, get correction suggestions
- **Interactive Controls**: Show/hide layers, toggle dimensions, explore data points
- **Genre-Aware**: Compares against genre-specific ideal trajectories
- **Dynamic Data**: Load any trajectory JSON file
- **Real-Time Updates**: Edit code, see changes instantly

### Requirements

- Node.js and npm (download from https://nodejs.org/)
- First-time setup takes 2-3 minutes to install dependencies

### Manual Setup (If Needed)

```bash
cd viz-app
chmod +x setup.sh
./setup.sh

# Then launch manually
npm run dev
```

See `viz-app/README.md` for full documentation.

---

## OPTION 2: HTML Static Reports (No Setup Required)

Perfect for quick analysis and sharing with critique partners.

### Option 2A: Dimensional HTML Report

Shows scene-level dimensions (intimacy, trust, desire, etc.) over time.

### Generate Report

```bash
python scripts/generate_html_report.py your_trajectory.json romance output.html
```

### Example

```bash
# Generate dimensional report
python scripts/generate_html_report.py examples/verity_cozy_fantasy_trajectory.json cozy_fantasy verity_report.html
```

---

### Option 2B: NPE HTML Report

Shows high-level NPE axes for arc planning and validation.

### Generate Report

```bash
python scripts/generate_npe_html_report.py your_trajectory.json cozy_fantasy output.html
```

### What You Get (NPE Report)

- **Interactive chart** showing 4 NPE axes over time
- **Axis explanations** (what IA, RA, EA, TA mean)
- **Key statistics** (character transformation, relationship closure, dark night location)
- **Automatic insights** (polarity flip detection, arc validation)
- **Beautiful design** optimized for arc-level analysis

### Example

```bash
# Generate NPE report for cozy fantasy
python scripts/generate_npe_html_report.py examples/verity_cozy_fantasy_trajectory.json cozy_fantasy verity_npe_report.html

# Open in browser
open verity_npe_report.html  # Mac
start verity_npe_report.html  # Windows
xdg-open verity_npe_report.html  # Linux
```

The NPE HTML report shows:
- 💜 **IA** (Internal Axis): Character's wound-to-healing journey
- 💕 **RA** (Relational Axis): Relationship orbital distance
- ⚡ **EA** (Environmental Axis): External pressure curve
- ✅ **TA** (Task Axis): Quest completion arc
- 🎯 **Polarity flip** detection (when IA crosses zero)
- 🌑 **Dark night** identification (lowest IA point)

---

## Which Report Should I Use?

**Use Dimensional Report when:**
- Diagnosing specific scenes or chapters
- Engineering tension in a sequence
- Tracking detailed emotional dynamics
- Want to see individual dimensions (intimacy, trust, desire, etc.)

**Use NPE Report when:**
- Planning or validating overall story arc
- Checking genre physics compliance
- Finding the polarity flip and dark night
- Want big-picture character transformation view

**Pro tip:** Generate both! They complement each other.

---

## OPTION 3: Export Data for Custom Integration

If you have the React visualization tool, export your data in the right format:

```bash
python scripts/export_for_viz.py your_trajectory.json output_viz.json romance
```

This creates a JSON file formatted for the `UniversalNarrativeAnalyzer` React component.

### Using the Export

1. **Export your trajectory:**
   ```bash
   python scripts/export_for_viz.py examples/verity_cozy_fantasy_trajectory.json verity_viz.json romance
   ```

2. **Import in React:**
   ```javascript
   import verityData from './verity_viz.json';

   // Replace preset arc with your actual data
   const presetArcs = {
     romance: verityData.data,  // Use your actual story
     // ... other presets
   };
   ```

3. **Component will now show your real story** instead of sample data

### Genre Mapping

The export script maps to React component genre keys:
- `romance` → Romance genres (Contemporary, Dark Romance, etc.)
- `scienceFiction` → Sci-Fi genres (Space Opera, Cyberpunk, etc.)
- `fantasy` → Fantasy genres (Epic, Urban, Dark, etc.)
- `mysteryThrillerSuspense` → Mystery/Thriller genres

---

## Comparison: All Visualization Options

| Feature | React App ⭐ | HTML Dimensional | HTML NPE |
|---------|-------------|------------------|----------|
| **Ease of Use** | ✓✓ One command (after setup) | ✓✓✓ Just open in browser | ✓✓✓ Just open in browser |
| **Setup Required** | ✓ Node.js + npm (one-time) | ✗ No setup | ✗ No setup |
| **Interactivity** | ✓✓✓ Full interactive controls | ✓ Hover tooltips | ✓ Hover tooltips |
| **Multi-Layer Analysis** | ✓✓✓ Ideal/Actual/Diff/Correction | ✗ Single layer | ✗ Single layer |
| **Mode Switching** | ✓✓✓ Toggle Dimensions↔NPE live | ✗ Fixed mode | ✗ Fixed mode |
| **Data Loading** | ✓✓✓ Dynamic JSON loading | ✓ Generated once | ✓ Generated once |
| **Sharing** | ✗ Needs running server | ✓✓✓ Single HTML file | ✓✓✓ Single HTML file |
| **Gap Analysis** | ✓✓✓ Shows difference layer | ✗ Not available | ✗ Not available |
| **Correction Suggestions** | ✓✓✓ Target trajectory layer | ✗ Not available | ✗ Not available |
| **Analysis Level** | ✓✓✓ All modes | Scene/chapter detail | Arc/genre validation |
| **Dimensions Shown** | ✓✓✓ All + toggle | 5-6 genre-specific | 4 NPE axes |
| **Genre Comparison** | ✓✓✓ Live ideal overlay | ✗ No comparison | ✗ No comparison |
| **Best For** | Deep analysis, revision planning | Quick sharing, critique partners | Arc validation, genre check |

---

## Recommended Workflow

### For Authors (No Coding)

1. **Analyze with NPE text report:**
   ```bash
   python scripts/npe_author_report.py trajectory.json cozy_fantasy > analysis.txt
   ```

2. **Visualize - Generate BOTH reports:**
   ```bash
   # NPE report for arc validation
   python scripts/generate_npe_html_report.py trajectory.json cozy_fantasy npe_report.html

   # Dimensional report for scene analysis
   python scripts/generate_html_report.py trajectory.json cozy_fantasy dimensional_report.html
   ```

3. **Review:**
   - Open `npe_report.html` to check overall arc, polarity flip, dark night
   - Open `dimensional_report.html` to see scene-level tension and pacing
   - Read `analysis.txt` for actionable feedback

4. **Share:**
   - Email HTML reports to critique partners
   - Take screenshots for social media
   - Use NPE report for pitch/structure discussions

### For Developers

1. **Generate all formats:**
   ```bash
   # Text analysis (plain English)
   python scripts/npe_author_report.py story.json romance > npe_analysis.txt

   # NPE visual report (arc level)
   python scripts/generate_npe_html_report.py story.json romance npe_report.html

   # Dimensional visual report (scene level)
   python scripts/generate_html_report.py story.json romance dimensional_report.html

   # React export (JSON)
   python scripts/export_for_viz.py story.json romance viz_data.json
   ```

2. **Integrate into workflow:**
   - Use NPE HTML for arc validation and genre physics
   - Use dimensional HTML for tension analysis and pacing
   - Use React component for interactive exploration
   - Use author reports for client/stakeholder feedback

---

## Example Output

### HTML Report Includes

**Statistics Dashboard:**
```
Total Chapters: 26
Intimacy Growth: +8.5 (from 0.5 → 9.0)
Trust Journey: +7.0 (from 2.0 → 9.0)
Peak Tension: 8.2/10 (at Chapter 17)
```

**Key Insights:**
- 💡 Strong character growth: Intimacy increased by 8.5 points
- 💡 Well-timed dark night: Peak tension at Chapter 17 (65% through)
- 💡 Good pacing: Consistent emotional movement throughout
- 💡 Satisfying ending: High intimacy (9.0) and trust (9.0)

**Interactive Chart:**
- Hover over any chapter to see all dimension values
- Zoom in/out on timeline
- Toggle dimensions on/off
- Beautiful gradient design

---

## Tips for Best Visualizations

### 1. Use Descriptive Chapter Titles

Instead of:
```json
{"chapter": 1, "intimacy": 2, ...}
```

Use:
```json
{"chapter": 1, "title": "Meet Cute at the Library", "intimacy": 2, ...}
```

Tooltips will show "Meet Cute at the Library" instead of just "Chapter 1"

### 2. Track Key Dimensions for Your Genre

**Romance:**
- intimacy, trust, desire, vulnerability (relationship focus)

**Thriller:**
- danger, stakes, info_asymmetry, mystery (suspense focus)

**Fantasy:**
- danger, stakes, trust, alignment (quest focus)

### 3. Export at Different Story Stages

```bash
# After outlining
python scripts/generate_html_report.py outline.json romance outline_report.html

# After first draft
python scripts/generate_html_report.py draft1.json romance draft1_report.html

# After revisions
python scripts/generate_html_report.py final.json romance final_report.html
```

Compare HTML reports to see how your revisions affected the arc!

---

## Troubleshooting

### "File not found" error

Make sure you're in the repo directory:
```bash
cd /path/to/narrative-dimensions-analysis
python scripts/generate_html_report.py examples/verity_cozy_fantasy_trajectory.json
```

### Chart doesn't load in HTML

The HTML report uses Chart.js from CDN. Needs internet connection for first load.

### React component shows preset data

Make sure to replace the `presetArcs` object with your exported data:
```javascript
// Don't just add your data, replace the preset
const presetArcs = {
  romance: yourActualData.data,  // ← Use this
  // Remove or comment out the hardcoded preset
};
```

### Dimensions look weird

Check your trajectory JSON format:
- Dimensions should be 0-10 scale (except power_differential: -5 to +5)
- Each chapter needs: chapter number, title (optional), dimension values
- Consistent field names (intimacy not Intimacy, trust not Trust)

---

## Advanced: Customizing the HTML Report

The HTML report is a single file. You can edit it directly:

1. **Change colors:**
   Find the `borderColor` values in the JavaScript and change hex codes

2. **Add/remove dimensions:**
   Edit the `datasets` array in the Chart.js configuration

3. **Modify insights:**
   Edit the `generate_insights()` function in `generate_html_report.py`

4. **Adjust styling:**
   Modify the `<style>` section for different fonts, colors, layouts

---

## Getting Help

- HTML won't open? Check file path, try absolute path
- Chart looks wrong? Verify trajectory JSON format matches examples
- Need more customization? Check AUTHOR_GUIDE.md for report generators
- React component issues? See React documentation or web developer

**Remember:** Start with the HTML report - it's the fastest way to see your story visualized!
