# Tension Formula Quick Reference

## Base Formula

```
TENSION = w₁(stakes) + w₂(info_asymmetry) + w₃(goal_misalignment) +
          w₄(vulnerability_trust_gap) + w₅(desire_proximity_gap) +
          w₆(power_differential) + [genre-specific dimensions]
```

**Where**:
- `goal_misalignment = 10 - goal_alignment`
- `vulnerability_trust_gap = max(0, vulnerability - trust)`
- `desire_proximity_gap = max(0, desire - proximity)`
- `power_differential = abs(power_differential)`

## Weights by Genre (Side-by-Side)

| Component | Contemp Romance | Dark Romance | Psych Thriller | Action Thriller | Cozy Mystery | Noir Mystery |
|-----------|----------------|--------------|----------------|-----------------|--------------|--------------|
| **Stakes** | 0.15 | 0.25 | 0.20 | **0.30** | 0.10 | 0.20 |
| **Info Asymmetry** | 0.10 | 0.15 | **0.25** | 0.10 | **0.40** | **0.25** |
| **Goal Misalign** | 0.15 | 0.10 | 0.15 | 0.10 | 0.15 | 0.15 |
| **Vuln-Trust Gap** | **0.25** | 0.15 | 0.10 | - | - | - |
| **Desire-Prox Gap** | **0.25** | 0.15 | - | - | - | - |
| **Power Diff** | 0.10 | **0.20** | 0.15 | 0.10 | - | 0.15 |
| **Danger** | - | - | 0.15 | **0.30** | - | - |
| **Trust (direct)** | - | - | - | - | 0.15 | 0.10 |
| **Mystery** | - | - | - | - | 0.20 | - |
| **Moral Ambiguity** | - | - | - | - | - | 0.15 |
| **Proximity (direct)** | - | - | - | 0.10 | - | - |

**Bold** = Primary drivers for that genre

## Quick Calculation Steps

1. **Score each dimension** (0-10 scale, except power_differential: -5 to +5)
2. **Calculate derived values**:
   - Goal misalignment = 10 - goal_alignment
   - Vulnerability-trust gap = max(0, vulnerability - trust)
   - Desire-proximity gap = max(0, desire - proximity)
   - Power differential = abs(power_differential)
3. **Apply formula** for your genre
4. **Interpret result**:
   - 0-3: Low tension (scene may drag)
   - 3-5: Moderate tension (adequate for quiet scenes)
   - 5-7: Good tension (reader engaged)
   - 7-9: High tension (peak scenes, use sparingly)
   - 9-10: Extreme tension (crisis only, risk reader fatigue)

## Boosting Tension Checklist

### Universal Techniques
☐ **Raise stakes** - Make failure matter more
☐ **Increase info asymmetry** - Create secrets/hidden knowledge
☐ **Widen desire-proximity gap** - Want close but forced apart (or vice versa)
☐ **Create goal conflict** - Make characters want opposing things
☐ **Imbalance power** - Create dependency/vulnerability
☐ **Open vulnerability without trust** - Risk without safety

### Genre-Specific Focus

**Romance**:
- Focus on vulnerability-trust gap and desire-proximity gap
- Create yearning (high desire, low proximity)
- Force vulnerability when trust is shaky

**Thriller**:
- Maintain high stakes and danger
- Never let both drop simultaneously
- Create tension waves, not constant high

**Mystery**:
- Control info asymmetry carefully
- Stepwise revelation maintains engagement
- Fluctuate trust in suspects

## Common Tension Problems & Fixes

| Problem | Diagnosis | Fix |
|---------|-----------|-----|
| **Scene feels flat** | Tension < 3 | Raise any 2 components by 2-3 points |
| **Reader numb** | Tension constant >7 for 3+ chapters | Create wave: High → Medium → Higher |
| **Unearned drama** | High tension from single dimension | Spread across multiple dimensions |
| **Confusing** | Too many dimensions moving | Focus on 2-3 primary dimensions |
| **Chemistry weak** | Low desire-proximity gap | High desire + low proximity = yearning |
| **Conflict fake** | Only info asymmetry high | Add goal misalignment or power imbalance |

## Example Calculations

### Contemporary Romance - First Kiss Scene
```
Stakes: 6 (risking friendship)
Info Asymmetry: 3
Goal Alignment: 8 → Misalignment: 2
Vulnerability: 7
Trust: 6 → Gap: 1
Desire: 8
Proximity: 10 → Gap: 0
Power Diff: 0 → Abs: 0

TENSION = 0.15(6) + 0.10(3) + 0.15(2) + 0.25(1) + 0.25(0) + 0.10(0)
        = 0.90 + 0.30 + 0.30 + 0.25 + 0 + 0
        = 1.75

Level: LOW to MODERATE (quieter romantic moment)
```

### Dark Romance - Black Moment
```
Stakes: 9
Info Asymmetry: 2
Goal Alignment: 3 → Misalignment: 7
Vulnerability: 9
Trust: 2 → Gap: 7
Desire: 9
Proximity: 8 → Gap: 1
Power Diff: -3 → Abs: 3

TENSION = 0.25(9) + 0.15(2) + 0.10(7) + 0.15(7) + 0.15(1) + 0.20(3)
        = 2.25 + 0.30 + 0.70 + 1.05 + 0.15 + 0.60
        = 5.05

Level: GOOD (engaging, sustainable tension)
```

### Psychological Thriller - Betrayal
```
Stakes: 8
Info Asymmetry: 7
Goal Alignment: 2 → Misalignment: 8
Vulnerability: 8
Trust: 1 → Gap: 7
Power Diff: 3 → Abs: 3
Danger: 6

TENSION = 0.20(8) + 0.25(7) + 0.15(8) + 0.10(7) + 0.15(3) + 0.15(6)
        = 1.60 + 1.75 + 1.20 + 0.70 + 0.45 + 0.90
        = 6.60

Level: GOOD to HIGH (peak tension for key scene)
```

### Cozy Mystery - Investigation
```
Stakes: 4
Info Asymmetry: 6
Goal Alignment: 7 → Misalignment: 3
Trust: 4
Mystery: 7

TENSION = 0.10(4) + 0.40(6) + 0.15(3) + 0.15(4) + 0.20(7)
        = 0.40 + 2.40 + 0.45 + 0.60 + 1.40
        = 5.25

Level: GOOD (engaging investigation)
```

## Modifiers

**Apply AFTER base calculation** to specific components:

| Modifier | Affected Component | Multiplier |
|----------|-------------------|------------|
| **Mafia** | Power differential, Danger, Stakes | 1.3x, 1.5x, 1.2x |
| **Stalker** | Info asymmetry, Proximity, Power diff | 1.5x, 1.3x, 1.2x |
| **Captive** | Power differential, Proximity, Goal misalign | 1.5x, 0.5x, 1.3x |
| **Second Chance** | Trust, Vulnerability, Info asymmetry | 0.5x, 1.3x, 0.8x |

## Target Tension by Act

**Romance**:
- Act 1: 3-5 (building)
- Act 2: 4-6 (sustained)
- Black Moment: 7-8 (peak)
- Resolution: 2-4 (settling)

**Thriller**:
- Act 1: 4-6 (establishing threat)
- Act 2: 6-8 (sustained high)
- Climax: 8-10 (maximum)
- Resolution: 2-3 (aftermath)

**Mystery**:
- Act 1: 3-4 (mystery established)
- Act 2: 4-6 (investigation)
- Act 3: 5-7 (revelation)
- Resolution: 1-2 (explained)

## Pro Tips

- **Most scenes**: 3-7 range
- **Extremes rare**: 0-2 and 9-10 should be exceptional
- **Variety matters**: Vary which components drive tension
- **Waves not walls**: High → Relief → Higher (not constant high)
- **Genre calibration**: Same score feels different across genres
- **Track change**: Movement matters more than absolute values
