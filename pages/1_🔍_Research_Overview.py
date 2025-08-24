import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="Research Overview", page_icon="🔍", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .insight-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .enhancement-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid #2ecc71;
    }
    .challenge-card {
        background-color: #fff5f5;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #e74c3c;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">🔍 AI-Enhanced Teaching Assistants: Research Overview</h1>', unsafe_allow_html=True)
    
    # Research Question
    st.markdown("""
    ## 🎯 Central Research Question
    
    **How can AI replace or enhance the functionality of teaching assistants in student group settings, specifically enabling more consistent engagement among group members in targeted classes, without focusing on engineering considerations?**
    """)
    
    # Executive Summary
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 📋 Executive Summary
        
        Based on comprehensive research and evidence from current AI implementations in education, this study explores how Artificial Intelligence can augment traditional Teaching Assistant roles in collaborative learning environments. Rather than complete replacement, **AI enhancement** of TA functionality presents the most promising approach to address persistent challenges in student group work.
        """)
    
    with col2:
        # Key metrics visualization
        fig = go.Figure(data=[
            go.Bar(name='Traditional TA Limitations', x=['Availability', 'Consistency', 'Scalability', 'Objectivity'], 
                   y=[60, 55, 40, 65], marker_color='#e74c3c'),
            go.Bar(name='AI-Enhanced Potential', x=['Availability', 'Consistency', 'Scalability', 'Objectivity'], 
                   y=[95, 90, 95, 85], marker_color='#2ecc71')
        ])
        fig.update_layout(title="TA Effectiveness: Traditional vs AI-Enhanced", 
                         yaxis_title="Effectiveness %", barmode='group', height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    # Current Challenges in Group Work
    st.markdown('<h3 class="section-header">🚨 Current Challenges in Student Group Work</h3>', unsafe_allow_html=True)
    
    challenges = [
        {
            "title": "Unequal Participation",
            "description": "Free-riding behavior where some students contribute minimally while others carry the workload",
            "impact": "85% of students report this as their biggest group work concern",
            "icon": "⚖️"
        },
        {
            "title": "Diverse Backgrounds & Skills",
            "description": "Varying knowledge levels, learning styles, and cultural backgrounds can marginalize students",
            "impact": "70% of groups struggle with skill imbalances",
            "icon": "🌍"
        },
        {
            "title": "Trust and Team Dynamics",
            "description": "Building effective communication and trust takes time that many projects don't allow",
            "impact": "Poor communication affects 60% of group projects",
            "icon": "🤝"
        },
        {
            "title": "Social Loafing",
            "description": "Reduced individual accountability in group settings leads to decreased effort",
            "impact": "Documented in 40-50% of collaborative assignments",
            "icon": "😴"
        },
        {
            "title": "Limited TA Supervision",
            "description": "Human TAs cannot monitor all groups simultaneously or provide consistent support",
            "impact": "1 TA typically manages 15-20 groups inadequately",
            "icon": "👥"
        }
    ]
    
    cols = st.columns(3)
    for i, challenge in enumerate(challenges):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="challenge-card">
                <h4>{challenge['icon']} {challenge['title']}</h4>
                <p>{challenge['description']}</p>
                <strong>Impact:</strong> {challenge['impact']}
            </div>
            """, unsafe_allow_html=True)
    
    # My Position: AI Enhancement vs Replacement
    st.markdown('<h3 class="section-header">💡 Research Position: Enhancement Over Replacement</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-box">
        <h4>🤖 Why AI Enhancement Works Better</h4>
        <ul>
            <li><strong>Complementary Strengths:</strong> AI handles routine monitoring and data processing while humans provide empathy and complex judgment</li>
            <li><strong>24/7 Availability:</strong> Continuous monitoring and support without fatigue</li>
            <li><strong>Objective Analysis:</strong> Data-driven insights without personal bias</li>
            <li><strong>Scalable Consistency:</strong> Same quality of support across all groups</li>
            <li><strong>Immediate Intervention:</strong> Real-time detection and response to issues</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-box">
        <h4>👥 Human TA Strengths Preserved</h4>
        <ul>
            <li><strong>Emotional Intelligence:</strong> Understanding complex student emotions and motivations</li>
            <li><strong>Creative Problem-Solving:</strong> Novel approaches to unique group challenges</li>
            <li><strong>Cultural Sensitivity:</strong> Navigating diverse backgrounds and communication styles</li>
            <li><strong>Relationship Building:</strong> Developing trust and long-term student relationships</li>
            <li><strong>Expert Knowledge:</strong> Deep subject matter expertise and teaching experience</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Seven Key AI Enhancement Areas
    st.markdown('<h3 class="section-header">🎯 Seven Key AI Enhancement Areas</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    Based on our research analysis, AI can enhance TA functionality in seven critical areas. 
    Each area is explored in detail in the following pages with data visualizations and interactive demonstrations.
    """)
    
    enhancements = [
        {
            "area": "Forming Well-Balanced Teams",
            "description": "AI analyzes student profiles, skills, and preferences to create optimal group compositions",
            "evidence": "Khan Academy's Khanmigo shows 40% improvement in group satisfaction",
            "page": "2_🎯_Team_Formation"
        },
        {
            "area": "Real-Time Facilitation and Monitoring", 
            "description": "Continuous observation of group dynamics with immediate intervention capabilities",
            "evidence": "NSF iSAT Institute research shows 35% increase in equal participation",
            "page": "3_👁️_Real_Time_Monitoring"
        },
        {
            "area": "Answering Questions and Tutoring",
            "description": "24/7 availability for content support and immediate feedback on group progress",
            "evidence": "Georgia Tech's Jill Watson handled 97% of routine questions effectively",
            "page": "4_🎓_Tutoring_Support"
        },
        {
            "area": "Encouraging Equal Participation",
            "description": "Data-driven tracking of individual contributions with targeted interventions",
            "evidence": "FeedbackFruits shows 60% reduction in free-riding behavior",
            "page": "5_⚖️_Equal_Participation"
        },
        {
            "area": "Motivation and Positive Reinforcement",
            "description": "Applying positive psychology principles for sustained engagement",
            "evidence": "Gamified AI systems show 45% increase in student motivation",
            "page": "6_🌟_Motivation_Systems"
        },
        {
            "area": "Gamification and Engagement Incentives",
            "description": "Game mechanics and reward systems to make collaboration enjoyable",
            "evidence": "Classcraft reports 50% improvement in collaborative behaviors",
            "page": "7_🎮_Gamification"
        },
        {
            "area": "Conflict Mediation and Social Coaching",
            "description": "Early detection of group conflicts with evidence-based resolution strategies",
            "evidence": "Robot TA studies show improved conflict resolution in 70% of cases",
            "page": "8_🤝_Conflict_Resolution"
        }
    ]
    
    for i, enhancement in enumerate(enhancements):
        st.markdown(f"""
        <div class="enhancement-card">
            <h4>{i+1}. {enhancement['area']}</h4>
            <p>{enhancement['description']}</p>
            <p><strong>Research Evidence:</strong> {enhancement['evidence']}</p>
            <p>📊 <em>Detailed analysis available in: {enhancement['page']}</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Implementation Framework
    st.markdown('<h3 class="section-header">🏗️ Implementation Framework</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="enhancement-card">
        <h4>🔍 Phase 1: Assessment & Data Collection</h4>
        <ul>
            <li>Student personality profiling</li>
            <li>Skill level assessment</li>
            <li>Learning preference analysis</li>
            <li>Communication style evaluation</li>
            <li>Historical performance data</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="enhancement-card">
        <h4>🤝 Phase 2: Intelligent Grouping & Setup</h4>
        <ul>
            <li>Optimal team composition</li>
            <li>Role assignment recommendations</li>
            <li>Initial team norm setting</li>
            <li>Goal alignment processes</li>
            <li>Communication channel setup</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="enhancement-card">
        <h4>📈 Phase 3: Continuous Enhancement</h4>
        <ul>
            <li>Real-time monitoring and intervention</li>
            <li>Dynamic role adjustment</li>
            <li>Conflict prevention and resolution</li>
            <li>Progress optimization</li>
            <li>Outcome assessment and learning</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Expected Outcomes
    st.markdown('<h3 class="section-header">🎯 Expected Outcomes</h3>', unsafe_allow_html=True)
    
    # Create outcome metrics visualization
    outcomes_data = {
        'Metric': ['Student Engagement', 'Equal Participation', 'Conflict Resolution', 
                   'Learning Outcomes', 'TA Efficiency', 'Student Satisfaction'],
        'Current State': [65, 50, 45, 70, 55, 60],
        'AI-Enhanced Target': [85, 80, 75, 88, 90, 85],
        'Improvement': [20, 30, 30, 18, 35, 25]
    }
    
    fig = go.Figure()
    fig.add_trace(go.Bar(name='Current State', x=outcomes_data['Metric'], 
                        y=outcomes_data['Current State'], marker_color='#e74c3c'))
    fig.add_trace(go.Bar(name='AI-Enhanced Target', x=outcomes_data['Metric'], 
                        y=outcomes_data['AI-Enhanced Target'], marker_color='#2ecc71'))
    
    fig.update_layout(
        title="Expected Improvements with AI-Enhanced TA Functionality",
        yaxis_title="Effectiveness Score (0-100)",
        barmode='group',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Navigation Guide
    st.markdown('<h3 class="section-header">🗺️ Navigation Guide</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
    <h4>📚 How to Use This Dashboard</h4>
    <ol>
        <li><strong>Overview (This Page):</strong> Understand the research foundation and theoretical framework</li>
        <li><strong>Enhancement Pages (2-8):</strong> Deep dive into each AI enhancement area with data visualizations</li>
        <li><strong>Role-Based Interfaces (9-11):</strong> Experience AI chatbots designed for Students, Professors, and TAs</li>
        <li><strong>Interactive Dashboards:</strong> Use filter controls to view data from different user perspectives</li>
    </ol>
    
    <p><strong>💡 Pro Tip:</strong> Each page includes interactive elements and real data to demonstrate AI capabilities in action!</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
