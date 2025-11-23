#!/usr/bin/env python3
"""
Author-Friendly Dimensional Analysis Report
Practical scene and chapter-level feedback in plain English.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class AuthorDimensionalReport:
    def __init__(self, title: str, genre: str, content_level: str = "chapter"):
        self.title = title
        self.genre = genre.lower().replace('-', '_')
        self.content_level = content_level
        self.timestamp = datetime.now().strftime("%B %d, %Y")

    def generate(self, current_state: Dict, trajectory: Optional[List[Dict]] = None) -> str:
        """Generate author-friendly dimensional report."""
        lines = []

        # Header
        lines.extend(self._create_header())
        lines.append("")

        # Current Scene/Chapter Snapshot
        lines.extend(self._current_snapshot(current_state))
        lines.append("")

        # Tension Analysis
        lines.extend(self._tension_analysis(current_state))
        lines.append("")

        # What's Happening Emotionally
        lines.extend(self._emotional_dynamics(current_state))
        lines.append("")

        # If trajectory provided, analyze movement
        if trajectory and len(trajectory) > 1:
            lines.extend(self._trajectory_analysis(trajectory))
            lines.append("")

            lines.extend(self._pacing_check(trajectory))
            lines.append("")

        # Suggestions
        lines.extend(self._suggestions(current_state, trajectory))
        lines.append("")

        # Footer
        lines.append("=" * 70)
        lines.append("These dimensions are lenses for analysis, not rules for writing.")
        lines.append("Trust your storytelling instincts!")
        lines.append("=" * 70)

        return "\n".join(lines)

    def _create_header(self) -> List[str]:
        return [
            "=" * 70,
            f"SCENE ANALYSIS: {self.title}",
            "=" * 70,
            f"Genre: {self.genre.replace('_', ' ').title()}",
            f"Level: {self.content_level.title()}",
            f"Analysis Date: {self.timestamp}",
            "",
            "This report looks at the emotional state and tension in your scene/chapter."
        ]

    def _current_snapshot(self, state: Dict) -> List[str]:
        lines = ["=" * 70, "CURRENT EMOTIONAL STATE", "=" * 70, ""]

        # Group dimensions for clarity
        relationship = {
            'Intimacy': state.get('intimacy', 0),
            'Trust': state.get('trust', 0),
            'Desire': state.get('desire', 0),
            'Vulnerability': state.get('vulnerability', 0)
        }

        external = {
            'Stakes': state.get('stakes', 0),
            'Physical Proximity': state.get('proximity', 5)
        }

        dynamics = {
            'Goal Alignment': state.get('goal_alignment', 5),
            'Power Balance': state.get('power_differential', 0),
            'Information Gaps': state.get('info_asymmetry', 0)
        }

        # Relationship state
        lines.append("Relationship Dimensions:")
        for dim, value in relationship.items():
            bar = self._make_bar(value)
            lines.append(f"  {dim:20s} {bar} {value:.1f}/10")
            lines.append(f"                      ({self._interpret_dimension(dim.lower(), value)})")
        lines.append("")

        # External factors
        lines.append("External Factors:")
        for dim, value in external.items():
            if 'proximity' in dim.lower():
                bar = self._make_bar(value)
                lines.append(f"  {dim:20s} {bar} {value:.1f}/10")
            else:
                bar = self._make_bar(value)
                lines.append(f"  {dim:20s} {bar} {value:.1f}/10")
            lines.append(f"                      ({self._interpret_dimension(dim.lower().replace(' ', '_'), value)})")
        lines.append("")

        # Dynamics
        lines.append("Character Dynamics:")
        for dim, value in dynamics.items():
            if 'power' in dim.lower():
                bar = self._make_power_bar(value)
                lines.append(f"  {dim:20s} {bar} {value:+.1f}")
                lines.append(f"                      ({self._interpret_power(value)})")
            else:
                bar = self._make_bar(value)
                lines.append(f"  {dim:20s} {bar} {value:.1f}/10")
                lines.append(f"                      ({self._interpret_dimension(dim.lower().replace(' ', '_'), value)})")
        lines.append("")

        return lines

    def _tension_analysis(self, state: Dict) -> List[str]:
        lines = ["=" * 70, "TENSION ANALYSIS", "=" * 70, ""]

        # Calculate tension components
        components = self._calculate_tension_components(state)
        total = sum(components.values())
        total = min(10, total)

        # Overall tension
        bar = self._make_bar(total)
        lines.append(f"Overall Tension: {bar} {total:.1f}/10")
        lines.append(f"Assessment: {self._tension_label(total)}")
        lines.append("")

        # Show what's creating tension
        lines.append("What's Creating Tension:")
        sorted_components = sorted(components.items(), key=lambda x: x[1], reverse=True)

        for component, value in sorted_components[:5]:
            if value > 0.5:
                lines.append(f"  • {component}: {value:.1f}")

        lines.append("")

        # Explain the tension
        lines.append("Why This Matters:")
        lines.append(self._explain_tension(state, total))

        return lines

    def _emotional_dynamics(self, state: Dict) -> List[str]:
        lines = ["=" * 70, "EMOTIONAL DYNAMICS", "=" * 70, ""]

        # Identify key gaps and tensions
        dynamics = []

        # Desire-proximity gap
        desire = state.get('desire', 0)
        proximity = state.get('proximity', 5)
        if desire - proximity > 3:
            dynamics.append(f"• HIGH YEARNING: Strong desire ({desire:.1f}) but low proximity ({proximity:.1f})")
            dynamics.append(f"  This creates longing and anticipation")

        # Vulnerability-trust gap
        vuln = state.get('vulnerability', 0)
        trust = state.get('trust', 0)
        if vuln - trust > 3:
            dynamics.append(f"• EMOTIONAL RISK: High vulnerability ({vuln:.1f}) with low trust ({trust:.1f})")
            dynamics.append(f"  Character is emotionally exposed and scared")

        # Intimacy-desire gap
        intimacy = state.get('intimacy', 0)
        if desire - intimacy > 4:
            dynamics.append(f"• SLOW BURN: High desire ({desire:.1f}) outpaces intimacy ({intimacy:.1f})")
            dynamics.append(f"  Perfect for sexual tension")

        # Goal misalignment
        goal_align = state.get('goal_alignment', 5)
        if goal_align < 4:
            dynamics.append(f"• CONFLICT: Characters want different things (alignment: {goal_align:.1f})")
            dynamics.append(f"  They're working against each other")

        # Power imbalance
        power_diff = state.get('power_differential', 0)
        if abs(power_diff) > 3:
            if power_diff > 0:
                dynamics.append(f"• POWER IMBALANCE: One character has more control (+{power_diff:.1f})")
            else:
                dynamics.append(f"• POWER IMBALANCE: One character is disadvantaged ({power_diff:.1f})")
            dynamics.append(f"  Creates dynamic tension and potential for arc")

        if dynamics:
            for dynamic in dynamics:
                lines.append(dynamic)
        else:
            lines.append("• Balanced state - no major tensions or gaps")
            lines.append("  This might work for quiet moments, but could feel flat")

        return lines

    def _trajectory_analysis(self, trajectory: List[Dict]) -> List[str]:
        lines = ["=" * 70, "STORY PROGRESSION", "=" * 70, ""]

        first = trajectory[0]
        last = trajectory[-1]

        # Track biggest changes
        changes = {}
        for dim in ['intimacy', 'trust', 'desire', 'vulnerability', 'goal_alignment', 'stakes']:
            if dim in first and dim in last:
                if isinstance(first[dim], (int, float)) and isinstance(last[dim], (int, float)):
                    change = last[dim] - first[dim]
                    if abs(change) >= 1:
                        changes[dim] = change

        if changes:
            lines.append("Biggest Changes:")
            sorted_changes = sorted(changes.items(), key=lambda x: abs(x[1]), reverse=True)
            for dim, change in sorted_changes:
                direction = "increased" if change > 0 else "decreased"
                arrow = "↑" if change > 0 else "↓"
                lines.append(f"  {arrow} {dim.title()}: {direction} by {abs(change):.1f} points")
                lines.append(f"     ({self._interpret_change(dim, change)})")
            lines.append("")
        else:
            lines.append("⚠ WARNING: No significant dimensional changes detected")
            lines.append("   Story may feel static - consider moving 2-3 dimensions")
            lines.append("")

        return lines

    def _pacing_check(self, trajectory: List[Dict]) -> List[str]:
        lines = ["=" * 70, "PACING CHECK", "=" * 70, ""]

        # Calculate movement per step
        movements = []
        for i in range(1, len(trajectory)):
            total_movement = 0
            for dim in trajectory[i]:
                if dim in trajectory[i-1]:
                    if isinstance(trajectory[i][dim], (int, float)) and isinstance(trajectory[i-1][dim], (int, float)):
                        total_movement += abs(trajectory[i][dim] - trajectory[i-1][dim])
            movements.append(total_movement)

        avg_movement = sum(movements) / len(movements) if movements else 0

        lines.append(f"Average Movement: {avg_movement:.1f} points per chapter")
        lines.append(self._movement_assessment(avg_movement))
        lines.append("")

        # Find stuck points
        stuck_points = [i+2 for i, m in enumerate(movements) if m < 1]
        if stuck_points:
            lines.append(f"⚠ Low Movement Detected:")
            lines.append(f"   Chapters/scenes: {', '.join(map(str, stuck_points[:5]))}")
            lines.append(f"   These sections may feel like they're dragging")
            lines.append("")

        # Find jumps
        big_jumps = [i+2 for i, m in enumerate(movements) if m > 10]
        if big_jumps:
            lines.append(f"⚡ Big Jumps Detected:")
            lines.append(f"   Chapters/scenes: {', '.join(map(str, big_jumps[:5]))}")
            lines.append(f"   Make sure these feel earned, not sudden")
            lines.append("")

        return lines

    def _suggestions(self, state: Dict, trajectory: Optional[List[Dict]]) -> List[str]:
        lines = ["=" * 70, "SUGGESTIONS", "=" * 70, ""]

        suggestions = []

        # Tension-based suggestions
        total_tension = sum(self._calculate_tension_components(state).values())
        total_tension = min(10, total_tension)

        if total_tension < 3:
            suggestions.append("LOW TENSION - Scene may feel flat:")
            suggestions.append("  • Increase stakes (what's at risk?)")
            suggestions.append("  • Create information asymmetry (secrets, lies)")
            suggestions.append("  • Widen desire-proximity gap (they want but can't have)")
            suggestions.append("  • Add goal conflict (they want different things)")
            suggestions.append("")

        elif total_tension > 8:
            suggestions.append("VERY HIGH TENSION - Can't sustain for long:")
            suggestions.append("  • Provide a moment of relief soon")
            suggestions.append("  • Resolve one source of tension")
            suggestions.append("  • Give characters a small win")
            suggestions.append("")

        # Specific dimensional suggestions
        desire = state.get('desire', 0)
        proximity = state.get('proximity', 5)
        intimacy = state.get('intimacy', 0)
        trust = state.get('trust', 0)
        vuln = state.get('vulnerability', 0)

        # Good tension setups
        if desire > 7 and proximity < 4:
            suggestions.append("✓ STRONG SETUP: High desire with low proximity")
            suggestions.append("  This creates excellent yearning and anticipation")
            suggestions.append("")

        if vuln > 6 and trust < 4:
            suggestions.append("✓ POWERFUL MOMENT: High vulnerability with low trust")
            suggestions.append("  Character is taking a huge risk - milk this!")
            suggestions.append("")

        # Missing elements
        if desire < 3 and intimacy < 3 and self.genre in ['romance', 'dark_romance']:
            suggestions.append("⚠ ROMANCE CONCERN: Both desire and intimacy are low")
            suggestions.append("  For romance, readers need to feel the connection")
            suggestions.append("")

        stakes = state.get('stakes', 0)
        if stakes < 3:
            suggestions.append("⚠ LOW STAKES: Not much feels at risk")
            suggestions.append("  Consider: What does the character stand to lose?")
            suggestions.append("")

        # Movement suggestions
        if trajectory and len(trajectory) > 1:
            last_movement = self._calculate_recent_movement(trajectory)
            if last_movement < 1:
                suggestions.append("⚠ STATIC SCENE: Little dimensional movement")
                suggestions.append("  Try moving 2-3 of these:")
                suggestions.append("  • Trust (up or down)")
                suggestions.append("  • Intimacy (closer or pull back)")
                suggestions.append("  • Stakes (raise the pressure)")
                suggestions.append("  • Information asymmetry (reveal or hide something)")
                suggestions.append("")

        if not suggestions:
            suggestions.append("✓ Scene is well-balanced!")
            suggestions.append("  Tension is appropriate and dynamics are working.")

        for suggestion in suggestions:
            lines.append(suggestion)

        return lines

    # Helper methods
    def _make_bar(self, value: float, max_val: float = 10) -> str:
        filled = int((value / max_val) * 10)
        return f"[{'█' * filled}{'░' * (10 - filled)}]"

    def _make_power_bar(self, value: float) -> str:
        center = 10
        position = int((value + 5) / 10 * 20)
        position = max(0, min(20, position))
        bar = ['░'] * 21
        bar[center] = '|'
        if 0 <= position <= 20:
            bar[position] = '█'
        return f"[{''.join(bar)}]"

    def _calculate_tension_components(self, state: Dict) -> Dict[str, float]:
        return {
            'High Stakes': state.get('stakes', 0) * 0.2,
            'Low Trust': max(0, 10 - state.get('trust', 5)) * 0.15,
            'Conflicting Goals': max(0, 10 - state.get('goal_alignment', 5)) * 0.15,
            'Vulnerability Gap': max(0, state.get('vulnerability', 0) - state.get('trust', 0)) * 0.2,
            'Desire-Proximity Gap': max(0, state.get('desire', 0) - state.get('proximity', 5)) * 0.2,
            'Power Imbalance': abs(state.get('power_differential', 0)) * 0.1,
            'Secrets/Unknown Info': state.get('info_asymmetry', 0) * 0.1
        }

    def _tension_label(self, tension: float) -> str:
        if tension < 3:
            return "Low - May lack engagement"
        elif tension < 5:
            return "Moderate - Good for quieter scenes"
        elif tension < 7:
            return "Good - Reader engaged"
        elif tension < 9:
            return "High - Peak tension moment"
        else:
            return "Extreme - Maximum intensity"

    def _explain_tension(self, state: Dict, total: float) -> str:
        if total < 3:
            return "This scene is calm and low-tension. Great for breathing room or setup, but extended low tension may lose reader engagement."
        elif total < 5:
            return "This scene has moderate tension. Good for relationship building or recovery scenes. Characters can connect without high drama."
        elif total < 7:
            return "This scene has solid tension. Readers will be engaged and wanting to know what happens next. This is a sweet spot."
        elif total < 9:
            return "This scene is high-tension. Use these sparingly - they're your big dramatic moments. Follow with relief/recovery."
        else:
            return "This scene is at maximum tension. Everything is at stake. You can't sustain this level for long - plan for resolution soon."

    def _interpret_dimension(self, dim: str, value: float) -> str:
        interpretations = {
            'intimacy': {
                (0, 2): "strangers/distant",
                (2, 4): "acquaintances",
                (4, 6): "friends/warming",
                (6, 8): "close/intimate",
                (8, 10): "deep bond"
            },
            'trust': {
                (0, 2): "no trust/betrayed",
                (2, 4): "suspicious/wary",
                (4, 6): "cautious trust",
                (6, 8): "solid trust",
                (8, 10): "complete faith"
            },
            'desire': {
                (0, 2): "no attraction",
                (2, 4): "mild interest",
                (4, 6): "growing attraction",
                (6, 8): "strong desire",
                (8, 10): "intense longing"
            },
            'vulnerability': {
                (0, 2): "walls up/guarded",
                (2, 4): "somewhat guarded",
                (4, 6): "cautiously open",
                (6, 8): "emotionally open",
                (8, 10): "fully exposed"
            },
            'stakes': {
                (0, 2): "low consequences",
                (2, 4): "mild consequences",
                (4, 6): "moderate risk",
                (6, 8): "high stakes",
                (8, 10): "everything at risk"
            },
            'goal_alignment': {
                (0, 2): "opposing goals",
                (2, 4): "conflicting aims",
                (4, 6): "partial overlap",
                (6, 8): "mostly aligned",
                (8, 10): "perfect alignment"
            },
            'proximity': {
                (0, 2): "far apart/separated",
                (2, 4): "distant",
                (4, 6): "moderate distance",
                (6, 8): "close by",
                (8, 10): "intimate proximity"
            },
            'info_asymmetry': {
                (0, 2): "both know same things",
                (2, 4): "small secrets",
                (4, 6): "moderate secrets",
                (6, 8): "major secrets",
                (8, 10): "huge information gap"
            }
        }

        if dim not in interpretations:
            return ""

        ranges = interpretations[dim]
        for (low, high), desc in ranges.items():
            if low <= value < high:
                return desc
        return list(ranges.values())[-1]

    def _interpret_power(self, value: float) -> str:
        if value > 3:
            return "strong power advantage"
        elif value > 1:
            return "slight advantage"
        elif value < -3:
            return "strong disadvantage"
        elif value < -1:
            return "slight disadvantage"
        else:
            return "balanced power"

    def _interpret_change(self, dim: str, change: float) -> str:
        if dim == 'intimacy':
            return "getting closer" if change > 0 else "pulling apart"
        elif dim == 'trust':
            return "building trust" if change > 0 else "trust breaking"
        elif dim == 'desire':
            return "attraction growing" if change > 0 else "attraction fading"
        elif dim == 'vulnerability':
            return "opening up" if change > 0 else "closing off"
        elif dim == 'stakes':
            return "pressure increasing" if change > 0 else "stakes lowering"
        elif dim == 'goal_alignment':
            return "finding common ground" if change > 0 else "goals diverging"
        else:
            return "increasing" if change > 0 else "decreasing"

    def _movement_assessment(self, avg: float) -> str:
        if avg < 1:
            return "⚠ Very low - Story may feel stuck"
        elif avg < 3:
            return "⚠ Below optimal - Consider more dimensional shifts"
        elif avg < 6:
            return "✓ Good pacing - Steady progression"
        elif avg < 10:
            return "✓ Excellent - Dynamic and engaging"
        else:
            return "⚠ Very fast - Make sure changes feel earned"

    def _calculate_recent_movement(self, trajectory: List[Dict]) -> float:
        if len(trajectory) < 2:
            return 0

        recent = trajectory[-2:]
        total = 0

        for dim in recent[0]:
            if dim in recent[1]:
                if isinstance(recent[0][dim], (int, float)) and isinstance(recent[1][dim], (int, float)):
                    total += abs(recent[1][dim] - recent[0][dim])

        return total


# Main execution
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python dimensional_author_report.py <state_file.json> [genre]")
        sys.exit(1)

    filepath = Path(sys.argv[1])
    genre = sys.argv[2] if len(sys.argv) > 2 else "romance"

    # Load state
    with open(filepath, 'r') as f:
        data = json.load(f)

    # Check if it's a trajectory or single state
    if isinstance(data, list):
        current_state = data[-1]
        trajectory = data
    else:
        current_state = data
        trajectory = None

    # Extract title
    title = filepath.stem.replace('_', ' ').title()

    # Generate report
    reporter = AuthorDimensionalReport(title, genre)
    report = reporter.generate(current_state, trajectory)

    print(report)
