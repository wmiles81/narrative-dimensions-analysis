#!/bin/bash
# Demo script showing diagnostic system capabilities

echo "======================================================================"
echo "NARRATIVE DIAGNOSTIC SYSTEM DEMO"
echo "======================================================================"
echo ""

echo "1. Running diagnostics on PROBLEMATIC trajectory..."
echo "----------------------------------------------------------------------"
python3 ../scripts/diagnostic_patterns.py problematic_trajectory.json --genre romance
echo ""
echo ""

echo "2. Running diagnostics on WELL-STRUCTURED trajectory..."
echo "----------------------------------------------------------------------"
python3 ../scripts/diagnostic_patterns.py good_trajectory.json --genre romance --catalysts good_trajectory_catalysts.json
echo ""
echo ""

echo "======================================================================"
echo "DEMO COMPLETE"
echo "======================================================================"
echo ""
echo "Files created:"
echo "  - problematic_trajectory.json (example with 13 critical issues)"
echo "  - good_trajectory.json (well-structured romance)"
echo "  - good_trajectory_catalysts.json (catalyst events)"
echo ""
echo "Try it yourself:"
echo "  python3 ../scripts/diagnostic_patterns.py YOUR_TRAJECTORY.json --genre romance"
echo ""
