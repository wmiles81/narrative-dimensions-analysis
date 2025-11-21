# Advanced Techniques

Advanced applications of the Narrative Dimensions Analysis system.

## Multi-Subplot Tracking

### The Challenge

Complex stories have multiple arcs running simultaneously:
- Main romance
- External thriller plot
- Character growth arc
- Secondary romance (side couple)
- Mystery subplot

How do you track dimensions for all of them?

### Solution: Dimensional Layers

**Think of dimensions in layers:**

```
Layer 1 (Primary): Main relationship
  - intimacy, trust, desire (protagonist + love interest)

Layer 2 (Secondary): External plot
  - stakes, danger, info_asymmetry (thriller/mystery elements)

Layer 3 (Tertiary): Character growth
  - power, vulnerability (individual arc)

Layer 4 (Quaternary): Side couple
  - intimacy_B, trust_B, desire_B (secondary romance)
```

### Tracking Multiple Relationships

**Subscript notation:**

```python
state = {
    # Main couple (A + B)
    'intimacy_AB': 6,
    'trust_AB': 5,
    'desire_AB': 8,

    # Protagonist + rival (A + C)
    'trust_AC': 3,
    'power_diff_AC': -2,

    # Side couple (D + E)
    'intimacy_DE': 4,
    'trust_DE': 6,

    # Shared dimensions (affect all)
    'stakes': 8,
    'danger': 7
}
```

### Pacing Multiple Arcs

**Stagger the movements:**

**Chapter 5:**
```
Primary arc: intimacy_AB moves (5 → 6)
Secondary arc: stakes move (6 → 8)
Tertiary: vulnerability static
Quaternary: intimacy_DE static

Focus: Main romance + external pressure
```

**Chapter 6:**
```
Primary arc: trust_AB moves (5 → 4, setback)
Secondary arc: danger static at 7
Tertiary: power_diff moves (-3 → -2)
Quaternary: intimacy_DE moves (4 → 5)

Focus: Main romance setback + growth arc + side couple
```

**Rule:** Don't move everything every chapter. Rotate focus.

### Arc Priority System

**Assign weights:**

```
Primary arc (main romance): 50% of chapters should move
Secondary arc (thriller): 40% of chapters should move
Tertiary arc (character): 30% of chapters should move
Quaternary arc (side couple): 20% of chapters should move
```

**Per chapter:** Move 1-2 arcs significantly

### Convergence Points

**Some events affect multiple arcs:**

**Example: Betrayal revealed**
```
Affects:
- Main romance: trust_AB drops (8 → 1)
- External plot: info_asymmetry changes (7 → 3)
- Character arc: vulnerability exposed (forced to 9)
- Side couple: trust_DE affected (6 → 5, they knew?)

Single event, ripples across arcs
```

### Tracking Tools

**Spreadsheet approach:**

```
Chapter | intimacy_AB | trust_AB | stakes | danger | intimacy_DE | notes
1       | 3           | 4        | 5      | 3      | 2          | Meet
2       | 4           | 4        | 6      | 3      | 2          | First connection
3       | 4           | 3        | 6      | 5      | 3          | Danger introduced
...
```

**Graph approach:**
- Plot each arc as separate line
- See which arcs moving when
- Identify flat spots

---

## Customizing Tension Formulas

### Why Customize?

The base tension formula works for most stories, but you can tune it:

**Base formula:**
```
TENSION = w₁(stakes) + w₂(info_asymmetry) + w₃(goal_misalignment) +
          w₄(vulnerability - trust) + w₅(desire - proximity) + w₆(|power_diff|)
```

**Your story might emphasize different elements.**

### Understanding Weights

**Weights determine importance:**

```python
# Romance weights (emotional gaps matter most)
romance_weights = {
    'w_stakes': 0.8,
    'w_info_asym': 0.5,
    'w_goal_misalign': 0.7,
    'w_vuln_trust_gap': 1.2,      # ← Highest
    'w_desire_prox_gap': 1.0,
    'w_power_diff': 0.6
}

# Thriller weights (external pressure matters most)
thriller_weights = {
    'w_stakes': 1.5,              # ← Highest
    'w_info_asym': 1.0,
    'w_goal_misalign': 0.7,
    'w_vuln_trust_gap': 0.5,
    'w_desire_prox_gap': 0.3,
    'w_power_diff': 0.8
}
```

### Custom Weights for Your Story

**Identify what creates YOUR story's tension:**

**Example: Dark Romance**
```python
dark_romance_weights = {
    'w_stakes': 1.0,           # Always high stakes
    'w_info_asym': 0.8,        # Secrets important
    'w_goal_misalign': 0.6,    # Some opposition
    'w_vuln_trust_gap': 1.3,   # ← Highest (emotional exposure + uncertainty)
    'w_desire_prox_gap': 1.1,  # High (want but dangerous)
    'w_power_diff': 1.2,       # ← High (power dynamics central)
}
```

**Example: Mystery-Romance Hybrid**
```python
mystery_romance_weights = {
    'w_stakes': 0.9,
    'w_info_asym': 1.3,        # ← Highest (mystery element)
    'w_goal_misalign': 0.5,
    'w_vuln_trust_gap': 1.0,   # Romance element
    'w_desire_prox_gap': 0.8,  # Romance element
    'w_power_diff': 0.6,
}
```

### Adding Genre-Specific Terms

**Some genres need extra dimensions in tension formula:**

**Horror adds fear:**
```
TENSION_HORROR = base_tension + w₇(fear) + w₈(dread)
```

**Epic Fantasy adds fate:**
```
TENSION_FANTASY = base_tension + w₇(fate - acceptance)
```

**Noir adds moral weight:**
```
TENSION_NOIR = base_tension + w₇(moral_ambiguity)
```

### Testing Your Formula

**Verify it matches your intuition:**

```python
# High tension scene in your story
scene_state = {
    'stakes': 9,
    'vulnerability': 8,
    'trust': 2,
    # ... other dimensions
}

calculated_tension = apply_formula(scene_state, your_weights)

# Should be 7-9 if this is your high tension scene
# If not, adjust weights
```

**Calibration:**
- Low tension scenes should calculate to 2-4
- Medium tension scenes should calculate to 5-6
- High tension scenes should calculate to 7-9
- Peak tension (black moment) should calculate to 9-10

---

## Creating Genre Templates

### Why Templates?

If you write in a specific niche repeatedly, create your own template.

### Template Components

**1. Ending Requirements**
```python
cozy_mystery_template = {
    'ending_requirements': {
        'info_asymmetry': {'max': 2, 'required': True},
        'stakes': {'range': (3, 6), 'required': False},
        'danger': {'max': 3, 'required': True},
        'trust_in_community': {'min': 6, 'required': True}
    }
}
```

**2. Trajectory Patterns**
```python
'trajectory': {
    'info_asymmetry': 'decreasing_stepwise',  # -1 per chapter
    'trust': 'fluctuating',                   # Suspects change
    'danger': 'low_constant',                 # Always ≤ 3
    'stakes': 'moderate_stable'               # 4-6 range
}
```

**3. Tension Weights**
```python
'tension_weights': {
    'w_stakes': 0.7,
    'w_info_asym': 1.4,  # Primary driver
    'w_goal_misalign': 0.5,
    'w_vuln_trust_gap': 0.6,
    'w_desire_prox_gap': 0.3,
    'w_power_diff': 0.4
}
```

**4. Key Beats**
```python
'beats': {
    '10%': {'event': 'crime_discovered', 'dimensions': {'info_asym': (0, 10)}},
    '25%': {'event': 'suspects_introduced', 'dimensions': {'trust': 'variable'}},
    '50%': {'event': 'red_herring_peak', 'dimensions': {'info_asym': (7, 5)}},
    '75%': {'event': 'breakthrough', 'dimensions': {'info_asym': (5, 2)}},
    '90%': {'event': 'confrontation', 'dimensions': {'info_asym': (2, 0)}}
}
```

**5. Modifiers Allowed**
```python
'compatible_modifiers': [
    'small_town',
    'historical',
    'culinary',
    'amateur_detective'
],
'incompatible_modifiers': [
    'serial_killer',  # Too dark for cozy
    'graphic_violence'  # Violates danger requirement
]
```

### Example: Paranormal Romantic Suspense Template

```python
paranormal_romantic_suspense = {
    'base_genre': 'hybrid',
    'components': ['romance', 'thriller', 'paranormal'],

    'ending_requirements': {
        # Romance requirements
        'intimacy': {'min': 8},
        'trust': {'min': 7},
        'goal_alignment': {'min': 8},
        'power_differential': {'range': (-1, 1)},

        # Thriller requirements
        'danger': {'max': 3, 'or_acceptance': 8},

        # Paranormal requirements
        'acceptance_of_paranormal': {'min': 8}
    },

    'trajectory': {
        'intimacy': 'romance_pattern',
        'trust': 'complicated_by_secrets',
        'danger': 'sustained_high',
        'stakes': 'both_personal_and_world',
        'info_asymmetry': 'paranormal_reveal_70_percent'
    },

    'tension_weights': {
        'w_stakes': 1.1,           # Thriller element
        'w_info_asym': 1.0,        # Paranormal secrets
        'w_goal_misalign': 0.6,
        'w_vuln_trust_gap': 1.2,   # Romance element
        'w_desire_prox_gap': 0.9,  # Romance element
        'w_power_diff': 0.9        # Paranormal power imbalance
    },

    'unique_dimensions': [
        'acceptance_of_paranormal',
        'paranormal_power_differential'
    ],

    'key_beats': {
        '30%': 'paranormal_reveal',
        '50%': 'acceptance_crisis',
        '75%': 'black_moment_threatens_both_arcs'
    }
}
```

---

## Advanced Pacing Techniques

### Velocity Variance for Effect

**Deliberate pacing shifts create impact:**

```
Technique: Acceleration into Crisis
Ch 1-5: velocity = 2 (steady)
Ch 6-8: velocity = 2.5 (slightly faster)
Ch 9: velocity = 6 (sudden acceleration)
Effect: Reader feels the rush

Technique: Deceleration for Intimacy
Ch 10: velocity = 5 (action)
Ch 11: velocity = 2 (slow, intimate processing)
Effect: Reader feels the breath, emotional weight
```

### Dimensional Cycling

**Move different dimensions in patterns:**

```
Cycle 1 (Chapters 1-4): Intimacy + Trust focus
  Ch 1: intimacy +2, trust +1
  Ch 2: intimacy +1, trust +2
  Ch 3: intimacy +2, trust -1 (setback)
  Ch 4: intimacy +1, trust +2 (recovery)

Cycle 2 (Chapters 5-8): Stakes + Danger focus
  Ch 5: stakes +2, danger +3
  Ch 6: stakes +1, danger +2
  Ch 7: stakes +2, danger -2 (false security)
  Ch 8: stakes +3, danger +4 (spike)

Cycle 3 (Chapters 9-12): All converge
  Ch 9: intimacy, trust, stakes, danger all move
```

### Contrasting Velocities

**Different subplots at different speeds:**

```
Main romance: Slow burn (velocity = 1)
External thriller: Fast (velocity = 4)
Character growth: Medium (velocity = 2)

Effect: Creates texture, variety
```

### The Plateau-and-Spike Pattern

**Strategic plateaus make spikes more effective:**

```
Dimension: Trust
Ch 1-3: trust = 4 (plateau)
Ch 4: trust 4 → 7 (spike, catalyst)
Ch 5-7: trust = 7 (plateau)
Ch 8: trust 7 → 2 (spike down, betrayal)
Ch 9-11: trust = 2 (plateau, processing)
Ch 12: trust 2 → 8 (spike up, grand gesture)

Each spike feels earned because of plateau
```

---

## Emergent Property Engineering

### Beyond Tension: Other Emergent Properties

**Conflict:**
```
CONFLICT = (10 - goal_alignment) + |power_diff| +
           (desire × low_proximity_penalty)
```

**Chemistry:**
```
CHEMISTRY = desire × proximity_variance +
            vulnerability +
            info_asymmetry(sweet_spot_3_to_6)
```

**Suspense:**
```
SUSPENSE = info_asymmetry + stakes +
           (danger - power_to_handle_it)
```

**Satisfaction:**
```
SATISFACTION = (intimacy + trust)/2 +
               goal_alignment -
               (desire - proximity)
```

### Engineering Specific Effects

**Want high suspense?**
```
Maximize:
- info_asymmetry (reader doesn't know)
- stakes (matters deeply)
- danger (real threat)
Minimize:
- power (protagonist outmatched)
```

**Want satisfaction (HEA)?**
```
Maximize:
- intimacy (deep bond)
- trust (secure)
- goal_alignment (shared future)
Close gaps:
- desire ≈ proximity (want and have)
- vulnerability ≈ trust (safe to be open)
```

**Want delicious angst?**
```
Maximize:
- desire (want badly)
- vulnerability (emotionally exposed)
Minimize:
- proximity (can't be together)
- trust (uncertain)
Gap terms are HUGE = angst
```

---

## Dimensional Forecasting

### Predicting Reader Response

**Based on configuration, predict experience:**

```python
def predict_reader_experience(state):
    tension = calculate_tension(state)
    chemistry = calculate_chemistry(state)
    satisfaction = calculate_satisfaction(state)

    if tension > 7 and chemistry > 6:
        return "intense, engaging, can't put down"
    elif tension < 3 and velocity == 0:
        return "boring, might skim"
    elif satisfaction > 8 and tension < 4:
        return "happy, satisfied, maybe ready for book to end"
    # ... etc
```

### Planning Backward from Ending

**Start with ending requirements, work backward:**

```
Ending (Romance): intimacy=9, trust=8, goal_align=9

Chapter 20 (resolution): intimacy=9, trust=8, goal_align=9
  ← What needs to happen?

Chapter 19 (grand gesture): intimacy=7, trust=3, goal_align=3
  ← Need catalysts: vulnerability=10 event, trust-building action

Chapter 18 (black moment): intimacy=4, trust=1, goal_align=2
  ← Need catalysts: major betrayal, misalignment revealed

Chapter 17 (false victory): intimacy=7, trust=7, goal_align=8
  ← Building to this, then catastrophe

Work backward to Chapter 1
```

### Trajectory Optimization

**If you have draft with problems, optimize:**

```
Problem: Chapter 12-15 drag (velocity too low)

Solution:
1. Identify static dimensions (intimacy stuck at 5)
2. Add movement (intimacy 5 → 6 → 5 → 7 creates arc)
3. Verify doesn't create new problems (earned? catalyst?)
4. Recalculate velocity (now 2.5, good)
```

---

## Character-Specific Dimensionality

### Tracking Individual vs. Relationship Dimensions

**Some dimensions are relational, some individual:**

**Relational (between characters):**
- Intimacy (A's closeness with B)
- Trust (A's trust in B)
- Power differential (A's power vs B)
- Goal alignment (A's goals vs B's goals)

**Individual (character state):**
- Vulnerability (A's walls up/down)
- Power (A's absolute power level)
- Acceptance (A's peace with situation)

**Tracking both:**
```python
character_A_state = {
    # Individual
    'vulnerability': 6,
    'power': 3,
    'acceptance': 5,

    # Relational with B
    'intimacy_with_B': 7,
    'trust_in_B': 6,
    'desire_for_B': 8
}

character_B_state = {
    # Individual
    'vulnerability': 4,
    'power': 5,
    'acceptance': 3,

    # Relational with A
    'intimacy_with_A': 7,  # Might match A's
    'trust_in_A': 7,       # Might differ from A's trust in B!
    'desire_for_A': 7
}
```

### Asymmetric Dimensions

**Sometimes dimensions aren't mutual:**

```
A's trust in B: 8
B's trust in A: 3

Creates:
- Dramatic irony (reader knows the asymmetry)
- Character tension (one vulnerable, other guarded)
- Plot potential (when will they equalize?)
```

---

## Integration with Traditional Story Structure

### Mapping Dimensions to Save the Cat Beats

**Save the Cat structure with dimensional signatures:**

1. **Opening Image:** Baseline dimensions
2. **Theme Stated:** Core dimensional journey previewed
3. **Setup:** Establishing dimensional starting point
4. **Catalyst:** Major dimension spikes (stakes, info asymmetry)
5. **Debate:** Goal alignment questioned
6. **Break into Two:** Dimensional commitment (goal alignment increases)
7. **B Story:** Secondary dimensional arc begins
8. **Fun and Games:** Dimensions moving in "promise of premise" way
9. **Midpoint:** False victory (temporary high configuration)
10. **Bad Guys Close In:** Dimensional pressure (stakes rise, trust drops)
11. **All Is Lost:** Black moment (multiple dimensions crash)
12. **Dark Night of the Soul:** Dimensional low point
13. **Break into Three:** Dimensional shift (realization, plan)
14. **Finale:** Dimensions rapidly moving to resolution
15. **Final Image:** Ending dimensional configuration

### Mapping Dimensions to Hero's Journey

**Monomyth with dimensional lens:**

1. **Ordinary World:** power=-3, stakes=2, low all dimensions
2. **Call to Adventure:** stakes spike, info asymmetry increases
3. **Refusal:** goal_alignment low (don't want quest)
4. **Meeting Mentor:** trust begins, power starts growing
5. **Crossing Threshold:** stakes lock high, cannot retreat
6. **Tests/Allies/Enemies:** trust building, power growing
7. **Approach:** intimacy/trust deepening, stakes rising
8. **Ordeal:** black moment (dimensions crash)
9. **Reward:** power increase earned, knowledge gained
10. **Road Back:** bringing dimensional changes home
11. **Resurrection:** final dimensional test, all peak
12. **Return with Elixir:** stable new high configuration

---

## Advanced Diagnostic Tools

### Dimensional Variance Analysis

**Measure how much each dimension varies:**

```python
variance = {
    'intimacy': 4,     # Ranges from 2 to 6 (variance = 4)
    'trust': 7,        # Ranges from 1 to 8 (variance = 7)
    'stakes': 2        # Ranges from 6 to 8 (variance = 2)
}

# High variance dimensions = dynamic arcs
# Low variance dimensions = static (problem or feature?)
```

**Use it:**
- Identify which dimensions carry your story
- Spot flat dimensions that should move
- Verify character growth (variance in power, vulnerability)

### Correlation Analysis

**Do certain dimensions move together?**

```
When intimacy increases, does vulnerability increase?
When stakes rise, does trust drop?
When proximity increases, does desire increase or decrease?
```

**Useful for:**
- Understanding your story's logic
- Finding unintentional patterns
- Ensuring variety (don't want all dimensions correlating)

### Momentum Tracking

**Not just velocity (speed) but momentum (mass × velocity):**

```python
momentum = importance_weight × velocity

Example:
  intimacy: weight=10, velocity=2 → momentum=20
  danger: weight=5, velocity=3 → momentum=15

Intimacy has more momentum (matters more, moving)
```

**Use it:**
- Identify which arcs driving your story
- Ensure primary arc has highest momentum
- Balance multiple arcs

---

## Experimental Techniques

### Negative Space Storytelling

**What if you track what DOESN'T change?**

```
Everything changes except trust (remains 3)
Effect: Trust becomes the central question
Reader notices the unchanging dimension
```

### Dimensional Inversion

**What if you reverse expected trajectory?**

```
Normal romance: trust increases
Inverted: trust decreases (relationship darkens)

Normal thriller: danger increases
Inverted: danger decreases (anticlimax as technique)
```

### Quantum Dimensions

**What if dimension is uncertain until observed?**

```
Is the ally trustworthy? Trust=? until revelation
Schrödinger's trust: both high and low until collapsed
```

---

## Putting It All Together

**Advanced technique integration:**

1. **Define your custom template** (genre + modifiers)
2. **Set custom tension weights** (what creates tension in YOUR story)
3. **Track multiple arcs** (layers, subscripts)
4. **Plan dimensional forecasts** (work backward from ending)
5. **Monitor velocity and momentum** (pacing and importance)
6. **Apply advanced pacing** (cycling, variance, plateaus)
7. **Engineer emergent properties** (tension, chemistry, satisfaction)
8. **Integrate with structure** (Save the Cat, Hero's Journey, etc.)
9. **Diagnose and optimize** (variance, correlation, momentum)

---

**Next:** See `08-faq.md` for common questions, or return to `02-core-concepts.md` for fundamentals.
