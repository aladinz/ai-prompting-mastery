#!/bin/bash
# Git Setup Script for Generative AI Learning Platform

echo "🚀 Setting up Git repository for deployment..."

# Initialize git if not already done
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
fi

# Add all files
echo "📝 Adding files to Git..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "Initial commit: Generative AI Learning Platform with Streamlit deployment"

echo "✅ Git repository setup complete!"
echo ""
echo "🌟 Next steps:"
echo "1. Create a new repository on GitHub: https://github.com/new"
echo "2. Repository name: generative-ai-learning-platform"
echo "3. Set to Public (required for free Streamlit deployment)"
echo "4. Run the following commands (replace YOUR_USERNAME):"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/generative-ai-learning-platform.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "5. Deploy on Streamlit Cloud: https://share.streamlit.io/"
echo ""
echo "📚 See DEPLOYMENT_GUIDE.md for detailed instructions"
