#!/usr/bin/env python3
"""
Track and analyze multiple parallel narrative trajectories (subplots).
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from calculate_tension import calculate_tension

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent


class SubplotTracker:
    """Track and analyze multiple parallel narrative trajectories."""

    def __init__(self):
        self.plots = {}  # plot_name -> trajectory (list of states)
        self.plot_configs = {}  # plot_name -> configuration (genre, weights, etc.)

    def add_plot(self, name: str, trajectory: List[Dict],
                 genre: str = "romance", subgenre: Optional[str] = None,
                 custom_weights: Optional[Dict[str, float]] = None,
                 description: str = "") -> None:
        """
        Add a plot/subplot trajectory.

        Args:
            name: Identifier for this plot (e.g., 'main', 'romance_subplot', 'villain_arc')
            trajectory: List of dimensional states
            genre: Genre for this plot
            subgenre: Subgenre for this plot
            custom_weights: Optional custom tension weights
            description: Human-readable description
        """
        self.plots[name] = trajectory
        self.plot_configs[name] = {
            'genre': genre,
            'subgenre': subgenre,
            'custom_weights': custom_weights,
            'description': description
        }

    def remove_plot(self, name: str) -> None:
        """Remove a plot from tracking."""
        if name in self.plots:
            del self.plots[name]
            del self.plot_configs[name]

    def get_plot_names(self) -> List[str]:
        """Get list of all tracked plot names."""
        return list(self.plots.keys())

    def analyze_plot(self, name: str) -> Dict:
        """
        Analyze a single plot trajectory.

        Returns:
            Dictionary with tension over time, pacing, and key moments
        """
        if name not in self.plots:
            raise ValueError(f"Plot '{name}' not found")

        trajectory = self.plots[name]
        config = self.plot_configs[name]

        # Calculate tension for each state
        tension_timeline = []
        for i, state in enumerate(trajectory):
            tension_data = calculate_tension(
                state,
                genre=config['genre'],
                subgenre=config['subgenre'],
                custom_weights=config['custom_weights']
            )
            tension_timeline.append({
                'beat': i,
                'tension': tension_data['total_tension'],
                'primary_driver': tension_data['primary_driver']
            })

        # Find key moments
        tensions = [t['tension'] for t in tension_timeline]
        peak_tension_idx = tensions.index(max(tensions))
        low_tension_idx = tensions.index(min(tensions))

        # Calculate pacing (tension velocity)
        pacing = []
        for i in range(1, len(tensions)):
            velocity = tensions[i] - tensions[i-1]
            pacing.append({
                'beat': i,
                'velocity': round(velocity, 2),
                'acceleration': 'rising' if velocity > 0 else 'falling'
            })

        return {
            'name': name,
            'description': config['description'],
            'tension_timeline': tension_timeline,
            'pacing': pacing,
            'key_moments': {
                'peak_tension': {
                    'beat': peak_tension_idx,
                    'tension': tensions[peak_tension_idx]
                },
                'lowest_tension': {
                    'beat': low_tension_idx,
                    'tension': tensions[low_tension_idx]
                }
            },
            'stats': {
                'avg_tension': round(sum(tensions) / len(tensions), 2),
                'max_tension': max(tensions),
                'min_tension': min(tensions),
                'total_beats': len(trajectory)
            }
        }

    def compare_plots(self, plot_names: Optional[List[str]] = None) -> Dict:
        """
        Compare multiple plots side by side.

        Args:
            plot_names: List of plot names to compare (default: all plots)

        Returns:
            Comparison data including synchronized tension and intersections
        """
        if plot_names is None:
            plot_names = self.get_plot_names()

        if not plot_names:
            return {'error': 'No plots to compare'}

        # Analyze each plot
        analyses = {name: self.analyze_plot(name) for name in plot_names}

        # Find synchronized peaks (where multiple plots peak together)
        synchronized_peaks = self._find_synchronized_moments(
            analyses, 'peak_tension', tolerance=1
        )

        # Find tension intersections (where plot tensions cross)
        intersections = self._find_tension_intersections(analyses)

        return {
            'plots': analyses,
            'synchronized_peaks': synchronized_peaks,
            'intersections': intersections,
            'overall_stats': {
                'total_plots': len(plot_names),
                'avg_tension_all_plots': round(
                    sum(a['stats']['avg_tension'] for a in analyses.values()) / len(analyses), 2
                )
            }
        }

    def _find_synchronized_moments(self, analyses: Dict, moment_type: str,
                                   tolerance: int = 1) -> List[Dict]:
        """Find moments where multiple plots have similar events."""
        synchronized = []

        if len(analyses) < 2:
            return synchronized

        plot_names = list(analyses.keys())

        # Check each plot's moment against others
        for i, name1 in enumerate(plot_names):
            beat1 = analyses[name1]['key_moments'][moment_type]['beat']

            for name2 in plot_names[i+1:]:
                beat2 = analyses[name2]['key_moments'][moment_type]['beat']

                if abs(beat1 - beat2) <= tolerance:
                    synchronized.append({
                        'plots': [name1, name2],
                        'beat_range': (min(beat1, beat2), max(beat1, beat2)),
                        'moment_type': moment_type
                    })

        return synchronized

    def _find_tension_intersections(self, analyses: Dict) -> List[Dict]:
        """Find points where plot tension lines cross."""
        intersections = []

        if len(analyses) < 2:
            return intersections

        plot_names = list(analyses.keys())

        # Compare each pair of plots
        for i, name1 in enumerate(plot_names):
            timeline1 = analyses[name1]['tension_timeline']

            for name2 in plot_names[i+1:]:
                timeline2 = analyses[name2]['tension_timeline']

                # Find crossover points
                min_len = min(len(timeline1), len(timeline2))
                for beat in range(1, min_len):
                    t1_prev = timeline1[beat-1]['tension']
                    t1_curr = timeline1[beat]['tension']
                    t2_prev = timeline2[beat-1]['tension']
                    t2_curr = timeline2[beat]['tension']

                    # Check if lines crossed
                    if (t1_prev < t2_prev and t1_curr > t2_curr) or \
                       (t1_prev > t2_prev and t1_curr < t2_curr):
                        intersections.append({
                            'plots': [name1, name2],
                            'beat': beat,
                            'tensions': {
                                name1: round(t1_curr, 2),
                                name2: round(t2_curr, 2)
                            }
                        })

        return intersections

    def calculate_combined_tension(self, weights: Optional[Dict[str, float]] = None) -> List[float]:
        """
        Calculate combined tension from all plots.

        Args:
            weights: Optional weights for each plot (default: equal weighting)

        Returns:
            List of combined tension values per beat
        """
        if not self.plots:
            return []

        plot_names = list(self.plots.keys())

        # Default to equal weighting
        if weights is None:
            weights = {name: 1.0 / len(plot_names) for name in plot_names}

        # Normalize weights
        total_weight = sum(weights.values())
        weights = {k: v / total_weight for k, v in weights.items()}

        # Find maximum trajectory length
        max_length = max(len(traj) for traj in self.plots.values())

        combined_tensions = []

        for beat in range(max_length):
            beat_tension = 0

            for name in plot_names:
                trajectory = self.plots[name]
                config = self.plot_configs[name]

                # Use last state if trajectory is shorter
                if beat >= len(trajectory):
                    state = trajectory[-1]
                else:
                    state = trajectory[beat]

                tension_data = calculate_tension(
                    state,
                    genre=config['genre'],
                    subgenre=config['subgenre'],
                    custom_weights=config['custom_weights']
                )

                beat_tension += tension_data['total_tension'] * weights.get(name, 0)

            combined_tensions.append(round(beat_tension, 2))

        return combined_tensions

    def export_to_file(self, filepath: Path) -> None:
        """Export all plots and configurations to JSON file."""
        data = {
            'plots': self.plots,
            'configs': self.plot_configs
        }

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    def import_from_file(self, filepath: Path) -> None:
        """Import plots and configurations from JSON file."""
        with open(filepath, 'r') as f:
            data = json.load(f)

        self.plots = data.get('plots', {})
        self.plot_configs = data.get('configs', {})

    def generate_report(self) -> str:
        """Generate a text report of all plots."""
        if not self.plots:
            return "No plots tracked."

        lines = []
        lines.append("=" * 70)
        lines.append("SUBPLOT TRACKING REPORT")
        lines.append("=" * 70)
        lines.append(f"\nTotal Plots Tracked: {len(self.plots)}\n")

        # Analyze each plot
        for name in self.get_plot_names():
            analysis = self.analyze_plot(name)

            lines.append(f"\n{'-' * 70}")
            lines.append(f"Plot: {name}")
            if analysis['description']:
                lines.append(f"Description: {analysis['description']}")
            lines.append(f"{'-' * 70}")

            lines.append(f"\nStats:")
            lines.append(f"  Total Beats: {analysis['stats']['total_beats']}")
            lines.append(f"  Avg Tension: {analysis['stats']['avg_tension']}/10")
            lines.append(f"  Tension Range: {analysis['stats']['min_tension']}-{analysis['stats']['max_tension']}")

            lines.append(f"\nKey Moments:")
            peak = analysis['key_moments']['peak_tension']
            lines.append(f"  Peak Tension: Beat {peak['beat']} (tension: {peak['tension']})")
            low = analysis['key_moments']['lowest_tension']
            lines.append(f"  Lowest Tension: Beat {low['beat']} (tension: {low['tension']})")

        # Compare all plots
        if len(self.plots) > 1:
            lines.append(f"\n{'=' * 70}")
            lines.append("PLOT COMPARISONS")
            lines.append(f"{'=' * 70}")

            comparison = self.compare_plots()

            if comparison['synchronized_peaks']:
                lines.append("\nSynchronized Peaks:")
                for sync in comparison['synchronized_peaks']:
                    lines.append(f"  {' & '.join(sync['plots'])} peak together at beats {sync['beat_range']}")

            if comparison['intersections']:
                lines.append("\nTension Intersections:")
                for inter in comparison['intersections'][:5]:  # Show first 5
                    lines.append(f"  Beat {inter['beat']}: {' crosses '.join(inter['plots'])}")

        # Combined tension
        lines.append(f"\n{'=' * 70}")
        lines.append("COMBINED TENSION TIMELINE")
        lines.append(f"{'=' * 70}")

        combined = self.calculate_combined_tension()
        if combined:
            lines.append(f"\nAverage Combined Tension: {sum(combined) / len(combined):.2f}/10")
            lines.append(f"Peak Combined Tension: {max(combined):.2f} at beat {combined.index(max(combined))}")

        return "\n".join(lines)


# Example usage
if __name__ == "__main__":
    print("=" * 70)
    print("SUBPLOT TRACKER DEMONSTRATION")
    print("=" * 70)

    tracker = SubplotTracker()

    # Main plot: Thriller mystery
    main_plot = [
        {'stakes': 4, 'danger': 3, 'info_asymmetry': 8, 'trust': 3},
        {'stakes': 5, 'danger': 4, 'info_asymmetry': 7, 'trust': 3},
        {'stakes': 6, 'danger': 5, 'info_asymmetry': 6, 'trust': 4},
        {'stakes': 8, 'danger': 7, 'info_asymmetry': 5, 'trust': 4},
        {'stakes': 9, 'danger': 8, 'info_asymmetry': 3, 'trust': 5},
        {'stakes': 7, 'danger': 4, 'info_asymmetry': 2, 'trust': 7}
    ]

    # Romance subplot
    romance_subplot = [
        {'intimacy': 1, 'trust': 2, 'desire': 3, 'vulnerability': 1, 'goal_alignment': 4, 'proximity': 6},
        {'intimacy': 2, 'trust': 3, 'desire': 5, 'vulnerability': 3, 'goal_alignment': 5, 'proximity': 7},
        {'intimacy': 4, 'trust': 4, 'desire': 6, 'vulnerability': 4, 'goal_alignment': 6, 'proximity': 8},
        {'intimacy': 3, 'trust': 2, 'desire': 7, 'vulnerability': 2, 'goal_alignment': 3, 'proximity': 7},
        {'intimacy': 6, 'trust': 6, 'desire': 8, 'vulnerability': 7, 'goal_alignment': 8, 'proximity': 9},
        {'intimacy': 8, 'trust': 8, 'desire': 9, 'vulnerability': 8, 'goal_alignment': 9, 'proximity': 10}
    ]

    # Add plots to tracker
    tracker.add_plot(
        'main_plot',
        main_plot,
        genre='thriller',
        subgenre='psychological',
        description='Detective solving serial killer case'
    )

    tracker.add_plot(
        'romance_subplot',
        romance_subplot,
        genre='romance',
        subgenre='contemporary',
        description='Detective falls for witness'
    )

    # Generate and print report
    print(tracker.generate_report())

    # Calculate combined tension
    print("\n" + "=" * 70)
    print("COMBINED TENSION (60% main + 40% romance)")
    print("=" * 70)

    combined = tracker.calculate_combined_tension({
        'main_plot': 0.6,
        'romance_subplot': 0.4
    })

    print("\nBeat-by-beat combined tension:")
    for i, tension in enumerate(combined):
        print(f"  Beat {i}: {tension}/10")

    # Export to file
    export_path = PROJECT_ROOT / 'examples' / 'subplot_example.json'
    export_path.parent.mkdir(exist_ok=True)
    tracker.export_to_file(export_path)
    print(f"\n✓ Example exported to: {export_path}")
