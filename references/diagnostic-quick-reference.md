# Diagnostic Patterns - Quick Reference

## Critical Issues (Must Fix)

| Pattern | Threshold | Impact | Quick Fix |
|---------|-----------|--------|-----------|
| **Flatline** | Velocity < 0.5 | Reader disengages | Move 2-3 dimensions |
| **Teleportation** | Jump ≥ 3 pts | Feels unearned | Add catalyst |
| **Missing Black Moment** | No crisis @ 75-80% | Predictable | Drop trust/align to ≤3 |

## Warnings (Should Address)

| Pattern | Threshold | Impact | Quick Fix |
|---------|-----------|--------|-----------|
| **Melodrama** | >30% at extremes | Emotional fatigue | Moderate to 2-8 |
| **One-Note** | >70% one source | One-dimensional | Diversify tension |
| **Sawtooth** | >4 reversals | Exhausting | 1-2 reversals max |
| **Stuck Arc** | >60% plateau | No growth | Clear progression |
| **Rushed End** | Final 10% 2x faster | Unsatisfying | Spread or speed up |
| **Weak Chemistry** | Score < 3 | No investment | Desire + vuln + mystery |
| **Info Dump** | Drop > 3 pts | Exposition | 1-2 pts/scene |
| **Power Plateau** | >50% extreme | Toxic dynamic | Show exchange |

## Positive Patterns (Maintain)

| Pattern | Indicator | Why Good |
|---------|-----------|----------|
| **Tension Waves** | Variance > 2.0 | Natural rhythm |
| **Strong Climax** | High final velocity | Earned payoff |
| **Character Growth** | ≥3 pt progression | Clear transformation |
| **Proper Black Moment** | Crisis @ 75-85% | Maximum impact |

## Formulas

### Chemistry Score (Romance)
```
chemistry = (desire × 0.4) + (vulnerability × 0.4) + (min(info_asym, 5) × 0.2)

Good: > 4.0 in first 40%
Weak: < 3.0
```

### Velocity
```
velocity = sum(|dimension_changes|) / dimension_count

Flatline: < 0.5
Normal: 1.0 - 3.0
High: > 3.0
```

### Tension Components
```
See genre-weights.json for specific weights

One-note if any component > 70%
Good: All components 15-40%
```

## Usage Cheat Sheet

```bash
# Basic
python3 scripts/diagnostic_patterns.py FILE.json --genre GENRE

# With catalysts
python3 scripts/diagnostic_patterns.py FILE.json --genre GENRE --catalysts CAT.json

# Save report
python3 scripts/diagnostic_patterns.py FILE.json --genre GENRE --report OUT.txt
```

## Input Format

```json
{
  "trajectory": [
    {
      "beat": 0,
      "intimacy": 1,
      "trust": 3,
      "desire": 4
    }
  ]
}
```

## Catalyst Format

```json
[
  {
    "beat": 3,
    "type": "sacrifice",
    "dimensions": ["trust"]
  }
]
```

## Priority Guide

1. **Fix Critical** - Story-breaking
2. **Address Warnings** - Professional polish
3. **Maintain Strengths** - What works
4. **Re-run Diagnostics** - Verify fixes

## Common Fixes by Issue

| Issue | Typical Cause | Fix |
|-------|---------------|-----|
| Teleportation | No catalyst | Add revelation/sacrifice/confrontation |
| Flatline | Static scene | Change 2-3 dimensions by 1+ points |
| Missing Black Moment | Smooth sailing | Add betrayal/crisis @ beat 75-80% |
| Info Dump | Explaining backstory | Spread across 3-4 beats |
| Sawtooth | Artificial conflict | Build → break → rebuild (once) |
| Weak Chemistry | No attraction | Raise desire + vulnerability early |
| One-Note | Over-relying on stakes | Add interpersonal tension |
| Melodrama | Everything extreme | Moderate most values to 3-7 |

## Genre-Specific Checks

### Romance
- ✓ Black moment @ 75-80%
- ✓ Chemistry in first 40%
- ✓ Trust/intimacy growth
- ✓ HEA ending (trust ≥7, intimacy ≥8)

### Dark Romance
- ✓ Power exchange pattern
- ✓ Black moment (can be darker)
- ✓ Stakes/danger sustained
- ✓ Ending (intimacy ≥7, trust ≥6)

### Thriller
- ✓ Sustained danger/stakes
- ✓ Info asymmetry progression
- ✓ High final act velocity
- ✓ Resolution (danger ≤3)

## Quick Diagnostic Interpretation

```
🚨 CRITICAL (Red flags)
   → Fix before anything else
   → Story won't work without fixes

⚠️  WARNINGS (Yellow flags)
   → Address in revision
   → Weakens but not fatal

💪 STRENGTHS (Green flags)
   → Keep doing this
   → Model elsewhere
```

## When to Run Diagnostics

- [ ] After outline (structural check)
- [ ] After first draft (full analysis)
- [ ] After revisions (verify fixes)
- [ ] Before beta readers (final polish)

## Red Flags Requiring Immediate Attention

- Multiple teleportations in same beat
- Entire story at melodrama extremes
- No positive patterns detected
- Missing genre-required patterns
- >50% of beats are flatlines

## Green Flags Indicating Strong Trajectory

- All critical checks pass
- ≤3 warnings total
- Multiple positive patterns
- Chemistry score >5 (romance)
- Proper act structure pacing

---

**Remember:** Diagnostics are guidelines, not rigid rules. Use them to improve craft while maintaining your unique voice.
