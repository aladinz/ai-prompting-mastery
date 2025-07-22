@echo off
echo Starting AI Prompting Mastery Streamlit App...
echo.
echo The app will open in your browser at: http://localhost:8501
echo.
echo To stop the app, press Ctrl+C in this window
echo.

REM Check if virtual environment exists
if exist .venv\Scripts\streamlit.exe (
    echo Using virtual environment...
    .venv\Scripts\streamlit.exe run streamlit_app.py
) else (
    echo Using system Python...
    streamlit run streamlit_app.py
)

pause
