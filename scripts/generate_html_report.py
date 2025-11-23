#!/usr/bin/env python3
"""
Generate standalone HTML report with embedded visualization.
Creates a self-contained HTML file that doesn't require a web server.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List


def load_trajectory(filepath: Path) -> List[Dict]:
    """Load trajectory JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def generate_html_report(trajectory: List[Dict], genre: str, output_file: Path, title: str = "Story Analysis"):
    """
    Generate standalone HTML report with chart.

    Uses Chart.js for visualization (loaded from CDN).
    Creates simple, author-friendly visualization.
    """

    # Prepare data
    chapters = [f"Ch {c.get('chapter', i+1)}" for i, c in enumerate(trajectory)]

    # Extract key dimensions
    intimacy = [c.get('intimacy', 0) for c in trajectory]
    trust = [c.get('trust', 0) for c in trajectory]
    desire = [c.get('desire', 0) for c in trajectory]
    stakes = [c.get('stakes', 0) for c in trajectory]
    vulnerability = [c.get('vulnerability', 0) for c in trajectory]

    # Calculate tension (simplified)
    def calc_tension(chapter):
        misalignment = 10 - chapter.get('goal_alignment', 5)
        vuln_trust_gap = chapter.get('vulnerability', 0) * (10 - chapter.get('trust', 5)) / 10
        desire_intimacy_gap = chapter.get('desire', 0) * (10 - chapter.get('intimacy', 0)) / 10

        tension = (
            chapter.get('info_asymmetry', 0) * 0.6 +
            chapter.get('stakes', 0) * 0.8 +
            misalignment * 1.0 +
            abs(chapter.get('power_differential', 0)) * 0.4 +
            vuln_trust_gap * 1.2 +
            desire_intimacy_gap * 1.0
        )
        return min(10, tension / 5)  # Normalize to 0-10

    tension = [calc_tension(c) for c in trajectory]

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
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
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
            color: #d8b4fe;
        }}

        .legend {{
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            justify-content: center;
            margin-top: 1rem;
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
        <p class="subtitle">Story Arc Analysis • {genre.replace('_', ' ').title()}</p>

        <div class="stats-grid">
            <div class="stat-card">
                <h3>Total Chapters</h3>
                <div class="stat-value">{len(trajectory)}</div>
                <div class="stat-description">Complete story progression tracked</div>
            </div>

            <div class="stat-card">
                <h3>Intimacy Growth</h3>
                <div class="stat-value">{intimacy[-1] - intimacy[0]:+.1f}</div>
                <div class="stat-description">From {intimacy[0]:.1f} → {intimacy[-1]:.1f}</div>
            </div>

            <div class="stat-card">
                <h3>Trust Journey</h3>
                <div class="stat-value">{trust[-1] - trust[0]:+.1f}</div>
                <div class="stat-description">From {trust[0]:.1f} → {trust[-1]:.1f}</div>
            </div>

            <div class="stat-card">
                <h3>Peak Tension</h3>
                <div class="stat-value">{max(tension):.1f}/10</div>
                <div class="stat-description">Highest tension at Chapter {tension.index(max(tension)) + 1}</div>
            </div>
        </div>

        <div class="chart-container">
            <canvas id="storyChart"></canvas>
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-color" style="background: #e91e63;"></div>
                    <span>Intimacy</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #00e676;"></div>
                    <span>Trust</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #d500f9;"></div>
                    <span>Desire</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #ff1744;"></div>
                    <span>Stakes</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #2979ff;"></div>
                    <span>Vulnerability</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #ff9800; font-weight: bold;"></div>
                    <span>TENSION</span>
                </div>
            </div>
        </div>

        <div class="insights">
            <h2>📊 Key Insights</h2>
            <ul>
                {generate_insights(trajectory, intimacy, trust, tension)}
            </ul>
        </div>
    </div>

    <script>
        const ctx = document.getElementById('storyChart').getContext('2d');
        const chart = new Chart(ctx, {{
            type: 'line',
            data: {{
                labels: {json.dumps(chapters)},
                datasets: [
                    {{
                        label: 'Intimacy',
                        data: {json.dumps(intimacy)},
                        borderColor: '#e91e63',
                        backgroundColor: 'rgba(233, 30, 99, 0.1)',
                        tension: 0.4,
                        fill: false,
                        borderWidth: 2
                    }},
                    {{
                        label: 'Trust',
                        data: {json.dumps(trust)},
                        borderColor: '#00e676',
                        backgroundColor: 'rgba(0, 230, 118, 0.1)',
                        tension: 0.4,
                        fill: false,
                        borderWidth: 2
                    }},
                    {{
                        label: 'Desire',
                        data: {json.dumps(desire)},
                        borderColor: '#d500f9',
                        backgroundColor: 'rgba(213, 0, 249, 0.1)',
                        tension: 0.4,
                        fill: false,
                        borderWidth: 2
                    }},
                    {{
                        label: 'Stakes',
                        data: {json.dumps(stakes)},
                        borderColor: '#ff1744',
                        backgroundColor: 'rgba(255, 23, 68, 0.1)',
                        tension: 0.4,
                        fill: false,
                        borderWidth: 2
                    }},
                    {{
                        label: 'Vulnerability',
                        data: {json.dumps(vulnerability)},
                        borderColor: '#2979ff',
                        backgroundColor: 'rgba(41, 121, 255, 0.1)',
                        tension: 0.4,
                        fill: false,
                        borderWidth: 2
                    }},
                    {{
                        label: 'TENSION',
                        data: {json.dumps(tension)},
                        borderColor: '#ff9800',
                        backgroundColor: 'rgba(255, 152, 0, 0.2)',
                        tension: 0.4,
                        fill: true,
                        borderWidth: 3,
                        pointRadius: 4,
                        pointBackgroundColor: '#ff9800'
                    }}
                ]
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
                        borderColor: '#8b5cf6',
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
    print(f"  Open in browser to view interactive visualization")


def generate_insights(trajectory: List[Dict], intimacy: List[float], trust: List[float], tension: List[float]) -> str:
    """Generate insight bullet points based on trajectory analysis."""
    insights = []

    # Character growth
    intimacy_growth = intimacy[-1] - intimacy[0]
    if intimacy_growth > 5:
        insights.append(f"<li><strong>Strong character growth:</strong> Intimacy increased by {intimacy_growth:.1f} points, showing significant relationship development</li>")
    elif intimacy_growth < 2:
        insights.append(f"<li><strong>Limited intimacy growth:</strong> Consider deepening the emotional connection (only {intimacy_growth:.1f} point change)</li>")

    # Trust journey
    trust_change = trust[-1] - trust[0]
    if trust_change > 4:
        insights.append(f"<li><strong>Trust rebuilt successfully:</strong> Trust increased by {trust_change:.1f} points from start to finish</li>")

    # Dark night detection
    darkest_point = tension.index(max(tension))
    darkest_percent = (darkest_point / len(tension)) * 100
    if 65 <= darkest_percent <= 80:
        insights.append(f"<li><strong>Well-timed dark night:</strong> Peak tension at Chapter {darkest_point + 1} ({darkest_percent:.0f}% through) - perfect for dramatic structure</li>")
    elif darkest_percent < 50:
        insights.append(f"<li><strong>Early peak tension:</strong> Highest tension at Chapter {darkest_point + 1} ({darkest_percent:.0f}% through) - consider moving crisis later</li>")

    # Pacing check
    flat_chapters = sum(1 for i in range(1, len(intimacy)) if abs(intimacy[i] - intimacy[i-1]) < 0.3 and abs(trust[i] - trust[i-1]) < 0.3)
    if flat_chapters > len(trajectory) * 0.3:
        insights.append(f"<li><strong>Pacing concern:</strong> {flat_chapters} chapters with minimal emotional movement - consider adding more dimensional shifts</li>")
    else:
        insights.append(f"<li><strong>Good pacing:</strong> Consistent emotional movement throughout the story</li>")

    # Ending state
    if intimacy[-1] >= 8 and trust[-1] >= 7:
        insights.append(f"<li><strong>Satisfying ending:</strong> High intimacy ({intimacy[-1]:.1f}) and trust ({trust[-1]:.1f}) create strong resolution</li>")

    return "\n                ".join(insights)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_html_report.py <trajectory.json> [genre] [output.html]")
        print("\nGenre options: romance, dark_romance, cozy_fantasy, thriller, mystery")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    genre = sys.argv[2] if len(sys.argv) > 2 else "romance"
    output_path = Path(sys.argv[3]) if len(sys.argv) > 3 else input_path.parent / f"{input_path.stem}_report.html"

    trajectory = load_trajectory(input_path)
    title = input_path.stem.replace('_', ' ').title()

    generate_html_report(trajectory, genre, output_path, title)
