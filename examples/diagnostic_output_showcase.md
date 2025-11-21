# Diagnostic Pattern Detection Showcase

This document shows examples of each diagnostic pattern the system can detect.

---

## 1. Melodrama Detection

**Pattern:** Too many dimensions at extremes (0-1 or 9-10)

### Example Trajectory
```json
{
  "beat": 5,
  "intimacy": 10,
  "trust": 0,
  "desire": 10,
  "stakes": 10,
  "danger": 10,
  "vulnerability": 0
}
```

### Diagnostic Output
```
⚠️  WARNING: MELODRAMA
    44% of dimensional values are at extremes (0-1 or 9-10)
    Locations: beats 3, 5, 7, 9
    Examples:
      Beat 5: trust=0, desire=10, stakes=10, danger=10
      Beat 7: intimacy=10, vulnerability=0, stakes=10

    FIX: Consider moderating values to 2-8 range for emotional realism.
         Extremes lose impact when overused. Reserve 0-1 and 9-10 for
         truly critical moments.
```

---

## 2. One-Note Tension

**Pattern:** Single component drives >70% of total tension

### Example Analysis
```
Current tension breakdown:
  stakes: 82%
  vulnerability_trust_gap: 8%
  desire_proximity_gap: 6%
  goal_misalignment: 4%
```

### Diagnostic Output
```
⚠️  WARNING: ONE_NOTE_TENSION
    Single component (stakes) drives 82.0% of total tension

    Breakdown:
      stakes: 82.0%
      vulnerability_trust_gap: 8.0%
      desire_proximity_gap: 6.0%
      goal_misalignment: 4.0%

    FIX: Diversify tension sources. Currently over-relying on stakes.
         Try increasing other dimensions to create multi-layered tension.
         Consider adding conflict through goal_misalignment, info_asymmetry,
         or vulnerability_trust_gap.
```

---

## 3. Flatline Detection

**Pattern:** Scenes where nothing moves (velocity ≈ 0)

### Example Trajectory
```json
[
  {"beat": 4, "intimacy": 5, "trust": 6, "desire": 7},
  {"beat": 5, "intimacy": 5, "trust": 6, "desire": 7}  // No change!
]
```

### Diagnostic Output
```
🚨 CRITICAL: FLATLINE
    Beat 5 has minimal dimensional movement (velocity: 0.00)

    FIX: Beat 5: Add character development or relationship shift.
         At least 2-3 dimensions should move by 1+ points per scene.
```

---

## 4. Teleportation Detection

**Pattern:** Dimensional jumps ≥3 without catalyst events

### Example Trajectory
```json
[
  {"beat": 2, "trust": 3},
  {"beat": 3, "trust": 9}  // Jumped 6 points!
]
```

### Diagnostic Output
```
🚨 CRITICAL: TELEPORTATION
    Beat 3: trust jumped 6.0 points without catalyst event
    From: 3.0 → To: 9.0

    FIX: Add a catalyst event at beat 3 to justify trust changing from
         3.0 to 9.0. Examples: revelation, betrayal, sacrifice, confrontation.
```

### With Catalyst Provided
```json
// catalysts.json
[
  {
    "beat": 3,
    "type": "sacrifice",
    "description": "Hero takes bullet for heroine",
    "dimensions": ["trust", "vulnerability"]
  }
]
```

**Result:** No teleportation warning for trust at beat 3! ✓

---

## 5. Sawtooth Overuse

**Pattern:** Dimension oscillates too frequently (>4 direction changes)

### Example Trajectory
```
trust: 3 → 7 → 4 → 8 → 3 → 7 → 4 → 8
       ↑   ↓   ↑   ↓   ↑   ↓   ↑
       1   2   3   4   5   6   7  = 7 direction changes!
```

### Diagnostic Output
```
⚠️  WARNING: SAWTOOTH_OVERUSE
    trust oscillates 7 times (pattern: [3, 7, 4, 8, 3, 7, 4, 8])

    FIX: Too much back-and-forth in trust can feel exhausting.
         Consider a smoother progression with 1-2 major setbacks instead
         of constant oscillation. Build momentum in one direction before reversing.
```

---

## 6. Stuck Arc Detection

**Pattern:** Critical dimensions that should move but don't

### Example Trajectory (Romance)
```
intimacy: 3 → 3 → 3 → 3 → 3 → 3 → 3 → 4
          60% plateau, total movement: 1 point
```

### Diagnostic Output
```
⚠️  WARNING: STUCK_ARC
    intimacy barely moves (60% plateau, total change: 1.0)

    FIX: intimacy is critical for romance but shows minimal progression.
         Plan a clear arc: start at 3, have setbacks/growth, end significantly
         higher (7-9 range). Current endpoint: 4.
```

---

## 7. Rushed Ending Detection

**Pattern:** Too many dimensions shift in final 10%

### Example Analysis
```
Earlier story avg velocity: 1.8
Final 10% avg velocity: 4.5 (2.5x faster!)
```

### Diagnostic Output
```
⚠️  WARNING: RUSHED_ENDING
    Final 2 beats move 2.5x faster than earlier story
    Final velocity: 4.50
    Earlier velocity: 1.80

    FIX: Ending feels rushed. Final velocity (4.5) is much higher than
         earlier pacing (1.8). Either:
         (1) Slow down - give resolutions more space, or
         (2) Increase earlier pacing - move faster in middle acts.
```

---

## 8. Missing Black Moment

**Pattern:** No crisis at 75-80% mark (genre-specific)

### Example Trajectory (Romance)
```
Beat 7 (70%): trust=7, goal_alignment=8
Beat 8 (80%): trust=7, goal_alignment=8  // No crisis!
Beat 9 (90%): trust=9, goal_alignment=9
```

### Diagnostic Output
```
🚨 CRITICAL: MISSING_BLACK_MOMENT
    No crisis/black moment detected in expected range (beats 7-8)

    Current trust/alignment in range:
      beat 7: trust=7, align=8
      beat 8: trust=7, align=8

    FIX: Romance needs a dark moment around 75-80% where trust/alignment
         crashes. This is where everything seems lost. Add a major betrayal,
         misunderstanding, or sacrifice that drops trust or goal_alignment to ≤3.
```

---

## 9. Weak Chemistry (Romance)

**Pattern:** Low chemistry indicators in first 40%

### Example Analysis
```
Beats 0-4 average:
  desire: 2.5
  vulnerability: 1.8
  info_asymmetry: 2.0
→ Chemistry score: 2.1 / 10 (too low!)
```

### Diagnostic Output
```
⚠️  WARNING: WEAK_CHEMISTRY
    Low chemistry in early story (score: 2.1/10)

    Current averages:
      desire: 2.5
      vulnerability: 1.8

    FIX: Chemistry = desire + vulnerability + mystery. In first 40% of story:
         (1) Build desire - attraction, longing, charged moments
         (2) Show vulnerability - characters revealing themselves
         (3) Maintain mystery - some info_asymmetry keeps intrigue
```

---

## 10. Info Dump Detection

**Pattern:** Info_asymmetry dropping >3 points in single beat

### Example Trajectory
```json
[
  {"beat": 1, "info_asymmetry": 9},
  {"beat": 2, "info_asymmetry": 3}  // Dropped 6 points!
]
```

### Diagnostic Output
```
⚠️  WARNING: INFO_DUMP
    Beat 2: info_asymmetry drops 6.0 points (9.0 → 3.0)

    FIX: Beat 2: Spread revelations across multiple scenes. Instead of
         explaining everything at once, reveal gradually through action,
         dialogue, and discovery. Drop info_asymmetry by 1-2 points per
         scene, not 6.
```

---

## 11. Power Imbalance Plateau

**Pattern:** Power differential stays extreme (±4 or ±5) for >50% of story

### Example Trajectory
```
power_differential: -5 → -5 → -5 → -5 → -5 → -5
                    Stays at -5 for 60% of story!
```

### Diagnostic Output
```
⚠️  WARNING: POWER_IMBALANCE_PLATEAU
    Power differential stays extreme (±4 or ±5) for 60% of story
    Affected beats: [0, 1, 2, 3, 4, 5, 6]

    FIX: Even in dark/captive romance, power should shift. Show:
         (1) Moments where lower-power character gains leverage
         (2) Vulnerability from higher-power character
         (3) Gradual equalization as relationship deepens
```

---

## 12. Positive Pattern: Tension Waves

**Pattern:** Tension rises and falls naturally

### Example Analysis
```
Tension values: [4.2, 5.8, 6.5, 3.1, 7.2, 8.9, 4.5]
Variance: 3.4 (good variation!)
```

### Diagnostic Output
```
💪 STRENGTH: TENSION_WAVES
    Good tension variation (variance: 3.4)

    Why it works: Tension rises and falls naturally, creating rhythm
                  and preventing fatigue
```

---

## 13. Positive Pattern: Strong Climax

**Pattern:** High velocity in final third

### Example Analysis
```
Average velocity (beats 1-10): 1.8
Final third velocity: 4.2 (2.3x average)
```

### Diagnostic Output
```
💪 STRENGTH: STRONG_CLIMAX
    Strong climax with high velocity (4.2)

    Why it works: Final act has significant movement - story building
                  to powerful conclusion
```

---

## 14. Positive Pattern: Character Growth

**Pattern:** Key dimensions show significant progression

### Example Trajectory
```
              Start → End   Change
intimacy:     1 → 8         +7  ✓
trust:        3 → 7         +4  ✓
vulnerability: 1 → 8        +7  ✓
desire:       2 → 9         +7  ✓
```

### Diagnostic Output
```
💪 STRENGTH: CHARACTER_GROWTH
    Strong character development: intimacy(+7), trust(+4), desire(+7),
                                  vulnerability(+7)

    Why it works: Characters show clear progression and transformation
```

---

## 15. Positive Pattern: Proper Black Moment

**Pattern:** Crisis at 75-80% with trust/alignment crash

### Example Trajectory
```
Beat 7 (75%): trust=2, goal_alignment=2  // CRASH!
```

### Diagnostic Output
```
💪 STRENGTH: PROPER_BLACK_MOMENT
    Black moment at beat 7 (75% through story)

    Why it works: Crisis moment properly positioned in 75-85% range
                  for maximum impact
```

---

## Complete Diagnostic Report Example

### Input
```bash
python3 scripts/diagnostic_patterns.py trajectory.json --genre romance
```

### Full Output
```
======================================================================
NARRATIVE DIAGNOSTIC REPORT
======================================================================
Genre: romance
Trajectory Length: 10 beats
Catalysts Provided: 0

🚨 CRITICAL ISSUES (Must Fix)
----------------------------------------------------------------------

1. FLATLINE
   Beat 2 has minimal dimensional movement (velocity: 0.00)
   FIX: Beat 2: Add character development or relationship shift.

2. TELEPORTATION
   Beat 3: trust jumped 6.0 points without catalyst event
   FIX: Add catalyst event to justify trust changing from 3.0 to 9.0.

3. MISSING_BLACK_MOMENT
   No crisis detected in expected range (beats 7-8)
   FIX: Add major betrayal/crisis that drops trust or alignment to ≤3.

⚠️  WARNINGS (Should Address)
----------------------------------------------------------------------

1. INFO_DUMP
   Beat 1: info_asymmetry drops 6.0 points (9.0 → 3.0)
   FIX: Spread revelations across multiple scenes.

2. SAWTOOTH_OVERUSE
   trust oscillates 5 times
   FIX: Smoother progression with 1-2 major setbacks instead.

💪 STRENGTHS (What's Working)
----------------------------------------------------------------------

1. CHARACTER_GROWTH
   Strong development: intimacy(+7), trust(+5), desire(+7)
   Why it works: Clear progression and transformation

2. TENSION_WAVES
   Good tension variation (variance: 2.8)
   Why it works: Natural rhythm prevents fatigue

======================================================================
OVERALL: 3 critical issues require immediate attention.
======================================================================
```

---

## Using Diagnostic Results

### Priority Levels

1. **Critical Issues** → Fix immediately
   - Story-breaking problems
   - Readers will notice and disengage
   - Required before publishing

2. **Warnings** → Address in revision
   - Weakens impact but not fatal
   - Professional polish
   - Beta readers may notice

3. **Strengths** → Maintain and build on
   - What's working well
   - Don't "fix" what's not broken
   - Model these patterns elsewhere

### Iterative Process

```
1. Run diagnostics
   ↓
2. Fix critical issues
   ↓
3. Re-run diagnostics (verify fixes worked)
   ↓
4. Address warnings
   ↓
5. Re-run diagnostics (final check)
   ↓
6. Verify strengths maintained
```

---

## Summary of All 15 Diagnostic Patterns

| # | Pattern | Type | Severity | Genre-Specific |
|---|---------|------|----------|----------------|
| 1 | Melodrama | Issue | Warning | All |
| 2 | One-Note Tension | Issue | Warning | All |
| 3 | Flatline | Issue | Critical | All |
| 4 | Teleportation | Issue | Critical | All |
| 5 | Sawtooth Overuse | Issue | Warning | All |
| 6 | Stuck Arc | Issue | Warning | All |
| 7 | Rushed Ending | Issue | Warning | All |
| 8 | Missing Black Moment | Issue | Critical | Romance |
| 9 | Weak Chemistry | Issue | Warning | Romance |
| 10 | Info Dump | Issue | Warning | All |
| 11 | Power Plateau | Issue | Warning | Dark Romance |
| 12 | Tension Waves | Strength | N/A | All |
| 13 | Strong Climax | Strength | N/A | All |
| 14 | Character Growth | Strength | N/A | All |
| 15 | Proper Black Moment | Strength | N/A | Romance |

---

## Next Steps

- See `DIAGNOSTIC_EXAMPLES.md` for detailed examples
- See `positive-patterns.md` for patterns to model
- Run `./run_diagnostics_demo.sh` for interactive demo
- Try diagnostics on your own trajectory!
