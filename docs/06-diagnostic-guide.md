# Diagnostic Guide

Troubleshooting common story problems using dimensional analysis.

## How to Use This Guide

**Problem → Dimensional Diagnosis → Solution**

1. Identify your symptom (what feels wrong)
2. Run the dimensional diagnosis (what's actually happening)
3. Apply the solution (how to fix it)

---

## Quick Diagnostic Flowchart

```
Scene feels flat?
  → Check velocity (dimensions moving?)
    → Yes, but still flat → Check tension configuration
    → No movement → Move 2-3 dimensions

Development feels unearned?
  → Check for jumps ≥ 3 without catalyst
    → Add catalyst events
    → OR break into smaller steps

Pacing issues?
  → Map velocity curve
    → Dragging → Increase velocity
    → Rushed → Decrease velocity
    → Inconsistent → Smooth the curve

Tension plateau?
  → Check for constant high tension
    → Create valleys (tension waves)
    → Rotate tension sources

Ending unsatisfying?
  → Check genre requirements
    → Meet all dimensional thresholds
    → Complete all arcs
```

---

## The Flat Scene Syndrome

### Symptoms
- Readers skimming
- "Nothing happens" feeling
- Scenes feel like filler
- Low engagement

### Dimensional Diagnosis

**Run this check:**
```python
# Compare scene start to scene end
start_state = {'intimacy': 5, 'trust': 5, 'stakes': 6, 'desire': 7, ...}
end_state = {'intimacy': 5, 'trust': 5, 'stakes': 6, 'desire': 7, ...}

# Calculate movement
movement = sum(abs(end[dim] - start[dim]) for dim in dimensions)

if movement == 0:
    diagnosis = "FLAT SCENE - No dimensional movement"
elif movement < 2:
    diagnosis = "SLUGGISH - Minimal movement"
```

**Common patterns:**
- **All dimensions static** (velocity = 0)
- No dimensional movement for 2+ scenes in a row
- Tension below 3
- Only dialogue, no dimensional shifts

### Solutions

**Solution 1: Move 2-3 Dimensions**

Pick dimensions that create interesting conflict:

**Before (flat):**
```
Dinner scene:
intimacy=5, trust=5, vulnerability=5 (all static)
```

**After (dynamic):**
```
Dinner scene:
Start: intimacy=5, trust=5, vulnerability=3
  → Character shares embarrassing story (vulnerability 3 → 5)
  → Other's reaction tests trust (trust 5 → 4 → 6)
  → Connection deepens (intimacy 5 → 6)
End: intimacy=6, trust=6, vulnerability=5
Movement: 4 points total
```

**Solution 2: Create Micro-Arc**

Small rise and fall within scene:

```
Start: trust=6
Rising: trust=6 → 7 (promising moment)
Peak: trust=7 (vulnerability rewarded)
Fall: trust=7 → 6 (slight doubt creeps in)
End: trust=6 (back to start BUT reader felt the movement)
```

**Solution 3: Add Subplot Dimension**

If main relationship static, move subplot:

```
Main relationship: intimacy=5, trust=5 (stable)
Subplot: stakes=6 → 8 (work crisis escalates)
Result: Scene feels dynamic through stakes movement
```

**Solution 4: Increase Stakes Temporarily**

Even small stakes help:

```
Before: stakes=3 (casual conversation)
After: stakes=5 (conversation at job interview, matters)
```

---

## The Unearned Moment

### Symptoms
- Reader doesn't believe development
- "Too fast" criticism
- Emotional moments fall flat
- Seems like teleportation

### Dimensional Diagnosis

**Check for jumps ≥ 3 points:**

```python
chapter_5_end = {'trust': 3}
chapter_6_end = {'trust': 8}

jump = abs(8 - 3)  # = 5 points!

if jump >= 3:
    check_for_catalyst = required
    if no_catalyst_present:
        diagnosis = "UNEARNED - Dimensional teleportation"
```

**Common patterns:**
- Trust jumping 4+ points in single scene
- Intimacy leaping without buildup
- Stakes appearing from nowhere
- Missing trajectory steps

### Solutions

**Solution 1: Add Stepping Stones**

Break large jump into smaller moves:

**Before (unearned):**
```
Chapter 10: trust=3
Chapter 11: trust=8 (how?!)
```

**After (earned):**
```
Chapter 10: trust=3 → 4 (small risk rewarded)
Chapter 11: trust=4 → 5 (shares minor secret safely)
Chapter 12: trust=5 → 6 (helps without being asked)
Chapter 13: trust=6 → 8 (major sacrifice witnessed)
```

**Solution 2: Insert Catalyst Event**

Justify the jump with significant event:

**Trust 3 → 8 requires catalyst such as:**
- Took a bullet for them
- Turned down fortune to help them
- Revealed devastating secret first
- Proved loyalty under extreme pressure

See `references/catalyst-events.md` for event types.

**Solution 3: Show the Journey**

Make the change visible, not just stated:

```
Don't: "After that night, she trusted him completely."
Do: Show the night, show the vulnerability, show the response,
    show the internal shift, show the new behavior
```

**Solution 4: Slow the Velocity**

Take more scenes/chapters:

```
Instead of: 1 scene with 5-point jump
Use: 3-5 scenes with 1-2 point movements each
```

---

## The Pacing Problem

### Symptoms
- "Drags in the middle"
- "Rushed ending"
- Inconsistent reading experience
- Some scenes fly, others crawl

### Dimensional Diagnosis

**Calculate velocity per chapter:**

```python
# For each chapter
velocity = sum(abs(end[dim] - start[dim]) for dim in dimensions)

# Map the curve
Act 1: [4, 3, 5, 4]        # Good
Act 2: [1, 0.5, 1, 0, 1]   # PROBLEM: Too slow
Act 3: [8, 9, 10]          # PROBLEM: Too fast
```

**Diagnose patterns:**
- **Velocity < 1:** Too slow, dragging
- **Velocity > 6:** Too fast, rushing
- **Inconsistent:** Jarring pace changes
- **Middle act < 1.5:** Muddy middle

### Solutions

**Solution 1: Map Velocity Curve**

```
Target curve:
Act 1: 3-4 points/chapter (setup, movement)
Act 2: 2-3 points/chapter (sustained, never < 1.5)
Act 3: 4-6 points/chapter (escalation, not > 7)
```

**Solution 2: Redistribute Movement**

Spread changes more evenly:

**Before:**
```
Ch 1-5: velocity = 1 (slow)
Ch 6: velocity = 8 (sudden spike)
Ch 7-10: velocity = 1 (slow again)
```

**After:**
```
Ch 1-10: velocity = 2-3 consistently
  Spread Ch 6's movement across chapters
```

**Solution 3: Vary Dimensions Moved**

Don't move same dimensions every time:

**Boring:**
```
Ch 1: intimacy +2, trust +1
Ch 2: intimacy +2, trust +1
Ch 3: intimacy +2, trust +1
```

**Better:**
```
Ch 1: intimacy +2, trust +1
Ch 2: stakes +3, vulnerability +2
Ch 3: info_asymmetry -2, goal_alignment +2
```

**Solution 4: Add Parallel Arcs**

Subplot maintains movement when main plot static:

```
Main romance static at intimacy=6, trust=6
BUT:
Thriller subplot: danger 5 → 8, stakes 6 → 9
Result: Overall velocity maintained
```

---

## The Tension Plateau

### Symptoms
- Reader fatigue
- Numbness to stakes
- Diminishing impact
- "Just get it over with" feeling

### Dimensional Diagnosis

**Check for constant high tension:**

```python
chapters_8_to_15_tension = [8.5, 8.7, 8.5, 8.9, 8.6, 8.8, 8.5, 8.7]

if all(t > 7 for t in tensions):
    diagnosis = "TENSION PLATEAU - No relief valleys"
```

**Common patterns:**
- Tension constant > 7 for 4+ chapters
- No relief valleys
- Same dimensions driving tension
- Threat level never changes

### Solutions

**Solution 1: Create Tension Waves**

High/medium/high pattern:

```
Ch 1: Tension 8 (danger-driven, action)
Ch 2: Tension 5 (recovery, quiet bonding)
Ch 3: Tension 7 (trust-driven, betrayal suspected)
Ch 4: Tension 4 (false security, planning)
Ch 5: Tension 9 (stakes-driven, everything at risk)
```

**Solution 2: Rotate Tension Drivers**

Change what creates tension:

```
Ch 1-3: Tension from danger + stakes (external)
Ch 4-6: Tension from trust + vulnerability (internal)
Ch 7-9: Tension from info asymmetry + goal misalignment (relationship)
Ch 10+: All dimensions converge (climax)
```

**Solution 3: Moment of Relief**

Brief tension drop, strategic placement:

```
After high-intensity sequence (tension 8-9 for 3 chapters):
  Insert 1 chapter at tension 4-5
  Purpose: Emotional processing, relationship building, breathing room
  Effect: Next tension spike hits harder
```

**Solution 4: Change Tension Type**

Alternate between external and internal:

```
External: danger=9, stakes=10 (physical threat)
  → Relief →
Internal: vulnerability=8, trust=3 (emotional exposure)
  → Relief →
Mixed: danger=8, trust=2, stakes=9 (betrayal during crisis)
```

---

## The Muddy Middle

### Symptoms
- Story loses direction
- Multiple plotlines tangle
- Reader confusion
- "What's this about again?"

### Dimensional Diagnosis

**Check for dimensional chaos:**

```python
simultaneously_moving = count(dimensions with velocity > 0)

if simultaneously_moving > 5:
    diagnosis = "MUDDY MIDDLE - Too many dimensions moving"
```

**Common patterns:**
- 5+ dimensions moving at once
- Contradictory movements
- No clear primary arc
- Equal weight to all subplots

### Solutions

**Solution 1: Identify Primary Arc**

Choose 2-3 main dimensions:

```
Primary Arc (Romance): intimacy, trust, desire
Secondary Arc (External): stakes, danger
Tertiary Arc (Character): vulnerability, power_diff
```

**Solution 2: Subordinate Other Movements**

Support main arc, don't compete:

```
Primary: intimacy 5 → 7 (main focus)
Secondary: stakes 6 → 7 (background pressure)
Tertiary: vulnerability 4 → 5 (subtle growth)

Not: intimacy 5 → 7, stakes 6 → 9, info_asym 7 → 3, trust 4 → 7, danger 5 → 9
(Too much at once)
```

**Solution 3: Sequential Not Simultaneous**

Resolve some arcs before starting others:

```
Chapters 5-10: Focus on trust arc (resolve to stable 7)
Chapters 11-15: Focus on external stakes arc (resolve or escalate)
Chapters 16-20: Focus on intimacy arc (climax)
```

**Solution 4: Clear Hierarchy**

```
Every chapter, ask:
1. Primary dimension moving this chapter?
2. Secondary dimension supporting?
3. Tertiary dimension subtle shift?

Not: "Move everything!"
```

---

## The False Conflict

### Symptoms
- Conflict feels manufactured
- "Just talk to each other!" reader frustration
- Misunderstanding-based drama
- Easy fix if characters communicated

### Dimensional Diagnosis

**Check tension sources:**

```python
tension_sources = {
    'info_asymmetry': 6,      # Only this creating tension
    'goal_alignment': 9,      # Aligned
    'power_differential': 0,  # Balanced
    'stakes': 3,              # Low
    'trust': 7                # High
}

if only_info_asymmetry_creating_tension:
    diagnosis = "FALSE CONFLICT - One-dimensional tension"
```

**Red flags:**
- Only info asymmetry creating tension
- Characters want same thing
- No genuine opposition
- Simple conversation would solve everything

### Solutions

**Solution 1: Add Genuine Opposition**

Create goal misalignment:

```
Before (false):
Both want to be together
Only obstacle: misunderstanding about feelings
Goal alignment: 9 (actually want same thing)

After (real):
One wants relationship, other wants career move requiring relocation
Goal alignment: 3 (genuinely opposing goals)
Stakes: 8 (can't have both)
```

**Solution 2: Create Value Conflicts**

Different worldviews:

```
Not: "I thought you didn't like me" (info asymmetry)
But: "I don't believe in marriage" vs "Marriage is essential to me"
     (goal alignment 2, fundamental values conflict)
```

**Solution 3: External Pressure**

Forces preventing resolution:

```
Not: Just haven't talked yet
But: Talking would trigger threat (witness protection, blackmail, etc.)
     Stakes: 9 (conversation has real consequences)
     Goal alignment: 5 (want to talk but can't)
```

**Solution 4: Internal Barriers**

Character flaws blocking progress:

```
Not: External misunderstanding
But: Trust issues from past trauma prevent vulnerability
     Trust: 3 (character flaw, not simple miscommunication)
     Vulnerability: 2 (walls up, earned problem)
```

**Real Conflict Requires:**
- Goal Alignment < 5 (want different things)
- OR Power Differential > |3| (imbalance creates issues)
- OR Trust < 4 with legitimate cause
- OR Stakes that oppose each other

---

## The Weak Black Moment

### Symptoms
- Climax lacks impact
- Reader unmoved
- Resolution feels arbitrary
- "That's it?"

### Dimensional Diagnosis

**Check crisis configuration:**

```python
black_moment_state = {
    'intimacy': 6,    # Not crashed enough
    'trust': 4,       # Not low enough
    'stakes': 7,      # Not high enough
    'desire': 6       # Too low, reader disengaged
}

if not_threatening_core_promise:
    diagnosis = "WEAK BLACK MOMENT - Insufficient crash"
```

**Problems:**
- Insufficient dimensional crash (< 3 points)
- Not threatening genre promise
- Easy reversal possible
- Desire drops (reader stops caring)

### Solutions

**Solution 1: Crash Multiple Dimensions**

3+ simultaneously:

**Before (weak):**
```
Only trust drops: 8 → 3
Everything else stable
```

**After (strong):**
```
intimacy: 8 → 3 (emotional distance)
trust: 9 → 1 (shattered)
goal_alignment: 9 → 2 (opposing now)
stakes: 7 → 10 (everything at risk)
BUT desire: stays 7+ (reader still invested)
```

**Solution 2: Target Core Genre Promise**

**Romance:** Threaten the HEA
```
intimacy + trust + goal_alignment all crash
Cannot see path to ending requirements
```

**Thriller:** Maximize danger
```
danger=10, stakes=10, power_diff=-5 (utterly outmatched)
```

**Mystery:** Truth seems impossible
```
info_asymmetry increases (new lies discovered)
Every answer wrong
```

**Solution 3: Make Reversal Difficult**

Require major catalyst:

```
Not: Simple apology fixes it
But: Must sacrifice career, face fear, change fundamentally
     Requires 3+ chapters to earn resolution
```

**Solution 4: Maximum Divergence**

Dimensions at extremes:

```
Black Moment Formula:
- Stakes → 9-10 (everything at risk)
- Trust → 0-2 (shattered)
- Goal Alignment → 0-2 (incompatible)
- Desire remains 6+ (reader still cares)
- Vulnerability → 9-10 (emotionally raw)
- Proximity → forced extreme (0 or 10, not medium)
```

---

## The Limp Ending

### Symptoms
- Anticlimactic feeling
- Resolution too easy
- Genre expectations unmet
- "That's all?"

### Dimensional Diagnosis

**Check genre requirements:**

```python
romance_ending = {
    'intimacy': 7,    # Needs ≥ 8
    'trust': 6,       # Needs ≥ 7
    'goal_alignment': 7,  # Needs ≥ 8
    'power_differential': 3  # Needs ≤ |1|
}

if not_meeting_requirements:
    diagnosis = "LIMP ENDING - Genre requirements unmet"
```

**Problems:**
- Genre requirements not met
- Some dimensions unresolved
- Arcs incomplete
- Came together too easily

### Solutions

**Solution 1: Meet Genre Constraints**

**Romance:**
```
Required: intimacy ≥ 8, trust ≥ 7, goal_alignment ≥ 8
Check EACH dimension
```

**Thriller:**
```
Required: danger ≤ 3 OR acceptance ≥ 8
Info asymmetry ≤ 2 (know the truth)
```

**Mystery:**
```
Required: info_asymmetry ≤ 2
All questions answered
```

See genre guides for full requirements.

**Solution 2: Complete All Arcs**

```
Ending Checklist:
□ Primary dimensions resolved
□ Secondary dimensions addressed
□ Character growth shown across dimensions
□ Subplot dimensions concluded
```

**Solution 3: Earn Resolution**

Proper catalysts for final moves:

```
Not: Suddenly everyone forgives and aligns
But:
  - Grand gesture (vulnerability=10, stakes=9)
  - Sacrifice shown (trust earned)
  - Growth demonstrated (different behavior)
  - Time for processing (not instant)
```

**Solution 4: Establish Stable State**

```
Ending Configuration (Romance example):
intimacy: 9 (deep, stable)
trust: 9 (proven through crisis)
desire: 9 (strong, sustainable)
goal_alignment: 9 (merged futures)
power_differential: 0 (equal)
stakes: 4 (normal life, managed)
proximity: 9 (together, chosen)

All dimensions at sustainable high configuration
```

---

## The Cardboard Antagonist

### Symptoms
- Antagonist one-dimensional
- Conflict feels shallow
- No real threat
- Villain mustache-twirling

### Dimensional Diagnosis

**Check antagonist dimensions:**

```python
antagonist_complexity = {
    'dimensions_tracked': 1,  # Only power/danger
    'dimensions_moving': 0,   # Static
    'vulnerability_shown': 0,  # None
    'goal_validity': 0        # No understandable motive
}

if antagonist_flat:
    diagnosis = "CARDBOARD ANTAGONIST - No dimensional depth"
```

### Solutions

**Solution 1: Give Dimensional Depth**

Track 2-3 moving dimensions:

```
Antagonist arc:
power: high but vulnerable moment shown
goal_alignment: has own valid goals (not just oppose hero)
vulnerability: 1 moment where mask slips
stakes: personal (has something to lose too)
```

**Solution 2: Create Valid Goals**

Understandable if not agreeable:

```
Not: "I'm evil!"
But: "I must protect my family/kingdom/world, and hero threatens that"
     Goal alignment: 0 from different perspectives
     Both think they're right
```

**Solution 3: Show Vulnerability**

At least one soft dimension:

```
Antagonist vulnerability moment:
- Cares about one person
- Has fear or doubt
- Wasn't always this way
- Has valid pain/trauma

Makes them human, not sympathetic necessarily
```

**Solution 4: Give Them an Arc**

They change too:

```
Start: power=+5, trust_in_hench=7, goal_alignment=0
Mid: power=+3 (hero growing), trust_in_hench=5 (cracks showing)
End: power=+1, trust_in_hench=0 (betrayed), goal_alignment=-2 (desperate)

Antagonist degrades or escalates, not static
```

---

## The Chemistry Deficit

### Symptoms
- Romance unconvincing
- No spark between characters
- Reader doesn't ship them
- Telling not showing attraction

### Dimensional Diagnosis

**Check chemistry formula:**

```python
chemistry_check = {
    'desire': 8,              # High (good)
    'proximity_variance': 0,  # Always same (problem!)
    'vulnerability': 2,       # Low (problem!)
    'info_asymmetry': 1       # Too transparent (no mystery)
}

if chemistry_low:
    diagnosis = "CHEMISTRY DEFICIT - Missing components"
```

**Problems:**
- Desire without foundation
- Intimacy without vulnerability
- No push-pull dynamic
- Static proximity (always together OR always apart)

### Solutions

**Solution 1: Build Attraction Layers**

Physical + Emotional + Intellectual:

```
Physical: desire=6 (base attraction)
Emotional: vulnerability=6 (connection forming)
Intellectual: respect=7 (admire mind/competence)
Mystery: info_asymmetry=4 (discovering each other)

All layers present
```

**Solution 2: Create Productive Tension**

Desire vs. obstacle:

```
High desire (8) + obstacle = tension
Obstacles:
- Low proximity (want but apart)
- Low trust (want but uncertain)
- Goal misalignment (want but incompatible)
- Stakes (consequences of being together)
```

**Solution 3: Show Private Moments**

Vulnerability glimpses:

```
Not: Always together in group
But: Moments of:
  - Guard down (vulnerability spikes to 7)
  - Genuine laughter (intimacy grows)
  - Seeing beyond facade (info asymmetry decreases)
```

**Solution 4: Unique Connection**

What only they share:

```
Specific to their dynamic:
- Shared trauma (vulnerability bond)
- Inside jokes (intimacy specificity)
- Complementary strengths (power balance)
- Unique understanding (low info asymmetry between them)

Not generic attraction
```

**Chemistry Formula:**
```
CHEMISTRY = (desire ≥ 6) +
            (proximity variance: close/far/close pattern) +
            (vulnerability ≥ 5 shown) +
            (info_asymmetry 3-6: some mystery/discovery) +
            (power balance shifts)
```

---

## Quick Diagnostic Reference

| Problem | Check | Solution |
|---------|-------|----------|
| **Flat scene** | Velocity = 0? | Move 2-3 dimensions |
| **Unearned** | Jumps ≥ 3? | Add catalyst or steps |
| **Dragging pace** | Velocity < 1.5? | Increase movement |
| **Rushed pace** | Velocity > 6? | Slow down, add steps |
| **High tension plateau** | Tension constant > 7? | Create valleys |
| **Muddy middle** | 5+ dimensions moving? | Focus on 2-3 primary |
| **False conflict** | Only info asymmetry? | Add goal misalignment |
| **Weak black moment** | < 3 dimensions crash? | Crash 3+ simultaneously |
| **Limp ending** | Genre requirements? | Meet all thresholds |
| **Flat antagonist** | Tracking dimensions? | Give 2-3 moving dimensions |
| **No chemistry** | Proximity static? | Create variance + vulnerability |

---

**For more:** See genre-specific guides in `04-genre-guides/` or core concepts in `02-core-concepts.md`
