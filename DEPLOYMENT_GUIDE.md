# GitHub Repository Setup Guide

## Quick Setup (Command Line)

1. **Initialize Git Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Generative AI Learning Platform"
   ```

2. **Create GitHub Repository**
   - Go to https://github.com/new
   - Repository name: `generative-ai-learning-platform`
   - Description: `Interactive web-based learning platform for Generative AI concepts`
   - Set to Public (required for free Streamlit deployment)
   - Don't initialize with README (we already have one)

3. **Link Local Repository to GitHub**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/generative-ai-learning-platform.git
   git branch -M main
   git push -u origin main
   ```

## Streamlit Cloud Deployment

1. **Visit Streamlit Cloud**
   - Go to https://share.streamlit.io/
   - Sign in with your GitHub account

2. **Deploy Your App**
   - Click "New app"
   - Repository: `YOUR_USERNAME/generative-ai-learning-platform`
   - Branch: `main`
   - Main file path: `streamlit_app.py`
   - App URL: Choose a custom URL or use the default

3. **App Settings**
   - Python version: 3.9+ (recommended)
   - Dependencies will be installed from `requirements.txt`
   - Configuration from `.streamlit/config.toml`

## Repository Structure
```
generative-ai-learning-platform/
├── streamlit_app.py           # Main Streamlit application
├── requirements.txt           # Python dependencies
├── README.md                 # Documentation
├── LICENSE                   # MIT License
├── .gitignore               # Git ignore rules
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── setup_windows.bat        # Windows setup script
├── setup_linux.sh          # Linux setup script
├── generative_ai_tutorial.htm  # Educational content
└── dark_mode.css           # Styling

```

## Live App Features
- 📚 Interactive module navigation
- 🌙 Dark/Light mode toggle
- 📱 Mobile-responsive design
- 🔄 Real-time progress tracking
- 📊 Visual learning components
- 🎨 Beautiful Material Design UI

## Access Your Live App
Once deployed on Streamlit Cloud, your app will be accessible at:
`https://YOUR_APP_NAME.streamlit.app/`

## Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run streamlit_app.py
```

## Support
For issues or questions, please create an issue on the GitHub repository.
