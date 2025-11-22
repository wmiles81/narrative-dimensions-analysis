# Visualization Showcase

This document demonstrates all visualization types available in the Narrative Dimensions Analysis framework.

## Available Visualization Types

### 1. **Single Dimension Over Time**
Tracks one dimension through the entire story.

```
Trust Trajectory

  10 |
   9 |
   8 |
   7 |                                                 ★
   6 |
   5 |                                            ★
   4 |             ★
   3 |★       ★                      ★        ★
   2 |    ★                     ★        ★
   1 |                 ★    ★
   0 |___________________________________________________
       Beat 1                Beat 6               Beat 12

Range: 1.0 to 7.0
Change: +4.0 points
```

**Usage:**
```bash
python3 scripts/visualize_trajectory.py trajectory.json --dimension trust
```

**Use Case:** Track specific relationship dynamics (intimacy growth, trust recovery, stakes escalation)

---

### 2. **Multi-Dimension Comparison**
Shows multiple dimensions on the same graph.

```
Multiple Dimensions

  15 |                                          ■
  14 |
  13 |                     ■                    ●          ■     ★
  12 |                ●         ■                     ■    ★     ●
  11 |
  10 |          ●     ■    ●               ■    ★                ■
   9 |     ●    ■     ★               ■    ★          ★
   8 |
   7 |●                    ★          ★                    ◆
   6 |     ■    ★     ◆         ★
   5 |
   4 |◆    ★    ◆                          ◆          ◆
   3 |■    ◆                          ◆         ◆
   2 |
   1 |                     ◆    ◆
   0 |____________________________________________________________
       ★=Intimacy ◆=Trust ●=Desire ■=Vulnerability
```

**Usage:**
```bash
python3 scripts/visualize_trajectory.py trajectory.json \
  --multi intimacy trust desire vulnerability --genre romance
```

**Use Case:** See relationship dynamics interacting (trust vs. vulnerability, intimacy vs. desire)

---

### 3. **Tension Timeline**
Shows calculated tension based on genre formula.

```
Tension Trajectory

  10 |
   9 |
   8 |
   7 |
   6 |                         ████           ████
   5 |                    ████ ████           ████
   4 |                    ████ ████ ████      ████ ████
   3 |████ ████ ████ ████ ████ ████ ████ ████ ████ ████ ████
   2 |████ ████ ████ ████ ████ ████ ████ ████ ████ ████ ████
   1 |████ ████ ████ ████ ████ ████ ████ ████ ████ ████ ████ ████
   0 |____________________________________________________________
          1    2    3    4    5    6    7    8    9   10   11   12

Average Tension: 4.1/10
Peak Tension: 6.6/10 at Beat 6
Lowest Tension: 1.2/10 at Beat 12
```

**Usage:**
```bash
python3 scripts/visualize_trajectory.py trajectory.json \
  --tension --genre romance --subgenre contemporary
```

**Use Case:** Check story pacing, identify tension peaks/valleys, verify 3-act structure

---

### 4. **Tension Heatmap**
Compact view of tension across entire story.

```
Tension Heatmap

Ch  1 ▒
Ch  2 ▒
Ch  3 ▒
Ch  4 ▒
Ch  5 ▓  ← Rising
Ch  6 ▓  ← Peak
Ch  7 ▒
Ch  8 ▒
Ch  9 ▓  ← Climax
Ch 10 ▒
Ch 11 ▒
Ch 12 ░  ← Relief scene

Legend: ░=Low ▒=Medium ▓=High █=Extreme
```

**Usage:**
```bash
python3 scripts/visualize_trajectory.py trajectory.json --heatmap --genre romance
```

**Use Case:** Quick at-a-glance story structure review, identify "sagging middle"

---

### 5. **Pacing Velocity**
Shows rate of change (how fast dimensions are moving).

```
Pacing Velocity

 2.2 |                     ★
 1.9 |         ★              ★
 1.7 |                           ★  ★
 1.5 |               ★  ★
 1.3 |★           ★
 1.1 |      ★
 0.9 |   ★
 0.6 |
 0.4 |
 0.2 |
 0.0 |                              ____
        1  2  3  4  5  6  7  8  9 10 11

Velocity: Avg 1.7 points/chapter
```

**Usage:**
```bash
python3 scripts/visualize_trajectory.py trajectory.json --velocity
```

**Use Case:** Diagnose pacing issues (rushed endings, slow middle, velocity spikes)

---

### 6. **Full Report**
Combines all visualizations with pattern analysis.

**Usage:**
```bash
python3 scripts/visualize_trajectory.py trajectory.json \
  --full-report --genre romance --subgenre contemporary
```

**Use Case:** Comprehensive story analysis for revision

---

### 7. **Subplot Comparison**
Analyze multiple parallel storylines simultaneously.

```
MAIN ROMANCE ARC: Multiple Dimensions

  12 |                                                           ●
  11 |
  10 |                                               ●           ◆
   9 |                       ●           ●
   8 |           ●                                   ◆
   7 |●
   6 |                       ◆
   5 |
   4 |           ◆                       ★
   3 |◆          ★
   2 |★                                  ◆
   1 |
   0 |____________________________________________________________
       ★=Intimacy ◆=Trust ●=Desire

Combined Tension Timeline (50% romance, 50% career):

Beat  1: ███████████████████ 1.35
Beat  2: █████████████████████ 1.50
Beat  3: █████████████████████████ 1.73
Beat  4: ████████████████████████████████████████ 2.73  ← Peak!
Beat  5: █████████████████████████ 1.75
Beat  6: ██████████████████ 1.23
```

**Usage:**
```python
from subplot_tracker import SubplotTracker

tracker = SubplotTracker()
tracker.add_plot('main', main_trajectory, genre='romance')
tracker.add_plot('subplot', sub_trajectory, genre='thriller')

print(tracker.generate_report())
```

**Use Case:** Track parallel storylines, find synchronized peaks, balance subplot weight

---

### 8. **Diagnostic Pattern Detection**
Automatic identification of narrative problems and strengths.

```
🚨 CRITICAL ISSUES (Must Fix)

1. SAGGING_MIDDLE
   Act 2 tension drops below 50% of Act 1 peak (2.5 vs 5.3)
   FIX: Acts 4-6 need stronger conflict. Raise stakes, add obstacles,
   or introduce new complications. Target tension: 4.0+

2. TELEPORTATION
   Beat 7: trust jumped 6.0 points without catalyst event
   FIX: Add a catalyst event to justify this dramatic shift.
   Examples: revelation, betrayal, sacrifice, confrontation.

💪 STRENGTHS (What's Working)

1. COMPELLING_ARC
   Excellent emotional journey with clear progression
   Why it works: Strong character growth across all dimensions
```

**Usage:**
```bash
python3 scripts/diagnostic_patterns.py trajectory.json \
  --genre romance --catalysts catalysts.json
```

**Use Case:** Automated manuscript review, identify structural problems before beta readers

---

## Quick Tips

### Best Practices
1. **Use multi-dimension** to see relationship dynamics interacting
2. **Use tension timeline** to check 3-act structure
3. **Use velocity** to diagnose "rushed" or "dragging" sections
4. **Use diagnostics** before sending to beta readers
5. **Use subplot tracker** for books with B-plots or POV changes

### Common Workflows

**Planning a new story:**
```bash
# Create worksheet interactively
python3 scripts/dimension_worksheet.py

# Visualize planned trajectory
python3 scripts/visualize_trajectory.py exports/mystory.json --full-report
```

**Revising existing story:**
```bash
# Run diagnostics first
python3 scripts/diagnostic_patterns.py mystory.json --genre romance

# Fix issues and visualize
python3 scripts/visualize_trajectory.py mystory.json --tension --velocity
```

**Complex multi-POV story:**
```python
# Track each POV separately
tracker = SubplotTracker()
tracker.add_plot('pov1', trajectory1, genre='romance')
tracker.add_plot('pov2', trajectory2, genre='thriller')

# Find where they intersect
comparison = tracker.compare_plots()
print(comparison['synchronized_peaks'])
```

---

## Output Formats

All visualizations support:
- **Console output** (default) - ASCII art for terminal display
- **File export** via `--output filename.txt`
- **Programmatic access** - Import functions for custom tools

---

## Examples Directory

See `examples/` for pre-built trajectories demonstrating:
- Contemporary romance (`romance-contemporary-example.md`)
- Dark romance (`dark-romance-trajectory.md`)
- Psychological thriller (`psychological-thriller-analysis.md`)
- Cozy mystery (`cozy-mystery-example.md`)
- Romantic fantasy (`romantic-fantasy-hybrid.md`)

Each example includes full trajectory JSON and detailed analysis.
