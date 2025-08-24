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
from prompts.professor_prompts import SYSTEM_PROMPT, CLASS_ANALYTICS_PROMPT, INTERVENTION_RECOMMENDATIONS_PROMPT

# Add the project root to the path
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import DATA_PATHS_STR

st.set_page_config(page_title="Professor AI Dashboard", page_icon="👨‍🏫", layout="wide")

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
    .alert-high {
        background-color: #f8d7da;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #dc3545;
        margin: 1rem 0;
    }
    .alert-medium {
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
    .metric-card {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_professor_data():
    """Load all data for professor dashboard"""
    students_df = pd.read_csv(DATA_PATHS_STR['students'])
    groups_df = pd.read_csv(DATA_PATHS_STR['groups'])
    monitoring_df = pd.read_csv(DATA_PATHS_STR['monitoring'])
    tutoring_df = pd.read_csv(DATA_PATHS_STR['tutoring'])
    participation_df = pd.read_csv(DATA_PATHS_STR['participation'])
    conflicts_df = pd.read_csv(DATA_PATHS_STR['conflicts'])
    return students_df, groups_df, monitoring_df, tutoring_df, participation_df, conflicts_df

def generate_professor_ai_response(prompt: str, class_data: dict) -> str:
    """Generate contextual AI responses for professors using Azure OpenAI"""
    try:
        # Format context data for the AI
        context = format_context_data(
            additional_context={
                "class_metrics": class_data,
                "course_context": "Columbia University Introduction to Machine Learning course",
                "class_size": "80 students in 20 groups of 4",
                "project_type": "8-week collaborative ML pipeline development"
            }
        )
        
        # Determine the appropriate prompt template based on user input
        prompt_lower = prompt.lower()
        
        if any(word in prompt_lower for word in ['performance', 'analytics', 'progress', 'overview', 'class']):
            system_prompt = SYSTEM_PROMPT
            # Prepare data for CLASS_ANALYTICS_PROMPT with safe defaults
            analytics_data = {
                'avg_engagement': class_data.get('avg_engagement', 7.0),
                'participation_equality': class_data.get('participation_equality', 7.4),
                'at_risk_groups': ', '.join(class_data.get('at_risk_groups', [])),
                'recent_interventions': 'AI-guided discussion improvements, conflict mediation',
                'student_satisfaction': '8.4',
                'personality_distribution': 'Analytical: 32%, Creative: 28%, Collaborative: 25%, Leadership: 15%',
                'skill_distribution': 'Advanced: 20%, Intermediate: 60%, Beginner: 20%',
                'engagement_trends': 'Generally improving, some groups need attention'
            }
            formatted_prompt = CLASS_ANALYTICS_PROMPT.format(**analytics_data)
            user_prompt = f"User request: {prompt}\n\n{formatted_prompt}"
            
        elif any(word in prompt_lower for word in ['intervention', 'support', 'help', 'struggling', 'urgent']):
            system_prompt = SYSTEM_PROMPT
            # Prepare data for INTERVENTION_RECOMMENDATIONS_PROMPT with safe defaults
            intervention_data = {
                'at_risk_groups': ', '.join(class_data.get('at_risk_groups', [])),
                'struggling_students': f"{class_data.get('at_risk_students', 5)} students with engagement below 6.5",
                'common_issues': ', '.join(class_data.get('common_issues', ['Participation inequality', 'Communication barriers']))
            }
            formatted_prompt = INTERVENTION_RECOMMENDATIONS_PROMPT.format(**intervention_data)
            user_prompt = f"User request: {prompt}\n\n{formatted_prompt}"
            
        else:
            # General query
            system_prompt = SYSTEM_PROMPT
            user_prompt = f"""
            The user is asking: "{prompt}"
            
            Based on the current class data and context, provide a helpful response that addresses their question.
            
            Current class context:
            - Average engagement: {class_data.get('avg_engagement', 0):.1f}/10
            - Active groups: {class_data.get('active_groups', 0)}/20
            - At-risk students: {class_data.get('at_risk_students', 0)}
            - Top performing groups: {', '.join(class_data.get('top_groups', []))}
            - Groups needing attention: {', '.join(class_data.get('at_risk_groups', []))}
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
        # Fallback to static response if AI fails
        st.error(f"AI service error: {str(e)}")
        st.error(f"Error type: {type(e).__name__}")
        return f"""
📊 **Class Performance Overview** (Static Mode)

**Current Status:**
- Average Engagement: {class_data.get('avg_engagement', 0):.1f}/10
- Active Groups: {class_data.get('active_groups', 0)}/20 performing well
- At-Risk Students: {class_data.get('at_risk_students', 0)} need attention

**Top Performing Groups:** {', '.join(class_data.get('top_groups', []))}
**Groups Needing Support:** {', '.join(class_data.get('at_risk_groups', []))}

The AI assistant is temporarily unavailable. Please try again in a moment, or explore the interactive dashboard features for detailed analytics.
        """

def main():
    st.markdown('<h1 class="main-header">👨‍🏫 Professor AI Teaching Dashboard</h1>', unsafe_allow_html=True)
    
    # Load data
    students_df, groups_df, monitoring_df, tutoring_df, participation_df, conflicts_df = load_professor_data()
    
    # Calculate class analytics
    class_data = {
        'avg_engagement': students_df['engagement_score'].mean(),
        'participation_equality': monitoring_df['participation_equality'].mean(),
        'active_groups': len(groups_df[groups_df['risk_level'] == 'Low']),
        'intervention_success': 87.3,
        'top_groups': groups_df.nlargest(3, 'avg_engagement_score')['group_name'].tolist(),
        'at_risk_groups': groups_df[groups_df['risk_level'] == 'High']['group_name'].tolist(),
        'common_issues': ['Unequal participation', 'Technical difficulties', 'Communication barriers'],
        'vs_institution': 12.4,
        'improvement': 18.7,
        'ai_impact': 23.1,
        'priority_groups': groups_df[groups_df['risk_level'] == 'High']['group_name'].tolist()[:3],
        'high_performers': len(students_df[students_df['engagement_score'] >= 8.5]),
        'avg_performers': len(students_df[(students_df['engagement_score'] >= 6.5) & (students_df['engagement_score'] < 8.5)]),
        'at_risk_students': len(students_df[students_df['engagement_score'] < 6.5]),
        'analytical_count': len(students_df[students_df['personality_type'] == 'Analytical']),
        'creative_count': len(students_df[students_df['personality_type'] == 'Creative']),
        'collaborative_count': len(students_df[students_df['personality_type'] == 'Collaborative']),
        'leadership_count': len(students_df[students_df['personality_type'] == 'Leadership']),
        'success_prediction': 67,
        'dropout_risk': 8,
        'leadership_potential': 15,
        'ta_interventions': 45,
        'response_time': 12.3,
        'ta_success_rate': 89.2,
        'ta_satisfaction': 8.4,
        'red_priority': groups_df[groups_df['risk_level'] == 'High'],
        'yellow_priority': groups_df[groups_df['risk_level'] == 'Medium'],
        'green_priority': groups_df[groups_df['risk_level'] == 'Low'],
        'weekly_highlight': "3 struggling groups showed significant improvement after AI interventions",
        'improvement_note': "Class engagement increased 8% this week",
        'success_story': "Group dynamics conflicts resolved 40% faster with AI early detection"
    }
    
    # Top-level metrics dashboard
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Class Engagement", f"{class_data['avg_engagement']:.1f}/10", "▲ 0.8")
    with col2:
        st.metric("Active Groups", f"{class_data['active_groups']}/20", "▲ 2")
    with col3:
        st.metric("At-Risk Students", class_data['at_risk_students'], "▼ 3")
    with col4:
        st.metric("AI Success Rate", f"{class_data['intervention_success']:.1f}%", "▲ 2.1%")
    with col5:
        st.metric("TA Efficiency", "▲ 45%", "vs baseline")
    
    # Alert System
    st.markdown("## 🚨 Priority Alerts")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if class_data['at_risk_students'] > 0:
            st.markdown(f"""
            <div class="alert-high">
            <strong>🔴 HIGH PRIORITY</strong><br>
            {class_data['at_risk_students']} students need immediate attention<br>
            <em>Engagement scores below 6.5/10</em>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        if len(class_data['at_risk_groups']) > 0:
            st.markdown(f"""
            <div class="alert-medium">
            <strong>🟡 MEDIUM PRIORITY</strong><br>
            {len(class_data['at_risk_groups'])} groups showing warning signs<br>
            <em>Conflicts or participation issues detected</em>
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="success-box">
        <strong>🟢 SUCCESS HIGHLIGHT</strong><br>
        {class_data['active_groups']} groups performing excellently<br>
        <em>Above target engagement levels</em>
        </div>
        """, unsafe_allow_html=True)
    
    # Main Interface
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Course overview stats
        st.markdown("### 📊 Course Statistics")
        
        # Engagement distribution
        engagement_ranges = ['High (8.5-10)', 'Medium (6.5-8.4)', 'Low (<6.5)']
        engagement_counts = [class_data['high_performers'], class_data['avg_performers'], class_data['at_risk_students']]
        
        fig_engagement = px.pie(values=engagement_counts, names=engagement_ranges,
                              title="Student Engagement Distribution",
                              color_discrete_map={'High (8.5-10)': '#2ecc71', 
                                                'Medium (6.5-8.4)': '#f39c12',
                                                'Low (<6.5)': '#e74c3c'})
        st.plotly_chart(fig_engagement, use_container_width=True)
        
        # Group risk levels
        risk_counts = groups_df['risk_level'].value_counts()
        fig_risk = px.bar(x=risk_counts.index, y=risk_counts.values,
                         title="Group Risk Distribution",
                         color=risk_counts.index,
                         color_discrete_map={'Low': '#2ecc71', 'Medium': '#f39c12', 'High': '#e74c3c'})
        st.plotly_chart(fig_risk, use_container_width=True)
    
    with col2:
        # AI Chat Interface
        st.markdown("### 🤖 AI Teaching Assistant")
        
        # Initialize chat history
        if "professor_messages" not in st.session_state:
            st.session_state.professor_messages = [
                {"role": "assistant", "content": "Hello! I'm your AI teaching assistant. I can help you monitor class performance, identify students who need support, and optimize your course effectiveness. What would you like to know?"}
            ]
        
        # Chat history display
        chat_container = st.container()
        with chat_container:
            for message in st.session_state.professor_messages:
                if message["role"] == "user":
                    st.markdown(f"""
                    <div style="background-color: #e3f2fd; padding: 1rem; border-radius: 10px; margin: 0.5rem 0; margin-left: 20%;">
                    {message["content"]}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="background-color: #f5f5f5; padding: 1rem; border-radius: 10px; margin: 0.5rem 0; margin-right: 20%;">
                    {message["content"]}
                    </div>
                    """, unsafe_allow_html=True)
        
        # Chat input
        if prompt := st.chat_input("Ask about class performance, student interventions, or course optimization..."):
            st.session_state.professor_messages.append({"role": "user", "content": prompt})
            
            # Generate AI response
            response = generate_professor_ai_response(prompt, class_data)
            st.session_state.professor_messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    # Detailed Analytics Tabs
    st.markdown("## 📊 Detailed Analytics")
    
    tab1, tab2, tab3, tab4 = st.tabs(["👥 Student Performance", "🎯 Group Dynamics", "📈 Intervention Tracking", "🎓 Course Optimization"])
    
    with tab1:
        # Student performance analysis
        col1, col2 = st.columns(2)
        
        with col1:
            # Performance vs engagement scatter
            fig_scatter = px.scatter(students_df, x='engagement_score', y='academic_performance',
                                   color='personality_type', size='collaboration_score',
                                   title="Student Performance Analysis",
                                   hover_data=['student_name', 'preferred_role'])
            st.plotly_chart(fig_scatter, use_container_width=True)
        
        with col2:
            # Skill distribution by major
            fig_skills = px.box(students_df, x='major', y='technical_skills',
                              title="Technical Skills by Major")
            fig_skills.update_layout(xaxis=dict(tickangle=45))
            st.plotly_chart(fig_skills, use_container_width=True)
        
        # At-risk student table
        st.markdown("### 🚨 Students Requiring Attention")
        at_risk_students = students_df[students_df['engagement_score'] < 6.5][
            ['student_name', 'engagement_score', 'academic_performance', 'group_id', 'personality_type']
        ].sort_values('engagement_score')
        
        if not at_risk_students.empty:
            st.dataframe(at_risk_students, use_container_width=True)
        else:
            st.success("🎉 No students currently at risk!")
    
    with tab2:
        # Group dynamics analysis
        col1, col2 = st.columns(2)
        
        with col1:
            # Group performance metrics
            fig_group_perf = px.scatter(groups_df, x='avg_collaboration_score', y='avg_engagement_score',
                                      color='risk_level', size='progress_percentage',
                                      title="Group Performance Overview",
                                      hover_data=['group_name'])
            st.plotly_chart(fig_group_perf, use_container_width=True)
        
        with col2:
            # Diversity vs performance
            fig_diversity = px.scatter(groups_df, x='personality_diversity', y='avg_engagement_score',
                                     color='risk_level', size='avg_technical_skills',
                                     title="Personality Diversity Impact")
            st.plotly_chart(fig_diversity, use_container_width=True)
        
        # Group intervention recommendations
        st.markdown("### 💡 Group Intervention Recommendations")
        
        for _, group in groups_df[groups_df['risk_level'].isin(['High', 'Medium'])].iterrows():
            risk_color = {'High': 'alert-high', 'Medium': 'alert-medium'}[group['risk_level']]
            st.markdown(f"""
            <div class="{risk_color}">
            <strong>{group['group_name']}</strong> - {group['project_topic']}<br>
            Risk Level: {group['risk_level']} | Progress: {group['progress_percentage']:.1f}%<br>
            Engagement: {group['avg_engagement_score']:.1f}/10 | Collaboration: {group['avg_collaboration_score']:.1f}/10
            </div>
            """, unsafe_allow_html=True)
    
    with tab3:
        # Intervention tracking
        monitoring_weekly = monitoring_df.groupby(['week', 'ai_intervention']).size().unstack(fill_value=0)
        
        fig_interventions = go.Figure()
        fig_interventions.add_trace(go.Scatter(x=monitoring_weekly.index, y=monitoring_weekly[True],
                                             name='With AI Intervention', line=dict(color='#e74c3c')))
        fig_interventions.add_trace(go.Scatter(x=monitoring_weekly.index, y=monitoring_weekly[False],
                                             name='No Intervention', line=dict(color='#2ecc71')))
        fig_interventions.update_layout(title="AI Intervention Frequency Over Time",
                                      xaxis_title="Week", yaxis_title="Number of Sessions")
        st.plotly_chart(fig_interventions, use_container_width=True)
        
        # Success rate metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Intervention Success Rate", "87.3%", "▲ 2.1%")
        with col2:
            st.metric("Early Detection Rate", "94.2%", "▲ 1.8%")
        with col3:
            st.metric("Student Satisfaction", "8.4/10", "▲ 0.3")
    
    with tab4:
        # Course optimization insights
        st.markdown("### 🎓 Learning Outcome Analysis")
        
        # Engagement trends over time
        engagement_trend = monitoring_df.groupby('week')['avg_engagement'].mean()
        fig_trend = px.line(x=engagement_trend.index, y=engagement_trend.values,
                          title="Class Engagement Trend")
        fig_trend.add_hline(y=7.5, line_dash="dash", line_color="red", 
                          annotation_text="Target Engagement Level")
        st.plotly_chart(fig_trend, use_container_width=True)
        
        # Curriculum effectiveness
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📚 Most Effective Components
            1. **Collaborative Coding Sessions** - 94% engagement
            2. **Peer Review Exercises** - 89% satisfaction
            3. **Real-world Case Studies** - 87% retention
            4. **Interactive Tutorials** - 85% completion
            """)
        
        with col2:
            st.markdown("""
            ### 🔧 Areas for Improvement
            1. **Statistical Foundations** - 23% struggle rate
            2. **Advanced Model Concepts** - 31% need support
            3. **Research Methodology** - 28% confusion
            4. **Technical Documentation** - 35% incomplete
            """)
    
    # Quick Action Buttons
    st.markdown("## 🚀 Quick Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📊 Class Overview"):
            st.session_state.professor_messages.append({"role": "user", "content": "Give me a class performance overview"})
            st.rerun()
    
    with col2:
        if st.button("🚨 Urgent Interventions"):
            st.session_state.professor_messages.append({"role": "user", "content": "What interventions are needed urgently?"})
            st.rerun()
    
    with col3:
        if st.button("👥 Student Analytics"):
            st.session_state.professor_messages.append({"role": "user", "content": "Show me individual student insights"})
            st.rerun()
    
    with col4:
        if st.button("🎓 Course Optimization"):
            st.session_state.professor_messages.append({"role": "user", "content": "How can I improve my course design?"})
            st.rerun()

if __name__ == "__main__":
    main()
