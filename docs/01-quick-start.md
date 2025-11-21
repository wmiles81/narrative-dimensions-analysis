# Quick Start Guide

Get started with the Narrative Dimensions Analysis system in 5 minutes.

## What Is This System?

Narrative Dimensions Analysis treats stories as trajectories through multidimensional space. Instead of arbitrary "tension" or vague "pacing," we measure specific independent variables (intimacy, trust, power, stakes, etc.) and let dramatic qualities emerge from their configuration.

**Think of it like this:** The same kiss hits differently at intimacy=2 vs intimacy=8. Context is configuration.

## What You Can Do

- **Engineer tension** in specific scenes by adjusting dimensional configurations
- **Diagnose pacing issues** by measuring velocity through phase space
- **Validate character arcs** by ensuring dimensional changes are properly earned
- **Check genre compliance** by verifying ending requirements are met
- **Fix flat scenes** by identifying which dimensions are stuck

## The Core Idea

Your story's state at any moment can be represented as:

```python
state = {
    'intimacy': 5,           # Emotional closeness (0-10)
    'trust': 4,              # Belief in reliability (0-10)
    'desire': 8,             # Attraction/pull (0-10)
    'power_differential': -2, # Agency imbalance (-5 to +5)
    'stakes': 7,             # Magnitude of consequences (0-10)
    'vulnerability': 6,      # Emotional walls down (0-10)
    'goal_alignment': 5,     # Shared objectives (0-10)
    'info_asymmetry': 6,     # Knowledge gaps (0-10)
    'proximity': 3           # Physical closeness (0-10)
}
```

**Key Insight:** Tension emerges from the configuration of these dimensions, not arbitrary assignment.

## Choose Your Genre

Different genres have different dimensional requirements and patterns:

### Romance
- **Ending requirement:** intimacy ≥ 8, trust ≥ 7, goal alignment ≥ 8
- **Pattern:** Steady intimacy climb with trust following sawtooth (build-break-rebuild)
- **See:** `docs/04-genre-guides/romance.md`

### Thriller
- **Key dimensions:** Danger + stakes high, trust variable
- **Pattern:** Danger spikes and plateaus, stakes escalate in discrete jumps
- **See:** `docs/04-genre-guides/thriller.md`

### Mystery
- **Key dimension:** Information asymmetry drives plot until revelation
- **Pattern:** Info asymmetry reduces stepwise with clues
- **See:** `docs/04-genre-guides/mystery.md`

### Fantasy
- **Key dimensions:** Stakes global (≥ 9), world complexity high
- **Pattern:** Power grows through journey, stakes revealed progressively
- **See:** `docs/04-genre-guides/fantasy.md`

## Score Your First Scene

Let's practice with a simple romance scene: **First date at a coffee shop**

### Step 1: Identify the Scene Context
- They've been flirting for weeks but this is first official date
- Both are nervous but interested
- Sharing personal stories for the first time

### Step 2: Score Each Dimension

Use the quick reference (see `03-dimension-reference.md` for full rubric):

```python
first_date_scene = {
    'intimacy': 3,           # Getting to know each other, not deep yet
    'trust': 5,              # Some trust built from previous interactions
    'desire': 6,             # Clear attraction, nervous energy
    'power_differential': 0, # Equal footing
    'stakes': 5,             # Risk of rejection, but not life-changing
    'vulnerability': 5,      # Sharing some personal info, testing waters
    'goal_alignment': 8,     # Both want to explore this connection
    'info_asymmetry': 5,     # Learning about each other
    'proximity': 7           # Sitting across from each other, close
}
```

### Step 3: Calculate What's Creating Tension

For romance, tension comes from:
- **(desire - proximity)** = 6 - 7 = -1 (actually quite satisfied on this front)
- **(vulnerability - trust)** = 5 - 5 = 0 (balanced, comfortable)
- **stakes** = 5 (moderate tension from what's at risk)

**Result:** This is a comfortable, low-tension scene. Good for early connection building.

### Step 4: What If We Want More Tension?

Adjust the configuration:

```python
adjusted_scene = {
    'intimacy': 3,
    'trust': 4,              # ↓ One mentions an ex, other uncertain
    'desire': 8,             # ↑ Attraction intensifying
    'power_differential': 0,
    'stakes': 6,             # ↑ One of them is leaving town soon
    'vulnerability': 7,      # ↑ Sharing something more personal
    'info_asymmetry': 6,     # ↑ One is hiding something
    'proximity': 5           # ↓ Keeping more distance despite attraction
}
```

Now tension emerges from:
- **(desire - proximity)** = 8 - 5 = 3 (wanting closeness but maintaining distance)
- **(vulnerability - trust)** = 7 - 4 = 3 (exposed but uncertain)
- **stakes** = 6 + **info_asymmetry** = 6 (more at risk, secrets present)

**Result:** Higher tension! The scene now has productive conflict.

## Understanding Movement

Stories are not static snapshots - they're trajectories. What matters is **how dimensions change**:

### Example: The Kiss That Changes Everything

**Before the kiss:**
```python
before = {'intimacy': 5, 'vulnerability': 5, 'proximity': 8}
```

**After the kiss:**
```python
after = {'intimacy': 7, 'vulnerability': 8, 'proximity': 10}
```

**Movement:**
- Intimacy: +2 points (significant emotional shift)
- Vulnerability: +3 points (walls came down) ← Needs a catalyst event!
- Proximity: +2 points (in each other's arms)

**The Rule:** Jumps ≥ 3 points require a catalyst event. A kiss can justify vulnerability jumping 3 points because it's a significant moment of emotional exposure.

## Next Steps

### 1. Learn the Full Dimension Set
Read `02-core-concepts.md` to understand:
- How dimensions interact
- Why tension emerges from configuration
- What "pacing as velocity" means
- The physics metaphor in depth

### 2. Get the Full Scoring Rubric
See `03-dimension-reference.md` for:
- Detailed 0-10 scales for each dimension
- Concrete examples at each level
- Common scoring mistakes to avoid

### 3. Explore Your Genre
Read your genre's specific guide in `04-genre-guides/`:
- Ending requirements
- Trajectory patterns
- Key beats and their dimensional signatures
- Common pitfalls

### 4. Learn Diagnostic Techniques
See `06-diagnostic-guide.md` for:
- How to diagnose flat scenes
- Fixing pacing problems
- Engineering specific effects
- Troubleshooting formulas

### 5. Apply Modifiers and Advanced Techniques
- `05-tropes-and-modifiers.md` - How mafia, captive, second-chance affects dimensions
- `07-advanced-techniques.md` - Multi-subplot tracking, custom formulas

## Quick Reference Card

**The 9 Primary Dimensions:**
1. Intimacy (0-10): Emotional closeness
2. Trust (0-10): Belief in reliability
3. Desire (0-10): Attraction/pull
4. Vulnerability (0-10): Emotional walls down
5. Goal Alignment (0-10): Shared objectives
6. Power Differential (-5 to +5): Agency balance
7. Information Asymmetry (0-10): Knowledge gaps
8. Stakes (0-10): Magnitude of consequences
9. Proximity (0-10): Physical closeness

**Key Rules:**
- Move 2-3 dimensions per scene (avoid static scenes)
- Jumps ≥ 3 points need catalyst events
- Genre determines ending requirements
- Tension emerges from dimensional configuration

**Tension Formula (simplified):**
```
TENSION = stakes + info_asymmetry + (10 - goal_alignment) +
          (vulnerability - trust) + (desire - proximity) + |power_diff|
```

## Common First Questions

**Q: Do I have to score every dimension for every scene?**
A: No. Focus on the 3-4 dimensions most relevant to your scene. Others can stay static.

**Q: What if my scene doesn't fit the patterns?**
A: The patterns are templates, not rules. Your unique story may have a different trajectory - just ensure it's intentional and earned.

**Q: Can dimensions go backward?**
A: Absolutely! Trust dropping, intimacy retreating, stakes lowering - these are all valid movements that create story dynamics.

**Q: How precise do I need to be?**
A: Don't overthink it. "Around 5" is fine. What matters is tracking relative changes over time, not perfect absolute scores.

## Try It Now

Pick a scene from your current work and score these 5 dimensions:
1. **Intimacy:** How close are the characters emotionally?
2. **Trust:** How much do they rely on each other?
3. **Stakes:** What's at risk in this scene?
4. **Desire:** How much pull is there between them?
5. **Proximity:** How physically close are they?

Then ask: **What moves in this scene?** If nothing moves, you've found your first fix.

---

**Next:** Read `02-core-concepts.md` to understand the theory behind the system.
