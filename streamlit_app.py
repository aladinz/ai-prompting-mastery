import streamlit as st
import os
import base64
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="AI Prompting Mastery - Complete Learning Platform",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Streamlit
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .module-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .module-title {
        color: #2d3748;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .module-description {
        color: #4a5568;
        margin-bottom: 1rem;
    }
    
    .status-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 0.5rem;
    }
    
    .status-complete {
        background: #f0fff4;
        color: #38a169;
    }
    
    .status-available {
        background: #fef5e7;
        color: #d69e2e;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .feature-card {
        background: #f7fafc;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #e2e8f0;
        text-align: center;
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)

def get_file_content(file_path):
    """Read file content and return as string"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        st.error(f"Error reading file {file_path}: {str(e)}")
        return None

def render_html_page(html_content, css_content=None):
    """Render HTML page with embedded CSS"""
    if css_content:
        # Inject CSS into HTML
        css_injection = f"<style>{css_content}</style></head>"
        html_content = html_content.replace("</head>", css_injection)
    
    # Use iframe to render HTML
    st.components.v1.html(html_content, height=800, scrolling=True)

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🤖 AI Prompting Mastery</h1>
        <p>Complete Learning Platform - Master the Art of AI Communication</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("📚 Navigation")
    st.sidebar.markdown("---")
    
    # Module selection
    modules = {
        "🏠 Home": "index.html",
        "📖 Module 1: Getting Started": "module1.html",
        "💡 Module 2: Types of Prompts": "module2.html", 
        "🏗️ Module 3: Building Better Prompts": "module3.html",
        "🔄 Module 4: Refining Outputs": "module4.html",
        "🎯 Module 5: Context & Specificity": "module5.html",
        "🚀 Module 6: Advanced Techniques": "module6.html",
        "⚡ Module 7: Iterative Prompting": "module7.html"
    }
    
    selected_module = st.sidebar.selectbox("Choose a module:", list(modules.keys()))
    
    # Progress tracking
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Your Progress")
    
    # Mock progress - in a real app, this would come from user data
    progress_data = {
        "📖 Module 1": True,
        "💡 Module 2": True,
        "🏗️ Module 3": False,
        "🔄 Module 4": False,
        "🎯 Module 5": False,
        "🚀 Module 6": False,
        "⚡ Module 7": False
    }
    
    for module, completed in progress_data.items():
        status = "✅ Complete" if completed else "⏳ Available"
        st.sidebar.markdown(f"**{module}**: {status}")
    
    # Features section
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🌟 Features")
    st.sidebar.markdown("""
    - 🎓 **7 Complete Modules**
    - 🔄 **Restart Anytime**
    - 📱 **Mobile Friendly**
    - 🧠 **Interactive Learning**
    - 📊 **Progress Tracking**
    - 🎯 **Real Examples**
    """)
    
    # Main content area
    if selected_module == "🏠 Home":
        # Home page content
        st.markdown("""
        <div class="feature-grid">
            <div class="feature-card">
                <div class="feature-icon">🎓</div>
                <h3>Complete Curriculum</h3>
                <p>7 comprehensive modules covering everything from basic prompting to advanced iterative techniques.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🔄</div>
                <h3>Restart Anytime</h3>
                <p>Study modules multiple times without losing your completion history - perfect for reinforcement learning.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🧠</div>
                <h3>Interactive Learning</h3>
                <p>Hands-on exercises, quizzes, and real-world examples to build practical skills.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Progress Tracking</h3>
                <p>Track your learning journey with completion badges and achievement history.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Module overview
        st.markdown("## 📚 Learning Modules")
        
        module_info = [
            ("Module 1: Getting Started", "Learn the fundamentals of AI prompting and why it matters", "📖"),
            ("Module 2: Types of Prompts", "Explore different prompt categories and their applications", "💡"),
            ("Module 3: Building Better Prompts", "Master the art of crafting clear, effective prompts", "🏗️"),
            ("Module 4: Refining Outputs", "Learn techniques to improve and iterate on AI responses", "🔄"),
            ("Module 5: Context & Specificity", "Understand how context shapes AI understanding", "🎯"),
            ("Module 6: Advanced Techniques", "Explore sophisticated prompting strategies", "🚀"),
            ("Module 7: Iterative Prompting", "Master the complete iterative improvement process", "⚡")
        ]
        
        for i, (title, description, icon) in enumerate(module_info, 1):
            st.markdown(f"""
            <div class="module-card">
                <div class="module-title">{icon} {title}</div>
                <div class="module-description">{description}</div>
                <span class="status-badge status-{'complete' if i <= 2 else 'available'}">
                    {'✅ Complete' if i <= 2 else '⏳ Available'}
                </span>
            </div>
            """, unsafe_allow_html=True)
    
    else:
        # Load and display selected module
        html_file = modules[selected_module]
        css_file = html_file.replace('.html', '.css')
        
        # Read HTML content
        html_content = get_file_content(html_file)
        css_content = get_file_content(css_file)
        
        if html_content:
            st.markdown(f"## {selected_module}")
            st.markdown("---")
            
            # Option to view in full screen
            if st.button("🔍 View in Full Screen"):
                st.info("💡 **Tip**: Click the expand button in the top-right of the module viewer for a better experience!")
            
            # Render the HTML page
            render_html_page(html_content, css_content)
            
            # Module navigation
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                if st.button("⬅️ Previous Module"):
                    st.info("Navigate to previous module")
            
            with col2:
                if st.button("🏠 Back to Home"):
                    st.experimental_rerun()
            
            with col3:
                if st.button("Next Module ➡️"):
                    st.info("Navigate to next module")
        else:
            st.error(f"Could not load module: {html_file}")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #718096;">
        <p>🤖 <strong>AI Prompting Mastery</strong> - Your Complete Guide to Effective AI Communication</p>
        <p>Built with ❤️ for learners who want to master AI prompting</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
