@echo off
echo 🤖 AI Prompting Mastery - Setup Script
echo ========================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python 3.7 or higher.
    pause
    exit /b 1
)

echo ✅ Python found
python --version

REM Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ pip is not installed. Please install pip.
    pause
    exit /b 1
)

echo ✅ pip found
pip --version

REM Create virtual environment
echo 🔨 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r requirements.txt

REM Run the application
echo 🚀 Starting the application...
echo 📖 The application will open in your browser at http://localhost:8501
echo 🛑 Press Ctrl+C to stop the application
echo.

streamlit run streamlit_app.py

pause
