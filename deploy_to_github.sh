#!/bin/bash
# GitHub Deployment Script - Run AFTER creating your GitHub repository

echo "🚀 GitHub Deployment for AI Prompting Mastery Platform"
echo "==============================================="
echo
echo "📋 Prerequisites:"
echo "✅ GitHub repository created at: https://github.com/YOUR_USERNAME/REPO_NAME"
echo "✅ Repository set to PUBLIC (required for free Streamlit deployment)"
echo "✅ Do NOT initialize with README (we have one already)"
echo
echo "🔧 Now running deployment commands..."
echo

# Add your GitHub repository (replace with your actual repo URL)
echo "🔗 Adding GitHub remote..."
read -p "Enter your GitHub username: " username
read -p "Enter your repository name: " reponame

git remote add origin https://github.com/$username/$reponame.git

# Rename branch to main
echo "🌟 Setting main branch..."
git branch -M main

# Push to GitHub
echo "🚀 Pushing to GitHub..."
git push -u origin main

echo
echo "✅ Deployment complete!"
echo "📁 Your code is now on GitHub: https://github.com/$username/$reponame"
echo
echo "🌐 Next step: Deploy to Streamlit Cloud"
echo "1. Go to: https://share.streamlit.io/"
echo "2. Sign in with your GitHub account"
echo "3. Create new app from your repository"
echo "4. Set main file: streamlit_app.py"
echo "5. Your app will be live at: https://$reponame.streamlit.app"
echo
echo "🎉 Your AI learning platform will soon be accessible worldwide!"
