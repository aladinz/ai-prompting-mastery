#!/bin/bash

echo "Starting AI Prompting Mastery Streamlit App..."
echo ""
echo "The app will open in your browser at: http://localhost:8501"
echo ""
echo "To stop the app, press Ctrl+C in this terminal"
echo ""

# Check if virtual environment exists
if [ -d ".venv" ]; then
    echo "Using virtual environment..."
    source .venv/bin/activate
fi

streamlit run streamlit_app.py
