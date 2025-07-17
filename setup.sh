#!/bin/bash

# AI Prompting Mastery - Setup Script
# This script helps you set up the project for local development or deployment

echo "🤖 AI Prompting Mastery - Setup Script"
echo "========================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3."
    exit 1
fi

echo "✅ pip3 found: $(pip3 --version)"

# Create virtual environment
echo "🔨 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run the application
echo "🚀 Starting the application..."
echo "📖 The application will open in your browser at http://localhost:8501"
echo "🛑 Press Ctrl+C to stop the application"
echo ""

streamlit run streamlit_app.py
