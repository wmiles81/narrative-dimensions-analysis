#!/usr/bin/env python3
"""
Interactive worksheet for scoring story dimensions beat-by-beat.
Helps authors systematically track dimensional changes through their story.
"""

import json
import sys
import csv
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import math


class DimensionalWorksheet:
    """Interactive tool for building story trajectories."""

    # Dimension definitions with valid ranges
    PRIMARY_DIMENSIONS = {
        'intimacy': (0, 10),
        'trust': (0, 10),
        'desire': (0, 10),
        'vulnerability': (0, 10),
        'goal_alignment': (0, 10),
        'power_differential': (-5, 5),
        'info_asymmetry': (0, 10),
        'stakes': (0, 10),
        'proximity': (0, 10)
    }

    SECONDARY_DIMENSIONS = {
        'danger': (0, 10),
        'fear_dread': (0, 10),
        'mystery': (0, 10),
        'moral_ambiguity': (0, 10),
        'acceptance': (0, 10)
    }

    ALL_DIMENSIONS = {**PRIMARY_DIMENSIONS, **SECONDARY_DIMENSIONS}

    def __init__(self, story_title: str, genre: str, num_beats: int = 12):
        """
        Initialize worksheet.

        Args:
            story_title: Title of the story being analyzed
            genre: Primary genre (romance, thriller, etc.)
            num_beats: Number of story beats to track (default 12)
        """
        self.story_title = story_title
        self.genre = genre.lower()
        self.num_beats = num_beats
        self.beats = []
        self.project_root = Path(__file__).parent.parent
        self.metadata = {
            'created': datetime.now().isoformat(),
            'last_modified': datetime.now().isoformat()
        }

    def add_beat(self, beat_name: str, beat_percent: float, dimensions: Dict[str, float],
                 notes: Optional[str] = None) -> None:
        """
        Add a story beat with dimension values.

        Args:
            beat_name: Name of the beat (e.g., "Meet Cute", "Black Moment")
            beat_percent: Position in story (0-100)
            dimensions: Dict of dimension scores {"intimacy": 5, "trust": 3, ...}
            notes: Optional notes about what happens at this beat
        """
        # Validate dimensions
        errors = self.validate_dimensions(dimensions)
        if errors:
            raise ValueError(f"Validation errors: {', '.join(errors)}")

        # Validate beat_percent
        if not 0 <= beat_percent <= 100:
            raise ValueError(f"beat_percent must be 0-100, got {beat_percent}")

        beat = {
            'name': beat_name,
            'percent': beat_percent,
            'dimensions': dimensions.copy(),
            'notes': notes or ""
        }

        self.beats.append(beat)
        self.metadata['last_modified'] = datetime.now().isoformat()

    def validate_dimensions(self, dimensions: Dict[str, float]) -> List[str]:
        """Validate dimension scores are in acceptable ranges."""
        errors = []

        for dim_name, value in dimensions.items():
            if dim_name not in self.ALL_DIMENSIONS:
                errors.append(f"Unknown dimension: {dim_name}")
                continue

            min_val, max_val = self.ALL_DIMENSIONS[dim_name]
            if not min_val <= value <= max_val:
                errors.append(
                    f"{dim_name} = {value} (valid range: {min_val} to {max_val})"
                )

        return errors

    def generate_trajectory(self) -> List[Dict]:
        """Generate trajectory list sorted by beat_percent."""
        sorted_beats = sorted(self.beats, key=lambda b: b['percent'])
        return [beat['dimensions'] for beat in sorted_beats]

    def calculate_velocity(self) -> List[float]:
        """Calculate velocity (rate of change) between beats."""
        if len(self.beats) < 2:
            return []

        trajectory = self.generate_trajectory()
        velocities = []

        for i in range(1, len(trajectory)):
            prev_state = trajectory[i-1]
            curr_state = trajectory[i]

            total_movement = 0
            dimensions_counted = 0

            for dimension in curr_state:
                if dimension in prev_state:
                    movement = abs(curr_state[dimension] - prev_state[dimension])
                    total_movement += movement
                    dimensions_counted += 1

            velocity = total_movement / dimensions_counted if dimensions_counted > 0 else 0
            velocities.append(velocity)

        return velocities

    def export_to_json(self, filepath: Optional[Path] = None) -> Path:
        """Export worksheet to JSON for use with other scripts."""
        if filepath is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_title = "".join(c if c.isalnum() else "_" for c in self.story_title)
            filename = f"{safe_title}_{timestamp}.json"
            filepath = self.project_root / "exports" / filename

        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        export_data = {
            'story_title': self.story_title,
            'genre': self.genre,
            'metadata': self.metadata,
            'beats': sorted(self.beats, key=lambda b: b['percent']),
            'trajectory': self.generate_trajectory()
        }

        with open(filepath, 'w') as f:
            json.dump(export_data, f, indent=2)

        return filepath

    def export_to_csv(self, filepath: Optional[Path] = None) -> Path:
        """Export to CSV for spreadsheet analysis."""
        if filepath is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_title = "".join(c if c.isalnum() else "_" for c in self.story_title)
            filename = f"{safe_title}_{timestamp}.csv"
            filepath = self.project_root / "exports" / filename

        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        sorted_beats = sorted(self.beats, key=lambda b: b['percent'])

        if not sorted_beats:
            raise ValueError("No beats to export")

        # Get all dimension names used
        all_dimensions = set()
        for beat in sorted_beats:
            all_dimensions.update(beat['dimensions'].keys())
        all_dimensions = sorted(all_dimensions)

        with open(filepath, 'w', newline='') as f:
            writer = csv.writer(f)

            # Header row
            header = ['Beat Name', 'Story %'] + all_dimensions + ['Notes']
            writer.writerow(header)

            # Data rows
            for beat in sorted_beats:
                row = [
                    beat['name'],
                    beat['percent']
                ]
                for dim in all_dimensions:
                    row.append(beat['dimensions'].get(dim, ''))
                row.append(beat['notes'])
                writer.writerow(row)

        return filepath

    def visualize_ascii(self, dimensions: Optional[List[str]] = None) -> str:
        """Create ASCII art graph of specified dimensions over time."""
        if not self.beats:
            return "No beats to visualize"

        sorted_beats = sorted(self.beats, key=lambda b: b['percent'])

        # Determine which dimensions to show
        if dimensions is None:
            # Use most common dimensions
            dim_counts = {}
            for beat in sorted_beats:
                for dim in beat['dimensions']:
                    dim_counts[dim] = dim_counts.get(dim, 0) + 1
            dimensions = sorted(dim_counts.keys(), key=lambda d: dim_counts[d], reverse=True)[:4]

        lines = []
        lines.append(f"\n{'='*70}")
        lines.append(f"  {self.story_title} - Dimensional Trajectory")
        lines.append(f"{'='*70}\n")

        # Create graph for each dimension
        for dim in dimensions:
            if dim not in self.ALL_DIMENSIONS:
                continue

            min_val, max_val = self.ALL_DIMENSIONS[dim]
            lines.append(f"{dim.upper().replace('_', ' ')}")
            lines.append(f"  Range: {min_val} to {max_val}")

            # Extract values
            values = []
            for beat in sorted_beats:
                values.append(beat['dimensions'].get(dim, None))

            # Skip if dimension not used
            if all(v is None for v in values):
                lines.append("  (not tracked)\n")
                continue

            # Create ASCII graph (height = 10 rows)
            graph_height = 10
            graph_width = min(len(values), 50)

            # Normalize values to graph height
            graph = [[' ' for _ in range(graph_width)] for _ in range(graph_height)]

            for i, val in enumerate(values[:graph_width]):
                if val is None:
                    continue

                # Normalize to 0-1 range
                normalized = (val - min_val) / (max_val - min_val) if max_val != min_val else 0.5
                # Convert to row (inverted, 0 = top)
                row = graph_height - 1 - int(normalized * (graph_height - 1))
                graph[row][i] = '*'

            # Print graph
            lines.append(f"  {max_val:>4} |" + "".join(graph[0]))
            for row in range(1, graph_height - 1):
                lines.append(f"       |" + "".join(graph[row]))
            lines.append(f"  {min_val:>4} |" + "".join(graph[graph_height - 1]))
            lines.append(f"       +" + "-" * graph_width)
            lines.append("")

        # Add beat markers
        lines.append("BEATS:")
        for i, beat in enumerate(sorted_beats[:10]):
            lines.append(f"  {i+1}. {beat['name']} ({beat['percent']:.0f}%)")

        return "\n".join(lines)

    def get_analysis_summary(self) -> str:
        """Generate summary report of the trajectory."""
        if not self.beats:
            return "No beats recorded yet."

        lines = []
        lines.append(f"\n{'='*70}")
        lines.append(f"  TRAJECTORY ANALYSIS: {self.story_title}")
        lines.append(f"  Genre: {self.genre}")
        lines.append(f"{'='*70}\n")

        # Basic stats
        lines.append(f"Total Beats: {len(self.beats)}")
        sorted_beats = sorted(self.beats, key=lambda b: b['percent'])
        lines.append(f"Story Coverage: {sorted_beats[0]['percent']:.0f}% to {sorted_beats[-1]['percent']:.0f}%")

        # Velocity analysis
        velocities = self.calculate_velocity()
        if velocities:
            avg_velocity = sum(velocities) / len(velocities)
            lines.append(f"Average Velocity: {avg_velocity:.2f} points/beat")
            lines.append(f"Max Velocity: {max(velocities):.2f} points/beat")
            lines.append(f"Min Velocity: {min(velocities):.2f} points/beat")

        lines.append("")

        # Dimension analysis
        lines.append("DIMENSIONAL CHANGES:")

        # Calculate total change for each dimension
        first_beat = sorted_beats[0]['dimensions']
        last_beat = sorted_beats[-1]['dimensions']

        changes = []
        for dim in first_beat:
            if dim in last_beat:
                change = last_beat[dim] - first_beat[dim]
                changes.append((dim, change, first_beat[dim], last_beat[dim]))

        # Sort by absolute change
        changes.sort(key=lambda x: abs(x[1]), reverse=True)

        for dim, change, start, end in changes[:5]:
            direction = "↑" if change > 0 else "↓" if change < 0 else "→"
            lines.append(f"  {dim:20s} {direction} {change:+.1f} ({start:.1f} → {end:.1f})")

        lines.append("")

        # Potential issues
        issues = self._detect_issues()
        if issues:
            lines.append("POTENTIAL ISSUES:")
            for issue in issues:
                lines.append(f"  ⚠ {issue}")
        else:
            lines.append("✓ No major issues detected")

        return "\n".join(lines)

    def _detect_issues(self) -> List[str]:
        """Detect potential trajectory issues."""
        issues = []

        if len(self.beats) < 2:
            return issues

        sorted_beats = sorted(self.beats, key=lambda b: b['percent'])

        # Check for huge jumps
        for i in range(1, len(sorted_beats)):
            prev = sorted_beats[i-1]['dimensions']
            curr = sorted_beats[i]['dimensions']

            for dim in curr:
                if dim in prev:
                    jump = abs(curr[dim] - prev[dim])
                    if jump > 3:
                        issues.append(
                            f"Large jump in {dim} at '{sorted_beats[i]['name']}' "
                            f"({jump:.1f} points) - needs catalyst event"
                        )

        # Check for flatlines (no change in primary dimensions)
        if len(sorted_beats) >= 3:
            first = sorted_beats[0]['dimensions']
            last = sorted_beats[-1]['dimensions']

            for dim in self.PRIMARY_DIMENSIONS:
                if dim in first and dim in last:
                    if abs(last[dim] - first[dim]) < 0.5:
                        issues.append(f"{dim} shows minimal change (flatline)")

        # Check velocity consistency
        velocities = self.calculate_velocity()
        if len(velocities) >= 3:
            avg_velocity = sum(velocities) / len(velocities)
            for i, v in enumerate(velocities):
                if v > avg_velocity * 3:
                    issues.append(
                        f"Pacing spike at beat {i+2} "
                        f"(velocity: {v:.2f} vs avg: {avg_velocity:.2f})"
                    )

        return issues

    def interactive_mode(self) -> None:
        """Run interactive CLI to build worksheet step by step."""
        print(f"\n{'='*70}")
        print(f"  DIMENSIONAL WORKSHEET: {self.story_title}")
        print(f"  Genre: {self.genre}")
        print(f"  Target Beats: {self.num_beats}")
        print(f"{'='*70}\n")

        print("This tool will guide you through scoring your story beat-by-beat.")
        print("You can track as many or as few dimensions as you like.\n")

        # Ask if user wants to use a template
        use_template = input("Load template beats for this genre? (y/n): ").lower().strip()
        if use_template == 'y':
            self._load_genre_template()

        # Get dimensions to track
        print("\nWhich dimensions do you want to track?")
        print("\nPRIMARY DIMENSIONS (romance/relationship):")
        for dim in self.PRIMARY_DIMENSIONS:
            print(f"  - {dim}")
        print("\nSECONDARY DIMENSIONS (genre-specific):")
        for dim in self.SECONDARY_DIMENSIONS:
            print(f"  - {dim}")

        print("\nEnter dimension names separated by commas")
        print("(or press Enter to track all primary dimensions):")
        dims_input = input("> ").strip()

        if dims_input:
            tracking_dims = [d.strip().lower() for d in dims_input.split(',')]
        else:
            tracking_dims = list(self.PRIMARY_DIMENSIONS.keys())

        # Validate dimensions
        invalid = [d for d in tracking_dims if d not in self.ALL_DIMENSIONS]
        if invalid:
            print(f"\n⚠ Unknown dimensions: {', '.join(invalid)}")
            print("Continuing with valid dimensions only...")
            tracking_dims = [d for d in tracking_dims if d in self.ALL_DIMENSIONS]

        print(f"\nTracking: {', '.join(tracking_dims)}\n")

        # Add beats
        beat_num = 1
        while True:
            print(f"\n{'─'*70}")
            print(f"  BEAT {beat_num} of {self.num_beats}")
            print(f"{'─'*70}")

            # Get beat name
            beat_name = input(f"Beat name (or 'done' to finish, 'help' for examples): ").strip()

            if beat_name.lower() == 'done':
                break
            elif beat_name.lower() == 'help':
                self._show_beat_examples()
                continue
            elif not beat_name:
                print("⚠ Beat name cannot be empty")
                continue

            # Get beat position
            default_percent = (beat_num / self.num_beats) * 100
            percent_input = input(f"Story position % (default: {default_percent:.0f}%): ").strip()

            if percent_input:
                try:
                    beat_percent = float(percent_input)
                    if not 0 <= beat_percent <= 100:
                        print("⚠ Percent must be 0-100")
                        continue
                except ValueError:
                    print("⚠ Invalid number")
                    continue
            else:
                beat_percent = default_percent

            # Get dimension scores
            print(f"\nEnter scores for each dimension:")
            dimensions = {}

            for dim in tracking_dims:
                min_val, max_val = self.ALL_DIMENSIONS[dim]

                while True:
                    score_input = input(f"  {dim} ({min_val} to {max_val}, '?' for guide): ").strip()

                    if score_input == '?':
                        self._show_dimension_guide(dim)
                        continue
                    elif not score_input:
                        print(f"    Skipping {dim}")
                        break

                    try:
                        score = float(score_input)
                        if not min_val <= score <= max_val:
                            print(f"    ⚠ Must be {min_val} to {max_val}")
                            continue

                        dimensions[dim] = score

                        # Warn on extremes
                        if score == min_val or score == max_val:
                            print(f"    ⚠ Extreme value! Make sure this is intentional.")

                        # Warn on large jumps
                        if self.beats:
                            last_beat = sorted(self.beats, key=lambda b: b['percent'])[-1]
                            if dim in last_beat['dimensions']:
                                jump = abs(score - last_beat['dimensions'][dim])
                                if jump > 3:
                                    print(f"    ⚠ Large jump ({jump:.1f} points) - catalyst event needed!")

                        break
                    except ValueError:
                        print("    ⚠ Invalid number")

            if not dimensions:
                print("⚠ No dimensions scored, beat not added")
                continue

            # Get notes
            notes = input("\nNotes (what happens in this beat?): ").strip()

            # Add beat
            try:
                self.add_beat(beat_name, beat_percent, dimensions, notes)
                print(f"\n✓ Beat '{beat_name}' added!")
                beat_num += 1
            except ValueError as e:
                print(f"\n⚠ Error: {e}")

        # Summary
        print(f"\n{'='*70}")
        print(f"  WORKSHEET COMPLETE")
        print(f"{'='*70}")
        print(f"\nTotal beats recorded: {len(self.beats)}")

        if self.beats:
            print("\nWould you like to:")
            print("  1. View analysis summary")
            print("  2. View ASCII visualization")
            print("  3. Export to JSON")
            print("  4. Export to CSV")
            print("  5. Save session")
            print("  6. All of the above")
            print("  0. Exit")

            choice = input("\nChoice: ").strip()

            if choice in ['1', '6']:
                print(self.get_analysis_summary())

            if choice in ['2', '6']:
                print(self.visualize_ascii())

            if choice in ['3', '6']:
                json_path = self.export_to_json()
                print(f"\n✓ Exported to JSON: {json_path}")

            if choice in ['4', '6']:
                csv_path = self.export_to_csv()
                print(f"✓ Exported to CSV: {csv_path}")

            if choice in ['5', '6']:
                session_path = self.save_session()
                print(f"✓ Session saved: {session_path}")

    def _load_genre_template(self) -> None:
        """Load template beats for the genre."""
        template_file = self.project_root / "templates" / f"{self.genre}-beat-template.csv"

        if not template_file.exists():
            print(f"⚠ No template found for '{self.genre}'")
            return

        try:
            with open(template_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    beat_name = row['Beat Name']
                    beat_percent = float(row['Story %'])

                    dimensions = {}
                    for key, value in row.items():
                        if key not in ['Beat Name', 'Story %', 'Notes'] and value:
                            dimensions[key] = float(value)

                    notes = row.get('Notes', '')

                    if dimensions:
                        self.add_beat(beat_name, beat_percent, dimensions, notes)

            print(f"✓ Loaded {len(self.beats)} template beats from {template_file.name}")
        except Exception as e:
            print(f"⚠ Error loading template: {e}")

    def _show_beat_examples(self) -> None:
        """Show example beat names for the genre."""
        examples = {
            'romance': [
                "Meet Cute (5%)", "First Connection (15%)", "Growing Closer (25%)",
                "First Conflict (35%)", "Deepening Bond (45%)", "False Victory (55%)",
                "Major Setback (65%)", "Black Moment (75%)", "Grand Gesture (85%)",
                "Resolution (95%)", "HEA (100%)"
            ],
            'thriller': [
                "Normal World (5%)", "Inciting Incident (12%)", "Point of No Return (25%)",
                "Rising Danger (40%)", "Midpoint Twist (50%)", "False Victory (60%)",
                "Reversal (70%)", "Dark Night (80%)", "Final Battle (90%)",
                "Resolution (100%)"
            ],
            'mystery': [
                "Crime Discovered (5%)", "Initial Investigation (15%)", "First Clue (25%)",
                "Red Herring (35%)", "Breakthrough (45%)", "Midpoint Revelation (50%)",
                "Complications (60%)", "Second Death (70%)", "Truth Revealed (85%)",
                "Confrontation (95%)", "Resolution (100%)"
            ]
        }

        genre_examples = examples.get(self.genre, examples.get('romance'))
        print("\nExample beats:")
        for example in genre_examples:
            print(f"  - {example}")
        print()

    def _show_dimension_guide(self, dimension: str) -> None:
        """Show scoring guide for a dimension."""
        guides = {
            'intimacy': {
                0: "Complete strangers",
                2: "Acquaintances",
                4: "Friends / developing connection",
                6: "Close friends / strong romantic interest",
                8: "Deep connection",
                10: "Complete emotional unity"
            },
            'trust': {
                0: "Complete distrust / active betrayal",
                2: "Suspicious / guarded",
                4: "Cautious trust",
                6: "Working trust",
                8: "Strong trust",
                10: "Absolute unwavering trust"
            },
            'desire': {
                0: "Repulsion / no interest",
                2: "Minimal attraction",
                4: "Noticeable attraction / interest",
                6: "Strong attraction / longing",
                8: "Intense desire / yearning",
                10: "Overwhelming all-consuming desire"
            },
            'vulnerability': {
                0: "Completely guarded / armored",
                2: "Highly defensive",
                4: "Selectively open",
                6: "Moderately vulnerable",
                8: "Highly vulnerable",
                10: "Completely unguarded"
            },
            'stakes': {
                0: "Nothing at risk",
                2: "Minor personal stakes",
                4: "Moderate personal stakes",
                6: "High personal stakes",
                8: "Life-changing stakes",
                10: "Maximum life-or-death stakes"
            }
        }

        guide = guides.get(dimension, {})
        if guide:
            print(f"\n  {dimension.upper()} scoring guide:")
            for score, description in sorted(guide.items()):
                print(f"    {score:2d}: {description}")
            print()
        else:
            min_val, max_val = self.ALL_DIMENSIONS[dimension]
            print(f"\n  {dimension}: {min_val} (minimum) to {max_val} (maximum)\n")

    def save_session(self, filepath: Optional[Path] = None) -> Path:
        """Save current worksheet state to resume later."""
        if filepath is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_title = "".join(c if c.isalnum() else "_" for c in self.story_title)
            filename = f"{safe_title}_session_{timestamp}.json"
            filepath = self.project_root / "sessions" / filename

        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        session_data = {
            'story_title': self.story_title,
            'genre': self.genre,
            'num_beats': self.num_beats,
            'beats': self.beats,
            'metadata': self.metadata
        }

        with open(filepath, 'w') as f:
            json.dump(session_data, f, indent=2)

        return filepath

    @classmethod
    def load_session(cls, filepath: Path) -> 'DimensionalWorksheet':
        """Load a previously saved worksheet session."""
        filepath = Path(filepath)

        with open(filepath, 'r') as f:
            session_data = json.load(f)

        worksheet = cls(
            story_title=session_data['story_title'],
            genre=session_data['genre'],
            num_beats=session_data.get('num_beats', 12)
        )

        worksheet.beats = session_data['beats']
        worksheet.metadata = session_data.get('metadata', {})

        return worksheet


# Example usage and CLI interface
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Interactive dimensional analysis worksheet",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Start new interactive session
  %(prog)s --title "My Romance Novel" --genre romance --interactive

  # Resume saved session
  %(prog)s --load sessions/my_story_session.json --interactive

  # Quick export of session to JSON
  %(prog)s --load sessions/my_story_session.json --export-json

  # Show analysis of saved session
  %(prog)s --load sessions/my_story_session.json --analyze
        """
    )

    parser.add_argument("--title", help="Story title")
    parser.add_argument("--genre", help="Genre (romance, thriller, mystery, etc.)")
    parser.add_argument("--beats", type=int, default=12, help="Number of beats to track (default: 12)")
    parser.add_argument("--load", help="Load saved session file")
    parser.add_argument("--interactive", action="store_true", help="Run interactive mode")
    parser.add_argument("--analyze", action="store_true", help="Show analysis summary")
    parser.add_argument("--visualize", action="store_true", help="Show ASCII visualization")
    parser.add_argument("--export-json", help="Export to JSON file")
    parser.add_argument("--export-csv", help="Export to CSV file")

    args = parser.parse_args()

    # Load existing session or create new worksheet
    if args.load:
        try:
            worksheet = DimensionalWorksheet.load_session(args.load)
            print(f"✓ Loaded session: {worksheet.story_title}")
        except FileNotFoundError:
            print(f"Error: Session file not found: {args.load}")
            sys.exit(1)
        except Exception as e:
            print(f"Error loading session: {e}")
            sys.exit(1)
    elif args.title and args.genre:
        worksheet = DimensionalWorksheet(args.title, args.genre, args.beats)
    else:
        # Interactive mode without arguments
        print("\n" + "="*70)
        print("  DIMENSIONAL WORKSHEET")
        print("="*70 + "\n")

        title = input("Story title: ").strip()
        if not title:
            print("Error: Title required")
            sys.exit(1)

        genre = input("Genre (romance/thriller/mystery/fantasy): ").strip()
        if not genre:
            print("Error: Genre required")
            sys.exit(1)

        beats_input = input("Number of beats to track (default 12): ").strip()
        beats = int(beats_input) if beats_input else 12

        worksheet = DimensionalWorksheet(title, genre, beats)
        args.interactive = True

    # Execute requested action
    if args.interactive:
        worksheet.interactive_mode()
    elif args.analyze:
        print(worksheet.get_analysis_summary())
    elif args.visualize:
        print(worksheet.visualize_ascii())
    elif args.export_json:
        path = worksheet.export_to_json(args.export_json)
        print(f"✓ Exported to JSON: {path}")
    elif args.export_csv:
        path = worksheet.export_to_csv(args.export_csv)
        print(f"✓ Exported to CSV: {path}")
    else:
        # No action specified, show help
        parser.print_help()
