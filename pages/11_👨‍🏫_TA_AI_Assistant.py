import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import random
import sys
import os

# Add the project root to the path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.azure_openai import get_ai_response, format_context_data
from prompts.ta_prompts import SYSTEM_PROMPT, TASK_PRIORITIZATION_PROMPT, CONFLICT_MEDIATION_PROMPT

st.set_page_config(page_title="TA AI Assistant", page_icon="👨‍🏫", layout="wide")

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
    .task-card {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
        border-left: 4px solid #3498db;
    }
    .urgent-task {
        border-left-color: #e74c3c;
        background-color: #fdf2f2;
    }
    .medium-task {
        border-left-color: #f39c12;
        background-color: #fffbf2;
    }
    .low-task {
        border-left-color: #2ecc71;
        background-color: #f2fdf7;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .user-message {
        background-color: #e3f2fd;
        margin-left: 20%;
    }
    .assistant-message {
        background-color: #f5f5f5;
        margin-right: 20%;
    }
    .success-metric {
        background-color: #d4edda;
        padding: 0.5rem;
        border-radius: 5px;
        text-align: center;
        margin: 0.3rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_ta_data():
    """Load data relevant for TA dashboard"""
    students_df = pd.read_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/students.csv')
    groups_df = pd.read_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/groups.csv')
    monitoring_df = pd.read_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/monitoring.csv')
    tutoring_df = pd.read_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/tutoring.csv')
    conflicts_df = pd.read_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/conflicts.csv')
    participation_df = pd.read_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/participation.csv')
    return students_df, groups_df, monitoring_df, tutoring_df, conflicts_df, participation_df

def generate_ta_ai_response(prompt: str, ta_data: dict) -> str:
    """Generate contextual AI responses for TAs using Azure OpenAI"""
    try:
        # Format context data for the AI
        context = format_context_data(
            additional_context={
                "ta_metrics": ta_data,
                "course_context": "Columbia University Introduction to Machine Learning course",
                "class_size": "80 students in 20 groups of 4",
                "ta_role": "Teaching Assistant supporting collaborative ML projects"
            }
        )
        
        # Determine the appropriate prompt template based on user input
        prompt_lower = prompt.lower()
        
        if any(word in prompt_lower for word in ['priority', 'urgent', 'task', 'today']):
            system_prompt = SYSTEM_PROMPT
            formatted_prompt = TASK_PRIORITIZATION_PROMPT.format(
                active_conflicts=ta_data.get('active_conflicts', 3),
                at_risk_students=ta_data.get('at_risk_count', 5),
                struggling_groups=ta_data.get('high_risk_groups', 3),
                routine_tasks=ta_data.get('review_groups', []),
                office_hours_requests=random.randint(5, 15),
                available_hours=8,
                student_needs_data="Multiple students need technical and collaboration support",
                group_status_data="Several groups showing early warning signs"
            )
            user_prompt = f"User request: {prompt}\n\n{formatted_prompt}"
            
        elif any(word in prompt_lower for word in ['conflict', 'mediate', 'dispute', 'argument']):
            system_prompt = SYSTEM_PROMPT
            formatted_prompt = CONFLICT_MEDIATION_PROMPT.format(
                group_id=ta_data.get('conflict_group', 'GRP007'),
                conflict_type=ta_data.get('conflict_type', 'Leadership role dispute'),
                participants="2 students with different leadership styles",
                conflict_duration="6 hours",
                learning_impact="25% decrease in group productivity",
                background_context="Group struggling with role clarity and decision-making authority",
                personality_profiles="Analytical vs Creative personality types causing approach conflicts"
            )
            user_prompt = f"User request: {prompt}\n\n{formatted_prompt}"
            
        else:
            # General TA query
            system_prompt = SYSTEM_PROMPT
            user_prompt = f"""
            The TA is asking: "{prompt}"
            
            Current TA context:
            - Priority tasks: {ta_data.get('priority_tasks', 6)}
            - At-risk students: {ta_data.get('at_risk_count', 5)}
            - Active conflicts: {ta_data.get('active_conflicts', 3)}
            - Success rate: {ta_data.get('ta_success_rate', 89.2)}%
            - Time saved through AI: {ta_data.get('time_saved', 12.5)} hours/week
            
            Provide helpful guidance that addresses their question while considering their role as a TA supporting collaborative ML projects.
            """
        
        # Get AI response
        response = get_ai_response(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            context_data=context,
            temperature=0.7,
            max_tokens=1200
        )
        
        return response
        
    except Exception as e:
        # Fallback to basic response if AI fails
        st.error(f"AI service error: {str(e)}")
        st.error(f"Error type: {type(e).__name__}")
        return f"""
🎯 **TA Priority Dashboard** (Static Mode)

**Current Status:**
- Priority Tasks: {ta_data.get('priority_tasks', 6)}
- At-Risk Students: {ta_data.get('at_risk_count', 5)}
- Active Conflicts: {ta_data.get('active_conflicts', 3)}
- Success Rate: {ta_data.get('ta_success_rate', 89.2)}%

**Quick Actions Available:**
- Use the dashboard visualizations for group insights
- Check student analytics for intervention guidance
- Review conflict resolution resources
- Monitor progress through the performance tracking tools

        Please try your question again when the AI service is restored!
        """

def main():
    st.markdown('<h1 class="main-header">👨‍🏫 TA AI Assistant Dashboard</h1>', unsafe_allow_html=True)
    
    # Load data
    students_df, groups_df, monitoring_df, tutoring_df, conflicts_df, participation_df = load_ta_data()
    
    # Calculate TA-specific metrics
    ta_data = {
        'urgent_groups': ['007', '012'],
        'medium_groups': ['003', '018'],
        'at_risk_student': 'STU025',
        'tech_help_groups': ['GRP003', 'GRP008', 'GRP015'],
        'review_groups': groups_df[groups_df['risk_level'] == 'Low'],
        'active_conflicts': 3,
        'resolution_rate': 87.3,
        'avg_resolution_time': 4.2,
        'common_conflicts': ['Unequal participation', 'Technical disagreements', 'Communication styles'],
        'conflict_group': 'GRP007',
        'conflict_type': 'Leadership role dispute',
        'high_priority_students': 5,
        'medium_priority_students': 12,
        'improved_students': 8,
        'focus_student': 'Alex Chen',
        'student_engagement': 5.8,
        'student_collaboration': 6.2,
        'student_technical': 7.1,
        'participation_trend': '▼ Declining',
        'student_personality': 'Analytical',
        'best_approach': 'structured guidance',
        'learning_style': 'Visual learner',
        'learning_support': 'diagrams and examples',
        'motivation_type': 'Achievement-focused',
        'motivation_strategy': 'clear progress milestones',
        'stress_level': 'Moderate',
        'stress_support': 'workload management',
        'high_performing_groups': 12,
        'moderate_risk_groups': 5,
        'high_risk_groups': 3,
        'priority_group_1': 'GRP007',
        'project_topic_1': 'Customer Churn Prediction',
        'risk_factors_1': ['Personality conflicts', 'Missed deadlines'],
        'last_checkin_1': 3,
        'progress_1': 65,
        'ai_recommendation_1': 'Immediate conflict mediation + timeline adjustment',
        'priority_group_2': 'GRP012',
        'project_topic_2': 'Image Classification for Medical Diagnosis',
        'opportunity_2': 'Strong technical skills but communication gaps',
        'strengths_2': 'Advanced coding abilities',
        'growth_area_2': 'Team coordination',
        'suggested_action_2': 'Communication workshop + role clarification',
        'avg_engagement': 7.4,
        'avg_meetings': 2.3,
        'avg_commits': 18,
        'doc_quality': 78,
        'comm_issues': 4,
        'workload_issues': 3,
        'tech_struggles': 6,
        'motivation_decline': 2,
        'students_supported': 45,
        'groups_guided': 18,
        'conflicts_resolved': 12,
        'ta_success_rate': 89.2,
        'response_time': 11.3,
        'student_satisfaction': 8.6,
        'intervention_effectiveness': 87.5,
        'workload_efficiency': 45.2,
        'success_group_1': 'GRP009',
        'success_student': 'Maria Rodriguez',
        'success_group_2': 'GRP014',
        'success_group_3': 'GRP006',
        'engagement_improvement': 23.1,
        'conflict_prevention': 67.8,
        'learning_improvement': 18.4,
        'time_optimization': 42.6,
        'priority_tasks': 6,
        'at_risk_count': 5,
        'time_saved': 12.5
    }
    
    # Top-level TA metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Priority Tasks", ta_data['priority_tasks'], "▼ 2 from yesterday")
    with col2:
        st.metric("Response Time", f"{ta_data['response_time']:.1f} min", "▼ 3.2 min")
    with col3:
        st.metric("Student Satisfaction", f"{ta_data['student_satisfaction']:.1f}/10", "▲ 0.4")
    with col4:
        st.metric("Success Rate", f"{ta_data['ta_success_rate']:.1f}%", "▲ 2.1%")
    with col5:
        st.metric("Time Saved", f"{ta_data['time_saved']:.1f}h/week", "AI automation")
    
    # Priority Task Dashboard
    st.markdown("## 🎯 Priority Task Board")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🔴 Urgent Tasks")
        urgent_tasks = [
            {"title": "Group 007 Conflict", "desc": "Leadership dispute escalation", "time": "2 hours"},
            {"title": "Student Check-in", "desc": "Alex Chen - engagement drop", "time": "30 min"}
        ]
        
        for task in urgent_tasks:
            st.markdown(f"""
            <div class="task-card urgent-task">
            <strong>{task['title']}</strong><br>
            {task['desc']}<br>
            <em>Est. time: {task['time']}</em>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🟡 Medium Priority")
        medium_tasks = [
            {"title": "Group 012 Dynamics", "desc": "Communication improvement needed", "time": "45 min"},
            {"title": "Technical Support", "desc": "3 groups need preprocessing help", "time": "90 min"}
        ]
        
        for task in medium_tasks:
            st.markdown(f"""
            <div class="task-card medium-task">
            <strong>{task['title']}</strong><br>
            {task['desc']}<br>
            <em>Est. time: {task['time']}</em>
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("### 🟢 Low Priority")
        low_tasks = [
            {"title": "Progress Reviews", "desc": "12 groups routine check-ins", "time": "2 hours"},
            {"title": "Resource Updates", "desc": "Update tutorial materials", "time": "30 min"}
        ]
        
        for task in low_tasks:
            st.markdown(f"""
            <div class="task-card low-task">
            <strong>{task['title']}</strong><br>
            {task['desc']}<br>
            <em>Est. time: {task['time']}</em>
            </div>
            """, unsafe_allow_html=True)
    
    # Main Interface
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Quick stats and alerts
        st.markdown("### 📊 Quick Analytics")
        
        # Group status pie chart
        group_status = {
            'High Risk': ta_data['high_risk_groups'],
            'Medium Risk': ta_data['moderate_risk_groups'], 
            'Low Risk': ta_data['high_performing_groups']
        }
        
        fig_status = px.pie(values=list(group_status.values()), names=list(group_status.keys()),
                           title="Group Risk Distribution",
                           color_discrete_map={'High Risk': '#e74c3c', 'Medium Risk': '#f39c12', 'Low Risk': '#2ecc71'})
        st.plotly_chart(fig_status, use_container_width=True)
        
        # Performance metrics
        st.markdown("### 🏆 Your Performance")
        performance_metrics = [
            ("Response Time", f"{ta_data['response_time']:.1f} min", "🎯"),
            ("Success Rate", f"{ta_data['ta_success_rate']:.1f}%", "📈"),
            ("Student Rating", f"{ta_data['student_satisfaction']:.1f}/10", "⭐"),
            ("Conflicts Resolved", f"{ta_data['conflicts_resolved']}", "🤝")
        ]
        
        for metric, value, icon in performance_metrics:
            st.markdown(f"""
            <div class="success-metric">
            {icon} <strong>{metric}:</strong> {value}
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # AI Chat Interface
        st.markdown("### 🤖 AI Assistant Chat")
        
        # Initialize chat history
        if "ta_messages" not in st.session_state:
            st.session_state.ta_messages = [
                {"role": "assistant", "content": "Hello! I'm your AI TA assistant. I can help you prioritize tasks, resolve conflicts, support students, and track your effectiveness. What would you like to focus on today?"}
            ]
        
        # Chat display
        chat_container = st.container()
        with chat_container:
            for message in st.session_state.ta_messages:
                css_class = "user-message" if message["role"] == "user" else "assistant-message"
                st.markdown(f"""
                <div class="chat-message {css_class}">
                {message["content"]}
                </div>
                """, unsafe_allow_html=True)
        
        # Chat input
        if prompt := st.chat_input("Ask about priorities, conflicts, students, or analytics..."):
            st.session_state.ta_messages.append({"role": "user", "content": prompt})
            
            # Generate AI response
            response = generate_ta_ai_response(prompt, ta_data)
            st.session_state.ta_messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    # Detailed Analytics Tabs
    st.markdown("## 📊 Detailed Analytics")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🚨 Active Issues", "👥 Student Support", "📈 Performance Tracking", "🛠️ Resources"])
    
    with tab1:
        # Active issues that need attention
        st.markdown("### 🔍 Issues Requiring Immediate Attention")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Conflict timeline
            conflict_timeline = [
                {"time": "2 hours ago", "group": "GRP007", "issue": "Leadership dispute detected", "severity": "High"},
                {"time": "4 hours ago", "group": "GRP012", "issue": "Participation inequality", "severity": "Medium"},
                {"time": "1 day ago", "group": "GRP003", "issue": "Technical barriers", "severity": "Low"}
            ]
            
            st.markdown("**Recent Issues Detected:**")
            for issue in conflict_timeline:
                severity_colors = {"High": "#e74c3c", "Medium": "#f39c12", "Low": "#2ecc71"}
                st.markdown(f"""
                <div style="border-left: 4px solid {severity_colors[issue['severity']]}; padding: 0.5rem; margin: 0.5rem 0; background-color: #f8f9fa;">
                <strong>{issue['group']}</strong> - {issue['issue']}<br>
                <em>{issue['time']} | Severity: {issue['severity']}</em>
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            # Student engagement alerts
            at_risk_students = students_df[students_df['engagement_score'] < 6.5].head(5)
            
            st.markdown("**Students Needing Support:**")
            for _, student in at_risk_students.iterrows():
                st.markdown(f"""
                <div style="border-left: 4px solid #e74c3c; padding: 0.5rem; margin: 0.5rem 0; background-color: #fdf2f2;">
                <strong>{student['student_name']}</strong><br>
                Engagement: {student['engagement_score']}/10 | Group: {student['group_id']}<br>
                <em>Personality: {student['personality_type']} | Role: {student['preferred_role']}</em>
                </div>
                """, unsafe_allow_html=True)
    
    with tab2:
        # Student support tracking
        col1, col2 = st.columns(2)
        
        with col1:
            # Support effectiveness over time
            weeks = list(range(1, 9))
            supported_engagement = [6.2, 6.8, 7.1, 7.5, 7.8, 8.0, 8.2, 8.4]
            baseline_engagement = [6.2, 6.1, 6.0, 5.9, 5.8, 5.7, 5.6, 5.5]
            
            fig_support = go.Figure()
            fig_support.add_trace(go.Scatter(x=weeks, y=supported_engagement, name='With TA Support', line=dict(color='#2ecc71')))
            fig_support.add_trace(go.Scatter(x=weeks, y=baseline_engagement, name='Without Support', line=dict(color='#e74c3c')))
            fig_support.update_layout(title="Student Engagement: Supported vs Unsupported", xaxis_title="Week", yaxis_title="Engagement Score")
            st.plotly_chart(fig_support, use_container_width=True)
        
        with col2:
            # Intervention success rates by type
            intervention_types = ['Conflict Resolution', 'Technical Support', 'Motivation Coaching', 'Communication Help']
            success_rates = [87, 94, 79, 85]
            
            fig_interventions = px.bar(x=intervention_types, y=success_rates,
                                     title="Intervention Success Rates by Type")
            fig_interventions.update_layout(yaxis_range=[0, 100])
            st.plotly_chart(fig_interventions, use_container_width=True)
    
    with tab3:
        # Performance tracking
        col1, col2 = st.columns(2)
        
        with col1:
            # Weekly performance metrics
            performance_weeks = list(range(1, 9))
            response_times = [15.2, 14.1, 13.5, 12.8, 12.1, 11.7, 11.4, 11.3]
            satisfaction_scores = [7.8, 8.0, 8.1, 8.3, 8.4, 8.5, 8.5, 8.6]
            
            fig_performance = make_subplots(specs=[[{"secondary_y": True}]])
            fig_performance.add_trace(go.Scatter(x=performance_weeks, y=response_times, name="Response Time (min)"))
            fig_performance.add_trace(go.Scatter(x=performance_weeks, y=satisfaction_scores, name="Satisfaction Score"), secondary_y=True)
            fig_performance.update_layout(title="TA Performance Trends")
            fig_performance.update_yaxes(title_text="Response Time (minutes)", secondary_y=False)
            fig_performance.update_yaxes(title_text="Satisfaction Score", secondary_y=True)
            st.plotly_chart(fig_performance, use_container_width=True)
        
        with col2:
            # Workload distribution
            task_categories = ['Conflict Resolution', 'Technical Help', 'Progress Reviews', 'Individual Support', 'Administrative']
            time_spent = [25, 30, 20, 15, 10]
            ai_savings = [40, 35, 60, 25, 70]  # Percentage saved by AI
            
            fig_workload = go.Figure(data=[
                go.Bar(name='Human Time', x=task_categories, y=time_spent, marker_color='#3498db'),
                go.Bar(name='AI Automated', x=task_categories, y=ai_savings, marker_color='#2ecc71')
            ])
            fig_workload.update_layout(title="Workload Distribution: Human vs AI", barmode='stack')
            st.plotly_chart(fig_workload, use_container_width=True)
    
    with tab4:
        # Resources and tools
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🛠️ AI-Powered Tools")
            tools = [
                {"name": "Conflict Detector", "status": "Active", "accuracy": "94%"},
                {"name": "Student Risk Predictor", "status": "Active", "accuracy": "89%"},
                {"name": "Engagement Monitor", "status": "Active", "accuracy": "92%"},
                {"name": "Response Generator", "status": "Learning", "accuracy": "87%"}
            ]
            
            for tool in tools:
                status_color = "#2ecc71" if tool["status"] == "Active" else "#f39c12"
                st.markdown(f"""
                <div style="border: 1px solid {status_color}; padding: 0.5rem; margin: 0.5rem 0; border-radius: 5px;">
                <strong>{tool['name']}</strong><br>
                Status: <span style="color: {status_color};">{tool['status']}</span> | Accuracy: {tool['accuracy']}
                </div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("### 📚 Resource Library")
            resources = [
                "Conflict Resolution Scripts",
                "Student Motivation Strategies", 
                "Technical Support Guides",
                "Communication Templates",
                "Assessment Rubrics",
                "Professional Development Materials"
            ]
            
            for resource in resources:
                st.markdown(f"• [{resource}](#)")
    
    # Quick Action Buttons
    st.markdown("## 🚀 Quick Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🎯 Priority Tasks"):
            st.session_state.ta_messages.append({"role": "user", "content": "What are my priority tasks today?"})
            st.rerun()
    
    with col2:
        if st.button("🤝 Conflict Help"):
            st.session_state.ta_messages.append({"role": "user", "content": "Help me with conflict resolution"})
            st.rerun()
    
    with col3:
        if st.button("👥 Student Support"):
            st.session_state.ta_messages.append({"role": "user", "content": "Show me students who need individual help"})
            st.rerun()
    
    with col4:
        if st.button("📈 My Performance"):
            st.session_state.ta_messages.append({"role": "user", "content": "How am I performing as a TA?"})
            st.rerun()

if __name__ == "__main__":
    main()
