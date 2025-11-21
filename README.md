# Narrative Dimensions Analysis

A physics-inspired story analysis system that treats narrative as trajectories through multidimensional phase space. This Skill helps writers engineer tension, validate pacing, diagnose story problems, and ensure genre compliance.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

Stories exist as trajectories through N-dimensional space where each dimension represents an independent narrative variable (intimacy, trust, power, stakes, etc.). Tension and other dramatic qualities emerge from the configuration of these dimensions.

**Perfect for:**
- Analyzing story structure and pacing
- Engineering tension in specific scenes
- Validating character arcs and trajectories
- Diagnosing pacing issues and flat scenes
- Ensuring genre requirements are met
- Planning dimensional targets for chapters

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/narrative-dimensions-analysis.git
cd narrative-dimensions-analysis

# No dependencies required - uses Python standard library only
# Requires Python 3.7+
```

### Basic Usage

```bash
# Calculate tension for a scene
cd scripts
python3 calculate_tension.py

# Validate a story trajectory
python3 validate_trajectory.py

# Generate a full dimensional report
python3 generate_report.py
```

### Using as a Claude Skill

When using with Claude Code, simply specify:
1. **Content level**: concept, outline, chapter, book, or series
2. **Genre**: romance, dark-romance, thriller, mystery, sci-fi, fantasy, or hybrid
3. **What to analyze**: structure, pacing, tension, character arcs, or full diagnostic

Example:
```
Analyze my dark romance chapter for tension and pacing issues.
Current state: intimacy=6, trust=3, desire=9, stakes=8
```

## Core Concepts

### State Vector

Stories are represented as dimensional states:

```python
state = {
    'intimacy': 6,        # Emotional closeness (0-10)
    'trust': 4,           # Belief in reliability (0-10)
    'desire': 8,          # Attraction/pull (0-10)
    'power_differential': -2,  # Agency imbalance (-5 to +5)
    'stakes': 7,          # Magnitude of consequences (0-10)
    'vulnerability': 7,   # Emotional walls down (0-10)
    'goal_alignment': 5,  # Shared objectives (0-10)
    'info_asymmetry': 6,  # Knowledge gaps (0-10)
    'proximity': 3        # Physical closeness (0-10)
}
```

### Tension Formula

Tension emerges from dimensional configuration:

```
TENSION = w₁(stakes) + w₂(info_asymmetry) + w₃(goal_misalignment) +
          w₄(vulnerability - trust) + w₅(desire - proximity) + w₆(|power_diff|)
```

Genre-specific weights are defined in `references/genre-weights.json`.

### Key Principles

1. **Stories are trajectories** - Not events but dimensional movement
2. **Tension emerges** - From configuration, not arbitrary assignment
3. **Pacing is velocity** - How fast you move through phase space
4. **Genres constrain paths** - Not destinations but allowable trajectories
5. **Earned moments** - Require proper path integration, not jumps

## Documentation

### Main Documentation
- **[SKILL.md](SKILL.md)** - Complete system documentation with formulas, examples, and usage

### Reference Files
- **[genre-weights.json](references/genre-weights.json)** - Tension formula weights for each genre
- **[genre-configs.md](references/genre-configs.md)** - Genre conventions, requirements, and trajectory patterns
- **[catalyst-events.md](references/catalyst-events.md)** - Events that justify dimensional jumps (3+ points)
- **[diagnostic-patterns.md](references/diagnostic-patterns.md)** - Common story problems and solutions

## Scripts

### calculate_tension.py
Calculate tension from dimensional state and identify primary drivers.

```python
from scripts.calculate_tension import calculate_tension

tension = calculate_tension(
    state={'intimacy': 6, 'trust': 2, 'desire': 9, 'stakes': 8, ...},
    genre='romance',
    subgenre='dark',
    modifiers=['captive']
)

print(f"Tension: {tension['total_tension']}/10")
print(f"Primary driver: {tension['primary_driver']}")
```

### validate_trajectory.py
Validate story trajectories for proper progression.

```python
from scripts.validate_trajectory import TrajectoryValidator

validator = TrajectoryValidator(genre='romance')
report = validator.validate_trajectory(trajectory_list)

if not report['valid']:
    for error in report['errors']:
        print(f"ERROR: {error}")
```

### generate_report.py
Generate comprehensive dimensional analysis reports.

```python
from scripts.generate_report import DimensionalReport

reporter = DimensionalReport(
    title="Chapter 15",
    genre="dark-romance",
    content_level="chapter"
)

report = reporter.generate_full_report(
    current_state=state,
    trajectory=trajectory_history
)

print(report)
```

## Example Analyses

### Diagnosing a Flat Scene

**Problem:** Scene feels like nothing happens

**Dimensional Diagnosis:**
- All dimensions static (velocity = 0)
- Tension below 3

**Solution:**
```python
# Current: intimacy=5, trust=5, all static
# Fix: Move 2-3 dimensions
state = {
    'intimacy': 5,
    'vulnerability': 7,  # +2 (shares embarrassing story)
    'trust': 6,          # +1 (tests, rewards response)
    'proximity': 9       # Forced high (small table)
}
```

### Engineering High Tension

**Goal:** Create peak tension for black moment

**Target Configuration:**
```python
black_moment = {
    'stakes': 9,           # Maximum consequences
    'trust': 1,            # Shattered
    'goal_alignment': 2,   # Opposing
    'vulnerability': 8,    # Emotionally exposed
    'desire': 8,           # Maintains investment
    'proximity': 8         # Forced closeness
}

tension = calculate_tension(black_moment, genre='romance')
# Expected: ~8.5/10 tension
```

### Validating Romance Arc

**Genre Requirements:**
- Ending: intimacy ≥ 8, trust ≥ 7, goal_alignment ≥ 8
- No jumps > 3 points without catalyst
- Minimum 2 dimensions moving per chapter

```python
validator = TrajectoryValidator(genre='romance')
report = validator.validate_trajectory(chapter_states)

# Check for issues
if report['errors']:
    print("FAILED:", report['errors'])
```

## Supported Genres

### Romance Subgenres
- Contemporary (emotional journey, HEA)
- Dark Romance (power dynamics, high stakes)
- Paranormal (magic + romance)
- Enemies-to-Lovers (goal alignment slowest mover)
- Serial Killer Romance (moral ambiguity)

### Thriller Subgenres
- Psychological (trust unreliable, info asymmetry)
- Action (danger sustained, trust through action)

### Mystery Subgenres
- Cozy (info asymmetry primary, low danger)
- Noir (trust low, moral ambiguity)

### Fantasy Subgenres
- Epic (global stakes, power growth)
- Romantic Fantasy (magic affects all dimensions)

### Modifiers
- Mafia (power differential, danger)
- Captive (proximity forced, power extreme)
- Stalker (info asymmetry, proximity)
- Second Chance (trust deficit, shared history)

## Common Use Cases

### For Writers
- Plan chapter-by-chapter dimensional targets
- Diagnose why a scene feels flat
- Engineer specific emotional effects
- Validate character arc progression
- Check genre compliance before querying

### For Editors
- Identify pacing issues objectively
- Spot unearned character developments
- Verify tension curves
- Check genre expectations are met

### For Writing Groups
- Provide structured feedback
- Discuss story issues with shared vocabulary
- Track revision progress dimensionally

## Contributing

Contributions welcome! Areas for enhancement:
- Additional genre configurations
- More catalyst event patterns
- Visualization tools for trajectories
- CLI interface for scripts
- Additional diagnostic patterns

## License

MIT License - see LICENSE file for details

## Citation

If you use this system in academic work or publish analyses based on it:

```
Narrative Dimensions Analysis System (2024)
https://github.com/yourusername/narrative-dimensions-analysis
```

## Support

- **Issues**: Report bugs or request features via GitHub Issues
- **Documentation**: See [SKILL.md](SKILL.md) for complete reference
- **Examples**: Check the `scripts/` directory for usage examples

---

**Remember:** The same kiss hits differently at intimacy=2 vs intimacy=8. Context is configuration.
