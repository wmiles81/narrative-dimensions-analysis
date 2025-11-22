---
name: narrative-dimensions-analysis
description: Physics-inspired story analysis system with two complementary frameworks - (1) Dimensional analysis tracking 9+ dimensions (intimacy, trust, power, stakes, etc.) for scene-level tension engineering and pacing diagnostics, and (2) Narrative Physics Engine (NPE) with composite axes (IA/RA/EA/TA) for arc-level planning with genre-specific physics constraints. Supports 7 genres with waveform analysis, entropy tracking, and polarity flip detection. Use for story structure analysis, tension engineering, character arc validation, pacing diagnostics, or multi-genre trajectory planning.
# Narrative Dimensions Analysis System
---

A physics-inspired approach to story analysis that treats narrative as movement through multidimensional phase space.

## Quick Start

For immediate analysis, specify:
1. **Content level**: concept, outline, chapter, book, or series
2. **Genre**: romance, dark-romance, thriller, mystery, sci-fi, fantasy, or hybrid
3. **What to analyze**: structure, pacing, tension, character arcs, or full diagnostic

## Core Concept

Stories exist as trajectories through N-dimensional space where each dimension represents an independent narrative variable. Tension and other dramatic qualities emerge from the configuration of these dimensions.

**State Vector**: `s(t) = [intimacy, power_diff, info_asym, alignment, proximity, vulnerability, desire, stakes, trust]`

## Basis Dimensions (Independent Variables)

### Primary Dimensions (0-10 scale unless noted)

1. **INTIMACY** - Emotional closeness between characters
2. **POWER_DIFFERENTIAL** - Agency imbalance (-5 to +5, where 0 = balanced)
3. **INFORMATION_ASYMMETRY** - Knowledge gaps between characters
4. **GOAL_ALIGNMENT** - How much characters want the same thing
5. **PHYSICAL_PROXIMITY** - Literal spatial distance
6. **VULNERABILITY** - Emotional walls up/down state
7. **DESIRE** - Attraction/pull between characters
8. **STAKES** - Magnitude of consequences
9. **TRUST** - Belief in other's reliability

### Secondary Dimensions (genre-specific)

- **DANGER** - Physical threat level (thriller/suspense)
- **MYSTERY** - Unknown elements to reader (mystery/thriller)
- **WORLD_COMPLEXITY** - Setting intricacy (fantasy/sci-fi)
- **SOCIAL_PRESSURE** - External judgment (contemporary romance)
- **MORAL_AMBIGUITY** - Ethical grayness (dark romance)

## Emergent Properties (Calculated)

### Tension Formula

Base tension emerges from dimensional configuration:

```
TENSION = w₁(stakes) + w₂(info_asymmetry) + w₃(goal_misalignment) + 
          w₄(vulnerability - trust) + w₅(desire - proximity) + w₆(|power_diff|)
```

Genre-specific weights in `references/genre-weights.json`

### Other Emergent Properties

- **CONFLICT** = f(power_diff, goal_misalignment, desire with proximity deficit)
- **CHEMISTRY** = f(desire, proximity, vulnerability, productive info_asymmetry)
- **PACING** = ||ds/dt|| (velocity through phase space)
- **DRAMATIC_IRONY** = reader_info - character_info

## Analysis Procedures

### Structure Analysis

1. Map current dimensional configuration
2. Check genre constraint satisfaction
3. Identify trajectory patterns
4. Validate ending coordinates match genre requirements

### Pacing Diagnostic

Calculate velocity vector: `v(t) = ds/dt`

- **Stuck**: ||v|| ≈ 0 (no dimensional movement)
- **Rushed**: ||v|| > threshold (teleportation between states)
- **Optimal**: 2-3 dimensions shifting per unit

### Tension Engineering

To increase tension:
- Maximize (stakes - trust)
- Maximize (desire - proximity)
- Increase information asymmetry with high vulnerability
- Force proximity with misaligned goals

### Arc Validation

Check if dimensional changes are "earned":
- Each jump ≥ 3 points needs catalyst event
- Trajectory must be continuous (no teleportation)
- Character growth shows across multiple dimensions

### The "Black Moment" Formula

Peak crisis configuration:
- Stakes → MAX
- Trust → MIN
- Goal Alignment → SHATTERED
- Desire → HIGH (maintains investment)

## Genre-Specific Configurations

See `references/genre-configs.md` for detailed patterns

### Quick Genre Templates

**Romance**: Must end at intimacy ≥ 8, trust ≥ 7
**Dark Romance**: Maintain power_diff fluctuation, high stakes throughout
**Thriller**: Danger + stakes high, trust variable
**Mystery**: Information asymmetry drives plot until revelation
**Enemies-to-Lovers**: Goal alignment slowest mover

## Diagnostic Outputs

### Scene-Level Analysis
- Current dimensional state
- Dimensional velocity (what's changing)
- Tension calculation
- Suggested adjustments

### Chapter-Level Analysis
- Dimensional trajectory map
- Pacing assessment
- Arc progression check
- Genre compliance status

### Book-Level Analysis
- Full phase space trajectory
- Character arc paths
- Pacing heat map
- Black moment validation
- Ending coordinate check

## Narrative Physics Engine (NPE)

The NPE system provides a complementary high-level physics framework using composite axes for arc planning and validation across multiple genres.

### NPE Composite Axes

**IA (Internal Axis)**: Character's internal state (-1 to +1)
- Negative = Wounded, broken, in denial
- Zero = Transitional moment (polarity flip)
- Positive = Healed, whole, self-aware
- Calculated from: self_worth, emotional_regulation dimensions

**RA (Relational Axis)**: Relationship distance as orbital mechanics (0-180°)
- 0° = Perfect union, no distance
- 90° = Perpendicular, maximum tension
- 180° = Complete separation, bond broken
- Tracks relationship geometry, not just closeness

**EA (Environmental Axis)**: External pressure (-1 to +1)
- Measures forces acting on character from outside
- World stakes, antagonistic forces, circumstances
- Calculated from: stakes, danger, social_pressure

**TA (Task Axis)**: Quest/goal progression (0 to +1)
- 0 = Quest not started or failing
- 1 = Quest complete/goal achieved
- Calculated from: goal_alignment, info_asymmetry resolution

### NPE Physics Constraints

**Waveform Analysis**:
- Amplitude: Emotional swing range (genre-specific limits)
- Frequency: Rate of emotional oscillation
- Phase: Rising/falling state at any point

**Entropy**: Narrative disorder (0-1.0)
- Low entropy = Ordered, predictable, safe
- High entropy = Chaotic, unpredictable, dangerous
- Genre-specific tolerance levels

**Polarity Flip**: Critical moment when IA crosses zero
- Character shifts from broken to healing
- Must be earned through dimensional progression
- Timing varies by genre

### Multi-Genre NPE Profiles

The system includes physics constraints for 7 genres:

1. **Cozy Fantasy**: Low amplitude (1.5 max), must cross zero, entropy ≤ 0.6
2. **Psychological Thriller**: High amplitude (2.5 max), no zero-crossing required, entropy ≤ 1.0
3. **Dark Romance**: Medium-high amplitude (2.0), late polarity flip, entropy ≤ 0.95
4. **Epic Fantasy**: High amplitude, extended arcs, entropy ≤ 0.85
5. **Psychological Horror**: Maximum amplitude (2.5), can end broken, entropy ≤ 1.0
6. **Romantic Comedy**: Moderate amplitude (1.8), rapid oscillation, entropy ≤ 0.55
7. **Cozy Mystery**: Low amplitude (1.4), controlled chaos, entropy ≤ 0.5

See `references/npe_genre_profiles.py` for complete constraint definitions.

### NPE Analysis Capabilities

**Axis Progression Tracking**:
- Monitor IA wound-to-growth trajectory
- Track RA orbital closure/distance
- Validate EA pressure curves
- Measure TA quest completion arc

**Genre Validation**:
- Check waveform amplitude against genre limits
- Verify entropy stays within genre tolerance
- Validate required trajectory patterns (e.g., must cross zero)
- Confirm ending states match genre expectations

**Physics Diagnostics**:
- Dark Night detection (all axes at crisis point)
- Polarity flip identification and validation
- Entropy spike analysis
- Waveform frequency/amplitude violations

### NPE + Dimensions Integration

The two systems work complementarily:

**NPE for high-level planning**:
- Overall arc shape and physics
- Genre constraint validation
- Critical moment identification

**Dimensions for scene execution**:
- Granular state tracking
- Tension calculation
- Moment-to-moment pacing

**Bidirectional conversion**:
```python
# NPE axes derived from dimensions
IA = (self_worth / 5) - 1
RA_orbit = 180 - ((intimacy + trust) / 20 * 180)
EA = (stakes / 10) * 2 - 1
TA = (goal_alignment - info_asymmetry) / 10
```

## Scripts

### Dimensional Analysis
- `scripts/calculate_tension.py` - Compute tension from dimensional state
- `scripts/validate_trajectory.py` - Check if arc is properly earned
- `scripts/generate_report.py` - Create full dimensional analysis report

### NPE Analysis
- `scripts/npe_analyzer.py` - Analyze NPE axes, waveform, entropy, genre validation
- `scripts/npe_visualizer.py` - Generate ASCII visualizations of NPE progression
- `scripts/convert_dimensions_to_npe.py` - Convert dimensional trajectory to NPE axes

## References

### Dimensional System
- `references/genre-weights.json` - Tension formula weights by genre
- `references/genre-configs.md` - Detailed genre conventions and constraints
- `references/catalyst-events.md` - Events that justify dimensional jumps
- `references/diagnostic-patterns.md` - Common problems and solutions

### NPE System
- `references/npe_genre_profiles.py` - Complete physics constraints for 7 genres
- `NPE_MULTI_GENRE_GUIDE.md` - Technical guide to multi-genre NPE analysis
- `AUTHOR_GUIDE.md` - Non-technical guide for authors using NPE in Claude Chat

## Usage Examples

### Diagnosing a Flat Scene
```python
# Current state shows no movement
state = {"intimacy": 5, "trust": 5, "stakes": 5, ...}
# All dimensions static = death
# Solution: Move 2-3 dimensions
```

### Planning Dark Romance Arc
```
Start: power_diff=+5, trust=0, stakes=10, desire=3
Mid: power_diff oscillates, trust climbs slowly, stakes high
End: power_diff=0, trust=8, stakes=personal, desire=10
```

### Engineering High Tension Chapter
```
Target configuration:
- Stakes: 9
- Trust: 2
- Information Asymmetry: 8
- Vulnerability: 7
- Physical Proximity: 8 (forced closeness)
```

### NPE Arc Planning (Cozy Fantasy)
```
Genre: Cozy Fantasy
Chapters: 26

Chapter 1: IA=-0.85 (wounded), RA=160° (distant), EA=0.3, TA=0
Chapter 17: IA=-0.90 (DARK NIGHT), RA=160°, EA=1.0, TA=0
Chapter 22: IA=0 (POLARITY FLIP), RA=90°, EA=0.6, TA=0.5
Chapter 26: IA=+0.75 (healed), RA=60° (close), EA=0.2, TA=0.9

Validation: ✓ Crosses zero, ✓ Amplitude within 1.5, ✓ Entropy ≤ 0.6
```

### Multi-Genre Validation
```
# Check if psychological thriller arc violates genre physics
python scripts/npe_analyzer.py trajectory.json --genre psychological_thriller

# Validates:
- Waveform amplitude ≤ 2.5
- Entropy spikes ≤ 1.0
- No zero-crossing requirement (can end broken)
- Dark night timing and depth
```

## Terminology & Calculation Clarifications

### Goal Alignment vs. Goal Misalignment
- **Goal Alignment** is the primary dimension (0-10 scale)
  - 0 = Complete opposition (incompatible goals)
  - 5 = Neutral or partially aligned
  - 10 = Perfect alignment (wanting exactly the same thing)
- **Goal Misalignment** is calculated for tension formulas:
  - `goal_misalignment = 10 - goal_alignment`
  - Used in tension calculations to measure conflict from opposing objectives

### Information Asymmetry Types
The system tracks two types of information gaps:
- **Character Information Asymmetry**: Knowledge gaps between characters (primary dimension)
  - One character knows something the other doesn't
  - Secrets, hidden identities, withheld information
- **Reader Mystery**: Knowledge gaps between reader and story truth (genre-specific)
  - What the audience doesn't know yet
  - Used for suspense and mystery genres

### Acceptance Dimension (Optional)
- **Acceptance** (0-10): Character's psychological peace with an outcome
  - 0 = Cannot accept reality, in denial or fighting it
  - 5 = Struggling with acceptance
  - 10 = Complete peace with the situation
- Useful for endings where full resolution isn't possible
- Common in thrillers (accepting danger exists), tragedies (accepting loss)

### Catalyst Event Threshold
- Dimensional jumps **≥ 3 points** require a catalyst event
- Jumps of 1-2 points can occur through accumulated small moments
- See `references/catalyst-events.md` for event types that justify large shifts

## Key Principles

1. **Stories are trajectories** - Not events but dimensional movement
2. **Tension emerges** - From configuration, not arbitrary assignment
3. **Pacing is velocity** - How fast you move through phase space
4. **Genres constrain paths** - Not destinations but allowable trajectories
5. **Earned moments** - Require proper path integration, not jumps

Remember: The same kiss hits differently at intimacy=2 vs intimacy=8. Context is configuration.
