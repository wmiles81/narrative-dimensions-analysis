#!/usr/bin/env python3
"""
Launch the React visualization app with story data.
Prepares data file and opens browser to interactive visualization.
"""

import json
import sys
import os
import subprocess
import webbrowser
from pathlib import Path
from typing import Dict, List, Optional
import time
import signal


def prepare_viz_data(trajectory_file: Path, output_file: Path, metadata: Optional[Dict] = None):
    """
    Prepare trajectory data for visualization.
    Converts internal format to viz-app format.
    """
    with open(trajectory_file, 'r') as f:
        trajectory = json.load(f)

    # Auto-detect format and add metadata
    viz_data = {
        'trajectory': trajectory,
        'metadata': metadata or {
            'title': trajectory_file.stem.replace('_', ' ').title(),
            'genre': 'fantasy',  # Default, can be overridden
            'totalChapters': len(trajectory),
        }
    }

    # Write to public directory where React app can access it
    with open(output_file, 'w') as f:
        json.dump(viz_data, f, indent=2)

    print(f"✓ Prepared visualization data: {output_file}")
    return output_file


def check_viz_app_installed():
    """Check if viz-app dependencies are installed."""
    viz_dir = Path(__file__).parent.parent / 'viz-app'
    node_modules = viz_dir / 'node_modules'

    return node_modules.exists()


def install_viz_app():
    """Install viz-app dependencies."""
    viz_dir = Path(__file__).parent.parent / 'viz-app'

    print("📦 Installing visualization app dependencies...")
    print("   This may take a few minutes on first run...")

    try:
        result = subprocess.run(
            ['npm', 'install'],
            cwd=viz_dir,
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode == 0:
            print("✓ Dependencies installed successfully")
            return True
        else:
            print(f"✗ Installation failed: {result.stderr}")
            return False
    except FileNotFoundError:
        print("✗ npm not found. Please install Node.js and npm first.")
        print("   Download from: https://nodejs.org/")
        return False
    except subprocess.TimeoutExpired:
        print("✗ Installation timed out")
        return False


def start_dev_server(viz_dir: Path):
    """Start the Vite development server."""
    print("🚀 Starting visualization server...")

    process = subprocess.Popen(
        ['npm', 'run', 'dev'],
        cwd=viz_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        preexec_fn=os.setsid if os.name != 'nt' else None
    )

    # Wait for server to be ready
    print("   Waiting for server to start...")
    time.sleep(3)

    return process


def launch_viz(trajectory_file: Path, genre: str = 'fantasy', mode: str = 'dimensions',
               title: Optional[str] = None):
    """
    Main function to launch visualization app.

    Args:
        trajectory_file: Path to trajectory JSON file
        genre: Genre of the story (fantasy, romance, etc.)
        mode: Analysis mode ('dimensions' or 'npe')
        title: Optional story title
    """
    viz_dir = Path(__file__).parent.parent / 'viz-app'

    if not viz_dir.exists():
        print(f"✗ Visualization app not found at {viz_dir}")
        return

    # Check if dependencies are installed
    if not check_viz_app_installed():
        print("\n📦 First-time setup required...")
        if not install_viz_app():
            print("\n✗ Failed to install dependencies. Please run:")
            print(f"   cd {viz_dir}")
            print("   npm install")
            return

    # Prepare data file
    data_dir = viz_dir / 'public' / 'data'
    data_dir.mkdir(parents=True, exist_ok=True)

    data_file = data_dir / 'story_data.json'

    metadata = {
        'title': title or trajectory_file.stem.replace('_', ' ').title(),
        'genre': genre,
        'totalChapters': 0  # Will be set by prepare_viz_data
    }

    prepare_viz_data(trajectory_file, data_file, metadata)

    # Start dev server
    server_process = start_dev_server(viz_dir)

    # Build URL with query parameters
    url = f"http://localhost:3000/?data=/data/story_data.json&mode={mode}&genre={genre}"

    print(f"\n✓ Visualization app starting...")
    print(f"   URL: {url}")
    print(f"   Mode: {mode}")
    print(f"   Genre: {genre}")

    # Wait a bit more for server to fully start
    time.sleep(2)

    # Open browser
    print("\n🌐 Opening browser...")
    webbrowser.open(url)

    print("\n" + "=" * 60)
    print("📊 VISUALIZATION APP RUNNING")
    print("=" * 60)
    print(f"Story: {metadata['title']}")
    print(f"Analysis Mode: {mode.upper()}")
    print(f"Genre: {genre.title()}")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 60 + "\n")

    try:
        # Keep script running
        server_process.wait()
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down visualization server...")
        if os.name != 'nt':
            os.killpg(os.getpgid(server_process.pid), signal.SIGTERM)
        else:
            server_process.terminate()
        print("✓ Server stopped")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description='Launch interactive visualization for narrative analysis'
    )
    parser.add_argument(
        'trajectory',
        type=Path,
        help='Path to trajectory JSON file'
    )
    parser.add_argument(
        '--genre',
        default='fantasy',
        choices=['romance', 'fantasy', 'scienceFiction', 'mysteryThrillerSuspense'],
        help='Story genre (default: fantasy)'
    )
    parser.add_argument(
        '--mode',
        default='dimensions',
        choices=['dimensions', 'npe'],
        help='Analysis mode: dimensions or npe (default: dimensions)'
    )
    parser.add_argument(
        '--title',
        help='Story title (optional, defaults to filename)'
    )

    args = parser.parse_args()

    if not args.trajectory.exists():
        print(f"✗ File not found: {args.trajectory}")
        sys.exit(1)

    launch_viz(args.trajectory, args.genre, args.mode, args.title)
