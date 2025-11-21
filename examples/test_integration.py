#!/usr/bin/env python3
"""
Test integration between dimension_worksheet.py and validate_trajectory.py
"""

import sys
import json
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from dimension_worksheet import DimensionalWorksheet
from validate_trajectory import TrajectoryValidator


def test_worksheet_to_validator():
    """Test that worksheet output is compatible with validator."""

    print("\n" + "="*70)
    print("  INTEGRATION TEST: Worksheet → Validator")
    print("="*70 + "\n")

    # Create a simple romance trajectory
    worksheet = DimensionalWorksheet("Test Story", "romance", num_beats=5)

    # Add properly paced beats (should pass validation - small incremental changes)
    worksheet.add_beat(
        "Meet", 10,
        {'intimacy': 1, 'trust': 3, 'desire': 3, 'goal_alignment': 4, 'stakes': 5}
    )
    worksheet.add_beat(
        "Connect", 30,
        {'intimacy': 3, 'trust': 4, 'desire': 5, 'goal_alignment': 5, 'stakes': 6}
    )
    worksheet.add_beat(
        "Conflict", 60,
        {'intimacy': 4, 'trust': 2, 'desire': 6, 'goal_alignment': 4, 'stakes': 8}
    )
    worksheet.add_beat(
        "Reconcile", 85,
        {'intimacy': 6, 'trust': 5, 'desire': 8, 'goal_alignment': 7, 'stakes': 8}
    )
    worksheet.add_beat(
        "HEA", 100,
        {'intimacy': 8, 'trust': 8, 'desire': 9, 'goal_alignment': 9, 'stakes': 5}
    )

    print(f"✓ Created worksheet with {len(worksheet.beats)} beats")

    # Generate trajectory (format expected by validator)
    trajectory = worksheet.generate_trajectory()

    print(f"✓ Generated trajectory: {len(trajectory)} states")
    print(f"\nTrajectory format preview:")
    print(f"  {trajectory[0]}")

    # Validate with TrajectoryValidator
    validator = TrajectoryValidator(genre='romance')
    report = validator.validate_trajectory(trajectory)

    print(f"\n{'─'*70}")
    print("VALIDATION REPORT")
    print(f"{'─'*70}\n")

    print(f"Valid: {'✓ YES' if report['valid'] else '✗ NO'}\n")

    print("Checks:")
    for check in report['checks']:
        status = "✓ PASSED" if check['passed'] else "✗ FAILED"
        print(f"  {check['name']:25s} {status}")
        if check['issues']:
            for issue in check['issues'][:2]:
                print(f"    • {issue}")

    # Test JSON export → validator
    print(f"\n{'─'*70}")
    print("JSON EXPORT TEST")
    print(f"{'─'*70}\n")

    json_path = worksheet.export_to_json()
    print(f"✓ Exported to: {json_path}")

    # Load the JSON and extract trajectory
    with open(json_path, 'r') as f:
        data = json.load(f)

    loaded_trajectory = data['trajectory']
    print(f"✓ Loaded trajectory from JSON: {len(loaded_trajectory)} states")

    # Validate loaded trajectory
    report2 = validator.validate_trajectory(loaded_trajectory)
    print(f"✓ Re-validation: {'PASSED' if report2['valid'] else 'FAILED'}")

    # Verify trajectories match
    if trajectory == loaded_trajectory:
        print("✓ Generated and exported trajectories match perfectly")
    else:
        print("✗ Trajectories differ!")

    return report['valid']


def test_session_persistence():
    """Test session save/load cycle."""

    print("\n\n" + "="*70)
    print("  SESSION PERSISTENCE TEST")
    print("="*70 + "\n")

    # Create worksheet
    original = DimensionalWorksheet("Session Test", "thriller", num_beats=3)
    original.add_beat(
        "Start", 10,
        {'stakes': 3, 'danger': 2, 'trust': 5},
        notes="Normal world"
    )
    original.add_beat(
        "Crisis", 50,
        {'stakes': 8, 'danger': 7, 'trust': 3},
        notes="Danger escalates"
    )
    original.add_beat(
        "End", 100,
        {'stakes': 4, 'danger': 1, 'trust': 6},
        notes="Resolution"
    )

    print(f"✓ Created original worksheet: {len(original.beats)} beats")

    # Save session
    session_path = original.save_session()
    print(f"✓ Saved session to: {session_path}")

    # Load session
    loaded = DimensionalWorksheet.load_session(session_path)
    print(f"✓ Loaded session: {len(loaded.beats)} beats")

    # Verify data integrity
    checks = [
        ("Title", original.story_title == loaded.story_title),
        ("Genre", original.genre == loaded.genre),
        ("Beat count", len(original.beats) == len(loaded.beats)),
        ("First beat name", original.beats[0]['name'] == loaded.beats[0]['name']),
        ("Last beat notes", original.beats[-1]['notes'] == loaded.beats[-1]['notes'])
    ]

    print("\nData integrity checks:")
    all_passed = True
    for check_name, passed in checks:
        status = "✓" if passed else "✗"
        print(f"  {status} {check_name}")
        all_passed = all_passed and passed

    return all_passed


if __name__ == "__main__":
    print("\n" + "#"*70)
    print("#  INTEGRATION TEST SUITE")
    print("#"*70)

    test1_passed = test_worksheet_to_validator()
    test2_passed = test_session_persistence()

    print("\n\n" + "#"*70)
    print("#  TEST RESULTS")
    print("#"*70 + "\n")

    results = [
        ("Worksheet → Validator Integration", test1_passed),
        ("Session Persistence", test2_passed)
    ]

    for test_name, passed in results:
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"  {status}  {test_name}")

    all_passed = all(p for _, p in results)
    print(f"\nOverall: {'✓ ALL TESTS PASSED' if all_passed else '✗ SOME TESTS FAILED'}\n")

    sys.exit(0 if all_passed else 1)
