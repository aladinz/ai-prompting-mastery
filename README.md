# AI Prompting Mastery - Complete Learning Platform

Welcome to the interactive AI Prompting Mastery tutorial! This comprehensive learning platform is available in two versions:

## 🚀 Quick Start Options

### Option 1: Streamlit Web App (Recommended)
**Interactive web application with enhanced features**

1. **Install Dependencies:**
   ```bash
   pip install streamlit>=1.28.0 pathlib2>=2.3.0
   ```
   Or use the requirements file:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Streamlit App:**
   ```bash
   streamlit run streamlit_app.py
   ```
   
   **Quick Start Scripts (Convenience):**
   - **Windows:** Double-click `run_streamlit.bat`
   - **Mac/Linux:** Run `./run_streamlit.sh`

3. **Access the App:**
   - Open your browser and go to: `http://localhost:8501`
   - The app will automatically open in your default browser

### Option 2: Static HTML Version
**Traditional web pages for offline use**

1. **Open `index.html` in your browser:**
   - This is the homepage and main entry point
2. **Toggle Dark Mode (optional):**
   - Use the 🌙/☀️ switch in the top right to enable dark mode
3. **Choose Your Learning Path:**
   - Select Beginner, Intermediate, Advanced, or Complete Course
4. **Start a Module:**
   - Click any module button to begin learning

## ✨ Streamlit Features
- **Enhanced Full-Screen Display:** Optimized iframe rendering for better content viewing
- **Progress Tracking:** Complete module progress system with unlimited retakes
- **Dark Mode Toggle:** Persistent dark/light mode preference
- **Responsive Design:** Professional layout that adapts to any screen size
- **Interactive Navigation:** Smooth scrolling between sections
- **Live Module Updates:** Dynamic content loading without page refreshes

## 📚 Learning Modules
- **Module 1:** What Is Prompt Engineering? - Master the fundamentals
- **Module 2:** Types of Prompts - Explore different prompting strategies
- **Module 3:** Building Better Prompts - Advanced construction techniques
- **Module 4:** Essential Refinement Strategies - Color-coded improvement methods
- **Module 5:** Context Advantage - Leverage context for better results
- **Module 6:** Three-Layer Architecture - Systematic prompting approach
- **Module 7:** Advanced Techniques - Expert-level strategies

Each module includes:
- **Interactive Progress Tracking** with visual indicators
- **Copyable Prompt Examples** with one-click clipboard functionality
- **Comprehensive Examples** with real-world applications
- **Dark Mode Support** for comfortable learning
- **Printable Cheat Sheets** and downloadable guides
- **Unlimited Module Retakes** to reinforce learning

## 🌗 Dark Mode
- Dark mode is global. Toggle it on the homepage and it will apply to all modules.
- If you want to force dark mode, run `localStorage.setItem('darkMode', true)` in your browser console and reload.

## 📝 Features
- **Interactive Prompt Playground:** Try out prompt templates and see AI responses.
- **Progress Tracking:** Completion badges for each module.
- **Downloadable Cheat Sheets:** Click the download button in modules for quick reference.
- **Responsive Design:** Works on desktop and mobile.

## 🛠️ Development & Customization

### Running in Development Mode
```bash
# Clone the repository
git clone https://github.com/aladinz/ai-prompting-mastery.git
cd ai-prompting-mastery

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run streamlit_app.py

# For development with auto-reload
streamlit run streamlit_app.py --server.runOnSave true
```

### How to Edit or Extend
- **Add new modules:** Create new HTML files and update the Streamlit navigation
- **Customize styles:** Edit the CSS files (e.g., `module1.css`, `styles.css`)
- **Enhance Streamlit features:** Modify `streamlit_app.py` for new functionality
- **Update module content:** Edit individual module HTML files

## 💡 Troubleshooting

### Streamlit Issues
- **Port already in use:** Try `streamlit run streamlit_app.py --server.port 8502`
- **Import errors:** Ensure all dependencies are installed: `pip install -r requirements.txt`
- **Module not loading:** Check file paths and ensure HTML files are in the same directory

### HTML Version Issues
- **Dark mode not applying:** Toggle it on the homepage and reload the module page
- **Blank screens:** Check browser security settings for local file access
- **Best browsers:** Chrome, Edge, or Firefox for optimal experience

## 📦 Project Structure
```
streamlit_app.py     # Main Streamlit application
index.html           # Homepage (HTML version)
module1.html         # Module 1: What Is Prompt Engineering?
module2.html         # Module 2: Types of Prompts  
module3.html         # Module 3: Building Better Prompts
module4.html         # Module 4: Essential Refinement Strategies
module5.html         # Module 5: Context Advantage
module6.html         # Module 6: Three-Layer Architecture
module7.html         # Module 7: Advanced Techniques
module1.css          # Individual module styles
module2.css          # ...additional CSS files
styles.css           # Global styles
requirements.txt     # Python dependencies
README.md           # This documentation
```

## 🌐 Deployment Options

### Local Development
```bash
streamlit run streamlit_app.py
```

### Streamlit Cloud (Recommended)
1. Push your code to GitHub
2. Connect your repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy with one click

### Other Platforms
- **Heroku:** Add `setup.sh` and `Procfile` for Heroku deployment
- **Docker:** Create Dockerfile for containerized deployment
- **Vercel/Netlify:** Deploy the HTML version as static site

## ✨ Credits
Made with ❤️ by Aladdin. For questions or feedback, open an issue or contact via GitHub.
