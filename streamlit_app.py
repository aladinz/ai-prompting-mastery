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
        background: linear-gradient(135deg, #f0fff4 0%, #c6f6d5 100%);
        color: #38a169;
        border: 1px solid #9ae6b4;
    }
    
    .status-available {
        background: linear-gradient(135deg, #ebf8ff 0%, #bee3f8 100%);
        color: #3182ce;
        border: 1px solid #90cdf4;
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
    
    /* Full screen iframe styling */
    iframe {
        width: 100% !important;
        min-height: 1200px !important;
        border: none !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
    }
    
    /* Streamlit component container styling */
    .stHtml {
        border-radius: 8px !important;
        overflow: hidden !important;
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
    """Render HTML page with embedded CSS and navigation handling in full screen"""
    if css_content:
        # Inject CSS into HTML
        css_injection = f"<style>{css_content}</style></head>"
        html_content = html_content.replace("</head>", css_injection)
    
    # Inject JavaScript to handle navigation messages and auto-resize
    navigation_script = """
    <script>
        // Listen for navigation messages from the iframe content
        window.addEventListener('message', function(event) {
            if (event.data.type === 'streamlit_navigation') {
                // Store the navigation target in a way Streamlit can access
                const moduleTarget = event.data.module;
                console.log('Received navigation request for:', moduleTarget);
                
                // Create a temporary element to store the navigation target
                // This will be picked up by the Streamlit app
                const navElement = document.createElement('div');
                navElement.id = 'navigation-target';
                navElement.setAttribute('data-module', moduleTarget);
                navElement.style.display = 'none';
                document.body.appendChild(navElement);
                
                // Trigger a Streamlit rerun by dispatching a custom event
                const event_detail = new CustomEvent('streamlit_navigate', {
                    detail: { module: moduleTarget }
                });
                window.dispatchEvent(event_detail);
            }
        });
        
        // Auto-resize iframe to content height
        function resizeIframe() {
            const height = Math.max(
                document.body.scrollHeight,
                document.body.offsetHeight,
                document.documentElement.clientHeight,
                document.documentElement.scrollHeight,
                document.documentElement.offsetHeight,
                window.innerHeight
            );
            
            window.parent.postMessage({
                type: 'resize',
                height: Math.max(height, 1000) // Minimum height of 1000px
            }, '*');
        }
        
        // Initial resize and on content changes
        document.addEventListener('DOMContentLoaded', resizeIframe);
        window.addEventListener('load', resizeIframe);
        window.addEventListener('resize', resizeIframe);
        
        // Observe content changes for dynamic resizing
        if (window.ResizeObserver) {
            const resizeObserver = new ResizeObserver(resizeIframe);
            resizeObserver.observe(document.body);
        }
    </script>
    </head>
    """
    html_content = html_content.replace("</head>", navigation_script)
    
    # Use iframe to render HTML with dynamic height (full screen)
    components.html(html_content, height=1200, scrolling=True)

def main():
    # Initialize session state for dark mode
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False
    
    # Check for navigation requests from query parameters
    query_params = st.query_params
    if 'nav_to' in query_params:
        target_module = query_params['nav_to']
        # Clear the query parameter to prevent loops
        st.query_params.clear()
        # Set the target module in session state
        if 'selected_module' not in st.session_state:
            st.session_state.selected_module = "🏠 Home"
        st.session_state.selected_module = target_module
        st.rerun()
    
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
    
    # Add navigation handling JavaScript
    st.markdown("""
    <script>
        // Listen for navigation messages from iframes
        window.addEventListener('message', function(event) {
            if (event.data.type === 'streamlit_navigation') {
                console.log('Streamlit received navigation request:', event.data.module);
                
                // Store the navigation target
                window.navigationTarget = event.data.module;
                
                // Trigger Streamlit to check for navigation changes
                // We'll use the query parameters to trigger a rerun
                const url = new URL(window.location);
                url.searchParams.set('nav_to', encodeURIComponent(event.data.module));
                url.searchParams.set('nav_time', Date.now());
                window.history.pushState({}, '', url);
                
                // Force a page refresh to trigger Streamlit navigation
                window.location.reload();
            }
        });
    </script>
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
    
    # Initialize progress tracking in session state
    if 'module_completions' not in st.session_state:
        st.session_state.module_completions = {}
    
    # All modules are available for unlimited retakes
    modules_info = {
        "📖 Module 1": "Introduction to AI Prompting",
        "💡 Module 2": "Understanding Different Types of Prompts", 
        "🏗️ Module 3": "Advanced Prompt Engineering",
        "🔄 Module 4": "Iterative Prompt Refinement",
        "🎯 Module 5": "Context and Chain Prompting",
        "🚀 Module 6": "AI Integration Strategies",
        "⚡ Module 7": "Future of AI Prompting"
    }
    
    for module, description in modules_info.items():
        # Check if module has been completed (but still allow retakes)
        completion_count = st.session_state.module_completions.get(module, 0)
        
        if completion_count > 0:
            status = f"✅ Completed ({completion_count}x) - Available for retake"
            status_color = "#38a169"  # Green
        else:
            status = "📚 Available"
            status_color = "#667eea"  # Blue
        
        if st.session_state.dark_mode:
            st.sidebar.markdown(f'''
            <div style="
                background: rgba(255,255,255,0.05);
                padding: 0.75rem;
                border-radius: 8px;
                margin: 0.5rem 0;
                border-left: 4px solid {status_color};
            ">
                <p style="color: #f1f5f9; margin: 0; font-weight: 600;">{module}</p>
                <p style="color: #cbd5e0; margin: 0.25rem 0 0 0; font-size: 0.85rem;">{description}</p>
                <p style="color: {status_color}; margin: 0.25rem 0 0 0; font-size: 0.8rem; font-weight: 500;">{status}</p>
            </div>
            ''', unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f'''
            <div style="
                background: #f8fafc;
                padding: 0.75rem;
                border-radius: 8px;
                margin: 0.5rem 0;
                border-left: 4px solid {status_color};
                border: 1px solid #e2e8f0;
            ">
                <p style="color: #2d3748; margin: 0; font-weight: 600;">{module}</p>
                <p style="color: #4a5568; margin: 0.25rem 0 0 0; font-size: 0.85rem;">{description}</p>
                <p style="color: {status_color}; margin: 0.25rem 0 0 0; font-size: 0.8rem; font-weight: 500;">{status}</p>
            </div>
            ''', unsafe_allow_html=True)
    
    # Overall progress summary
    st.sidebar.markdown("---")
    total_modules = len(modules_info)
    completed_modules = len([m for m in modules_info.keys() if st.session_state.module_completions.get(m, 0) > 0])
    total_completions = sum(st.session_state.module_completions.values())
    
    if st.session_state.dark_mode:
        st.sidebar.markdown(f'''
        <div style="
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
        ">
            <h4 style="color: #f1f5f9; margin: 0 0 0.5rem 0;">📊 Overall Progress</h4>
            <p style="color: #cbd5e0; margin: 0.25rem 0;">Modules Completed: <strong style="color: #38a169;">{completed_modules}/{total_modules}</strong></p>
            <p style="color: #cbd5e0; margin: 0.25rem 0;">Total Completions: <strong style="color: #667eea;">{total_completions}</strong></p>
            <p style="color: #cbd5e0; margin: 0.25rem 0; font-size: 0.85rem;">All modules available for unlimited retakes!</p>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.sidebar.markdown(f'''
        <div style="
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            border: 1px solid #e2e8f0;
        ">
            <h4 style="color: #2d3748; margin: 0 0 0.5rem 0;">📊 Overall Progress</h4>
            <p style="color: #4a5568; margin: 0.25rem 0;">Modules Completed: <strong style="color: #38a169;">{completed_modules}/{total_modules}</strong></p>
            <p style="color: #4a5568; margin: 0.25rem 0;">Total Completions: <strong style="color: #667eea;">{total_completions}</strong></p>
            <p style="color: #4a5568; margin: 0.25rem 0; font-size: 0.85rem;">All modules available for unlimited retakes!</p>
        </div>
        ''', unsafe_allow_html=True)
    
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
            # Get completion count for this module
            module_key = f"{icon} Module {i}"
            completion_count = st.session_state.module_completions.get(module_key, 0)
            
            if completion_count > 0:
                status_class = "complete"
                status_text = f"✅ Completed ({completion_count}x) - Available for retake"
            else:
                status_class = "available"
                status_text = "📚 Available"
            
            st.markdown(f"""
            <div class="module-card">
                <div class="module-title">{icon} {title}</div>
                <div class="module-description">{description}</div>
                <span class="status-badge status-{status_class}">
                    {status_text}
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
            
            # Render the HTML page in full screen mode
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
            
            # Module completion section
            st.markdown("---")
            st.markdown("### 🎯 Module Completion")
            
            # Get current completion count
            current_completion_count = st.session_state.module_completions.get(selected_module, 0)
            
            if current_completion_count > 0:
                st.success(f"🎉 You've completed this module {current_completion_count} time(s)!")
                completion_text = f"✅ Complete Again (#{current_completion_count + 1})"
            else:
                completion_text = "✅ Mark as Complete"
            
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button(completion_text, key=f"complete_{selected_module}"):
                    # Mark module as complete
                    if selected_module not in st.session_state.module_completions:
                        st.session_state.module_completions[selected_module] = 0
                    st.session_state.module_completions[selected_module] += 1
                    
                    new_count = st.session_state.module_completions[selected_module]
                    st.balloons()
                    st.success(f"🎉 Congratulations! Module completed for the {new_count} time(s)!")
                    st.info("💡 Your progress has been saved. You can retake this module anytime!")
                    st.rerun()
                
                # Reset progress button (optional)
                if current_completion_count > 0:
                    if st.button("🔄 Reset Progress for This Module", key=f"reset_{selected_module}"):
                        if st.session_state.get(f"confirm_reset_{selected_module}", False):
                            st.session_state.module_completions[selected_module] = 0
                            st.session_state[f"confirm_reset_{selected_module}"] = False
                            st.success("✅ Progress reset! You can now complete this module again.")
                            st.rerun()
                        else:
                            st.session_state[f"confirm_reset_{selected_module}"] = True
                            st.warning("⚠️ Click again to confirm reset")
                            st.rerun()
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
