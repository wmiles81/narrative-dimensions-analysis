# Author's Guide to NPE (Narrative Physics Engine)
## Big Picture Arc Planning (No Coding Required!)

---

## What NPE Does (In Plain English)

Think of your story as having "physics" - like how far a character can fall emotionally, or when they must start healing to satisfy readers. NPE helps you:

- **Validate** your overall character arc structure
- **Plan** when the dark night and polarity flip should happen
- **Check** if your story matches genre expectations
- **Design** character transformation from wounded to healed
- **Track** relationship progression from distant to close

**No coding required.** You just have conversations with Claude, or generate automatic reports.

**Bonus:** Generate visual reports showing your NPE arc! See the "Getting Reports" section below.

---

## When to Use NPE

**Use NPE when:**
- Planning overall story arc structure
- Validating character transformation works
- Checking genre physics compliance
- Finding where dark night and polarity flip should be
- You want big-picture, zoomed-out analysis

**Use Dimensions instead when:**
- Diagnosing a specific scene that feels "off"
- Engineering tension in a chapter
- Tracking chapter-by-chapter emotional progression
- You want granular, zoomed-in analysis

**You can use both!** They complement each other.

---

## The Four NPE Axes (In Plain English)

Instead of tracking 9+ dimensions, NPE tracks 4 composite axes:

### 1. **IA (Internal Axis)**: Is your character wounded or whole?

**Scale:** -1 (broken) to +1 (healed)

- **-1 to 0**: Wounded, broken, in denial
  - Example: "I'm not good enough" / "I don't deserve love"
  - Character is hurting, feels inadequate

- **0**: The turning point (**Polarity Flip**)
  - Example: "Maybe I can change" / First moment of hope
  - This is where healing truly begins

- **0 to +1**: Healing, growing, becoming whole
  - Example: "I am worthy" / "I belong"
  - Character transforms, finds strength

**For authors:** Track how broken your character starts (-0.7 to -0.9 typical) and how healed they end (+0.6 to +0.9 for most genres).

**The Polarity Flip** (crossing zero) is THE critical moment - when your character shifts from wounded to healing.

---

### 2. **RA (Relational Axis)**: How far apart are they?

**Scale:** 0° (together) to 180° (broken apart)

Think of it like distance around a circle:
- **0-30°**: Close, intimate, together
- **60°**: Comfortable closeness
- **90°**: Maximum tension, perpendicular
- **160-180°**: Distant, broken, separated

**For authors:** Track the relationship distance from start to end.

**Examples:**
- Romance: Start 160° (strangers) → End 30° (intimate)
- Friendship: Start 180° (enemies) → End 60° (close friends)
- Family: Start 120° (estranged) → End 45° (reconciled)

---

### 3. **EA (Environmental Axis)**: How much external pressure?

**Scale:** -1 (low) to +1 (high)

- **Low (around 0)**: Peaceful, safe circumstances
- **Medium (0.5)**: Moderate pressure, challenges
- **High (around 1.0)**: Intense external pressure, danger, world stakes

**For authors:** Track how much the world is pushing on your character.

**Examples:**
- Cozy fantasy: Stay low (0.2-0.6)
- Thriller: Escalate high (0.8-1.0)
- Epic fantasy: Build from 0.3 → 1.0

---

### 4. **TA (Task Axis)**: Is the quest progressing?

**Scale:** 0 (not started) to 1 (complete)

- **0**: Quest not started or failing completely
- **0.5**: Midpoint, making progress
- **1.0**: Quest complete, goal achieved

**For authors:** Track plot/quest completion.

**Examples:**
- Mystery: Clues found → Killer identified (0 → 1.0)
- Quest: Artifact pieces collected → Final piece obtained (0 → 1.0)
- Romance: First meeting → Committed relationship (0 → 1.0)

---

## NPE Genre Physics (The Simple Version)

Different genres have different "physics rules" for how much characters can swing emotionally:

### **Cozy Fantasy / Cozy Mystery**

```
✓ Must start wounded (IA: -0.7 to -0.9)
✓ Must end healed (IA: +0.6 to +0.9)
✓ MUST cross zero (polarity flip required)
✓ Emotional swings stay gentle (max amplitude: 1.5)
✓ Dark night at 65-75% through story
✓ Even the dark night isn't traumatic
✓ Low chaos overall (entropy < 0.5)
```

**What this means:** Cozy readers need to see healing. Your character can be wounded but not shattered, and must end feeling whole.

---

### **Dark Romance**

```
✓ Must start wounded (IA: -0.8 to -0.95)
✓ Must end healed (IA: +0.5 to +0.9) for relationship to work
✓ MUST cross zero (late, at 80-85%)
✓ Intense emotional swings allowed (max amplitude: 2.0)
✓ Dark night at 75-85% through story
✓ Can sustain high tension longer
✓ High chaos OK (entropy up to 0.8)
```

**What this means:** Dark romance can be intense, but if it's truly romance, the relationship must heal. The polarity flip happens very late.

---

### **Psychological Thriller / Horror**

```
✓ Can start anywhere (IA: -0.5 to -0.9)
✗ Does NOT need to cross zero
✗ Does NOT need to end healed (can end wounded)
✓ Very intense swings allowed (max amplitude: 2.5)
✓ Dark night can be anywhere (or multiple)
✓ Very high chaos allowed (entropy up to 1.0)
```

**What this means:** Thrillers don't require healing. Your character can end broken if that serves the story.

---

### **Romance (Any Subgenre)**

```
✓ Must start with low intimacy (RA: 150-180°)
✓ Must end close (RA: 20-60°)
✓ MUST cross zero (IA polarity flip)
✓ MUST end healed for HEA/HFN
✓ Moderate swings (max amplitude: 1.8)
✓ Dark night at 70-75%
✓ Polarity flip at 75-85%
```

**What this means:** Romance = healing journey. Both characters must transform and relationship must close.

---

### **Epic Fantasy**

```
✓ Must start wounded (IA: -0.7 to -0.9)
✓ Must end healed (IA: +0.5 to +0.9)
✓ MUST cross zero
✓ High amplitude allowed (max: 2.2)
✓ Extended arcs (slow burn)
✓ Multiple mini dark nights OK
✓ Main dark night at 70-80%
```

**What this means:** Epic journeys need epic transformation. Allow for slow growth with multiple setbacks.

---

### **Romantic Comedy**

```
✓ Must cross zero (early-mid, 50-65%)
✓ Moderate amplitude (max: 1.8)
✓ Rapid oscillation (lots of ups/downs)
✓ Low overall chaos
✓ Light, bouncy feel
✓ Dark night is brief and not too dark
```

**What this means:** Rom-coms are about fun chaos, not deep wounds. Keep it light even in the lows.

---

## Quick Start: Using NPE in Claude Chat

### **Planning Your Story Arc**

Copy and paste this template:

```
I'm planning a [GENRE] story. Help me design the NPE arc.

Genre: [cozy fantasy / dark romance / thriller / etc.]
Chapters: [number]

Main character starts:
- IA (internal state): [wounded / broken / describe emotional state]
- RA (relationship distance): [far apart / strangers / separated]

Main character ends:
- IA: [healed / whole / describe final state]
- RA: [close / intimate / together]

Questions:
1. Where should the polarity flip happen (when IA crosses zero)?
2. Where should the dark night be?
3. What IA value at the dark night?
4. Does this match [GENRE] physics?
```

**Example:**
```
I'm planning a cozy fantasy story. Help me design the NPE arc.

Genre: Cozy fantasy
Chapters: 26

Main character (Verity) starts:
- IA: Very wounded, feels inadequate as a librarian (-0.85)
- RA: Distant from love interest, grumpy baker (160°)

Main character ends:
- IA: Healed, confident, belongs in community (+0.75)
- RA: Close, romantic relationship with baker (60°)

Questions:
1. Where should the polarity flip happen (when IA crosses zero)?
2. Where should the dark night be?
3. Does this match cozy fantasy physics?
```

**Claude will respond with:**
- Exact chapter numbers for key moments
- IA/RA values at each turning point
- Physics validation for your genre
- What the dark night should look like

---

### **Validating Your Genre**

When you finish your draft:

```
I finished my [GENRE] draft. Does it violate genre physics?

Genre: [your genre]
Chapters: [X]

Character arc:
- Starts: IA = [value or description]
- Dark night: Chapter [X], IA = [value]
- Polarity flip: Chapter [X], IA crosses zero
- Ends: IA = [value]

Relationship arc:
- Starts: RA = [value or description]
- Ends: RA = [value]

Does this match [GENRE] constraints?
What needs adjusting?
```

**Claude will tell you:**
- If your amplitude is too high/low for genre
- If dark night is in the wrong place
- If polarity flip timing is off
- Specific fixes to match genre expectations

---

## Getting NPE Reports

You have multiple ways to analyze your arc:

### **Option 1: Author-Friendly Text Report** ✅ Recommended

Generate plain English NPE analysis:

```bash
python scripts/npe_author_report.py your_story.json cozy_fantasy
```

**What you get:**
- Quick summary with arc health score
- Character journey from wounded to healed (visual ASCII chart!)
- Relationship arc progression
- Story pacing and flow analysis
- Genre fit validation
- Key moments identified (dark night, polarity flip)
- Strengths and opportunities
- Actionable suggestions in plain language

**Example output:**
```
Overall Arc Health: 100/100
[██████████] Excellent

Character Journey:
  • Starts: deeply wounded, feels broken/inadequate
  • Darkest moment: Chapter 17 (deeply wounded)
  • Ends: healed, whole, self-aware and strong

Relationship Arc:
  • Starts: distant/strangers
  • Ends: close, intimate connection
  • Distance closed: 100°
```

**No physics jargon - just practical feedback!**

---

### **Option 2: Technical NPE Report** (For Advanced Users)

Generate detailed physics analysis:

```bash
python scripts/npe_analyzer.py your_story.json --genre cozy_fantasy
```

**What you get:**
- Numerical axis progressions
- Waveform analysis (amplitude, frequency, phase)
- Entropy curves
- Orbital mechanics calculations
- Critical thresholds
- Genre constraint validation with formulas

**This includes technical terminology** - use if you want deep physics details.

---

### **Option 3: Visual NPE HTML Report**

Generate interactive chart:

```bash
python scripts/generate_npe_html_report.py your_story.json cozy_fantasy output.html
```

**What you get:**
- Beautiful interactive Chart.js visualization
- All 4 NPE axes plotted over time
- Zero line showing polarity flip point
- Statistics dashboard
- Axis explanations
- Self-contained HTML file (email to critique partners!)
- Dark night and polarity flip automatically identified

**Opens in any browser, no coding needed.**

---

### **Option 4: Interactive React App** ⭐ Most Powerful

Full-featured multi-layer analysis:

```bash
python scripts/launch_viz_app.py your_story.json --genre fantasy --mode npe
```

**What you get:**
- Toggle between NPE and Dimensions modes live
- **Multi-layer plotting:**
  - Ideal layer: Genre-typical arc
  - Actual layer: Your story
  - Difference layer: Gap analysis
  - Correction layer: Suggested target path
- Interactive controls: show/hide axes, toggle layers
- Genre comparison: see where you deviate from ideal
- Real-time exploration

**Requires Node.js but auto-installs.** See `viz-app/QUICKSTART.md`.

---

## Common NPE Questions

### **"When Should the Polarity Flip Happen?"**

**General rule:**
- **Cozy genres:** 75-85% through story
- **Romance:** 75-85%
- **Thriller:** Can skip entirely
- **Epic fantasy:** 75-80%
- **Rom-com:** 50-65% (earlier!)

**Why it matters:**
- Too early = no tension in Act 3
- Too late = feels rushed
- Must allow time for healing journey

**The flip happens AFTER the dark night** during recovery.

---

### **"Is This Too Intense for My Genre?"**

Ask Claude:
```
I'm writing cozy fantasy. My dark night has the protagonist completely
shattered (IA drops from -0.5 to -0.95), relationships break apart
(RA jumps to 180°), and she considers leaving town forever.

Is this too dark for cozy?
```

Claude will tell you:
- If IA value is too extreme (cozy max: -0.95)
- If RA separation is too severe (cozy max: 160°)
- If emotional response is too intense
- How to soften while keeping impact

**Or generate an author report** - it will flag genre violations automatically!

---

### **"How Do I Blend Multi-Genre Physics?"**

For genre blends (romantic thriller, cozy mystery, etc.):

```
I'm writing a romantic thriller (60% thriller, 40% romance).
What physics constraints apply?
```

**Claude will tell you:**
- Which constraints from each genre apply
- Which genre "wins" for specific axes
- How to satisfy both genre expectations

**General rule:** Romance requirements always apply if it's ANY percent romance (must cross zero, must end healed).

---

### **"My Character Doesn't Start Wounded - Is That OK?"**

**Most genres require wounded start:**
- Romance, cozy fantasy, epic fantasy: YES, must start wounded
- Thriller: Optional
- Mystery: Optional
- Horror: Optional

**If your character starts healed (IA > 0):**
- They can still have a journey (prevent backsliding, protect healing)
- External conflict must carry the story
- Consider if they're hiding wounds (appears healed, actually wounded)

**Ask Claude** if your specific genre allows it.

---

## NPE + Dimensions: How They Work Together

You don't have to choose! They complement each other.

### **Example Workflow:**

**1. Planning stage** (before writing): Use NPE
```
"Plan my cozy fantasy NPE arc for 26 chapters"
```
- Get overall structure
- Know where dark night and polarity flip happen
- Validate genre physics

**2. Drafting stage** (while writing): Use Dimensions
```
"Chapter 8 feels flat, diagnose using dimensions"
```
- Fix individual scenes
- Engineer tension chapter by chapter
- Track detailed emotional progression

**3. Revision stage** (after draft): Check both
```
"Does my overall arc match cozy fantasy NPE physics?
Generate NPE author report to see."

"Does Chapter 12 have enough dimensional movement?
Diagnose using dimensions."
```

---

## Copy-Paste NPE Templates

### **Template 1: NPE Arc Design**

```
Design an NPE arc for my [GENRE] story:

Genre: [genre]
Length: [X chapters]

Starting state (Chapter 1):
- IA: [value or description - how wounded?]
- RA: [value or description - how distant?]
- EA: [value - external pressure level]
- TA: 0 (quest not started)

Ending state (Chapter X):
- IA: [value or description - how healed?]
- RA: [value or description - relationship state]
- EA: [value - final circumstances]
- TA: 1 (quest complete)

Questions:
1. Where should the dark night happen?
2. When should IA cross zero (polarity flip)?
3. What IA value at dark night?
4. Does this match [GENRE] physics?
```

---

### **Template 2: Genre Validation**

```
Validate my arc against [GENRE] physics:

Genre: [genre]
Chapters: [X]

Act 1:
- IA progression: [start value] → [end of act 1 value]
- RA progression: [start] → [end of act 1]

Act 2:
- Dark night: Chapter [X] ([Y]% through)
- IA at dark night: [value]
- RA at dark night: [value]

Act 3:
- Polarity flip: Chapter [X] (IA crosses 0)
- Final IA: [value]
- Final RA: [value]

Questions:
1. Does this match [GENRE] amplitude limits?
2. Is the dark night in the right place?
3. Does the ending satisfy genre requirements?
```

---

### **Template 3: Quick NPE Check**

```
Quick NPE check for [GENRE]:

My character arc:
- Starts: [wounded/healed, describe]
- Dark night: Chapter [X], [describe emotional state]
- Polarity flip: Chapter [X]
- Ends: [wounded/healed, describe]

My relationship arc:
- Starts: [distant/close, describe]
- Ends: [distant/close, describe]

Does this work for [GENRE]?
What needs adjusting?
```

---

## Full NPE Conversation Example

**You:**
```
I'm planning a 26-chapter cozy fantasy. Librarian protagonist (Verity)
starts feeling inadequate and isolated. She ends confident and in love
with the grumpy baker.

Help me plan the NPE arc. When should she cross zero? When's the dark night?
```

**Claude:**
```
Great setup! Here's your NPE arc for cozy fantasy:

CHAPTER 1 (Opening):
- IA: -0.85 (wounded, feels inadequate)
- RA: 160° (distant from baker, they bicker)
- EA: 0.3 (low stakes, cozy setting)
- TA: 0 (no quest yet)

CHAPTER 8-10 (End of Act 1):
- IA: -0.70 (still wounded but small growth)
- RA: 140° (slightly closer, bickering softens)
- EA: 0.5 (stakes rising, mystery emerges)
- TA: 0.2 (quest beginning)

CHAPTER 17 (DARK NIGHT - 65% through):
- IA: -0.90 (LOWEST POINT - doubts everything)
- RA: 160° (pushed baker away)
- EA: 1.0 (external pressure peaks)
- TA: 0 (quest seems impossible)

CHAPTER 22 (POLARITY FLIP - 85% through):
- IA: 0 → +0.2 (CROSSES ZERO - first real hope)
- RA: 90° (perpendicular but tension shifting)
- EA: 0.6 (stakes easing)
- TA: 0.5 (breakthrough on quest)

CHAPTER 26 (ENDING):
- IA: +0.75 (healed, confident, belongs)
- RA: 60° (close, romantic, together)
- EA: 0.2 (peaceful, cozy)
- TA: 0.9 (quest complete)

PHYSICS CHECK:
✓ Crosses zero: Yes (Chapter 22)
✓ Amplitude: 1.65 (slightly over 1.5 but justified)
✓ Dark night at 65%: Perfect for cozy
✓ Ends healed: Yes (IA +0.75)
✓ Relationship closes: Yes (160° → 60° = 100° closure)

This matches cozy fantasy physics!
```

**You:**
```
Perfect! What should Chapter 17 (dark night) actually look like in terms
of story events?
```

**Claude:**
```
Chapter 17 dark night for cozy fantasy should include:

EMOTIONAL STATE:
- Verity doubts her competence (IA: -0.90)
- Feels she's failing everyone
- Has pushed Roric away (RA: 160°)
- Quest seems impossible

COZY CONSTRAINTS:
✓ She's sad, not destroyed
✓ Community still cares (even if she can't see it)
✓ Physical comfort present (cottage, tea, familiar nearby)
✓ Reader knows it will resolve warmly

SUGGESTED SCENE:
- Verity retreats to her cottage
- Roric leaves soup on her doorstep (she doesn't answer door)
- Her familiar curls up with her
- She cries but in a "safe cry" way
- The chapter ends with a tiny spark of hope (maybe a clue appears)

WHAT TO AVOID:
✗ No violence or danger to her person
✗ No permanent damage to relationships
✗ No trauma that would require therapy
✗ No sense of "this can never be fixed"

Remember: Cozy dark night = "I need help" not "I'm broken forever"
```

---

## Getting Started Right Now

### **For Planning:**
1. Copy **Template 1** (NPE Arc Design) above
2. Fill in your genre and story details
3. Paste into Claude Chat
4. Get your complete arc structure

### **For Validation:**
1. Copy **Template 2** (Genre Validation)
2. Fill in your current arc values
3. Paste into Claude Chat
4. Get validation and fixes

### **For Reports:**
Generate author-friendly NPE report:
```bash
python scripts/npe_author_report.py your_story.json cozy_fantasy > analysis.txt
```

Open `analysis.txt` to see plain English arc analysis!

**No physics degree required.** 📚✨

---

## What's Next?

**For scene-by-scene analysis:** See `AUTHOR_GUIDE_DIMENSIONS.md`

**For visualization:** See `VISUALIZATION_USAGE.md`

**For technical details:** See `SKILL.md`
