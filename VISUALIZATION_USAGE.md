# Visualization Guide

How to visualize your story analysis with author-friendly charts and graphs.

---

## Option 1: Standalone HTML Report (Easiest)

Creates a self-contained HTML file you can open in any browser. **No coding or web server required.**

### Generate Report

```bash
python scripts/generate_html_report.py your_trajectory.json romance output.html
```

### What You Get

- **Interactive chart** showing all dimensions over time
- **Key statistics** (chapter count, growth metrics, peak tension)
- **Automatic insights** based on your story arc
- **Beautiful design** that's easy to share with critique partners

### Example

```bash
# Analyze your cozy fantasy
python scripts/generate_html_report.py examples/verity_cozy_fantasy_trajectory.json cozy_fantasy verity_report.html

# Open in browser
open verity_report.html  # Mac
start verity_report.html  # Windows
xdg-open verity_report.html  # Linux
```

The HTML report shows:
- ❤️ Intimacy progression
- 🤝 Trust building
- 💘 Desire arc
- ⚡ Stakes curve
- 💔 Vulnerability journey
- 📈 **TENSION** (calculated automatically)

---

## Option 2: Export for React Component

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

## Comparison: HTML vs React

| Feature | HTML Report | React Component |
|---------|-------------|-----------------|
| **Ease of Use** | ✓✓✓ Just open in browser | Requires React setup |
| **Sharing** | ✓✓✓ Single file, email-friendly | Needs hosting |
| **Interactivity** | ✓✓ Hover tooltips, chart zoom | ✓✓✓ Full interactive controls |
| **Customization** | ✓ Edit HTML/CSS | ✓✓✓ React props, full control |
| **Genre Analysis** | ✓ Basic insights | ✓✓✓ Genre validation, plot beats |
| **Best For** | Quick analysis, sharing | Development, deep analysis |

---

## Recommended Workflow

### For Authors (No Coding)

1. **Analyze with NPE:**
   ```bash
   python scripts/npe_author_report.py trajectory.json cozy_fantasy > analysis.txt
   ```

2. **Visualize:**
   ```bash
   python scripts/generate_html_report.py trajectory.json cozy_fantasy report.html
   ```

3. **Share:**
   - Email `report.html` to critique partners
   - Open in browser to review yourself
   - Take screenshots for social media

### For Developers

1. **Generate multiple formats:**
   ```bash
   # Author report (text)
   python scripts/npe_author_report.py story.json romance > report.txt

   # Visual report (HTML)
   python scripts/generate_html_report.py story.json romance report.html

   # React export (JSON)
   python scripts/export_for_viz.py story.json romance viz_data.json
   ```

2. **Integrate into workflow:**
   - Use HTML reports for quick reviews
   - Use React component for detailed analysis
   - Use author reports for actionable feedback

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
