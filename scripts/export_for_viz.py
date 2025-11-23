#!/usr/bin/env python3
"""
Export trajectory data in format compatible with React visualization component.
Converts dimensional trajectory data to format expected by UniversalNarrativeAnalyzer.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List


def load_trajectory(filepath: Path) -> List[Dict]:
    """Load trajectory JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def convert_to_viz_format(trajectory: List[Dict], genre: str = "romance") -> Dict:
    """
    Convert internal trajectory format to React component format.

    Args:
        trajectory: List of chapter states with dimensions
        genre: Genre key (romance, scienceFiction, fantasy, mysteryThrillerSuspense)

    Returns:
        Dict with metadata and converted data points
    """
    total_chapters = len(trajectory)

    # Map chapter indices to percentage through story
    viz_data = []

    for i, chapter in enumerate(trajectory):
        # Calculate percentage through story
        time_percent = ((i + 1) / total_chapters) * 100

        # Extract dimensions (with defaults)
        point = {
            'time': round(time_percent, 1),
            'label': chapter.get('title', f"Chapter {chapter.get('chapter', i+1)}"),
            'chapter': chapter.get('chapter', i + 1),

            # Core dimensions
            'intimacy': chapter.get('intimacy', 0),
            'powerDiff': chapter.get('power_differential', 0),
            'infoAsym': chapter.get('info_asymmetry', 0),
            'alignment': chapter.get('goal_alignment', 5),
            'proximity': chapter.get('proximity', 5),
            'vulnerability': chapter.get('vulnerability', 0),
            'desire': chapter.get('desire', 0),
            'stakes': chapter.get('stakes', 0),
            'trust': chapter.get('trust', 0),

            # Optional dimensions
            'danger': chapter.get('danger', 0),
            'mystery': chapter.get('mystery', 0),
        }

        # Add beat information if available
        if 'beat' in chapter:
            point['beat'] = chapter['beat']

        viz_data.append(point)

    # Calculate genre from trajectory characteristics if not provided
    if not genre:
        genre = detect_genre(trajectory)

    return {
        'genre': genre,
        'totalChapters': total_chapters,
        'data': viz_data,
        'metadata': {
            'title': trajectory[0].get('title', 'Story'),
            'exported': True
        }
    }


def detect_genre(trajectory: List[Dict]) -> str:
    """
    Attempt to detect genre from trajectory characteristics.

    Returns genre key for React component:
    - 'romance'
    - 'scienceFiction'
    - 'fantasy'
    - 'mysteryThrillerSuspense'
    """
    # Calculate average values across trajectory
    avg_desire = sum(c.get('desire', 0) for c in trajectory) / len(trajectory)
    avg_intimacy = sum(c.get('intimacy', 0) for c in trajectory) / len(trajectory)
    avg_danger = sum(c.get('danger', 0) for c in trajectory) / len(trajectory)
    avg_mystery = sum(c.get('mystery', 0) for c in trajectory) / len(trajectory)

    # Simple heuristics
    if avg_desire > 5 and avg_intimacy > 4:
        return 'romance'
    elif avg_mystery > 5:
        return 'mysteryThrillerSuspense'
    elif avg_danger > 6:
        # Check for sci-fi vs fantasy indicators
        # This is a rough heuristic - in practice you'd want genre metadata
        return 'fantasy'
    else:
        return 'romance'  # Default


def export_for_react_viz(input_file: Path, output_file: Path, genre: str = None):
    """
    Export trajectory for React visualization component.

    Args:
        input_file: Path to trajectory JSON
        output_file: Path for output JSON
        genre: Optional genre override
    """
    # Load trajectory
    trajectory = load_trajectory(input_file)

    # Convert to viz format
    viz_data = convert_to_viz_format(trajectory, genre)

    # Write output
    with open(output_file, 'w') as f:
        json.dump(viz_data, f, indent=2)

    print(f"✓ Exported {len(viz_data['data'])} data points to {output_file}")
    print(f"  Genre: {viz_data['genre']}")
    print(f"  Chapters: {viz_data['totalChapters']}")
    print(f"\nTo use in React component:")
    print(f"  import vizData from './{output_file.name}';")
    print(f"  // Then replace presetArcs['{viz_data['genre']}'] with vizData.data")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python export_for_viz.py <trajectory.json> [output.json] [genre]")
        print("\nGenre options: romance, scienceFiction, fantasy, mysteryThrillerSuspense")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.parent / f"{input_path.stem}_viz.json"
    genre = sys.argv[3] if len(sys.argv) > 3 else None

    export_for_react_viz(input_path, output_path, genre)
