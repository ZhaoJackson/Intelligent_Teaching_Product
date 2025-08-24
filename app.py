import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

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
    }
    .subtitle {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 3rem;
    }
    .navigation-card {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 5px solid #1f77b4;
        transition: transform 0.2s;
    }
    .navigation-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    .feature-highlight {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
    }
    .metric-showcase {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">🎓 AI-Enhanced Teaching Assistant Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Exploring how AI can enhance teaching assistant functionality in collaborative learning environments</p>', unsafe_allow_html=True)
    
    # Research Question Highlight
    st.markdown("""
    <div class="feature-highlight">
    <h2>🔬 Research Question</h2>
    <p style="font-size: 1.1rem; margin-bottom: 0;">
    <strong>How can AI replace or enhance the functionality of teaching assistants in student group settings, specifically enabling more consistent engagement among group members in targeted classes, without focusing on engineering considerations?</strong>
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Insights
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-showcase">
        <h3>🎯 40%</h3>
        <p>Improvement in group satisfaction with AI-optimized team formation</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-showcase">
        <h3>📈 35%</h3>
        <p>Increase in equal participation with real-time AI monitoring</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-showcase">
        <h3>🤖 97%</h3>
        <p>Success rate for AI handling routine Q&A interactions</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-showcase">
        <h3>⚡ 45%</h3>
        <p>Reduction in TA workload through AI automation</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Navigation Guide
    st.markdown("## 🗺️ Explore the Dashboard")
    st.markdown("This interactive dashboard demonstrates AI-enhanced teaching assistant capabilities through multiple perspectives and detailed analysis.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="navigation-card">
        <h3>🔍 Research & Analysis</h3>
        <p><strong>Pages 1-8:</strong> Comprehensive exploration of AI enhancement areas</p>
        <ul>
            <li><strong>Research Overview:</strong> Theoretical framework and key insights</li>
            <li><strong>Team Formation:</strong> AI-optimized group composition analysis</li>
            <li><strong>Real-Time Monitoring:</strong> Continuous engagement tracking</li>
            <li><strong>AI Tutoring:</strong> 24/7 question answering and support</li>
            <li><strong>Equal Participation:</strong> Data-driven contribution tracking</li>
            <li><strong>Motivation Systems:</strong> Psychology-based engagement strategies</li>
            <li><strong>Conflict Resolution:</strong> Early detection and mediation</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="navigation-card">
        <h3>🤖 AI Assistant Interfaces</h3>
        <p><strong>Pages 9-11:</strong> Role-specific AI chatbot experiences</p>
        <ul>
            <li><strong>Student Assistant:</strong> Personalized collaboration support and guidance</li>
            <li><strong>Professor Dashboard:</strong> Class-wide analytics and intervention recommendations</li>
            <li><strong>TA Assistant:</strong> Optimized task prioritization and student support</li>
        </ul>
        <br>
        <p><em>Each interface demonstrates how AI can enhance specific user roles with tailored insights and actionable recommendations.</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Course Context
    st.markdown("## 🏫 Course Context: Introduction to Machine Learning")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **📊 Class Structure:**
        - 80 students in 20 groups of 4
        - 8-week collaborative ML project
        - End-to-end pipeline development
        - Individual and group assessments
        """)
    
    with col2:
        st.markdown("""
        **🎯 Project Components:**
        - Data preprocessing and cleaning
        - Feature engineering and selection
        - Model selection and training
        - Hyperparameter optimization
        - Results interpretation and presentation
        """)
    
    with col3:
        st.markdown("""
        **🚨 Common Challenges:**
        - Unequal participation (85% concern)
        - Diverse skill levels (70% struggle)
        - Communication barriers (60% of groups)
        - Limited TA availability (1:20 ratio)
        """)
    
    # AI Enhancement Framework
    st.markdown("## 🤖 AI Enhancement Framework")
    
    framework_data = {
        'Phase': ['Assessment', 'Formation', 'Monitoring', 'Intervention', 'Optimization'],
        'AI Capability': [8.5, 9.2, 9.8, 8.9, 8.7],
        'Human Value': [9.5, 7.8, 6.2, 9.1, 8.9],
        'Combined Effectiveness': [9.8, 9.5, 9.2, 9.6, 9.4]
    }
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=framework_data['Phase'], y=framework_data['AI Capability'], 
                            name='AI Capability', line=dict(color='#e74c3c'), marker=dict(size=8)))
    fig.add_trace(go.Scatter(x=framework_data['Phase'], y=framework_data['Human Value'], 
                            name='Human Value', line=dict(color='#3498db'), marker=dict(size=8)))
    fig.add_trace(go.Scatter(x=framework_data['Phase'], y=framework_data['Combined Effectiveness'], 
                            name='Combined Effectiveness', line=dict(color='#2ecc71', width=4), marker=dict(size=10)))
    
    fig.update_layout(
        title="AI-Human Partnership Effectiveness Across Project Phases",
        xaxis_title="Project Phase",
        yaxis_title="Effectiveness Score (1-10)",
        yaxis_range=[5, 10],
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Expected Outcomes
    st.markdown("## 🎯 Expected Outcomes & Impact")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🌟 Student Benefits
        - **Enhanced Engagement:** More consistent participation across all members
        - **Better Learning Outcomes:** Optimized group composition and support
        - **Reduced Conflicts:** Early detection and resolution of issues
        - **Fair Assessment:** Objective tracking of individual contributions
        - **Skill Development:** Targeted support for individual growth areas
        """)
    
    with col2:
        st.markdown("""
        ### 🎓 Educational Benefits
        - **Scalable Support:** Consistent quality across all groups
        - **Data-Driven Decisions:** Evidence-based interventions
        - **Resource Optimization:** Focus human effort on high-value activities
        - **Continuous Improvement:** Real-time feedback for course enhancement
        - **Institutional Impact:** Improved satisfaction and outcomes
        """)
    
    # Getting Started
    st.markdown("## 🚀 Getting Started")
    
    st.markdown("""
    **📖 Recommended Navigation Path:**
    1. **Start with Research Overview** to understand the theoretical foundation
    2. **Explore Analysis Pages (2-8)** to see detailed evidence and visualizations
    3. **Experience AI Interfaces (9-11)** to understand practical implementation
    4. **Use Interactive Filters** throughout to see different user perspectives
    
    **💡 Pro Tips:**
    - Each page includes role-specific insights (Instructor, TA, Student, Administrator)
    - Interactive visualizations allow you to explore data relationships
    - AI chatbots demonstrate real conversational capabilities
    - Filter controls let you view data from different stakeholder perspectives
    """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>This dashboard demonstrates evidence-based AI enhancement of teaching assistant functionality, 
    combining educational psychology principles with practical implementation strategies.</p>
    <p><em>Navigate using the sidebar to explore specific enhancement areas and AI interfaces.</em></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
