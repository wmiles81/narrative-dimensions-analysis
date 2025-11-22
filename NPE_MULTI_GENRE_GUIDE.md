# NPE Multi-Genre Expansion Guide

## Overview

The Narrative Physics Engine (NPE) now supports **7 major genres** with genre-specific physics constraints. The same fundamental axes (IA/RA/EA/TA) apply across all genres, but each genre has different "laws of physics."

---

## Supported Genres

### 1. **Cozy Fantasy**
**Profile**: Low-stakes, warm, comforting stories
**Constraints**:
- Waveform amplitude: ≤ 1.5 (gentle emotional swings)
- Frequency: ≤ 0.3 (slow, unhurried)
- Entropy peak: ≤ 0.6 (minimal disorder)
- IA polarity flip: Required (wound → wholeness)
- Dark night: Required but not too deep (≤ -0.95)

**Example**: Verity (Library of Haldwick), Legends & Lattes

**Physics Summary**:
```
IA: -0.8 → +0.7 (slow healing arc)
RA: 160° → 60° (gradual relationship closure)
EA: Low baseline, single crisis spike allowed
TA: Must complete successfully
Entropy: Starts ~0.1, peaks briefly ~0.6, resolves ~0.05
```

---

### 2. **Psychological Thriller**
**Profile**: High-tension mental games and paranoia
**Constraints**:
- Waveform amplitude: ≤ 2.5 (intense swings allowed)
- Frequency: ≤ 0.6 (rapid oscillations create unease)
- Entropy peak: ≤ 1.0 (maximum disorder acceptable)
- IA polarity flip: Optional (can end wounded)
- Dark night: Very deep (can hit -1.0)

**Example**: Gone Girl, Sharp Objects, The Silent Patient

**Physics Summary**:
```
IA: Variable start → Variable end (can end negative)
RA: Highly volatile (trust constantly tested)
EA: High sustained pressure (0.6-0.9)
TA: May end ambiguous or pyrrhic
Entropy: Sustained high (0.7-0.9), can peak at 1.0
```

---

### 3. **Dark Romance**
**Profile**: Morally complex love with power dynamics
**Constraints**:
- Waveform amplitude: ≤ 2.0 (intense emotions)
- Frequency: ≤ 0.5 (oscillating conflict/intimacy)
- Entropy peak: ≤ 0.95 (near-maximum tension)
- IA polarity flip: Required but very late (80-95%)
- Power differential: Must oscillate throughout

**Example**: Captive Prince, ACOTAR, From Blood and Ash

**Physics Summary**:
```
IA: -0.9 → +0.6 (slow burn transformation)
RA: Oscillating orbit (power dynamics)
EA: High sustained stakes (0.5-0.8)
TA: Must achieve HEA/HFN (together despite darkness)
Entropy: High baseline (0.4), peaks near max (0.95)
```

**Special Feature**: Tracks power_differential as orbital perturbation

---

### 4. **Epic Fantasy**
**Profile**: Large-scale quest with heroic transformation
**Constraints**:
- Waveform amplitude: ≤ 2.0 (moderate swings)
- Frequency: ≤ 0.25 (slow, epic pacing)
- Entropy peak: ≤ 0.9 (high climax allowed)
- IA polarity flip: Required (ordinary → hero)
- Arc shape: Gradual ascent

**Example**: Lord of the Rings, Wheel of Time, Stormlight

**Physics Summary**:
```
IA: -0.7 → +0.9 (heroic transformation)
RA: 130° → 50° (fellowship bonds)
EA: Gradual escalation (0.4 → 1.0 at climax)
TA: Must complete quest (can be bittersweet)
Entropy: Steady rise to peak (0.3 → 0.9 → 0.1)
```

---

### 5. **Psychological Horror**
**Profile**: Fear-driven mental deterioration
**Constraints**:
- Waveform amplitude: ≤ 2.5 (extreme terror)
- Frequency: ≤ 0.7 (erratic, chaotic)
- Entropy peak: 1.0 (maximum disorder)
- IA polarity flip: Not required (can end broken)
- Trajectory: Often descending (gets worse)

**Example**: House of Leaves, Haunting of Hill House

**Physics Summary**:
```
IA: -0.5 → -1.0 (deteriorating sanity)
RA: Diverging orbits (isolation increases)
EA: Sustained maximum fear (0.7-0.95)
TA: May end unresolved
Entropy: High sustained (0.8-1.0), little resolution
```

**Special Feature**: Can have *negative* IA trajectory (protagonist breaks)

---

### 6. **Romantic Comedy**
**Profile**: Light, funny romance with misunderstandings
**Constraints**:
- Waveform amplitude: ≤ 1.3 (moderate, never too intense)
- Frequency: ≤ 0.4 (bouncy rhythm)
- Entropy peak: ≤ 0.6 (conflicts are light)
- IA polarity flip: Required (insecurity → confidence)
- Dark night: Required but shallow (-0.7 max)

**Example**: The Hating Game, Beach Read, Red White & Royal Blue

**Physics Summary**:
```
IA: -0.5 → +0.8 (light insecurity → joy)
RA: 160° → 30° (bumpy closure with banter)
EA: Low baseline (0.2), stakes feel smaller
TA: Must end together happily
Entropy: Low throughout (0.2-0.4), clean resolution
```

---

### 7. **Cozy Mystery**
**Profile**: Gentle detective stories with community
**Constraints**:
- Waveform amplitude: ≤ 1.2 (puzzle-solving, not life-threatening)
- Frequency: ≤ 0.3 (steady clue revelation)
- Entropy peak: ≤ 0.7 (moderate from mystery)
- IA polarity flip: Required (doubt → competence)
- Dark night: Optional

**Example**: Agatha Raisin, Thursday Murder Club

**Physics Summary**:
```
IA: -0.4 → +0.7 (self-doubt → mastery)
RA: 120° → 60° (community bonds strengthen)
EA: Info asymmetry primary driver (not danger)
TA: Mystery must be solved
Entropy: Moderate (0.3-0.5), clean resolution (0.05)
```

---

## How Genre Physics Differ

### Waveform Characteristics

| Genre | Amplitude | Frequency | Pattern |
|-------|-----------|-----------|---------|
| Cozy Fantasy | 1.0 | 0.15 | Smooth ascent |
| Psych Thriller | 2.0 | 0.5 | Irregular spikes |
| Dark Romance | 1.7 | 0.3 | Power oscillation |
| Epic Fantasy | 1.5 | 0.15 | Heroic journey |
| Horror | 2.0 | 0.5 | Descending spiral |
| Rom-Com | 1.0 | 0.25 | Bouncing ascent |
| Cozy Mystery | 0.9 | 0.2 | Mystery descending |

### Entropy Tolerance

| Genre | Baseline | Peak | Resolution |
|-------|----------|------|------------|
| Cozy Fantasy | 0.1 | 0.6 | 0.05 |
| Psych Thriller | 0.5 | 1.0 | 0.3 |
| Dark Romance | 0.4 | 0.95 | 0.2 |
| Epic Fantasy | 0.3 | 0.9 | 0.1 |
| Horror | 0.6 | 1.0 | 0.5 |
| Rom-Com | 0.2 | 0.6 | 0.05 |
| Cozy Mystery | 0.3 | 0.7 | 0.05 |

### IA Trajectory Requirements

| Genre | Must Cross Zero? | Final Range | Can End Negative? |
|-------|------------------|-------------|-------------------|
| Cozy Fantasy | ✓ Yes | +0.5 to +0.9 | No |
| Psych Thriller | No | -0.5 to +0.8 | Yes |
| Dark Romance | ✓ Yes | +0.3 to +0.8 | No |
| Epic Fantasy | ✓ Yes | +0.6 to +1.0 | No |
| Horror | No | -1.0 to 0.0 | Yes |
| Rom-Com | ✓ Yes | +0.6 to +0.9 | No |
| Cozy Mystery | ✓ Yes | +0.4 to +0.8 | No |

---

## Usage Examples

### Validate Genre Compliance

```bash
# Check if trajectory matches cozy fantasy physics
python scripts/npe_analyzer.py trajectory.json --genre cozy_fantasy

# Check dark romance compliance
python scripts/npe_analyzer.py trajectory.json --genre dark_romance

# Check thriller compliance
python scripts/npe_analyzer.py trajectory.json --genre psychological_thriller
```

### Typical Output

```
======================================================================
GENRE CONSTRAINT VALIDATION
======================================================================

Genre: dark_romance
Description: Morally complex love stories with high stakes and power dynamics

Valid: ✓ YES

✓ Trajectory complies with dark_romance physics constraints
```

Or with violations:

```
Valid: ✗ NO

🚨 VIOLATIONS (2):
  - Waveform amplitude 1.2 exceeds dark_romance expectations (should be ~1.7)
    Dark romance needs intense emotional swings
  - No power differential oscillations detected
    Dark romance requires power dynamics to shift

⚠️  WARNINGS (1):
  - Average entropy 0.3 below dark_romance sustained (0.4-0.7)
```

---

## Genre Blending

The system supports blending multiple genres:

### Compatible Blends

**Cozy Fantasy + Romance**
- Use cozy constraints (dominant)
- Romance subplot enhances but doesn't override cozy feel

**Thriller + Romance (Romantic Suspense)**
- Use max of both constraints
- Both tension systems operate

**Dark Romance + Fantasy**
- Weighted average of constraints
- Dark romance dynamics in fantasy world

**Horror + Mystery**
- Use horror constraints (dominant)
- Mystery structure with horror atmosphere

### Blending Strategy

```python
# In code (future implementation):
from npe_genre_profiles import blend_genres

constraints = blend_genres([
    ('cozy_fantasy', 0.7),
    ('romance', 0.3)
])
```

---

## Key Insights

### 1. **Same Axes, Different Laws**
All genres use IA/RA/EA/TA, but physics constraints vary wildly:
- Horror can have descending IA (protagonist breaks)
- Cozy must have ascending IA (protagonist heals)
- Thriller allows extreme oscillations
- Romance requires polarity flip

### 2. **Entropy as Genre Signature**
- **Cozy genres**: Low entropy (0.1-0.6)
- **Intense genres**: High entropy (0.6-1.0)
- **Resolution patterns vary**: Cozy → 0.05, Horror → 0.5

### 3. **Waveform = Genre Feel**
- Low amplitude + low frequency = cozy/gentle
- High amplitude + high frequency = thriller/intense
- Oscillating patterns = dark romance power dynamics

### 4. **Dark Night Universality**
Almost all genres require a dark night, but:
- **Depth varies**: Cozy (-0.7), Horror (-1.0)
- **Timing varies**: Cozy (70-75%), Thriller (80-85%)
- **Resolution varies**: Cozy (full healing), Horror (may not recover)

---

## Practical Application

### For Writers

**Planning Phase**:
1. Choose your genre from NPE profiles
2. Note amplitude/frequency/entropy constraints
3. Plan IA trajectory within genre bounds
4. Map required thresholds (dark night, polarity flip)

**Drafting Phase**:
1. Track dimensions chapter-by-chapter
2. Calculate current entropy
3. Ensure waveform stays within genre constraints

**Revision Phase**:
1. Run NPE analyzer with genre flag
2. Check for violations
3. Adjust trajectory to comply

### Example: Converting Cozy → Thriller

If your cozy fantasy feels flat, check if you want thriller:

**Cozy Physics**:
- Amplitude: 1.0 → 1.5
- Entropy: 0.3 → 0.6
- IA: -0.8 → +0.7

**Thriller Physics**:
- Amplitude: 1.5 → 2.5
- Entropy: 0.5 → 1.0
- IA: -0.7 → -0.5 (can end wounded)

**Changes Needed**:
- Increase stakes throughout (raises entropy)
- Add more oscillations (raises frequency)
- Deepen dark night (-0.7 → -0.95)
- Can abandon polarity flip requirement

---

## Available Tools

### Genre Profiles Reference
- File: `references/npe_genre_profiles.py`
- Contains all 7 genre constraint definitions
- Includes examples and usage guide

### NPE Analyzer (Enhanced)
- File: `scripts/npe_analyzer.py`
- Now supports `--genre` flag
- Validates against genre-specific constraints
- Reports violations and warnings

### Genre Compliance Checking
```bash
# See available genres
python scripts/npe_analyzer.py

# Analyze with genre validation
python scripts/npe_analyzer.py trajectory.json --genre [GENRE]
```

---

## Conclusion

The NPE framework is now **fully multi-genre**, supporting everything from gentle cozy fantasy to intense psychological horror. The same physics concepts (axes, orbits, waveforms, entropy) apply universally, but each genre defines its own "laws of physics."

**Key Takeaway**: Genre isn't about content—it's about physics constraints. A cozy mystery and a psychological thriller both track IA/RA/EA/TA, but cozy constrains amplitude to 1.2 while thriller allows 2.5. Same tools, different rules.
