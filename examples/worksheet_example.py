#!/usr/bin/env python3
"""
Example usage of the DimensionalWorksheet class.
Demonstrates programmatic API without interactive mode.
"""

import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from dimension_worksheet import DimensionalWorksheet


def example_romance_trajectory():
    """Create a simple romance trajectory programmatically."""

    print("\n" + "="*70)
    print("  EXAMPLE: Creating a Romance Trajectory Programmatically")
    print("="*70 + "\n")

    # Initialize worksheet
    worksheet = DimensionalWorksheet(
        story_title="Love in the Time of Deadlines",
        genre="romance",
        num_beats=8
    )

    # Add beats with dimension scores
    beats_data = [
        {
            'name': 'Meet Cute',
            'percent': 5,
            'dimensions': {
                'intimacy': 0,
                'trust': 3,
                'desire': 2,
                'vulnerability': 1,
                'goal_alignment': 2,
                'power_differential': 0,
                'info_asymmetry': 4,
                'stakes': 4,
                'proximity': 2
            },
            'notes': 'They meet at a coffee shop - he spills coffee on her laptop'
        },
        {
            'name': 'Forced Proximity',
            'percent': 20,
            'dimensions': {
                'intimacy': 2,
                'trust': 4,
                'desire': 5,
                'vulnerability': 2,
                'goal_alignment': 4,
                'power_differential': 0,
                'info_asymmetry': 3,
                'stakes': 5,
                'proximity': 8
            },
            'notes': 'Boss assigns them to same project - must work together'
        },
        {
            'name': 'First Kiss',
            'percent': 40,
            'dimensions': {
                'intimacy': 5,
                'trust': 5,
                'desire': 8,
                'vulnerability': 6,
                'goal_alignment': 6,
                'power_differential': 0,
                'info_asymmetry': 2,
                'stakes': 6,
                'proximity': 10
            },
            'notes': 'Late night working - tension breaks into passionate kiss'
        },
        {
            'name': 'Secret Revealed',
            'percent': 60,
            'dimensions': {
                'intimacy': 6,
                'trust': 2,
                'desire': 8,
                'vulnerability': 7,
                'goal_alignment': 3,
                'power_differential': -2,
                'info_asymmetry': 8,
                'stakes': 8,
                'proximity': 5
            },
            'notes': 'She discovers he was assigned to evaluate her for promotion'
        },
        {
            'name': 'Black Moment',
            'percent': 75,
            'dimensions': {
                'intimacy': 3,
                'trust': 1,
                'desire': 8,
                'vulnerability': 8,
                'goal_alignment': 2,
                'power_differential': 0,
                'info_asymmetry': 1,
                'stakes': 9,
                'proximity': 1
            },
            'notes': 'She quits and prepares to move to another city'
        },
        {
            'name': 'Grand Gesture',
            'percent': 90,
            'dimensions': {
                'intimacy': 6,
                'trust': 5,
                'desire': 9,
                'vulnerability': 10,
                'goal_alignment': 7,
                'power_differential': 0,
                'info_asymmetry': 0,
                'stakes': 9,
                'proximity': 8
            },
            'notes': 'He quits his job and follows her - full confession'
        },
        {
            'name': 'HEA',
            'percent': 100,
            'dimensions': {
                'intimacy': 9,
                'trust': 8,
                'desire': 9,
                'vulnerability': 8,
                'goal_alignment': 10,
                'power_differential': 0,
                'info_asymmetry': 0,
                'stakes': 4,
                'proximity': 10
            },
            'notes': 'They start their own business together - partnership in life and work'
        }
    ]

    # Add all beats
    for beat in beats_data:
        worksheet.add_beat(
            beat_name=beat['name'],
            beat_percent=beat['percent'],
            dimensions=beat['dimensions'],
            notes=beat['notes']
        )

    print(f"✓ Added {len(beats_data)} beats to worksheet\n")

    # Show analysis
    print(worksheet.get_analysis_summary())

    # Show visualization
    print(worksheet.visualize_ascii(['intimacy', 'trust', 'desire', 'vulnerability']))

    # Calculate and show velocities
    velocities = worksheet.calculate_velocity()
    print("\nVELOCITY ANALYSIS:")
    print("Beat-to-beat velocity (average dimensional change):")
    for i, v in enumerate(velocities):
        beat_from = worksheet.beats[i]['name']
        beat_to = worksheet.beats[i+1]['name']
        print(f"  {beat_from} → {beat_to}: {v:.2f} points/dimension")

    # Export to files
    print("\n" + "="*70)
    print("  EXPORTING FILES")
    print("="*70 + "\n")

    json_path = worksheet.export_to_json()
    print(f"✓ JSON exported to: {json_path}")

    csv_path = worksheet.export_to_csv()
    print(f"✓ CSV exported to: {csv_path}")

    session_path = worksheet.save_session()
    print(f"✓ Session saved to: {session_path}")

    # Demonstrate validation
    print("\n" + "="*70)
    print("  VALIDATION TEST")
    print("="*70 + "\n")

    trajectory = worksheet.generate_trajectory()

    # Import validator
    sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
    from validate_trajectory import TrajectoryValidator

    validator = TrajectoryValidator(genre='romance')
    report = validator.validate_trajectory(trajectory)

    print(f"Trajectory Valid: {report['valid']}")
    print(f"\nChecks Performed:")
    for check in report['checks']:
        status = "✓ PASSED" if check['passed'] else "✗ FAILED"
        print(f"  {check['name']}: {status}")

    if report['errors']:
        print("\nErrors:")
        for error in report['errors']:
            print(f"  - {error}")

    if report['warnings']:
        print("\nWarnings:")
        for warning in report['warnings']:
            print(f"  - {warning}")

    return worksheet


def example_validation_errors():
    """Demonstrate validation and error handling."""

    print("\n\n" + "="*70)
    print("  EXAMPLE: Validation and Error Handling")
    print("="*70 + "\n")

    worksheet = DimensionalWorksheet("Test Story", "romance")

    # Test 1: Invalid dimension range
    print("Test 1: Invalid dimension value")
    try:
        worksheet.add_beat(
            "Invalid Beat",
            50,
            {'intimacy': 15}  # Invalid - max is 10
        )
    except ValueError as e:
        print(f"  ✓ Caught error: {e}\n")

    # Test 2: Invalid power_differential range
    print("Test 2: Invalid power_differential value")
    try:
        worksheet.add_beat(
            "Invalid Beat",
            50,
            {'power_differential': -10}  # Invalid - min is -5
        )
    except ValueError as e:
        print(f"  ✓ Caught error: {e}\n")

    # Test 3: Unknown dimension
    print("Test 3: Unknown dimension name")
    errors = worksheet.validate_dimensions({'fake_dimension': 5})
    if errors:
        print(f"  ✓ Validation errors: {errors}\n")

    # Test 4: Valid beat with warnings
    print("Test 4: Large jump warning (programmatic detection)")
    worksheet.add_beat("Beat 1", 10, {'intimacy': 2, 'trust': 3})
    worksheet.add_beat("Beat 2", 20, {'intimacy': 8, 'trust': 4})  # 6-point jump!

    issues = worksheet._detect_issues()
    for issue in issues:
        print(f"  ⚠ {issue}")


def example_load_template():
    """Demonstrate loading a genre template."""

    print("\n\n" + "="*70)
    print("  EXAMPLE: Loading Genre Template")
    print("="*70 + "\n")

    worksheet = DimensionalWorksheet("Templated Romance", "romance")

    # Load the template
    template_file = Path(__file__).parent.parent / "templates" / "romance-beat-template.csv"

    if template_file.exists():
        worksheet._load_genre_template()
        print(f"\n✓ Loaded template with {len(worksheet.beats)} beats")
        print("\nFirst 5 beats:")
        for i, beat in enumerate(sorted(worksheet.beats, key=lambda b: b['percent'])[:5]):
            print(f"  {i+1}. {beat['name']} ({beat['percent']}%)")

        # Show quick visualization
        print(worksheet.visualize_ascii(['intimacy', 'trust', 'desire']))
    else:
        print(f"Template not found at {template_file}")


if __name__ == "__main__":
    # Run all examples
    example_romance_trajectory()
    example_validation_errors()
    example_load_template()

    print("\n\n" + "="*70)
    print("  EXAMPLES COMPLETE")
    print("="*70)
    print("\nCheck the 'exports/' and 'sessions/' directories for generated files.")
    print()
