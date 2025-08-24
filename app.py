import streamlit as st
import sys
import os

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(
    page_title="AI-Enhanced Teaching Assistant Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #1f77b4, #2ecc71);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .subtitle {
        font-size: 1.3rem;
        text-align: center;
        color: #666;
        margin-bottom: 3rem;
    }
    .feature-card {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }
    .page-link {
        text-decoration: none;
        color: inherit;
    }
    .page-link:hover {
        text-decoration: none;
        color: inherit;
    }
    .navigation-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">🎓 AI-Enhanced Teaching Assistant Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Enhancing Collaborative Learning Through Evidence-Based AI Solutions</p>', unsafe_allow_html=True)
    
    # Introduction
    st.markdown("""
    ## 🌟 Welcome to the Future of Collaborative Education
    
    This dashboard explores how **Artificial Intelligence can enhance teaching assistant functionality** 
    in student group settings, focusing on **social psychology** and **evidence-based educational research** 
    rather than technical implementation.
    
    ### 🎯 Research Question
    *"How can AI replace or enhance the functionality of teaching assistants in student group settings, 
    specifically enabling more consistent engagement among group members in targeted classes?"*
    """)
    
    # Navigation sections
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Research & Analysis Pages")
        
        research_pages = [
            ("🔍 Research Overview", "Theoretical framework and key insights"),
            ("🎯 Team Formation", "AI-optimized group composition analysis"),
            ("👁️ Real-Time Monitoring", "Continuous engagement tracking"),
            ("🎓 AI Tutoring Support", "24/7 question answering and guidance"),
            ("⚖️ Equal Participation", "Data-driven contribution tracking"),
            ("🌟 Motivation Systems", "Psychology-based engagement strategies"),
            ("🎮 Gamification Engagement", "Game mechanics and behavioral science"),
            ("🤝 Conflict Resolution", "Early detection and mediation strategies")
        ]
        
        for page_name, description in research_pages:
            st.markdown(f"""
            <div class="feature-card">
            <h4>{page_name}</h4>
            <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🤖 AI Assistant Interfaces")
        
        ai_pages = [
            ("🎓 Student AI Assistant", "Personalized learning support and team formation guidance"),
            ("👨‍🏫 Professor AI Dashboard", "Class analytics and intervention recommendations"),
            ("👨‍🏫 TA AI Assistant", "Priority task management and student support tools")
        ]
        
        for page_name, description in ai_pages:
            st.markdown(f"""
            <div class="feature-card">
            <h4>{page_name}</h4>
            <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### 🔧 Key Features")
        st.markdown("""
        - **Social Psychology Focus**: Evidence-based approaches rooted in educational research
        - **Interactive Dashboards**: Dynamic visualizations of group dynamics and engagement
        - **AI-Powered Insights**: Intelligent analysis of student collaboration patterns
        - **Role-Specific Tools**: Customized interfaces for students, TAs, and professors
        - **Real-Time Feedback**: Continuous monitoring and adaptive interventions
        """)
    
    # Course context
    st.markdown("""
    ---
    
    ### 📚 Course Context: Columbia University Introduction to Machine Learning
    
    - **👥 Class Size**: 80 students organized into 20 groups of 4
    - **⏱️ Duration**: 8-week collaborative ML pipeline development project
    - **🎯 Focus Areas**: Data preprocessing, feature engineering, model selection, training, and evaluation
    - **🧠 Group Dynamics**: Addressing personality diversity, trust building, and equal participation
    - **📈 Success Metrics**: Individual learning outcomes + collaborative effectiveness
    
    ---
    
    ### 🚀 Navigate Using the Sidebar
    Use the sidebar navigation to explore different aspects of AI-enhanced teaching assistance.
    Each page provides interactive visualizations, research insights, and practical applications.
    """)
    
    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 3rem; padding: 2rem; background-color: #f8f9fa; border-radius: 10px;">
    <h4>🎓 Evidence-Based Educational Innovation</h4>
    <p>This dashboard demonstrates how AI can enhance rather than replace human teaching, 
    focusing on social psychology principles and collaborative learning research.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()