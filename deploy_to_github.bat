@echo off
REM GitHub Deployment Script - Run AFTER creating your GitHub repository

echo 🚀 GitHub Deployment for AI Prompting Mastery Platform
echo ===============================================
echo.
echo 📋 Prerequisites:
echo ✅ GitHub repository created at: https://github.com/YOUR_USERNAME/REPO_NAME
echo ✅ Repository set to PUBLIC (required for free Streamlit deployment)
echo ✅ Do NOT initialize with README (we have one already)
echo.
echo 🔧 Manual deployment commands:
echo.
echo 1. Replace YOUR_USERNAME and REPO_NAME in the commands below:
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo 2. Then deploy to Streamlit Cloud:
echo    - Go to: https://share.streamlit.io/
echo    - Sign in with GitHub
echo    - Create new app from your repository
echo    - Set main file: streamlit_app.py
echo.
echo 🎉 Your AI learning platform will be accessible worldwide!
echo.
pause
