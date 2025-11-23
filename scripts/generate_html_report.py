#!/usr/bin/env python3
"""
Generate standalone HTML report with embedded visualization.
Creates a self-contained HTML file that doesn't require a web server.
Genre-aware: shows appropriate dimensions based on story genre.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple


# Genre-specific dimension configurations
GENRE_DIMENSIONS = {
    'romance': {
        'dimensions': ['intimacy', 'trust', 'desire', 'vulnerability', 'stakes'],
        'labels': ['Intimacy', 'Trust', 'Desire', 'Vulnerability', 'Stakes'],
        'colors': ['#e91e63', '#00e676', '#d500f9', '#2979ff', '#ff1744'],
        'stats': [
            ('intimacy', 'Intimacy Growth'),
            ('trust', 'Trust Journey'),
            ('desire', 'Desire Arc')
        ]
    },
    'dark_romance': {
        'dimensions': ['intimacy', 'trust', 'vulnerability', 'stakes', 'power_differential'],
        'labels': ['Intimacy', 'Trust', 'Vulnerability', 'Stakes', 'Power Imbalance'],
        'colors': ['#e91e63', '#00e676', '#2979ff', '#ff1744', '#9c27b0'],
        'stats': [
            ('intimacy', 'Intimacy Arc'),
            ('vulnerability', 'Vulnerability Journey'),
            ('stakes', 'Stakes Escalation')
        ]
    },
    'cozy_fantasy': {
        'dimensions': ['self_worth', 'trust', 'vulnerability', 'stakes', 'goal_alignment'],
        'labels': ['Self-Worth', 'Trust (in Magic/Friends)', 'Vulnerability', 'Stakes', 'Quest Progress'],
        'colors': ['#8b5cf6', '#00e676', '#2979ff', '#ff1744', '#10b981'],
        'stats': [
            ('self_worth', 'Character Growth'),
            ('trust', 'Trust Building'),
            ('goal_alignment', 'Quest Progress')
        ]
    },
    'cozy_mystery': {
        'dimensions': ['self_worth', 'trust', 'stakes', 'info_asymmetry', 'goal_alignment'],
        'labels': ['Self-Worth', 'Trust', 'Stakes', 'Mystery/Clues', 'Investigation Progress'],
        'colors': ['#8b5cf6', '#00e676', '#ff1744', '#f59e0b', '#10b981'],
        'stats': [
            ('self_worth', 'Character Growth'),
            ('info_asymmetry', 'Mystery Depth'),
            ('goal_alignment', 'Case Progress')
        ]
    },
    'thriller': {
        'dimensions': ['stakes', 'info_asymmetry', 'vulnerability', 'trust', 'goal_alignment'],
        'labels': ['Stakes/Danger', 'Secrets/Unknown', 'Vulnerability', 'Trust', 'Goal Clarity'],
        'colors': ['#ff1744', '#f59e0b', '#2979ff', '#00e676', '#10b981'],
        'stats': [
            ('stakes', 'Peak Danger'),
            ('info_asymmetry', 'Mystery Complexity'),
            ('vulnerability', 'Character Exposure')
        ]
    },
    'psychological_horror': {
        'dimensions': ['self_worth', 'vulnerability', 'stakes', 'trust', 'info_asymmetry'],
        'labels': ['Self-Worth (Dissolution)', 'Vulnerability', 'Stakes', 'Trust (Erosion)', 'Reality/Unreality'],
        'colors': ['#6b21a8', '#2979ff', '#ff1744', '#9ca3af', '#f59e0b'],
        'stats': [
            ('self_worth', 'Psychological State'),
            ('vulnerability', 'Emotional Exposure'),
            ('info_asymmetry', 'Reality Distortion')
        ]
    },
    'epic_fantasy': {
        'dimensions': ['self_worth', 'stakes', 'trust', 'goal_alignment', 'vulnerability'],
        'labels': ['Hero Development', 'World Stakes', 'Alliances/Trust', 'Quest Progress', 'Sacrifice/Risk'],
        'colors': ['#8b5cf6', '#ff1744', '#00e676', '#10b981', '#2979ff'],
        'stats': [
            ('self_worth', 'Hero Journey'),
            ('stakes', 'World Peril'),
            ('goal_alignment', 'Quest Progress')
        ]
    }
}


def load_trajectory(filepath: Path) -> List[Dict]:
    """Load trajectory JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def get_genre_config(genre: str) -> Dict:
    """Get dimension configuration for genre, with fallback to cozy_fantasy."""
    genre_normalized = genre.lower().replace(' ', '_')

    if genre_normalized in GENRE_DIMENSIONS:
        return GENRE_DIMENSIONS[genre_normalized]

    # Fallback to cozy_fantasy for unknown genres
    print(f"Warning: Unknown genre '{genre}', using cozy_fantasy dimensions")
    return GENRE_DIMENSIONS['cozy_fantasy']


def calc_tension_for_genre(chapter: Dict, genre: str) -> float:
    """Calculate tension based on genre-specific factors."""
    genre_normalized = genre.lower().replace(' ', '_')

    # Base components
    stakes = chapter.get('stakes', 0)
    info_asym = chapter.get('info_asymmetry', 0)
    misalignment = 10 - chapter.get('goal_alignment', 5)
    vuln = chapter.get('vulnerability', 0)
    trust = chapter.get('trust', 5)
    vuln_trust_gap = vuln * (10 - trust) / 10

    if genre_normalized in ['romance', 'dark_romance']:
        desire = chapter.get('desire', 0)
        intimacy = chapter.get('intimacy', 0)
        desire_intimacy_gap = desire * (10 - intimacy) / 10
        power_diff = abs(chapter.get('power_differential', 0))

        tension = (
            info_asym * 0.6 +
            stakes * 0.8 +
            misalignment * 1.0 +
            power_diff * 0.4 +
            vuln_trust_gap * 1.2 +
            desire_intimacy_gap * 1.0
        )
    elif genre_normalized in ['cozy_fantasy', 'cozy_mystery']:
        # Cozy genres: tension from stakes, vulnerability, and progress barriers
        tension = (
            stakes * 0.8 +
            info_asym * 0.5 +
            misalignment * 1.2 +
            vuln_trust_gap * 0.8
        )
    elif genre_normalized in ['thriller', 'psychological_horror']:
        # Suspense genres: high stakes, mystery, vulnerability
        tension = (
            stakes * 1.5 +
            info_asym * 1.2 +
            misalignment * 0.8 +
            vuln_trust_gap * 1.0
        )
    else:  # epic_fantasy and others
        tension = (
            stakes * 1.2 +
            info_asym * 0.6 +
            misalignment * 1.0 +
            vuln_trust_gap * 0.8
        )

    return min(10, tension / 5)  # Normalize to 0-10


def generate_insights(trajectory: List[Dict], dimension_values: List[List[float]],
                      dimension_names: List[str], tension: List[float], genre: str) -> str:
    """Generate insight bullet points based on trajectory analysis."""
    insights = []

    # Generic insights for first tracked dimension (usually primary emotional dimension)
    if dimension_values and len(dimension_values[0]) > 1:
        primary_dim = dimension_names[0]
        primary_values = dimension_values[0]
        growth = primary_values[-1] - primary_values[0]

        if growth > 3:
            insights.append(f"<li><strong>Strong {primary_dim} progression:</strong> Increased by {growth:.1f} points - clear character development</li>")
        elif growth < -2:
            insights.append(f"<li><strong>{primary_dim} decline:</strong> Decreased by {abs(growth):.1f} points - character faces setbacks</li>")

    # Tension insights
    peak_tension_idx = tension.index(max(tension))
    peak_tension_percent = (peak_tension_idx / len(tension)) * 100

    if 60 <= peak_tension_percent <= 80:
        insights.append(f"<li><strong>Well-paced crisis:</strong> Peak tension at Chapter {peak_tension_idx + 1} ({peak_tension_percent:.0f}% through) - ideal timing</li>")
    elif peak_tension_percent < 40:
        insights.append(f"<li><strong>Early crisis:</strong> Peak tension at Chapter {peak_tension_idx + 1} ({peak_tension_percent:.0f}% through) - consider building more toward climax</li>")

    # Low tension warning
    low_tension_chapters = [i+1 for i, t in enumerate(tension) if t < 2.0]
    if len(low_tension_chapters) > len(tension) * 0.3:
        insights.append(f"<li><strong>Pacing concern:</strong> {len(low_tension_chapters)} chapters with low tension - story may feel slow in places</li>")

    # Arc shape
    if len(tension) > 5:
        first_third_avg = sum(tension[:len(tension)//3]) / (len(tension)//3)
        last_third_avg = sum(tension[-len(tension)//3:]) / (len(tension)//3)

        if last_third_avg > first_third_avg * 1.5:
            insights.append(f"<li><strong>Escalating tension:</strong> Final act is {last_third_avg/first_third_avg:.1f}x more tense than opening - good momentum building</li>")

    return "\n                ".join(insights)


def generate_html_report(trajectory: List[Dict], genre: str, output_file: Path, title: str = "Story Analysis"):
    """
    Generate standalone HTML report with chart.
    Uses Chart.js for visualization (loaded from CDN).
    Shows genre-appropriate dimensions.
    """

    # Get genre configuration
    config = get_genre_config(genre)

    # Prepare data
    chapters = [f"Ch {c.get('chapter', i+1)}" for i, c in enumerate(trajectory)]

    # Extract genre-specific dimensions
    dimension_data = []
    for dim in config['dimensions']:
        dimension_data.append([c.get(dim, 0) for c in trajectory])

    # Calculate tension
    tension = [calc_tension_for_genre(c, genre) for c in trajectory]

    # Generate stat cards HTML
    stat_cards_html = f"""
            <div class="stat-card">
                <h3>Total Chapters</h3>
                <div class="stat-value">{len(trajectory)}</div>
                <div class="stat-description">Complete story progression tracked</div>
            </div>
"""

    for dim_key, dim_label in config['stats']:
        if dim_key in config['dimensions']:
            idx = config['dimensions'].index(dim_key)
            values = dimension_data[idx]
            growth = values[-1] - values[0]
            stat_cards_html += f"""
            <div class="stat-card">
                <h3>{dim_label}</h3>
                <div class="stat-value">{growth:+.1f}</div>
                <div class="stat-description">From {values[0]:.1f} → {values[-1]:.1f}</div>
            </div>
"""

    stat_cards_html += f"""
            <div class="stat-card">
                <h3>Peak Tension</h3>
                <div class="stat-value">{max(tension):.1f}/10</div>
                <div class="stat-description">Highest tension at Chapter {tension.index(max(tension)) + 1}</div>
            </div>
"""

    # Generate legend HTML
    legend_html = ""
    for i, (label, color) in enumerate(zip(config['labels'], config['colors'])):
        legend_html += f"""
                <div class="legend-item">
                    <div class="legend-color" style="background: {color};"></div>
                    <span>{label}</span>
                </div>
"""
    legend_html += """
                <div class="legend-item">
                    <div class="legend-color" style="background: #ff9800; font-weight: bold;"></div>
                    <span>TENSION</span>
                </div>
"""

    # Generate dataset JSON for Chart.js
    datasets_json = []
    for i, (label, color, values) in enumerate(zip(config['labels'], config['colors'], dimension_data)):
        datasets_json.append({
            'label': label,
            'data': values,
            'borderColor': color,
            'backgroundColor': f'rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.1)',
            'tension': 0.4,
            'fill': False,
            'borderWidth': 2
        })

    # Add tension dataset
    datasets_json.append({
        'label': 'TENSION',
        'data': tension,
        'borderColor': '#ff9800',
        'backgroundColor': 'rgba(255, 152, 0, 0.1)',
        'tension': 0.4,
        'fill': False,
        'borderWidth': 3,
        'borderDash': [5, 5]
    })

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Narrative Analysis</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #1e293b 0%, #581c87 100%);
            color: #fff;
            padding: 2rem;
            min-height: 100vh;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        h1 {{
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            background: linear-gradient(to right, #e91e63, #9c27b0);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .subtitle {{
            text-align: center;
            color: #c084fc;
            margin-bottom: 2rem;
            font-size: 1.1rem;
        }}

        .chart-container {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 1rem;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }}

        .stat-card {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 0.5rem;
            padding: 1.5rem;
            border: 1px solid rgba(192, 132, 252, 0.3);
        }}

        .stat-card h3 {{
            color: #c084fc;
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .stat-value {{
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 0.25rem;
        }}

        .stat-description {{
            font-size: 0.85rem;
            color: #e9d5ff;
        }}

        .legend {{
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            justify-content: center;
            margin-top: 1.5rem;
        }}

        .legend-item {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.9rem;
        }}

        .legend-color {{
            width: 20px;
            height: 3px;
            border-radius: 2px;
        }}

        .insights {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 1rem;
            padding: 2rem;
            margin-top: 2rem;
        }}

        .insights h2 {{
            color: #c084fc;
            margin-bottom: 1rem;
        }}

        .insights ul {{
            list-style: none;
            padding-left: 0;
        }}

        .insights li {{
            padding: 0.75rem;
            margin-bottom: 0.5rem;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 0.5rem;
            border-left: 3px solid #9c27b0;
        }}

        .insights li::before {{
            content: "💡 ";
            margin-right: 0.5rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📖 {title}</h1>
        <p class="subtitle">Dimensional Analysis • {genre.replace('_', ' ').title()}</p>

        <div class="stats-grid">
{stat_cards_html}
        </div>

        <div class="chart-container">
            <canvas id="storyChart"></canvas>
            <div class="legend">
{legend_html}
            </div>
        </div>

        <div class="insights">
            <h2>📊 Key Insights</h2>
            <ul>
                {generate_insights(trajectory, dimension_data, config['labels'], tension, genre)}
            </ul>
        </div>
    </div>

    <script>
        const ctx = document.getElementById('storyChart').getContext('2d');
        const chart = new Chart(ctx, {{
            type: 'line',
            data: {{
                labels: {json.dumps(chapters)},
                datasets: {json.dumps(datasets_json)}
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: true,
                aspectRatio: 2,
                plugins: {{
                    legend: {{
                        display: false
                    }},
                    tooltip: {{
                        mode: 'index',
                        intersect: false,
                        backgroundColor: 'rgba(30, 41, 59, 0.95)',
                        titleColor: '#c084fc',
                        bodyColor: '#fff',
                        borderColor: '#9c27b0',
                        borderWidth: 1,
                        padding: 12,
                        displayColors: true
                    }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        max: 10,
                        grid: {{
                            color: 'rgba(255, 255, 255, 0.1)'
                        }},
                        ticks: {{
                            color: '#c084fc'
                        }}
                    }},
                    x: {{
                        grid: {{
                            color: 'rgba(255, 255, 255, 0.05)'
                        }},
                        ticks: {{
                            color: '#c084fc',
                            maxRotation: 45,
                            minRotation: 45
                        }}
                    }}
                }},
                interaction: {{
                    mode: 'nearest',
                    axis: 'x',
                    intersect: false
                }}
            }}
        }});
    </script>
</body>
</html>"""

    # Write HTML file
    with open(output_file, 'w') as f:
        f.write(html)

    print(f"✓ Generated HTML report: {output_file}")
    print(f"  Genre: {genre}")
    print(f"  Dimensions: {', '.join(config['labels'])}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_html_report.py <trajectory.json> [genre] [output.html]")
        print("\nGenre options:")
        for genre in GENRE_DIMENSIONS.keys():
            print(f"  - {genre}")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    genre = sys.argv[2] if len(sys.argv) > 2 else "cozy_fantasy"
    output_path = Path(sys.argv[3]) if len(sys.argv) > 3 else input_path.parent / f"{input_path.stem}_report.html"

    trajectory = load_trajectory(input_path)
    title = input_path.stem.replace('_trajectory', '').replace('_', ' ').title()

    generate_html_report(trajectory, genre, output_path, title)
