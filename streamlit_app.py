import streamlit as st
import streamlit.components.v1 as components
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
        background: var(--background-color);
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid var(--secondary-background-color);
        text-align: center;
        color: var(--text-color);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    /* Dark mode support */
    @media (prefers-color-scheme: dark) {
        .feature-card {
            background: #1f2937;
            border: 2px solid #374151;
            color: #f9fafb;
        }
        
        .module-card {
            background: #1f2937;
            color: #f9fafb;
        }
        
        .module-title {
            color: #f9fafb;
        }
        
        .module-description {
            color: #d1d5db;
        }
    }
    
    /* Streamlit dark theme support */
    .stApp[data-theme="dark"] .feature-card {
        background: #1f2937;
        border: 2px solid #374151;
        color: #f9fafb;
    }
    
    .stApp[data-theme="dark"] .module-card {
        background: #1f2937;
        color: #f9fafb;
    }
    
    .stApp[data-theme="dark"] .module-title {
        color: #f9fafb;
    }
    
    .stApp[data-theme="dark"] .module-description {
        color: #d1d5db;
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
    components.html(html_content, height=800, scrolling=True)

def main():
    # Initialize session state for dark mode
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False
    
    # Dark mode toggle in sidebar
    if st.session_state.dark_mode:
        st.sidebar.markdown('<h1 style="color: #f1f5f9;">🎨 Theme</h1>', unsafe_allow_html=True)
    else:
        st.sidebar.title("🎨 Theme")
    
    # Current theme indicator
    current_theme = "🌙 Dark Mode" if st.session_state.dark_mode else "☀️ Light Mode"
    st.sidebar.markdown(f"**Current Theme:** {current_theme}")
    
    # Toggle button
    toggle_text = "☀️ Switch to Light Mode" if st.session_state.dark_mode else "🌙 Switch to Dark Mode"
    if st.sidebar.button(toggle_text):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()
    
    # Apply dark mode CSS if enabled
    if st.session_state.dark_mode:
        st.markdown("""
        <style>
        .stApp {
            background-color: #0f172a;
            color: #f1f5f9;
        }
        .main-header {
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
        }
        .feature-card {
            background: #1e293b !important;
            border: 2px solid #334155 !important;
            color: #f1f5f9 !important;
        }
        .feature-card h3 {
            color: #f1f5f9 !important;
        }
        .feature-card p {
            color: #cbd5e1 !important;
        }
        .module-card {
            background: #1e293b !important;
            color: #f1f5f9 !important;
        }
        .module-title {
            color: #f1f5f9 !important;
        }
        .module-description {
            color: #cbd5e1 !important;
        }
        .stSidebar {
            background-color: #1e293b;
        }
        .stSidebar > div {
            background-color: #1e293b;
        }
        .stSidebar .stMarkdown {
            color: #f1f5f9;
        }
        .stSidebar .stMarkdown p {
            color: #f1f5f9;
        }
        .stSidebar .stMarkdown h1, 
        .stSidebar .stMarkdown h2, 
        .stSidebar .stMarkdown h3 {
            color: #f1f5f9;
        }
        .stSidebar .stMarkdown strong {
            color: #f1f5f9;
        }
        .stSidebar .stMarkdown ul li {
            color: #cbd5e1;
        }
        .stSidebar .stMarkdown ul li::marker {
            color: #cbd5e1;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🤖 AI Prompting Mastery</h1>
        <p>Complete Learning Platform - Master the Art of AI Communication</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.markdown("---")
    if st.session_state.dark_mode:
        st.sidebar.markdown('<h1 style="color: #f1f5f9;">📚 Navigation</h1>', unsafe_allow_html=True)
    else:
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
    
    # Initialize selected module in session state
    if 'selected_module' not in st.session_state:
        st.session_state.selected_module = "🏠 Home"
    
    # Module selection with session state
    selected_module = st.sidebar.selectbox(
        "Choose a module:", 
        list(modules.keys()),
        index=list(modules.keys()).index(st.session_state.selected_module)
    )
    
    # Update session state when selection changes
    if selected_module != st.session_state.selected_module:
        st.session_state.selected_module = selected_module
    
    # Progress tracking
    st.sidebar.markdown("---")
    if st.session_state.dark_mode:
        st.sidebar.markdown('<h3 style="color: #f1f5f9;">📊 Your Progress</h3>', unsafe_allow_html=True)
    else:
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
        if st.session_state.dark_mode:
            st.sidebar.markdown(f'<p style="color: #f1f5f9;"><strong>{module}</strong>: {status}</p>', unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"**{module}**: {status}")
    
    # Features section
    st.sidebar.markdown("---")
    if st.session_state.dark_mode:
        st.sidebar.markdown('<h3 style="color: #f1f5f9;">🌟 Features</h3>', unsafe_allow_html=True)
    else:
        st.sidebar.markdown("### 🌟 Features")
    
    features_list = [
        "🎓 **7 Complete Modules**",
        "🔄 **Restart Anytime**",
        "📱 **Mobile Friendly**",
        "🧠 **Interactive Learning**",
        "📊 **Progress Tracking**",
        "🎯 **Real Examples**"
    ]
    
    for feature in features_list:
        if st.session_state.dark_mode:
            st.sidebar.markdown(f'<p style="color: #cbd5e1;">- {feature}</p>', unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"- {feature}")
    
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
        
        # Add start learning button at the bottom of homepage
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🚀 Start Learning - Go to Module 1", key="start_learning"):
                st.session_state.selected_module = "📖 Module 1: Getting Started"
                st.rerun()
            
            if st.button("📚 Continue to Module 2", key="continue_module2"):
                st.session_state.selected_module = "💡 Module 2: Types of Prompts"
                st.rerun()
    
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
                    # Find current module index and navigate to previous
                    current_modules = list(modules.keys())
                    current_idx = current_modules.index(selected_module)
                    if current_idx > 0:
                        prev_module = current_modules[current_idx - 1]
                        st.session_state.selected_module = prev_module
                        st.rerun()
                    else:
                        st.info("You're already at the first module")
            
            with col2:
                if st.button("🏠 Back to Home"):
                    st.session_state.selected_module = "🏠 Home"
                    st.rerun()
            
            with col3:
                if st.button("Next Module ➡️"):
                    # Find current module index and navigate to next
                    current_modules = list(modules.keys())
                    current_idx = current_modules.index(selected_module)
                    if current_idx < len(current_modules) - 1:
                        next_module = current_modules[current_idx + 1]
                        st.session_state.selected_module = next_module
                        st.rerun()
                    else:
                        st.success("🎉 You've completed all modules!")
        else:
            st.error(f"Could not load module: {html_file}")

    # Footer
    st.markdown("---")
    footer_style = "color: #94a3b8;" if st.session_state.dark_mode else "color: #718096;"
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem; {footer_style}">
        <p>🤖 <strong>AI Prompting Mastery</strong> - Your Complete Guide to Effective AI Communication</p>
        <p>Built with ❤️ for learners who want to master AI prompting</p>
        <p>💡 <em>Tip: Use the theme toggle in the sidebar to switch between light and dark modes!</em></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
