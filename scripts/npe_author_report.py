#!/usr/bin/env python3
"""
Author-Friendly NPE Report Generator
Translates physics analysis into practical writing advice.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime

# Import genre profiles
sys.path.insert(0, str(Path(__file__).parent.parent / 'references'))
try:
    from npe_genre_profiles import NPE_GENRE_PROFILES
except ImportError:
    NPE_GENRE_PROFILES = {}


class AuthorNPEReport:
    def __init__(self, title: str, genre: str, total_chapters: int):
        self.title = title
        self.genre = genre.lower().replace(' ', '_').replace('-', '_')
        self.total_chapters = total_chapters
        self.timestamp = datetime.now().strftime("%B %d, %Y")

    def generate(self, trajectory: List[Dict]) -> str:
        """Generate author-friendly NPE report."""
        lines = []

        # Header
        lines.extend(self._create_header())
        lines.append("")

        # Quick Summary
        lines.extend(self._executive_summary(trajectory))
        lines.append("")

        # Character Journey
        lines.extend(self._character_arc_analysis(trajectory))
        lines.append("")

        # Relationship Arc
        lines.extend(self._relationship_analysis(trajectory))
        lines.append("")

        # Pacing & Story Flow
        lines.extend(self._pacing_analysis(trajectory))
        lines.append("")

        # Genre Fit
        lines.extend(self._genre_validation(trajectory))
        lines.append("")

        # Critical Moments
        lines.extend(self._key_moments(trajectory))
        lines.append("")

        # What's Working
        lines.extend(self._strengths(trajectory))
        lines.append("")

        # Opportunities to Strengthen
        lines.extend(self._improvements(trajectory))
        lines.append("")

        # Specific Fixes
        lines.extend(self._actionable_fixes(trajectory))
        lines.append("")

        # Footer
        lines.append("=" * 70)
        lines.append("This analysis is here to help, not dictate. Trust your storytelling")
        lines.append("instincts - these are suggestions based on genre patterns, not rules.")
        lines.append("=" * 70)

        return "\n".join(lines)

    def _create_header(self) -> List[str]:
        return [
            "=" * 70,
            f"STORY ARC ANALYSIS: {self.title}",
            "=" * 70,
            f"Genre: {self.genre.replace('_', ' ').title()}",
            f"Length: {self.total_chapters} chapters",
            f"Analysis Date: {self.timestamp}",
            "",
            "This report looks at your character's emotional journey and relationship",
            "arc to help you spot pacing issues, identify key moments, and ensure",
            f"your story matches {self.genre.replace('_', ' ')} reader expectations.",
        ]

    def _executive_summary(self, trajectory: List[Dict]) -> List[str]:
        lines = ["=" * 70, "QUICK SUMMARY", "=" * 70, ""]

        # Get IA progression
        ia_values = [s.get('IA', 0) for s in trajectory]
        ia_start = ia_values[0]
        ia_end = ia_values[-1]
        ia_darkest = min(ia_values)
        darkest_chapter = ia_values.index(ia_darkest) + 1

        # Get RA progression
        ra_values = [s.get('RA_orbit', 180) for s in trajectory]
        ra_start = ra_values[0]
        ra_end = ra_values[-1]

        # Overall arc health
        health_score = self._calculate_health_score(trajectory)

        lines.append(f"Overall Arc Health: {health_score}/100")
        lines.append(self._health_bar(health_score))
        lines.append("")

        # Character journey summary
        lines.append("Character Journey:")
        lines.append(f"  • Starts: {self._describe_internal_state(ia_start)}")
        lines.append(f"  • Darkest moment: Chapter {darkest_chapter} ({self._describe_internal_state(ia_darkest)})")
        lines.append(f"  • Ends: {self._describe_internal_state(ia_end)}")
        lines.append("")

        # Relationship summary
        lines.append("Relationship Arc:")
        lines.append(f"  • Starts: {self._describe_relationship_distance(ra_start)}")
        lines.append(f"  • Ends: {self._describe_relationship_distance(ra_end)}")
        lines.append(f"  • Distance closed: {ra_start - ra_end}°")
        lines.append("")

        # Quick verdict
        verdict = self._quick_verdict(trajectory)
        lines.append(f"Quick Take: {verdict}")

        return lines

    def _character_arc_analysis(self, trajectory: List[str]) -> List[str]:
        lines = ["=" * 70, "CHARACTER'S EMOTIONAL ARC", "=" * 70, ""]

        ia_values = [s.get('IA', 0) for s in trajectory]

        # Track the journey
        lines.append("The Journey from Wounded to Healed:")
        lines.append("")

        # Visualize IA progression
        lines.extend(self._visualize_ia_arc(trajectory))
        lines.append("")

        # Find key moments
        darkest_idx = ia_values.index(min(ia_values))
        darkest_chapter = darkest_idx + 1

        # Check for polarity flip
        flip_chapter = None
        for i in range(1, len(ia_values)):
            if ia_values[i-1] < 0 and ia_values[i] >= 0:
                flip_chapter = i + 1
                break

        lines.append("Key Emotional Moments:")
        lines.append(f"  • Chapter {darkest_chapter}: DARK NIGHT - Lowest emotional point")
        lines.append(f"    Your character feels: {self._describe_internal_state(min(ia_values))}")
        lines.append("")

        if flip_chapter:
            lines.append(f"  • Chapter {flip_chapter}: TURNING POINT")
            lines.append(f"    Your character shifts from wounded to healing")
            lines.append(f"    This is where hope returns")
        else:
            lines.append(f"  ⚠ No healing moment detected - character stays wounded")

        return lines

    def _relationship_analysis(self, trajectory: List[Dict]) -> List[str]:
        lines = ["=" * 70, "RELATIONSHIP ARC", "=" * 70, ""]

        ra_values = [s.get('RA_orbit', 180) for s in trajectory]

        # Visualize relationship distance
        lines.extend(self._visualize_relationship_arc(trajectory))
        lines.append("")

        # Calculate key metrics
        start_distance = ra_values[0]
        end_distance = ra_values[-1]
        closest = min(ra_values)
        furthest = max(ra_values)

        total_closure = start_distance - end_distance

        lines.append("Relationship Distance:")
        lines.append(f"  • Starting distance: {self._describe_relationship_distance(start_distance)}")
        lines.append(f"  • Ending distance: {self._describe_relationship_distance(end_distance)}")
        lines.append(f"  • Total progress: {total_closure}° closer")
        lines.append("")

        # Check for pushback moments
        pushbacks = 0
        for i in range(1, len(ra_values)):
            if ra_values[i] > ra_values[i-1]:  # Got more distant
                pushbacks += 1

        lines.append(f"Relationship Dynamics:")
        lines.append(f"  • Times they pushed apart: {pushbacks}")
        lines.append(f"  • Closest moment: Chapter {ra_values.index(closest) + 1} ({closest}°)")

        if pushbacks == 0:
            lines.append("")
            lines.append("  ⚠ WARNING: Relationship only gets closer, never has conflict")
            lines.append("     Consider adding moments where they pull apart")

        return lines

    def _pacing_analysis(self, trajectory: List[Dict]) -> List[str]:
        lines = ["=" * 70, "STORY PACING & FLOW", "=" * 70, ""]

        # Calculate chapter-by-chapter movement
        movement_per_chapter = []
        for i in range(1, len(trajectory)):
            ia_change = abs(trajectory[i].get('IA', 0) - trajectory[i-1].get('IA', 0))
            ra_change = abs(trajectory[i].get('RA_orbit', 180) - trajectory[i-1].get('RA_orbit', 180))
            total_change = ia_change + (ra_change / 180)  # Normalize
            movement_per_chapter.append(total_change)

        # Find slow/fast sections
        slow_chapters = [i+2 for i, m in enumerate(movement_per_chapter) if m < 0.1]
        fast_chapters = [i+2 for i, m in enumerate(movement_per_chapter) if m > 0.5]

        lines.append("Story Movement:")
        lines.extend(self._visualize_pacing(movement_per_chapter))
        lines.append("")

        if slow_chapters:
            lines.append(f"⚠ SLOW SECTIONS (little emotional change):")
            lines.append(f"   Chapters: {self._format_chapter_list(slow_chapters)}")
            lines.append(f"   These chapters might feel like they're dragging.")
            lines.append(f"   Consider adding emotional shifts or conflict.")
            lines.append("")

        if fast_chapters:
            lines.append(f"⚡ FAST SECTIONS (rapid emotional changes):")
            lines.append(f"   Chapters: {self._format_chapter_list(fast_chapters)}")
            lines.append(f"   These are your intense, page-turning moments.")
            lines.append("")

        # Check for flatlines
        flatline_start = None
        for i in range(len(movement_per_chapter)):
            if movement_per_chapter[i] < 0.05:
                if flatline_start is None:
                    flatline_start = i + 2
            else:
                if flatline_start and (i + 1 - flatline_start) >= 3:
                    lines.append(f"🛑 FLATLINE DETECTED: Chapters {flatline_start}-{i+1}")
                    lines.append(f"   Story feels stuck here - needs injection of movement")
                    lines.append("")
                flatline_start = None

        return lines

    def _genre_validation(self, trajectory: List[Dict]) -> List[str]:
        lines = ["=" * 70, f"GENRE FIT: {self.genre.replace('_', ' ').title()}", "=" * 70, ""]

        if self.genre not in NPE_GENRE_PROFILES:
            lines.append(f"No specific genre profile available for {self.genre}")
            return lines

        profile = NPE_GENRE_PROFILES[self.genre]
        ia_profile = profile['axis_profiles']['IA']

        # Extract values
        ia_values = [s.get('IA', 0) for s in trajectory]
        ia_start = ia_values[0]
        ia_end = ia_values[-1]
        ia_min = min(ia_values)

        violations = []
        matches = []

        # Check starting range
        expected_start = ia_profile['start_range']
        if expected_start[0] <= ia_start <= expected_start[1]:
            matches.append(f"✓ Character starts wounded (IA: {ia_start:+.2f})")
        else:
            violations.append(f"✗ Character should start more wounded (expected {expected_start[0]} to {expected_start[1]}, got {ia_start:+.2f})")

        # Check ending range
        expected_end = ia_profile['final_range']
        if expected_end[0] <= ia_end <= expected_end[1]:
            matches.append(f"✓ Character ends healed (IA: {ia_end:+.2f})")
        else:
            violations.append(f"✗ Character should end more healed (expected {expected_end[0]} to {expected_end[1]}, got {ia_end:+.2f})")

        # Check polarity flip requirement
        if ia_profile.get('must_cross_zero'):
            crosses_zero = any(ia_values[i] < 0 and ia_values[i+1] >= 0 for i in range(len(ia_values)-1))
            if crosses_zero:
                matches.append(f"✓ Character crosses from wounded to healing (required for {self.genre})")
            else:
                violations.append(f"✗ Character must cross from negative to positive for {self.genre}")

        # Check dark night depth
        expected_depth = ia_profile.get('dark_night_depth', -0.9)
        if ia_min <= expected_depth:
            matches.append(f"✓ Dark night is deep enough (IA: {ia_min:+.2f})")
        else:
            violations.append(f"✗ Dark night could be deeper for {self.genre} (got {ia_min:+.2f}, expected ≤ {expected_depth})")

        # Display results
        if matches:
            lines.append("What's Working:")
            for match in matches:
                lines.append(f"  {match}")
            lines.append("")

        if violations:
            lines.append("Genre Expectations Not Met:")
            for violation in violations:
                lines.append(f"  {violation}")
            lines.append("")

        if not violations:
            lines.append(f"🎉 Your arc matches {self.genre.replace('_', ' ')} expectations perfectly!")

        return lines

    def _key_moments(self, trajectory: List[Dict]) -> List[str]:
        lines = ["=" * 70, "KEY STORY MOMENTS", "=" * 70, ""]

        moments = []

        ia_values = [s.get('IA', 0) for s in trajectory]
        ra_values = [s.get('RA_orbit', 180) for s in trajectory]

        # Dark night
        darkest_idx = ia_values.index(min(ia_values))
        darkest_chapter = darkest_idx + 1
        percent_through = (darkest_chapter / self.total_chapters) * 100

        moments.append({
            'chapter': darkest_chapter,
            'name': 'DARK NIGHT',
            'description': f'Lowest emotional point (IA: {ia_values[darkest_idx]:+.2f})',
            'timing': f'{percent_through:.0f}% through story',
            'assessment': self._assess_dark_night_timing(percent_through)
        })

        # Polarity flip
        for i in range(1, len(ia_values)):
            if ia_values[i-1] < 0 and ia_values[i] >= 0:
                flip_chapter = i + 1
                flip_percent = (flip_chapter / self.total_chapters) * 100
                moments.append({
                    'chapter': flip_chapter,
                    'name': 'TURNING POINT',
                    'description': 'Character shifts from wounded to healing',
                    'timing': f'{flip_percent:.0f}% through story',
                    'assessment': self._assess_flip_timing(flip_percent)
                })
                break

        # Biggest relationship breakthroughs
        biggest_closure = 0
        closure_chapter = None
        for i in range(1, len(ra_values)):
            closure = ra_values[i-1] - ra_values[i]
            if closure > biggest_closure:
                biggest_closure = closure
                closure_chapter = i + 1

        if biggest_closure > 20:
            moments.append({
                'chapter': closure_chapter,
                'name': 'RELATIONSHIP BREAKTHROUGH',
                'description': f'Relationship closes {biggest_closure:.0f}° in one chapter',
                'timing': '',
                'assessment': '💕 Major connection moment'
            })

        # Display moments
        for moment in moments:
            lines.append(f"Chapter {moment['chapter']}: {moment['name']}")
            lines.append(f"  {moment['description']}")
            if moment['timing']:
                lines.append(f"  Timing: {moment['timing']}")
            if moment['assessment']:
                lines.append(f"  {moment['assessment']}")
            lines.append("")

        return lines

    def _strengths(self, trajectory: List[Dict]) -> List[str]:
        lines = ["=" * 70, "WHAT'S WORKING WELL", "=" * 70, ""]

        strengths = []

        ia_values = [s.get('IA', 0) for s in trajectory]
        ra_values = [s.get('RA_orbit', 180) for s in trajectory]

        # Check for good character growth
        ia_growth = ia_values[-1] - ia_values[0]
        if ia_growth > 1.0:
            strengths.append("✓ Strong character growth - clear journey from wounded to healed")

        # Check for relationship closure
        ra_closure = ra_values[0] - ra_values[-1]
        if ra_closure > 80:
            strengths.append("✓ Significant relationship development - they get much closer")

        # Check for conflict
        pushbacks = sum(1 for i in range(1, len(ra_values)) if ra_values[i] > ra_values[i-1])
        if pushbacks >= 2:
            strengths.append("✓ Good relationship conflict - they don't just smoothly get closer")

        # Check for dark night
        if min(ia_values) < -0.5:
            strengths.append("✓ Dark night has real weight - character truly struggles")

        # Check for recovery
        if ia_values[-1] > 0.3:
            strengths.append("✓ Satisfying ending - character finds healing/wholeness")

        # Display
        if strengths:
            for strength in strengths:
                lines.append(strength)
        else:
            lines.append("(See 'Opportunities to Strengthen' section)")

        return lines

    def _improvements(self, trajectory: List[Dict]) -> List[str]:
        lines = ["=" * 70, "OPPORTUNITIES TO STRENGTHEN", "=" * 70, ""]

        opportunities = []

        ia_values = [s.get('IA', 0) for s in trajectory]
        ra_values = [s.get('RA_orbit', 180) for s in trajectory]

        # Check character arc issues
        ia_growth = ia_values[-1] - ia_values[0]
        if ia_growth < 0.5:
            opportunities.append("⚠ Limited character growth - consider deepening the transformation")

        # Check for polarity flip
        crosses_zero = any(ia_values[i] < 0 and ia_values[i+1] >= 0 for i in range(len(ia_values)-1))
        if not crosses_zero and self.genre in ['cozy_fantasy', 'cozy_mystery', 'dark_romance']:
            opportunities.append(f"⚠ Character should cross from 'wounded' to 'healing' for {self.genre}")

        # Check relationship progress
        ra_closure = ra_values[0] - ra_values[-1]
        if ra_closure < 50:
            opportunities.append("⚠ Limited relationship development - they don't get much closer")

        # Check for flatlines
        movement_per_chapter = []
        for i in range(1, len(trajectory)):
            ia_change = abs(ia_values[i] - ia_values[i-1])
            ra_change = abs(ra_values[i] - ra_values[i-1])
            movement_per_chapter.append(ia_change + ra_change/180)

        slow_chapters = [i+2 for i, m in enumerate(movement_per_chapter) if m < 0.05]
        if len(slow_chapters) > 3:
            opportunities.append(f"⚠ Multiple chapters with little movement: {self._format_chapter_list(slow_chapters)}")

        # Check dark night timing
        darkest_idx = ia_values.index(min(ia_values))
        darkest_percent = ((darkest_idx + 1) / self.total_chapters) * 100
        if darkest_percent < 60:
            opportunities.append(f"⚠ Dark night comes early ({darkest_percent:.0f}% through) - consider moving to 65-75%")

        # Display
        if opportunities:
            for opp in opportunities:
                lines.append(opp)
            lines.append("")
            lines.append("These aren't necessarily problems - just patterns that differ from")
            lines.append(f"typical {self.genre.replace('_', ' ')} stories. Use your judgment!")
        else:
            lines.append("Your arc is solid! No major issues detected.")

        return lines

    def _actionable_fixes(self, trajectory: List[Dict]) -> List[str]:
        lines = ["=" * 70, "SPECIFIC SUGGESTIONS", "=" * 70, ""]

        fixes = []

        ia_values = [s.get('IA', 0) for s in trajectory]
        ra_values = [s.get('RA_orbit', 180) for s in trajectory]

        # Find flatline sections
        movement_per_chapter = []
        for i in range(1, len(trajectory)):
            ia_change = abs(ia_values[i] - ia_values[i-1])
            ra_change = abs(ra_values[i] - ra_values[i-1])
            movement_per_chapter.append(ia_change + ra_change/180)

        # Find consecutive slow chapters
        slow_start = None
        for i in range(len(movement_per_chapter)):
            if movement_per_chapter[i] < 0.05:
                if slow_start is None:
                    slow_start = i + 2
            else:
                if slow_start and (i + 1 - slow_start) >= 2:
                    fixes.append({
                        'chapters': f"{slow_start}-{i+1}",
                        'problem': 'Story feels stuck - little emotional or relationship change',
                        'fix': [
                            f"Add a conflict or complication in chapter {slow_start}",
                            f"Have the characters disagree or pull apart temporarily",
                            f"Introduce new information that shifts emotions",
                            f"Create a mini-crisis that tests the character"
                        ]
                    })
                slow_start = None

        # Check for missing polarity flip
        crosses_zero = any(ia_values[i] < 0 and ia_values[i+1] >= 0 for i in range(len(ia_values)-1))
        if not crosses_zero and min(ia_values) < 0:
            recovery_chapter = ia_values.index(min(ia_values)) + 3
            fixes.append({
                'chapters': f"{recovery_chapter}",
                'problem': 'Character never crosses from wounded to healing',
                'fix': [
                    f"In chapter {recovery_chapter}, show the first moment of hope",
                    "This is where they realize they CAN change",
                    "Not fully healed yet, just the turn toward healing",
                    "Could be a realization, a gesture from someone, or an achievement"
                ]
            })

        # Check for too-smooth relationship
        pushbacks = sum(1 for i in range(1, len(ra_values)) if ra_values[i] > ra_values[i-1])
        if pushbacks == 0 and len(trajectory) > 10:
            mid_chapter = len(trajectory) // 2
            fixes.append({
                'chapters': f"{mid_chapter}",
                'problem': 'Relationship only gets closer - no conflict or setbacks',
                'fix': [
                    f"Around chapter {mid_chapter}, have them pull apart temporarily",
                    "Could be a misunderstanding, fear, or external pressure",
                    "This makes the eventual closeness more earned",
                    "Doesn't have to be dramatic - even small distance creates tension"
                ]
            })

        # Display fixes
        if fixes:
            for i, fix in enumerate(fixes, 1):
                lines.append(f"{i}. CHAPTERS {fix['chapters']}: {fix['problem']}")
                lines.append("")
                lines.append("   How to fix:")
                for suggestion in fix['fix']:
                    lines.append(f"   • {suggestion}")
                lines.append("")
        else:
            lines.append("No specific fixes needed - your story flow looks good!")

        return lines

    # Helper visualization methods
    def _visualize_ia_arc(self, trajectory: List[Dict]) -> List[str]:
        lines = []
        ia_values = [s.get('IA', 0) for s in trajectory]

        # Create ASCII visualization
        height = 10
        width = min(60, len(trajectory) * 2)

        # Map IA values to graph
        min_ia = -1.0
        max_ia = 1.0

        lines.append("     +1.0 (Healed)")

        for row in range(height):
            threshold = max_ia - (row / height) * (max_ia - min_ia)
            line = f"{threshold:+5.1f} |"

            for ia in ia_values:
                if abs(ia - threshold) < 0.2:
                    if ia < 0:
                        line += "●"
                    else:
                        line += "○"
                elif threshold == 0:
                    line += "-"
                else:
                    line += " "

            lines.append(line)

        lines.append("     -1.0 (Wounded)")
        lines.append("      " + "".join([str((i+1) % 10) for i in range(len(trajectory))]))

        return lines

    def _visualize_relationship_arc(self, trajectory: List[Dict]) -> List[str]:
        lines = []
        ra_values = [s.get('RA_orbit', 180) for s in trajectory]

        lines.append("    180° (Distant)")

        for row in range(10):
            threshold = 180 - (row * 18)
            line = f"    {threshold:3.0f}° |"

            for ra in ra_values:
                if abs(ra - threshold) < 15:
                    line += "●"
                else:
                    line += " "

            lines.append(line)

        lines.append("      0° (Together)")
        lines.append("        " + "".join([str((i+1) % 10) for i in range(len(trajectory))]))

        return lines

    def _visualize_pacing(self, movement_per_chapter: List[float]) -> List[str]:
        lines = []

        max_movement = max(movement_per_chapter) if movement_per_chapter else 1

        lines.append("High |")
        for movement in movement_per_chapter:
            bars = int((movement / max_movement) * 10)
            if bars == 0:
                lines.append("   0 | .")
            else:
                lines.append(f"{movement:5.2f} | " + "█" * bars)
        lines.append("Low  |")

        return lines

    def _health_bar(self, score: int) -> str:
        filled = int(score / 10)
        bar = "█" * filled + "░" * (10 - filled)
        if score >= 80:
            return f"[{bar}] Excellent"
        elif score >= 60:
            return f"[{bar}] Good"
        elif score >= 40:
            return f"[{bar}] Needs Work"
        else:
            return f"[{bar}] Significant Issues"

    def _calculate_health_score(self, trajectory: List[Dict]) -> int:
        score = 50  # Base score

        ia_values = [s.get('IA', 0) for s in trajectory]
        ra_values = [s.get('RA_orbit', 180) for s in trajectory]

        # Character growth (+30 points)
        ia_growth = ia_values[-1] - ia_values[0]
        if ia_growth > 1.0:
            score += 30
        elif ia_growth > 0.5:
            score += 15

        # Relationship progress (+20 points)
        ra_closure = ra_values[0] - ra_values[-1]
        if ra_closure > 80:
            score += 20
        elif ra_closure > 40:
            score += 10

        # Has conflict (-10 if missing)
        pushbacks = sum(1 for i in range(1, len(ra_values)) if ra_values[i] > ra_values[i-1])
        if pushbacks == 0:
            score -= 10

        # Movement throughout (check for flatlines)
        movement_count = 0
        for i in range(1, len(ia_values)):
            if abs(ia_values[i] - ia_values[i-1]) > 0.05:
                movement_count += 1

        movement_ratio = movement_count / (len(ia_values) - 1)
        if movement_ratio > 0.7:
            score += 10

        return max(0, min(100, score))

    def _describe_internal_state(self, ia_value: float) -> str:
        if ia_value < -0.7:
            return "deeply wounded, feels broken/inadequate"
        elif ia_value < -0.3:
            return "struggling, hurting but not broken"
        elif ia_value < 0:
            return "wounded but starting to hope"
        elif ia_value < 0.3:
            return "beginning to heal, cautiously hopeful"
        elif ia_value < 0.7:
            return "healing well, growing in confidence"
        else:
            return "healed, whole, self-aware and strong"

    def _describe_relationship_distance(self, orbit: float) -> str:
        if orbit >= 160:
            return "distant/strangers"
        elif orbit >= 120:
            return "acquaintances, warming up"
        elif orbit >= 90:
            return "friends, growing closer"
        elif orbit >= 60:
            return "close, intimate connection"
        else:
            return "deep bond, fully connected"

    def _format_chapter_list(self, chapters: List[int]) -> str:
        if len(chapters) <= 5:
            return ", ".join(map(str, chapters))
        else:
            return f"{', '.join(map(str, chapters[:5]))}, ..."

    def _quick_verdict(self, trajectory: List[Dict]) -> str:
        health = self._calculate_health_score(trajectory)
        ia_values = [s.get('IA', 0) for s in trajectory]

        if health >= 80:
            return "Strong arc with good character growth and pacing."
        elif health >= 60:
            return "Solid foundation with a few areas to strengthen."
        else:
            crosses_zero = any(ia_values[i] < 0 and ia_values[i+1] >= 0 for i in range(len(ia_values)-1))
            if not crosses_zero:
                return "Character arc needs more transformation - no clear healing moment."
            else:
                return "Arc has potential but needs work on pacing and development."

    def _assess_dark_night_timing(self, percent: float) -> str:
        if 65 <= percent <= 75:
            return "✓ Perfect timing for dark night"
        elif 60 <= percent < 65:
            return "⚠ Slightly early - might work depending on story length"
        elif percent < 60:
            return "⚠ Too early - leaves too much recovery time"
        else:
            return "⚠ Late - may feel rushed in resolution"

    def _assess_flip_timing(self, percent: float) -> str:
        if 75 <= percent <= 85:
            return "✓ Good timing - enough space to show healing"
        elif percent < 75:
            return "⚠ Early flip - make sure there's still tension in Act 3"
        else:
            return "⚠ Very late - may feel rushed"


# Main execution
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python npe_author_report.py <trajectory_file.json> [genre]")
        sys.exit(1)

    filepath = Path(sys.argv[1])
    genre = sys.argv[2] if len(sys.argv) > 2 else "contemporary_romance"

    # Load trajectory
    with open(filepath, 'r') as f:
        trajectory = json.load(f)

    # Extract title and chapter count
    title = filepath.stem.replace('_', ' ').title()
    total_chapters = len(trajectory)

    # Generate report
    reporter = AuthorNPEReport(title, genre, total_chapters)
    report = reporter.generate(trajectory)

    print(report)
