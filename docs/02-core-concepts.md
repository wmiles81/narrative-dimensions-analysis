# Core Concepts

Understanding the theoretical foundation of the Narrative Dimensions Analysis system.

## The Physics Metaphor

### Stories as Trajectories

In physics, an object's position in space is described by coordinates (x, y, z). In narrative analysis, a story's "position" is described by dimensional coordinates:

```
Position in physical space: (x, y, z)
Position in narrative space: (intimacy, trust, power, stakes, ...)
```

A story is not a collection of events - **it's a trajectory through this multidimensional space.**

### Why This Matters

Traditional story analysis says "add more conflict" or "increase tension." But that's like saying "make the ball go faster" without understanding physics.

The dimensional approach says: **Tension emerges from configuration.** You don't assign tension arbitrarily - you create the right dimensional setup and tension appears naturally.

## State Vectors Explained

### What Is a State Vector?

A **state vector** is a snapshot of your story at a single moment in time, represented as values across all tracked dimensions.

```python
# State vector at Chapter 5, Scene 2
s(t) = {
    'intimacy': 6,
    'power_differential': -2,
    'info_asymmetry': 7,
    'goal_alignment': 5,
    'proximity': 8,
    'vulnerability': 7,
    'desire': 9,
    'stakes': 7,
    'trust': 4
}
```

### Independent vs. Dependent Variables

**Independent dimensions** (basis dimensions):
- Set directly by story events
- Examples: intimacy, trust, stakes, power differential
- These are your "control knobs"

**Dependent properties** (emergent):
- Calculate from independent dimensions
- Examples: tension, conflict, chemistry, pacing
- These emerge from configuration

This is crucial: **You don't control tension directly. You control the dimensions, and tension emerges.**

### Example: Engineering Chemistry

You can't just write "they have chemistry." But you can create the dimensional configuration that produces chemistry:

```python
chemistry_config = {
    'desire': 7+,              # Attraction present
    'proximity': variable,     # Close then apart then close (creates pull)
    'vulnerability': 6+,       # Glimpses of true self
    'info_asymmetry': 4-6,     # Some mystery, discovery possible
    'power_differential': oscillating  # Balance shifts create dynamics
}
```

**Result:** Chemistry emerges from this configuration.

## Tension Emergence

### The Tension Formula

Tension is not assigned - it's calculated from dimensional configuration:

```
TENSION = w₁(stakes) + w₂(info_asymmetry) + w₃(goal_misalignment) +
          w₄(vulnerability - trust) + w₅(desire - proximity) + w₆(|power_diff|)
```

Where:
- **w₁, w₂, ... w₆** are genre-specific weights
- **goal_misalignment** = 10 - goal_alignment
- **Terms in parentheses** create productive tension through gaps

### Understanding the Terms

**1. Stakes**
- High stakes = inherent tension
- Linear contribution to tension
- Foundation of dramatic importance

**2. Information Asymmetry**
- Secrets create suspense
- Knowledge gaps create dramatic irony
- More asymmetry = more tension

**3. Goal Misalignment**
- Characters wanting different things = conflict
- Complete opposition (alignment=0) → maximum conflict
- Perfect alignment (alignment=10) → no conflict from goals

**4. Vulnerability - Trust Gap**
- Being emotionally open (high vulnerability) while uncertain about reliability (low trust) = tension
- Vulnerable with high trust = intimacy, not tension
- Low vulnerability with low trust = coldness, not tension

**5. Desire - Proximity Gap**
- Wanting to be close but being apart = tension
- Want closeness and have it = satisfaction, not tension
- Don't want closeness and apart = indifference, not tension

**6. Power Differential**
- Imbalance creates tension
- Absolute value: both directions create tension
- Zero (balanced) = less tension from power

### Genre-Specific Weights

Romance emphasizes emotional gaps:
```python
romance_weights = {
    'w_stakes': 0.8,
    'w_info_asym': 0.5,
    'w_goal_misalign': 0.7,
    'w_vuln_trust_gap': 1.2,      # ← Highest weight
    'w_desire_prox_gap': 1.0,
    'w_power_diff': 0.6
}
```

Thriller emphasizes external pressure:
```python
thriller_weights = {
    'w_stakes': 1.5,              # ← Highest weight
    'w_info_asym': 1.0,
    'w_goal_misalign': 0.7,
    'w_vuln_trust_gap': 0.5,
    'w_desire_prox_gap': 0.3,
    'w_power_diff': 0.8
}
```

### Tension Configurations

**High tension romance scene:**
```python
state = {
    'desire': 9,         # Want each other badly
    'proximity': 3,      # But physically apart
    'vulnerability': 8,  # Emotionally exposed
    'trust': 3,          # But uncertain about other's feelings
    'stakes': 7,         # Risking the friendship/career/etc.
}
# Gap terms: (9-3) + (8-3) = 6 + 5 = 11 points from gaps alone
```

**Low tension satisfied scene:**
```python
state = {
    'desire': 8,         # Still want each other
    'proximity': 9,      # Together and close
    'vulnerability': 7,  # Open
    'trust': 8,          # Secure
    'stakes': 4,         # Lower consequences
}
# Gap terms: (8-9) + (7-8) = -1 + -1 = -2 (gaps closed, satisfaction high)
```

## Pacing as Velocity

### The Velocity Vector

Just as velocity in physics is **change in position over time**, narrative velocity is **change in dimensional state over time**:

```
v(t) = ds/dt = change in state vector / change in time
```

Practically: **How many dimensional points change per chapter/scene?**

### Measuring Pacing

```python
# Chapter 1 start
state_start = {'intimacy': 3, 'trust': 4, 'stakes': 5}

# Chapter 1 end
state_end = {'intimacy': 5, 'trust': 3, 'stakes': 7}

# Changes
intimacy: +2
trust: -1
stakes: +2

# Velocity magnitude: ||v|| = √(2² + 1² + 2²) = √9 = 3
# Or simpler: Total movement = |2| + |1| + |2| = 5 points
```

### Pacing Guidelines

**Static (problem):**
- Velocity ≈ 0
- No dimensional movement
- "Nothing happens" feeling
- **Fix:** Move 2-3 dimensions

**Optimal:**
- 2-3 dimensions shifting per chapter
- Total movement: 3-6 points per chapter
- Variety in which dimensions move

**Rushed (problem):**
- Velocity > 5
- Too many dimensions changing too fast
- "Teleportation" between states
- **Fix:** Slow down, add intermediate steps

### Pacing Variety

Good pacing varies velocity:

```
Chapter 1: velocity = 4 (setup, movement)
Chapter 2: velocity = 2 (settling, processing)
Chapter 3: velocity = 5 (crisis, rapid change)
Chapter 4: velocity = 2 (aftermath, recovery)
Chapter 5: velocity = 6 (climax, major shifts)
```

Constant high velocity = exhausting
Constant low velocity = boring
**Varied velocity = engaging**

## The "Earned Moment" Principle

### Catalyst Event Threshold

**Rule:** Dimensional jumps ≥ 3 points require a catalyst event.

**Why 3 points?**
- 1-2 point changes: Gradual, accumulated small moments
- 3+ point changes: Significant shift requiring justification

### Examples

**Trust: 3 → 6 (requires catalyst)**
- Not earned: "She just started trusting him"
- Earned: "He took a bullet for her, proving his loyalty"

**Intimacy: 5 → 8 (requires catalyst)**
- Not earned: "They talked and now they're close"
- Earned: "They shared their deepest trauma during a long vulnerable night"

**Stakes: 4 → 9 (requires catalyst)**
- Not earned: "Now it matters more"
- Earned: "The villain kidnapped her daughter"

### Catalyst Event Types

See `references/catalyst-events.md` for complete list. Common examples:

**For Trust jumps:**
- Sacrifice (someone risks something significant)
- Vulnerability rewarded (taking risk pays off)
- Consistency proven (promised thing delivered)

**For Intimacy jumps:**
- Trauma sharing (revealing deep wounds)
- Crisis bonding (surviving something together)
- Breaking point (emotional dam breaks)

**For Stakes jumps:**
- Escalation (villain raises the price)
- Personal investment (someone you love endangered)
- Point of no return (can't go back)

### Path Integration

Stories should show **continuous trajectories**, not teleportation:

**Bad (teleportation):**
```
Chapter 1: trust = 2
Chapter 2: trust = 8  (jumped 6 points!)
```

**Good (path integration):**
```
Chapter 1: trust = 2
  Event: Small promise kept
Chapter 2: trust = 3
  Event: Vulnerable moment handled well
Chapter 3: trust = 5
  Event: Major sacrifice witnessed
Chapter 4: trust = 8
```

## Genres Constrain Paths

### Genre as Boundary Conditions

Genres don't just define endings - they define **allowable trajectories**:

**Romance constraint:**
- Must reach: intimacy ≥ 8, trust ≥ 7, goal_alignment ≥ 8
- Cannot: End with power_differential > |2|
- Path: Trust follows sawtooth (build-break-rebuild)

**Thriller constraint:**
- Must maintain: stakes ≥ 7, danger ≥ 6
- Must resolve: danger ≤ 3 OR acceptance ≥ 8
- Path: Danger spikes and plateaus

**Mystery constraint:**
- Must resolve: info_asymmetry ≤ 2
- Path: Stepwise reduction with clues
- Cannot: Dump all info at once (unearned)

### Genre Hybrids

Combine constraints from both genres:

**Romantic Suspense:**
- Must satisfy romance ending: intimacy ≥ 8, trust ≥ 7
- Must satisfy thriller: resolve danger
- Path challenge: Balance both arcs

## Multi-Dimensional Phase Space

### Visualizing the Space

While we can't literally visualize 9-dimensional space, we can think about it:

```
3D space: (x, y, z)
Story space: (intimacy, trust, power, stakes, vulnerability, desire, alignment, info, proximity)
```

Each possible configuration is a point in this space.
Your story is a path through this space.
Genre defines which regions you can/must visit.

### Distance in Phase Space

Two story states can be "close" or "far" in phase space:

```python
state_A = {'intimacy': 2, 'trust': 2, 'desire': 3}
state_B = {'intimacy': 8, 'trust': 8, 'desire': 9}

# These are far apart - a long journey from A to B
```

**Pacing as distance:** How much phase-space territory you cover per chapter.

## Emergent Properties Summary

| Property | Formula/Definition | What It Means |
|----------|-------------------|---------------|
| **Tension** | Weighted sum of dimensions and gaps | Dramatic pressure reader feels |
| **Conflict** | f(power_diff, goal_misalignment, desire + proximity deficit) | Opposition between characters |
| **Chemistry** | f(desire, proximity variance, vulnerability, info_asymmetry) | Romantic/sexual spark |
| **Pacing** | ‖ds/dt‖ | Speed through phase space |
| **Dramatic Irony** | reader_info - character_info | Reader knows what character doesn't |

## Key Principles Revisited

### 1. Stories Are Trajectories
Not a series of events, but continuous movement through dimensional space.

### 2. Tension Emerges
From gaps and configuration, not arbitrary "make it tense."

### 3. Pacing Is Velocity
How fast you move through space. Vary it for best effect.

### 4. Genres Constrain Paths
Not just destinations but allowable routes.

### 5. Earned Moments
Require proper path integration. No teleportation.

## The Power of This Framework

### What You Can Do

**Engineer specific effects:**
- Want high tension? Maximize gaps and stakes
- Want satisfaction? Close the gaps
- Want chemistry? Create desire + proximity variance
- Want conflict? Misalign goals and power

**Diagnose problems:**
- Flat scene? Check velocity (probably zero)
- Unbelievable development? Check for jumps ≥ 3 without catalyst
- Pacing issues? Map velocity curve
- Wrong genre feel? Check dimensional constraints

**Plan systematically:**
- Map intended trajectory
- Mark required catalyst events
- Verify genre compliance
- Ensure variety in velocity

## The Same Event, Different Contexts

This is the most important insight:

**A kiss when:**
- intimacy=2, trust=3, desire=5 → Surprising, possibly unwanted
- intimacy=5, trust=6, desire=8 → Exciting, anticipated
- intimacy=8, trust=9, desire=9 → Satisfying, culmination

**Same event. Completely different impact. Because context is configuration.**

## Next Steps

Now that you understand the theory:

1. **Learn precise scoring:** `03-dimension-reference.md`
2. **See genre patterns:** `04-genre-guides/`
3. **Practice diagnosis:** `06-diagnostic-guide.md`
4. **Apply to your work:** Start mapping your current story's trajectory

---

**Remember:** You're not just writing events. You're choreographing movement through multidimensional space. Every scene should move at least 2-3 dimensions. Every major shift should be earned. And tension will emerge naturally from the right configuration.
