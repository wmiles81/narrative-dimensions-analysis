#!/usr/bin/env python3
"""
Generate standalone HTML report with NPE axis visualization.
Creates a self-contained HTML file showing IA, RA, EA, TA progression.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List


def load_trajectory(filepath: Path) -> List[Dict]:
    """Load trajectory JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def categorize_ia_state(ia_value: float) -> str:
    """Categorize IA state."""
    if ia_value < -0.7:
        return "Deep Wound"
    elif ia_value < -0.3:
        return "Wounded"
    elif ia_value < 0:
        return "Healing"
    elif ia_value < 0.5:
        return "Growing"
    else:
        return "Transformed/Whole"


def categorize_intimacy(orbit_degrees: float) -> str:
    """Categorize relationship intimacy by orbital distance."""
    if orbit_degrees >= 160:
        return "Distant/Strangers"
    elif orbit_degrees >= 120:
        return "Acquaintances"
    elif orbit_degrees >= 90:
        return "Friends/Warming"
    elif orbit_degrees >= 60:
        return "Close/Intimate"
    else:
        return "Deep Bond"


def generate_insights(trajectory: List[Dict], ia_values: List[float], ra_orbits: List[float]) -> str:
    """Generate insight bullet points based on NPE trajectory analysis."""
    insights = []

    # Character growth
    ia_growth = ia_values[-1] - ia_values[0]
    if ia_growth > 1.0:
        insights.append(f"<li><strong>Strong character transformation:</strong> IA increased by {ia_growth:.2f} points - character moves from wounded to healed</li>")
    elif ia_growth < 0.3:
        insights.append(f"<li><strong>Limited character growth:</strong> IA only changed by {ia_growth:.2f} points - consider deepening the internal arc</li>")

    # Check for polarity flip
    crosses_zero = any(ia_values[i] < 0 and ia_values[i+1] >= 0 for i in range(len(ia_values)-1))
    if crosses_zero:
        flip_idx = next(i for i in range(len(ia_values)-1) if ia_values[i] < 0 and ia_values[i+1] >= 0)
        flip_percent = ((flip_idx + 1) / len(ia_values)) * 100
        insights.append(f"<li><strong>Polarity flip detected:</strong> Character crosses from wounded to healing at Chapter {flip_idx + 1} ({flip_percent:.0f}% through)</li>")
    else:
        if ia_values[0] < 0:
            insights.append(f"<li><strong>No polarity flip:</strong> Character remains wounded throughout - may violate genre expectations</li>")

    # Dark night detection
    darkest_idx = ia_values.index(min(ia_values))
    darkest_percent = (darkest_idx / len(ia_values)) * 100
    if 65 <= darkest_percent <= 80:
        insights.append(f"<li><strong>Well-timed dark night:</strong> Lowest IA point at Chapter {darkest_idx + 1} ({darkest_percent:.0f}% through) - perfect for dramatic structure</li>")
    elif darkest_percent < 50:
        insights.append(f"<li><strong>Early dark night:</strong> Lowest IA at Chapter {darkest_idx + 1} ({darkest_percent:.0f}% through) - consider moving crisis later</li>")

    # Relationship journey
    orbital_closure = ra_orbits[0] - ra_orbits[-1]
    if orbital_closure > 80:
        insights.append(f"<li><strong>Significant relationship development:</strong> Relationship closed {orbital_closure:.0f}° from {categorize_intimacy(ra_orbits[0]).lower()} to {categorize_intimacy(ra_orbits[-1]).lower()}</li>")

    # Ending state
    if ia_values[-1] >= 0.6 and ra_orbits[-1] <= 70:
        insights.append(f"<li><strong>Satisfying ending:</strong> Character is healed (IA: {ia_values[-1]:.2f}) and relationship is close ({ra_orbits[-1]:.0f}°)</li>")

    return "\n                ".join(insights)


def generate_npe_html_report(trajectory: List[Dict], genre: str, output_file: Path, title: str = "NPE Story Analysis"):
    """
    Generate standalone HTML report with NPE axes chart.

    Uses Chart.js for visualization (loaded from CDN).
    Shows IA, RA, EA, TA progression over story.
    """

    # Prepare data
    chapters = [f"Ch {c.get('chapter', i+1)}" for i, c in enumerate(trajectory)]

    # Extract NPE axes
    ia_values = [c.get('IA', 0) for c in trajectory]
    ra_orbits = [c.get('RA_orbit', 180) for c in trajectory]
    ea_values = [c.get('EA', 0) for c in trajectory]
    ta_values = [c.get('TA', 0) for c in trajectory]

    # For chart display, normalize RA to -1 to +1 scale for visual consistency
    ra_normalized = [(180 - orbit) / 180 * 2 - 1 for orbit in ra_orbits]

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - NPE Analysis</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #4c1d95 100%);
            color: #fff;
            padding: 2rem;
            min-height: 100vh;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        h1 {{
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            background: linear-gradient(to right, #8b5cf6, #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .subtitle {{
            text-align: center;
            color: #a78bfa;
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
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }}

        .stat-card {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 0.5rem;
            padding: 1.5rem;
            border: 1px solid rgba(167, 139, 250, 0.3);
        }}

        .stat-card h3 {{
            color: #a78bfa;
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
            color: #c4b5fd;
        }}

        .legend {{
            display: flex;
            flex-wrap: wrap;
            gap: 1.5rem;
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
            width: 24px;
            height: 4px;
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
            color: #a78bfa;
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
            border-left: 3px solid #8b5cf6;
        }}

        .insights li::before {{
            content: "💡 ";
            margin-right: 0.5rem;
        }}

        .axis-explanation {{
            background: rgba(139, 92, 246, 0.2);
            border-radius: 0.5rem;
            padding: 1.5rem;
            margin-bottom: 2rem;
            border: 1px solid rgba(139, 92, 246, 0.4);
        }}

        .axis-explanation h3 {{
            color: #c4b5fd;
            margin-bottom: 1rem;
        }}

        .axis-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
        }}

        .axis-desc {{
            background: rgba(0, 0, 0, 0.2);
            padding: 1rem;
            border-radius: 0.5rem;
        }}

        .axis-desc h4 {{
            color: #e9d5ff;
            margin-bottom: 0.5rem;
            font-size: 1rem;
        }}

        .axis-desc p {{
            font-size: 0.85rem;
            color: #ddd6fe;
            line-height: 1.5;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📖 {title}</h1>
        <p class="subtitle">NPE Arc Analysis • {genre.replace('_', ' ').title()}</p>

        <div class="axis-explanation">
            <h3>Understanding NPE Axes</h3>
            <div class="axis-grid">
                <div class="axis-desc">
                    <h4>IA (Internal Axis)</h4>
                    <p>Character's emotional state: -1 (wounded/broken) → 0 (turning point) → +1 (healed/whole)</p>
                </div>
                <div class="axis-desc">
                    <h4>RA (Relational Axis)</h4>
                    <p>Relationship distance: 180° (strangers) → 90° (friends) → 0° (intimate)</p>
                </div>
                <div class="axis-desc">
                    <h4>EA (Environmental Axis)</h4>
                    <p>External pressure: -1 (peaceful) → +1 (high stakes/danger)</p>
                </div>
                <div class="axis-desc">
                    <h4>TA (Task Axis)</h4>
                    <p>Quest completion: 0 (not started) → 1 (complete)</p>
                </div>
            </div>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <h3>Total Chapters</h3>
                <div class="stat-value">{len(trajectory)}</div>
                <div class="stat-description">Complete arc tracked</div>
            </div>

            <div class="stat-card">
                <h3>Character Transformation (IA)</h3>
                <div class="stat-value">{ia_values[-1] - ia_values[0]:+.2f}</div>
                <div class="stat-description">From {categorize_ia_state(ia_values[0]).lower()} → {categorize_ia_state(ia_values[-1]).lower()}</div>
            </div>

            <div class="stat-card">
                <h3>Relationship Journey (RA)</h3>
                <div class="stat-value">{ra_orbits[0] - ra_orbits[-1]:.0f}°</div>
                <div class="stat-description">Closed from {ra_orbits[0]:.0f}° → {ra_orbits[-1]:.0f}°</div>
            </div>

            <div class="stat-card">
                <h3>Dark Night</h3>
                <div class="stat-value">Ch {ia_values.index(min(ia_values)) + 1}</div>
                <div class="stat-description">Lowest IA: {min(ia_values):.2f}</div>
            </div>

            <div class="stat-card">
                <h3>Quest Completion (TA)</h3>
                <div class="stat-value">{ta_values[-1]:.1f}</div>
                <div class="stat-description">{'✓ Complete' if ta_values[-1] >= 0.9 else '⚠ Incomplete'}</div>
            </div>
        </div>

        <div class="chart-container">
            <canvas id="npeChart"></canvas>
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-color" style="background: #8b5cf6;"></div>
                    <span><strong>IA</strong> (Internal - Wound to Healed)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #ec4899;"></div>
                    <span><strong>RA</strong> (Relational - Orbital Distance)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #f59e0b;"></div>
                    <span><strong>EA</strong> (Environmental Pressure)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #10b981;"></div>
                    <span><strong>TA</strong> (Task/Quest Progress)</span>
                </div>
            </div>
        </div>

        <div class="insights">
            <h2>📊 Key Insights</h2>
            <ul>
                {generate_insights(trajectory, ia_values, ra_orbits)}
            </ul>
        </div>
    </div>

    <script>
        const ctx = document.getElementById('npeChart').getContext('2d');

        // Custom plugin to draw zero line
        const zeroLinePlugin = {{
            id: 'zeroLine',
            afterDraw: (chart) => {{
                const ctx = chart.ctx;
                const yAxis = chart.scales.y;
                const xAxis = chart.scales.x;
                const zeroY = yAxis.getPixelForValue(0);

                ctx.save();
                ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.beginPath();
                ctx.moveTo(xAxis.left, zeroY);
                ctx.lineTo(xAxis.right, zeroY);
                ctx.stroke();
                ctx.restore();
            }}
        }};

        const chart = new Chart(ctx, {{
            type: 'line',
            data: {{
                labels: {json.dumps(chapters)},
                datasets: [
                    {{
                        label: 'IA (Internal Axis)',
                        data: {json.dumps(ia_values)},
                        borderColor: '#8b5cf6',
                        backgroundColor: 'rgba(139, 92, 246, 0.1)',
                        tension: 0.4,
                        fill: false,
                        borderWidth: 3,
                        pointRadius: 4,
                        pointBackgroundColor: '#8b5cf6'
                    }},
                    {{
                        label: 'RA (Relational - normalized)',
                        data: {json.dumps(ra_normalized)},
                        borderColor: '#ec4899',
                        backgroundColor: 'rgba(236, 72, 153, 0.1)',
                        tension: 0.4,
                        fill: false,
                        borderWidth: 3,
                        pointRadius: 4,
                        pointBackgroundColor: '#ec4899'
                    }},
                    {{
                        label: 'EA (Environmental)',
                        data: {json.dumps(ea_values)},
                        borderColor: '#f59e0b',
                        backgroundColor: 'rgba(245, 158, 11, 0.1)',
                        tension: 0.4,
                        fill: false,
                        borderWidth: 2,
                        pointRadius: 3,
                        pointBackgroundColor: '#f59e0b'
                    }},
                    {{
                        label: 'TA (Task Progress)',
                        data: {json.dumps(ta_values)},
                        borderColor: '#10b981',
                        backgroundColor: 'rgba(16, 185, 129, 0.1)',
                        tension: 0.4,
                        fill: false,
                        borderWidth: 2,
                        pointRadius: 3,
                        pointBackgroundColor: '#10b981'
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
                        backgroundColor: 'rgba(15, 23, 42, 0.95)',
                        titleColor: '#a78bfa',
                        bodyColor: '#fff',
                        borderColor: '#8b5cf6',
                        borderWidth: 1,
                        padding: 12,
                        displayColors: true,
                        callbacks: {{
                            afterLabel: function(context) {{
                                const chapterIdx = context.dataIndex;
                                const ia = {json.dumps(ia_values)}[chapterIdx];
                                const ra = {json.dumps(ra_orbits)}[chapterIdx];

                                if (context.datasetIndex === 0) {{
                                    return 'State: ' + {json.dumps([categorize_ia_state(ia) for ia in ia_values])}[chapterIdx];
                                }} else if (context.datasetIndex === 1) {{
                                    return 'Orbital: ' + ra.toFixed(0) + '° (' + {json.dumps([categorize_intimacy(orbit) for orbit in ra_orbits])}[chapterIdx] + ')';
                                }}
                                return '';
                            }}
                        }}
                    }}
                }},
                scales: {{
                    y: {{
                        min: -1,
                        max: 1,
                        grid: {{
                            color: 'rgba(255, 255, 255, 0.1)'
                        }},
                        ticks: {{
                            color: '#a78bfa',
                            callback: function(value) {{
                                if (value === 0) return '0 (Zero Point)';
                                if (value === -1) return '-1 (Wounded)';
                                if (value === 1) return '+1 (Healed)';
                                return value.toFixed(1);
                            }}
                        }}
                    }},
                    x: {{
                        grid: {{
                            color: 'rgba(255, 255, 255, 0.05)'
                        }},
                        ticks: {{
                            color: '#a78bfa',
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
            }},
            plugins: [zeroLinePlugin]
        }});
    </script>
</body>
</html>"""

    # Write HTML file
    with open(output_file, 'w') as f:
        f.write(html)

    print(f"✓ Generated NPE HTML report: {output_file}")
    print(f"  Open in browser to view interactive NPE visualization")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_npe_html_report.py <trajectory.json> [genre] [output.html]")
        print("\nGenre options: cozy_fantasy, dark_romance, thriller, mystery, etc.")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    genre = sys.argv[2] if len(sys.argv) > 2 else "cozy_fantasy"
    output_path = Path(sys.argv[3]) if len(sys.argv) > 3 else input_path.parent / f"{input_path.stem}_npe_report.html"

    trajectory = load_trajectory(input_path)
    title = input_path.stem.replace('_', ' ').title()

    generate_npe_html_report(trajectory, genre, output_path, title)
