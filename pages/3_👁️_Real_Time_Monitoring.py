import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

# Add the project root to the path
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import DATA_PATHS_STR

st.set_page_config(page_title="Real-Time Monitoring", page_icon="👁️", layout="wide")

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
    .insight-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .alert-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_monitoring_data():
    """Load real-time monitoring data"""
    return pd.read_csv(DATA_PATHS_STR['monitoring'])

@st.cache_data
def load_groups_data():
    """Load groups data"""
    return pd.read_csv(DATA_PATHS_STR['groups'])

def main():
    st.markdown('<h1 class="main-header">👁️ Real-Time Facilitation and Monitoring</h1>', unsafe_allow_html=True)
    
    # User Perspective Filter
    st.sidebar.markdown("### 👥 User Perspective")
    user_role = st.sidebar.selectbox(
        "View as:",
        ["Teaching Assistant", "Instructor", "Student", "AI System"]
    )
    
    # Time Range Filter
    st.sidebar.markdown("### ⏰ Time Range")
    time_range = st.sidebar.selectbox(
        "Monitoring Period:",
        ["Last 24 Hours", "Last Week", "Last Month", "Full Semester"]
    )
    
    # Load data
    monitoring_data = load_monitoring_data()
    groups_data = load_groups_data()
    
    # Convert timestamp
    monitoring_data['timestamp'] = pd.to_datetime(monitoring_data['timestamp'])
    
    # Key Research Insight
    st.markdown("""
    ## 🔬 Research Insight: Continuous Engagement Monitoring
    
    **Evidence from NSF iSAT Institute:** 35% increase in equal participation when AI systems monitor group dynamics in real-time with immediate intervention capabilities.
    """)
    
    # Real-time Dashboard Overview
    col1, col2, col3, col4 = st.columns(4)
    
    # Calculate key metrics
    current_engagement = monitoring_data['avg_engagement'].mean()
    intervention_rate = monitoring_data['ai_intervention'].mean() * 100
    participation_equality = monitoring_data['participation_equality'].mean()
    avg_meeting_duration = monitoring_data['meeting_duration'].mean()
    
    with col1:
        st.metric("Current Engagement", f"{current_engagement:.1f}/10", "▲ 0.8 from last week")
    with col2:
        st.metric("AI Intervention Rate", f"{intervention_rate:.1f}%", "▼ 2.3% from target")
    with col3:
        st.metric("Participation Equality", f"{participation_equality:.1f}/10", "▲ 1.2 improvement")
    with col4:
        st.metric("Avg Meeting Duration", f"{avg_meeting_duration:.0f} min", "Within target range")
    
    # Role-specific insights
    if user_role == "Teaching Assistant":
        st.markdown("""
        <div class="insight-box">
        <h4>👨‍🏫 TA Perspective: AI-Augmented Monitoring</h4>
        <p>Real-time AI monitoring allows you to manage more groups effectively:</p>
        <ul>
            <li><strong>Automated Alerts:</strong> Get notified when groups need intervention</li>
            <li><strong>Priority Dashboard:</strong> Focus attention on highest-risk groups first</li>
            <li><strong>Intervention Suggestions:</strong> AI recommends specific actions for each situation</li>
            <li><strong>Progress Tracking:</strong> Monitor improvement after interventions</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # TA-specific alerts
        high_risk_groups = monitoring_data[monitoring_data['avg_engagement'] < 6]['group_id'].unique()
        if len(high_risk_groups) > 0:
            st.markdown(f"""
            <div class="alert-box">
            <h4>⚠️ Attention Required</h4>
            <p><strong>{len(high_risk_groups)} groups</strong> need immediate attention: {', '.join(high_risk_groups[:5])}</p>
            </div>
            """, unsafe_allow_html=True)
        
    elif user_role == "Instructor":
        st.markdown("""
        <div class="insight-box">
        <h4>🎓 Instructor Perspective: Class-Wide Insights</h4>
        <p>Monitor overall class dynamics and intervention effectiveness:</p>
        <ul>
            <li><strong>Class Health Metrics:</strong> Overall engagement and participation trends</li>
            <li><strong>Intervention Effectiveness:</strong> Track success rates of AI recommendations</li>
            <li><strong>Resource Allocation:</strong> Optimize TA assignments based on group needs</li>
            <li><strong>Early Warning System:</strong> Identify at-risk students before they fall behind</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif user_role == "Student":
        st.markdown("""
        <div class="insight-box">
        <h4>🎓 Student Perspective: Collaborative Support</h4>
        <p>AI monitoring enhances your group experience:</p>
        <ul>
            <li><strong>Inclusive Participation:</strong> Ensures everyone's voice is heard</li>
            <li><strong>Timely Support:</strong> Get help when your group struggles</li>
            <li><strong>Fair Assessment:</strong> Accurate tracking of individual contributions</li>
            <li><strong>Conflict Prevention:</strong> Early intervention prevents major issues</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    else:  # AI System
        st.markdown("""
        <div class="insight-box">
        <h4>🤖 AI System Perspective: Monitoring Capabilities</h4>
        <p>Continuous analysis of multiple data streams:</p>
        <ul>
            <li><strong>Communication Patterns:</strong> Voice and text analysis for engagement</li>
            <li><strong>Participation Metrics:</strong> Speaking time, contribution frequency, idea generation</li>
            <li><strong>Emotional Indicators:</strong> Sentiment analysis and stress detection</li>
            <li><strong>Task Progress:</strong> Code commits, document edits, milestone completion</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Interactive Monitoring Dashboard
    st.markdown("## 📊 Real-Time Monitoring Dashboard")
    
    # Group selection for detailed view
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_groups = st.multiselect(
            "Select Groups to Monitor:",
            monitoring_data['group_id'].unique(),
            default=monitoring_data['group_id'].unique()[:5]
        )
    with col2:
        metric_to_show = st.selectbox(
            "Primary Metric:",
            ["avg_engagement", "participation_equality", "meeting_duration", "off_topic_minutes"]
        )
    with col3:
        show_interventions = st.checkbox("Highlight AI Interventions", value=True)
    
    # Filter data based on selections
    filtered_data = monitoring_data[monitoring_data['group_id'].isin(selected_groups)]
    
    # Time series visualization
    fig_timeline = px.line(filtered_data, x='timestamp', y=metric_to_show, color='group_id',
                          title=f"{metric_to_show.replace('_', ' ').title()} Over Time")
    
    if show_interventions:
        intervention_data = filtered_data[filtered_data['ai_intervention'] == True]
        fig_timeline.add_scatter(x=intervention_data['timestamp'], 
                               y=intervention_data[metric_to_show],
                               mode='markers', 
                               marker=dict(symbol='star', size=12, color='red'),
                               name='AI Interventions')
    
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Intervention Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        # Intervention effectiveness
        intervention_effect = filtered_data.groupby('ai_intervention').agg({
            'avg_engagement': 'mean',
            'participation_equality': 'mean'
        }).round(2)
        
        fig_intervention = go.Figure(data=[
            go.Bar(name='Engagement', x=['No Intervention', 'With Intervention'], 
                   y=[intervention_effect.loc[False, 'avg_engagement'], 
                      intervention_effect.loc[True, 'avg_engagement']],
                   marker_color='#3498db'),
            go.Bar(name='Participation Equality', x=['No Intervention', 'With Intervention'],
                   y=[intervention_effect.loc[False, 'participation_equality'],
                      intervention_effect.loc[True, 'participation_equality']],
                   marker_color='#2ecc71')
        ])
        
        fig_intervention.update_layout(
            title="AI Intervention Effectiveness",
            yaxis_title="Score (1-10)",
            barmode='group'
        )
        
        st.plotly_chart(fig_intervention, use_container_width=True)
    
    with col2:
        # Intervention types distribution
        intervention_types = filtered_data[filtered_data['ai_intervention'] == True]['intervention_type'].value_counts()
        
        fig_types = px.pie(values=intervention_types.values, names=intervention_types.index,
                          title="Types of AI Interventions")
        st.plotly_chart(fig_types, use_container_width=True)
    
    # Detailed Group Analysis
    st.markdown("## 🔍 Detailed Group Analysis")
    
    selected_group = st.selectbox("Select Group for Deep Dive:", selected_groups)
    
    if selected_group:
        group_data = filtered_data[filtered_data['group_id'] == selected_group]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            avg_engagement = group_data['avg_engagement'].mean()
            st.metric("Average Engagement", f"{avg_engagement:.1f}/10")
        with col2:
            intervention_count = group_data['ai_intervention'].sum()
            st.metric("Total Interventions", int(intervention_count))
        with col3:
            equality_trend = group_data['participation_equality'].diff().mean()
            trend_indicator = "▲" if equality_trend > 0 else "▼" if equality_trend < 0 else "►"
            st.metric("Equality Trend", f"{trend_indicator} {abs(equality_trend):.2f}")
        
        # Group timeline with annotations
        fig_group = make_subplots(
            rows=2, cols=1,
            subplot_titles=('Engagement Over Time', 'Meeting Characteristics'),
            shared_xaxes=True
        )
        
        # Engagement timeline
        fig_group.add_trace(
            go.Scatter(x=group_data['timestamp'], y=group_data['avg_engagement'],
                      name='Engagement', line=dict(color='#3498db')),
            row=1, col=1
        )
        
        # Meeting duration
        fig_group.add_trace(
            go.Scatter(x=group_data['timestamp'], y=group_data['meeting_duration'],
                      name='Duration (min)', line=dict(color='#e74c3c')),
            row=2, col=1
        )
        
        # Add intervention markers as scatter points to avoid timestamp arithmetic issues
        interventions = group_data[group_data['ai_intervention'] == True]
        if not interventions.empty:
            fig_group.add_trace(
                go.Scatter(
                    x=interventions['timestamp'],
                    y=[group_data['avg_engagement'].max()] * len(interventions),
                    mode='markers',
                    marker=dict(
                        symbol='line-ns',
                        size=15,
                        color='red',
                        line=dict(width=2)
                    ),
                    name='AI Interventions',
                    showlegend=True,
                    hovertext=[f"Intervention: {it}" for it in interventions['intervention_type']]
                ),
                row=1, col=1
            )
        
        fig_group.update_layout(height=600, title=f"Detailed Analysis: {selected_group}")
        st.plotly_chart(fig_group, use_container_width=True)
    
    # AI Monitoring Technology
    st.markdown("## 🤖 AI Monitoring Technology")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📡 Data Collection Methods
        
        **Audio Analysis:**
        - Speech pattern recognition
        - Speaking time distribution
        - Emotional tone detection
        - Silence pattern analysis
        
        **Text Analysis:**
        - Chat message sentiment
        - Idea contribution tracking
        - Question-answer patterns
        - Collaborative language use
        
        **Behavioral Metrics:**
        - Screen time and focus
        - Document collaboration
        - Code contribution patterns
        - Meeting attendance
        """)
    
    with col2:
        # Technology effectiveness metrics
        tech_metrics = {
            'Technology': ['Audio Analysis', 'Text Analysis', 'Behavioral Tracking', 'Combined AI'],
            'Accuracy': [78, 85, 82, 94],
            'Response Time': [95, 88, 92, 89]  # Inverted for better is higher
        }
        
        fig_tech = go.Figure(data=[
            go.Bar(name='Accuracy %', x=tech_metrics['Technology'], y=tech_metrics['Accuracy'], marker_color='#2ecc71'),
            go.Bar(name='Response Speed', x=tech_metrics['Technology'], y=tech_metrics['Response Time'], marker_color='#3498db')
        ])
        
        fig_tech.update_layout(
            title="Monitoring Technology Performance",
            yaxis_title="Performance Score",
            barmode='group'
        )
        
        st.plotly_chart(fig_tech, use_container_width=True)
    
    # Live Alerts Simulation
    st.markdown("## 🚨 Live Monitoring Alerts")
    
    # Simulate real-time alerts
    alerts = [
        {"group": "GRP003", "type": "Low Participation", "severity": "Medium", "action": "Prompt quiet member"},
        {"group": "GRP007", "type": "Off-topic Discussion", "severity": "Low", "action": "Redirect conversation"},
        {"group": "GRP012", "type": "Conflict Detected", "severity": "High", "action": "Immediate intervention"},
        {"group": "GRP015", "type": "Engagement Drop", "severity": "Medium", "action": "Suggest break"}
    ]
    
    for alert in alerts:
        severity_colors = {"Low": "success-box", "Medium": "alert-box", "High": "alert-box"}
        severity_icons = {"Low": "🟢", "Medium": "🟡", "High": "🔴"}
        
        st.markdown(f"""
        <div class="{severity_colors[alert['severity']]}">
        <strong>{severity_icons[alert['severity']]} {alert['group']}: {alert['type']}</strong><br>
        Severity: {alert['severity']} | Recommended Action: {alert['action']}
        </div>
        """, unsafe_allow_html=True)
    
    # Implementation Guidelines
    st.markdown("## 💡 Implementation Guidelines")
    
    guidelines = {
        "Teaching Assistant": [
            "Set up monitoring dashboard at beginning of each session",
            "Respond to high-severity alerts within 5 minutes",
            "Use AI suggestions but apply human judgment",
            "Document intervention outcomes for system learning"
        ],
        "Instructor": [
            "Review weekly monitoring reports for class trends",
            "Adjust intervention thresholds based on class dynamics",
            "Use data to inform future course design",
            "Share anonymized insights with other instructors"
        ],
        "Student": [
            "Understand that monitoring aims to improve group experience",
            "Provide feedback on AI intervention effectiveness",
            "Use individual engagement reports for self-reflection",
            "Respect privacy settings and data use policies"
        ],
        "AI System": [
            "Continuously calibrate detection algorithms",
            "Learn from successful intervention patterns",
            "Adapt to different group personalities and dynamics",
            "Maintain privacy and ethical monitoring standards"
        ]
    }
    
    if user_role in guidelines:
        st.markdown(f"### 📋 Guidelines for {user_role}s:")
        for i, guideline in enumerate(guidelines[user_role], 1):
            st.markdown(f"{i}. {guideline}")

if __name__ == "__main__":
    main()
