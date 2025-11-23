# Author's Guide to Dimensional Analysis
## Scene-by-Scene Emotional Tracking (No Coding Required!)

---

## What Dimensional Analysis Does (In Plain English)

Think of each scene as having an emotional "fingerprint." Dimensional analysis helps you:

- **Diagnose** why a specific scene feels flat or rushed
- **Track** emotional dynamics chapter-by-chapter
- **Engineer** tension in individual scenes
- **Balance** intimacy, trust, vulnerability, and stakes
- **Fix** pacing problems scene by scene

**No coding required.** You just have conversations with Claude, or generate automatic reports.

**Bonus:** Generate visual reports showing your dimensions over time! See the "Getting Reports" section below.

---

## When to Use Dimensional Analysis

**Use Dimensions when:**
- Diagnosing a specific scene that feels "off"
- Planning chapter-by-chapter emotional progression
- Engineering tension in a sequence
- Tracking detailed relationship dynamics
- You want granular, zoomed-in analysis

**Use NPE instead when:**
- Validating overall story arc structure
- Checking if your character's journey works
- Ensuring genre physics compliance
- You want big-picture, zoomed-out analysis

**You can use both!** They complement each other.

---

## The Core Dimensions Explained

### **Romance/Relationship Genres**

#### 1. **Intimacy** (0-10)
How emotionally close are the characters?
- **0-3**: Strangers, hostile, distant
- **4-6**: Warming up, tentative connection
- **7-9**: Close, vulnerable with each other
- **10**: Deep emotional bond

**For authors:** Track the journey from distant to close.

#### 2. **Trust** (0-10)
Do they believe in each other's good intentions?
- **0-3**: Suspicious, guarded
- **4-6**: Starting to trust, testing
- **7-9**: Solid trust, rely on each other
- **10**: Complete faith

**For authors:** Trust must be earned through actions, not told.

#### 3. **Desire/Attraction** (0-10)
How much do they want each other?
- **0-3**: Not attracted, indifferent
- **4-6**: Noticing, curiosity
- **7-9**: Strong pull, can't ignore it
- **10**: Consuming desire

**For authors:** Desire creates tension, especially when intimacy is low.

#### 4. **Vulnerability** (0-10)
How emotionally exposed are they?
- **0-3**: Walls up, protected
- **4-6**: Sharing some truth
- **7-9**: Raw, unguarded moments
- **10**: Completely open

**For authors:** Vulnerability + low trust = high tension.

### **All Genres**

#### 5. **Stakes** (0-10)
What will they lose if they fail?
- **0-3**: Low consequences
- **4-6**: Moderate pressure
- **7-9**: Serious risk
- **10**: Everything on the line

**For authors:** Stakes should escalate toward climax.

#### 6. **Self-Worth** (0-10)
Does the character value themselves?
- **0-3**: Broken, feels inadequate
- **4-6**: Struggling, uncertain
- **7-9**: Growing confidence
- **10**: Fully self-assured

**For authors:** Track internal character growth.

#### 7. **Goal Alignment** (0-10)
How aligned are their goals?
- **0-3**: Working against each other
- **4-6**: Partial alignment, some conflict
- **7-9**: Mostly aligned
- **10**: Perfect unity of purpose

**For authors:** Misalignment creates external conflict.

#### 8. **Info Asymmetry** (0-10)
How much do they know that others don't?
- **0-3**: Everyone knows everything
- **4-6**: Some secrets
- **7-9**: Major information gaps
- **10**: Massive deception

**For authors:** Secrets create mystery and tension.

#### 9. **Power Differential** (-5 to +5)
Who has more power in the relationship?
- **Negative**: One character dominates
- **0**: Balanced power
- **Positive**: Other character dominates

**For authors:** Power imbalance creates specific dynamics (dark romance, captive, etc.)

#### 10. **Proximity** (0-10)
How physically close are they forced to be?
- **0-3**: Separated, far apart
- **4-6**: Occasional contact
- **7-9**: Frequent interaction
- **10**: Forced together constantly

**For authors:** High proximity + low trust = forced proximity trope.

---

## Quick Start: Using Dimensions in Claude Chat

### **Diagnosing a Flat Scene**

Copy and paste this template:

```
This scene feels [flat/rushed/confusing]. Can you diagnose it using
narrative dimensions?

Scene: [brief description]

Current dimensional state:
- Intimacy: [0-10]
- Trust: [0-10]
- Vulnerability: [0-10]
- Stakes: [0-10]
- Desire: [0-10] (if romance)
- Goal Alignment: [0-10]

What's wrong and how do I fix it?
```

**Example:**
```
This scene feels flat. Can you diagnose it using narrative dimensions?

Scene: Hero and mentor talk about the quest over dinner

Current dimensional state:
- Intimacy: 6
- Trust: 7
- Vulnerability: 3
- Stakes: 3
- Goal Alignment: 9

What's wrong and how do I fix it?
```

**Claude will respond with:**
- What's missing (usually tension!)
- Specific dimensional gaps
- Concrete suggestions to fix it

---

### **Engineering Tension**

When you need to ramp up tension:

```
I need to increase tension in this scene using dimensions.

Current state:
- Intimacy: [number]
- Trust: [number]
- Vulnerability: [number]
- Stakes: [number]

What dimensional changes would create the most tension?
```

**Claude will suggest:**
- Vulnerability-trust gaps (emotionally exposed but not safe)
- Desire-intimacy gaps (want but can't have)
- High stakes + low goal alignment (working at cross purposes under pressure)

---

## Getting Dimensional Reports

You have multiple ways to analyze your story:

### **Option 1: Technical Analysis Report** (For Advanced Users)

Generate detailed numerical analysis with formulas:

```bash
python scripts/dimensional_analyzer.py your_story.json cozy_fantasy
```

**What you get:**
- Numerical dimensional progression with statistics (mean, stdev, range)
- Mathematical tension calculations with formulas
- Gradient analysis (rate of change per chapter)
- Correlation matrix showing dimensional relationships
- Dimensional gap analysis with tension contributions
- Chapter-by-chapter breakdown
- **Technical terminology included**

**Example output:**
```
Dimension         | Start | End   | Δ     | Mean  | StdDev | Range
------------------|-------|-------|-------|-------|--------|-------
intimacy          |   1.0 |   9.0 |  +8.0 |   4.8 |   2.47 | [1.0, 9.0]

Pearson Correlation:
  intimacy ⟷ trust: r = +0.978 ↑↑ (strong positive)

Volatile Chapters (|Δ| > 2.0): 14, 18, 19
```

**Use this if:** You want deep statistical analysis, formulas, and numerical precision.

---

### **Option 2: Author-Friendly Text Report**

Generate a scene analysis report in plain English:

```bash
python scripts/dimensional_author_report.py your_story.json cozy_fantasy
```

**What you get:**
- Scene-by-scene emotional state
- Tension analysis with recommendations
- Vulnerability-trust gaps identified
- Pacing feedback
- Actionable suggestions in plain language
- **No technical jargon**

**Example output:**
```
EMOTIONAL RISK: High vulnerability (8.0) with low trust (3.0)
Character is emotionally exposed and scared

YEARNING: Strong desire (9.0) but low intimacy (2.0)
Creates longing and anticipation
```

**Use this if:** You want practical writing advice without formulas.

---

### **Option 3: Visual HTML Report**

Generate a beautiful interactive chart:

```bash
python scripts/generate_html_report.py your_story.json cozy_fantasy output.html
```

**What you get:**
- Interactive Chart.js visualization
- All dimensions plotted over time
- Statistics dashboard
- Hover tooltips for each chapter
- Self-contained HTML file (email to critique partners!)

**Genre-aware:** Shows different dimensions for different genres:
- Romance: intimacy, trust, desire, vulnerability, stakes
- Cozy Fantasy: self-worth, trust, vulnerability, stakes, goal progress
- Thriller: stakes, secrets, vulnerability, trust, danger

**Use this if:** You want shareable visual reports without running a server.

---

### **Option 4: Interactive React App**

Full-featured visualization with multi-layer analysis:

```bash
python scripts/launch_viz_app.py your_story.json --genre fantasy --mode dimensions
```

**What you get:**
- Toggle individual dimensions on/off
- Compare your story vs. genre ideal
- See gap analysis (difference layer)
- Get correction suggestions
- Switch to NPE mode anytime

See `viz-app/QUICKSTART.md` for details.

**Use this if:** You want the most powerful analysis with multi-layer comparison and correction suggestions.

---

### **Which Report Should I Use?**

| Feature | Technical | Author-Friendly | HTML Visual | React App |
|---------|-----------|-----------------|-------------|-----------|
| **Formulas & Stats** | ✓✓✓ | ✗ | ✗ | ✗ |
| **Plain English** | ✗ | ✓✓✓ | ✓✓ | ✓✓ |
| **Visual Charts** | ✗ | ✗ | ✓✓✓ | ✓✓✓ |
| **Shareable** | ✓ Text file | ✓ Text file | ✓✓✓ HTML file | ✗ Needs server |
| **Gap Analysis** | ✓✓✓ Numerical | ✓✓ Descriptive | ✗ | ✓✓✓ Visual |
| **Correlation Matrix** | ✓✓✓ | ✗ | ✗ | ✗ |
| **Ideal Comparison** | ✗ | ✗ | ✗ | ✓✓✓ |
| **Setup Required** | ✗ | ✗ | ✗ | ✓ Node.js |
| **Best For** | Statistical analysis | Writing feedback | Quick visualization | Deep revision work |

**Quick Guide:**
- **Just starting?** → Author-Friendly Text Report
- **Need stats?** → Technical Report
- **Sharing with critique partners?** → HTML Visual Report
- **Serious revision?** → React App with multi-layer analysis

---

## Common Dimensional Patterns

### **The Flat Scene Problem**

**Symptoms:** Nothing feels urgent, characters just talk

**Diagnosis:**
- Stakes: 2-3 (too low)
- All dimensions aligned (no conflict)
- No vulnerability (no emotional risk)

**Fix:**
- Raise stakes: Add a ticking clock
- Create dimensional gap: High vulnerability + low trust
- Add goal misalignment: They want different things

---

### **The Rushed Romance**

**Symptoms:** Relationship feels unearned

**Diagnosis:**
- Intimacy jumps from 3 → 9 in one chapter
- Trust increases without scenes showing it
- No vulnerability progression

**Fix:**
- Slow intimacy growth: 3 → 4 → 5 → 6 over multiple scenes
- Show trust being earned: Promises kept, actions not words
- Build vulnerability gradually: Small reveals before big ones

---

### **The Tension Vacuum**

**Symptoms:** Everything is peaceful, reader gets bored

**Diagnosis:**
- Stakes plateau at mid-level
- No dimensional gaps (everything in harmony)
- Characters agree on everything

**Fix:**
- Escalate stakes every act
- Create gaps: High desire + low intimacy, or high vulnerability + low trust
- Add misalignment: They want the same goal but disagree on how

---

## Dimensional Gaps Create Tension

The most powerful scenes have **dimensional gaps**:

### **High Vulnerability + Low Trust** = EMOTIONAL RISK
Character is exposed and unsafe
- Example: Forced to reveal secret to someone who might use it against them
- Creates intense emotional tension

### **High Desire + Low Intimacy** = YEARNING
They want but can't have
- Example: Attracted to someone they barely know
- Creates romantic tension

### **High Stakes + Low Goal Alignment** = EXTERNAL CONFLICT
Fighting while the clock ticks
- Example: Must work together to survive but want different outcomes
- Creates plot tension

### **High Proximity + Low Trust** = FORCED PROXIMITY
Trapped together with someone dangerous/unknown
- Example: Road trip with enemy, locked in safe room
- Creates situational tension

---

## Genre Cheat Sheet: Dimensional Targets

### **Cozy Fantasy**
- **Self-Worth:** Start low (2-3) → End high (8-9)
- **Trust:** Build steadily (3 → 9)
- **Stakes:** Stay moderate (never exceed 7-8)
- **Vulnerability:** Gradual increase
- **Goal Alignment:** High by end (8-9)

### **Dark Romance**
- **Intimacy:** Volatile, can spike and crash
- **Power Differential:** High (±3 to ±5)
- **Vulnerability:** High + Low Trust = signature tension
- **Stakes:** Very high (8-10)
- **Desire:** High early, creates conflict

### **Thriller**
- **Stakes:** Escalate constantly (start 5 → end 10)
- **Info Asymmetry:** Very high (8-10)
- **Trust:** Low, character doesn't know who to trust
- **Vulnerability:** High risk of exposure
- **Goal Alignment:** Shifts as loyalties questioned

### **Romance (Any Subgenre)**
- **Intimacy:** 0 → 9-10 by end
- **Trust:** 1-3 → 8-10 (must be earned)
- **Desire:** Present early, creates tension
- **Vulnerability:** Required for deep connection
- **Final State:** Intimacy 8-10, Trust 7-10, Tension 0-3

---

## Workflows for Different Stages

### **Planning (Before You Write)**

1. **Map key scenes** with dimensional targets
   ```
   Chapter 5: First vulnerable moment
   - Intimacy: 4 (warming up)
   - Trust: 3 (still cautious)
   - Vulnerability: 7 (she reveals wound)
   - Creates gap: high vulnerability + low trust = tension!
   ```

2. **Plan dimensional progression**
   - Chapter 1-5: Build trust slowly (2 → 5)
   - Chapter 6-10: Increase intimacy (3 → 7)
   - Chapter 11-15: Spike vulnerability (create crisis)

### **Drafting (While You Write)**

Check each scene:
- What are the current dimensional values?
- Is there a gap creating tension?
- Does this move dimensions forward?

Use Claude Chat for quick checks.

### **Revising (After First Draft)**

Generate reports to see:
- Where dimensions plateau (boring sections)
- Where dimensions spike too fast (feels rushed)
- Where gaps close prematurely (lost tension)

**Fix:**
- Add scenes to slow growth
- Remove scenes where nothing changes
- Adjust dimensional values to create better pacing

---

## Copy-Paste Templates

### **Template 1: Scene Diagnosis**

```
Diagnose this scene using narrative dimensions:

Scene: [describe what happens]

Genre: [cozy fantasy / romance / thriller / etc.]

Current dimensions:
- Intimacy: [0-10]
- Trust: [0-10]
- Vulnerability: [0-10]
- Stakes: [0-10]
- Self-worth: [0-10]
- Goal alignment: [0-10]

Problem: Scene feels [flat / rushed / confusing]

What's wrong dimensionally and how do I fix it?
```

### **Template 2: Tension Engineering**

```
I need to engineer tension in this scene using dimensional gaps.

Scene: [describe]
Current state:
- Intimacy: [number]
- Trust: [number]
- Vulnerability: [number]
- Desire: [number] (if romance)
- Stakes: [number]

Which dimensional gap would create the most tension here?
```

### **Template 3: Chapter Planning**

```
Help me plan the dimensional progression for Chapter [X].

Genre: [your genre]
Story point: [what needs to happen plot-wise]

Previous chapter dimensions:
- Intimacy: [number]
- Trust: [number]
- [other relevant dimensions]

What should the dimensions be at the END of this chapter?
What gap should drive the tension?
```

---

## Visualizing Your Story

Once you have dimensional data, visualize it:

**Quick HTML Report:**
```bash
python scripts/generate_html_report.py my_story.json romance my_report.html
```

**Interactive Analysis:**
```bash
python scripts/launch_viz_app.py my_story.json --genre romance --mode dimensions
```

See `VISUALIZATION_USAGE.md` for complete guide.

---

## Getting Started Right Now

1. **Open Claude Chat**
2. **Copy Template 1 above** (Scene Diagnosis)
3. **Fill in your scene details**
4. **Paste and send**

Claude will analyze your dimensions and give you specific fixes.

**For reports:** Use the scripts above to generate visual analysis.

**No physics degree required.** 📚✨

---

## What's Next?

**For big-picture arc analysis:** See `AUTHOR_GUIDE_NPE.md`

**For visualization:** See `VISUALIZATION_USAGE.md`

**For technical details:** See `SKILL.md`
