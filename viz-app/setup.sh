#!/bin/bash
# Setup script for Narrative Dimensions Visualization App

echo "📦 Setting up Narrative Dimensions Visualization App..."
echo ""

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "✗ npm not found"
    echo ""
    echo "Please install Node.js and npm first:"
    echo "  - Download from: https://nodejs.org/"
    echo "  - Or use your package manager:"
    echo "    - macOS: brew install node"
    echo "    - Ubuntu: sudo apt install nodejs npm"
    echo "    - Windows: Download installer from nodejs.org"
    exit 1
fi

echo "✓ npm found: $(npm --version)"
echo "✓ node found: $(node --version)"
echo ""

# Install dependencies
echo "📥 Installing dependencies..."
npm install

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Setup complete!"
    echo ""
    echo "🚀 To start the visualization app:"
    echo "   npm run dev"
    echo ""
    echo "Or use the Python launcher:"
    echo "   python ../scripts/launch_viz_app.py <trajectory-file>"
    echo ""
else
    echo ""
    echo "✗ Installation failed"
    echo "Please check the error messages above"
    exit 1
fi
