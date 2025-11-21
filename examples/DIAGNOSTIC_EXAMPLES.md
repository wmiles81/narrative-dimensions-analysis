# Diagnostic System Examples

This document demonstrates the narrative diagnostic system with real examples.

## Overview

The diagnostic system analyzes story trajectories to detect:
- **Critical Issues** - Must fix (story-breaking problems)
- **Warnings** - Should address (weakens impact)
- **Strengths** - What's working well

## Example 1: Problematic Romance Trajectory

### Input Trajectory

```json
{
  "genre": "romance",
  "trajectory": [
    {
      "beat": 0,
      "description": "Meet-cute",
      "intimacy": 1,
      "trust": 3,
      "desire": 2,
      "stakes": 10,
      "info_asymmetry": 9
    },
    {
      "beat": 1,
      "description": "First connection (info dump!)",
      "intimacy": 2,
      "trust": 3,
      "desire": 5,
      "info_asymmetry": 3  // JUMPED 6 points!
    },
    {
      "beat": 2,
      "description": "Static scene - nothing moves",
      "intimacy": 2,  // No change
      "trust": 3,     // No change
      "desire": 5     // No change
      // ... all dimensions same
    }
  ]
}
```

### Detected Issues

#### Critical Issues (13)

1. **Flatline** - Beat 2
   - Velocity: 0.00 (nothing moved)
   - Fix: Add character development or relationship shift

2. **Teleportation** - Beat 1: info_asymmetry
   - Jumped 6 points (9 → 3) without catalyst
   - Fix: Add catalyst or spread revelation across multiple beats

3. **Teleportation** - Beat 3: trust
   - Jumped 6 points (3 → 9) without catalyst
   - Fix: Add vulnerability moment or sacrifice to justify

4-12. **Multiple Trust Jumps** - Beats 4-7
   - Trust oscillates wildly: 9 → 4 → 8 → 3 → 9
   - Creates sawtooth pattern (exhausting for readers)

13. **Missing Black Moment**
   - No crisis at 75-80% mark
   - Romance requires dark moment where trust/alignment crashes

#### Warnings (1)

1. **Info Dump** - Beat 1
   - Info_asymmetry drops 6 points in single beat
   - Suggests exposition dump vs gradual revelation

#### Strengths (1)

1. **Character Growth**
   - Strong development: intimacy +8, trust +7, desire +8
   - Characters show clear transformation

### How to Fix

**Priority 1: Fix Teleportation**
```json
// Add catalyst events
{
  "beat": 1,
  "catalyst": {
    "type": "forced_proximity",
    "description": "Trapped together, must share information to survive",
    "dimensions": ["info_asymmetry", "desire"]
  }
}

{
  "beat": 3,
  "catalyst": {
    "type": "sacrifice",
    "description": "Hero risks career to help heroine",
    "dimensions": ["trust", "vulnerability"]
  }
}
```

**Priority 2: Add Black Moment**
```json
// Insert at beat 7-8 (75-80%)
{
  "beat": 7,
  "description": "Betrayal revealed - everything falls apart",
  "trust": 2,           // Crash from 7+
  "goal_alignment": 2,  // Crash from 6+
  "stakes": 9          // Raise consequences
}
```

**Priority 3: Smooth Sawtooth**
- Instead of: 3 → 9 → 4 → 8 → 3 → 9
- Use: 3 → 4 → 5 → 6 → 3 (black moment) → 7
- One major break, steady rebuild

---

## Example 2: Well-Structured Romance

### Input Trajectory

```json
{
  "genre": "romance",
  "trajectory": [
    {
      "beat": 0,
      "intimacy": 1,
      "trust": 3,
      "desire": 4,
      "vulnerability": 2
    },
    {
      "beat": 1,
      "intimacy": 2,
      "trust": 4,
      "desire": 6,
      "vulnerability": 3
    },
    // ... gradual progression
    {
      "beat": 7,
      "description": "BLACK MOMENT",
      "intimacy": 5,
      "trust": 2,      // CRASH!
      "desire": 8,
      "vulnerability": 9,
      "goal_alignment": 2  // CRASH!
    },
    {
      "beat": 9,
      "description": "HEA",
      "intimacy": 8,
      "trust": 8,
      "desire": 9,
      "goal_alignment": 9
    }
  ],
  "catalysts": [
    {
      "beat": 3,
      "type": "first_kiss",
      "dimensions": ["intimacy", "desire"]
    },
    {
      "beat": 7,
      "type": "betrayal_revelation",
      "dimensions": ["trust", "goal_alignment"]
    }
  ]
}
```

### Detected Issues

#### Critical Issues (0)
- None! Clean trajectory

#### Warnings (0)
- None!

#### Strengths (2)

1. **Character Growth**
   - Intimacy: +7, Trust: +5, Desire: +5
   - Clear transformation arc

2. **Proper Black Moment**
   - Crisis at beat 7 (70% through story)
   - Positioned in optimal 75-85% range
   - Trust crashes from 7 to 2

---

## Common Diagnostic Patterns

### Melodrama
**Symptom:** >30% of dimensional values at extremes (0-1 or 9-10)

**Example:**
```json
Beat 5: stakes=10, trust=0, danger=10, desire=10
```

**Fix:** Moderate to 2-8 range for realism. Reserve extremes for crisis moments.

---

### One-Note Tension
**Symptom:** Single component drives >70% of total tension

**Example:**
```
Tension Breakdown:
- stakes: 82%
- vulnerability_trust_gap: 8%
- desire_proximity_gap: 6%
- other: 4%
```

**Fix:** Diversify tension sources. Add interpersonal conflict, mystery, desire.

---

### Rushed Ending
**Symptom:** Final 10% has 2x+ velocity of earlier story

**Example:**
```
Act 1-2 avg velocity: 1.8
Final beats velocity: 4.5  (2.5x faster!)
```

**Fix:** Either spread resolution across more beats, or increase earlier pacing.

---

### Weak Chemistry (Romance)
**Symptom:** Low chemistry score in first 40%

**Formula:** `chemistry = (desire × 0.4) + (vulnerability × 0.4) + (min(info_asym, 5) × 0.2)`

**Example:**
```
Beats 0-4 average:
- desire: 2.5
- vulnerability: 1.8
- info_asymmetry: 2.0
→ Chemistry score: 2.1 (too low!)
```

**Fix:**
- Raise desire (attraction, charged moments)
- Show vulnerability (fears, stakes, opening up)
- Maintain mystery (some info_asymmetry)

---

### Power Plateau (Dark Romance)
**Symptom:** Power differential stays at ±4 or ±5 for >50% of story

**Example:**
```
Beats 0-8: power_differential = -5 (constant)
```

**Fix:** Show power exchange
- Give lower-power character leverage moments
- Show higher-power character vulnerability
- Move toward equality as trust builds

---

## Using the Diagnostic System

### Basic Usage

```bash
# Run diagnostics
python3 scripts/diagnostic_patterns.py trajectory.json --genre romance

# Save report to file
python3 scripts/diagnostic_patterns.py trajectory.json --genre romance --report output.txt

# Include catalyst events
python3 scripts/diagnostic_patterns.py trajectory.json --genre romance --catalysts events.json
```

### Trajectory Format

```json
{
  "trajectory": [
    {
      "beat": 0,
      "chapter": "1-3",
      "description": "Optional description",
      "intimacy": 1,
      "trust": 3,
      "desire": 4
      // ... other dimensions
    }
  ]
}
```

### Catalyst Format

```json
[
  {
    "beat": 3,
    "type": "sacrifice",
    "description": "Hero saves heroine's life",
    "dimensions": ["trust", "vulnerability"]
  }
]
```

### Interpreting Results

**Critical Issues:**
- Must fix before publishing
- Story-breaking problems
- Readers will notice and disengage

**Warnings:**
- Should address
- Weakens impact but not fatal
- Professional polish

**Strengths:**
- What's working well
- Patterns to maintain
- Build on these

---

## Diagnostic Checklist

Run diagnostics at these stages:

1. **Outline Phase**
   - Check genre compliance
   - Verify black moment placement
   - Ensure character arc trajectory

2. **First Draft Complete**
   - Full diagnostic sweep
   - Fix critical issues
   - Note warnings for revision

3. **Revision Pass**
   - Re-run after major changes
   - Verify fixes worked
   - Address remaining warnings

4. **Final Polish**
   - Confirm no critical issues
   - All warnings resolved
   - Strengths maintained

---

## Integration with Other Tools

### Workflow

1. **Plan Trajectory**
   ```bash
   # Create initial dimensional plot
   vim trajectory.json
   ```

2. **Run Diagnostics**
   ```bash
   python3 scripts/diagnostic_patterns.py trajectory.json --genre romance
   ```

3. **Calculate Tension**
   ```bash
   python3 scripts/calculate_tension.py trajectory.json --genre romance
   ```

4. **Validate Genre Compliance**
   ```bash
   python3 scripts/validate_trajectory.py trajectory.json --genre romance
   ```

5. **Iterate**
   - Fix issues
   - Re-run diagnostics
   - Refine until clean

---

## Advanced Usage

### Custom Genre Requirements

Edit `validate_trajectory.py` to add custom genre rules:

```python
'my_genre': {
    'ending': {'custom_dim': 8},
    'sustained': {'other_dim': 5},
    'max_jump': 3
}
```

### Custom Diagnostic Patterns

Add to `NarrativeDiagnostics` class:

```python
def detect_custom_pattern(self) -> Optional[Dict]:
    """Detect your custom story pattern."""
    # Your detection logic
    if pattern_detected:
        return {
            'issue': 'custom_pattern',
            'severity': 'warning',
            'description': 'What was detected',
            'fix': 'How to fix it'
        }
    return None
```

Register in `run_full_diagnostic()`:

```python
custom = self.detect_custom_pattern()
if custom:
    results['warnings'].append(custom)
```

---

## Troubleshooting

### "No issues detected but story feels off"

1. Check positive patterns - are strengths present?
2. Review tension waves - is there variation?
3. Analyze pacing - is velocity consistent?
4. Consider reader expectations for genre

### "Too many warnings"

1. Prioritize critical issues first
2. Group related warnings (e.g., all trust jumps)
3. Fix underlying cause (e.g., add catalysts)
4. Some warnings OK in early drafts

### "Diagnostic contradicts my vision"

- Diagnostics are guidelines, not rules
- Breaking patterns intentionally is valid
- Understand WHY pattern exists before breaking
- Test with beta readers if uncertain

---

## References

- See `references/positive-patterns.md` for good patterns to model
- See `references/genre-weights.json` for tension configurations
- See example trajectories in `examples/` directory
