#!/usr/bin/env python3
"""
Demo of trajectory comparison feature.
Shows planned vs. actual trajectory.
"""

import sys
from pathlib import Path

# Add scripts directory to path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / 'scripts'))

from visualize_trajectory import compare_trajectories

# Planned trajectory (outline)
planned = [
    {'intimacy': 2, 'trust': 4, 'desire': 5},
    {'intimacy': 4, 'trust': 5, 'desire': 6},
    {'intimacy': 6, 'trust': 6, 'desire': 7},
    {'intimacy': 7, 'trust': 7, 'desire': 8},
    {'intimacy': 8, 'trust': 8, 'desire': 9},
]

# Actual trajectory (what got written)
actual = [
    {'intimacy': 2, 'trust': 3, 'desire': 5},  # Trust started lower
    {'intimacy': 3, 'trust': 2, 'desire': 6},  # Trust dropped (betrayal)
    {'intimacy': 5, 'trust': 3, 'desire': 7},  # Intimacy grew despite low trust
    {'intimacy': 6, 'trust': 4, 'desire': 8},  # Trust recovering slowly
    {'intimacy': 8, 'trust': 6, 'desire': 9},  # Didn't quite reach planned trust
]

print("COMPARISON: Planned vs Actual - Trust Dimension")
print("=" * 70)
print(compare_trajectories(planned, actual, 'trust', ('Planned', 'Actual')))
print()

print("COMPARISON: Planned vs Actual - Intimacy Dimension")
print("=" * 70)
print(compare_trajectories(planned, actual, 'intimacy', ('Planned', 'Actual')))
