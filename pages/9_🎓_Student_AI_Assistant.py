import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random
import sys
import os

# Add the project root to the path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.azure_openai import get_ai_response, format_context_data
from prompts.student_prompts import SYSTEM_PROMPT, TEAMMATE_MATCHING_PROMPT, PARTICIPATION_GUIDANCE_PROMPT

# Add the project root to the path
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import DATA_PATHS_STR

st.set_page_config(page_title="Student AI Assistant", page_icon="🎓", layout="wide")

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
    .feature-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid #2ecc71;
    }
    .dashboard-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #dee2e6;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_student_data():
    """Load student and related data"""
    students_df = pd.read_csv(DATA_PATHS_STR['students'])
    participation_df = pd.read_csv(DATA_PATHS_STR['participation'])
    motivation_df = pd.read_csv(DATA_PATHS_STR['motivation'])
    gamification_df = pd.read_csv(DATA_PATHS_STR['gamification'])
    return students_df, participation_df, motivation_df, gamification_df

def generate_student_ai_response(prompt: str, student_profile: dict, context_data: dict) -> str:
    """Generate contextual AI responses for students using Azure OpenAI"""
    try:
        # Format context data for the AI
        context = format_context_data(
            student_profile=student_profile,
            additional_context={
                "course_context": "Columbia University Introduction to Machine Learning course",
                "project_type": "8-week collaborative ML pipeline development",
                "participation_data": context_data.get('participation', {}),
                "motivation_data": context_data.get('motivation', {}),
                "gamification_data": context_data.get('gamification', {})
            }
        )
        
        # Determine the appropriate prompt template based on user input
        prompt_lower = prompt.lower()
        
        if any(word in prompt_lower for word in ['teammate', 'partner', 'group', 'team', 'match']):
            system_prompt = SYSTEM_PROMPT
            # Format available teammates (simplified for demo)
            available_teammates = "Sample teammates with diverse personalities and skills available"
            formatted_prompt = TEAMMATE_MATCHING_PROMPT.format(
                student_name=student_profile['student_name'],
                personality_type=student_profile['personality_type'],
                preferred_role=student_profile['preferred_role'],
                technical_skills=student_profile['technical_skills'],
                collaboration_score=student_profile['collaboration_score'],
                communication_style=student_profile['communication_style'],
                work_preference=student_profile['work_preference'],
                major=student_profile['major'],
                available_teammates=available_teammates
            )
            user_prompt = f"User request: {prompt}\n\n{formatted_prompt}"
            
        elif any(word in prompt_lower for word in ['contribution', 'participate', 'engage', 'involvement']):
            system_prompt = SYSTEM_PROMPT
            formatted_prompt = PARTICIPATION_GUIDANCE_PROMPT.format(
                engagement_score=student_profile['engagement_score'],
                contribution_percentage=random.randint(15, 35),  # Would come from real data
                peer_rating=random.uniform(6.5, 9.0),
                personality_type=student_profile['personality_type'],
                participation_trend="improving" if student_profile['engagement_score'] > 7 else "needs attention"
            )
            user_prompt = f"User request: {prompt}\n\n{formatted_prompt}"
            
        else:
            # General query
            system_prompt = SYSTEM_PROMPT
            user_prompt = f"""
            The student is asking: "{prompt}"
            
            Student Profile:
            - Name: {student_profile['student_name']}
            - Personality: {student_profile['personality_type']}
            - Preferred Role: {student_profile['preferred_role']}
            - Technical Skills: {student_profile['technical_skills']}/10
            - Engagement Score: {student_profile['engagement_score']}/10
            - Major: {student_profile['major']}
            
            Provide a helpful, encouraging response that addresses their question while considering their personality type and learning preferences. Focus on collaborative learning and social psychology principles.
            """
        
        # Get AI response
        response = get_ai_response(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            context_data=context,
            temperature=0.8,  # Slightly more creative for student interactions
            max_tokens=1000
        )
        
        return response
        
    except Exception as e:
        # Fallback to basic response if AI fails
        st.error(f"AI service error: {str(e)}")
        st.error(f"Error type: {type(e).__name__}")
        return f"""
👋 **Hello {student_profile['student_name']}!** (Static Mode)

I'm your AI Learning Assistant. While my full AI capabilities are temporarily unavailable, I can still help you with:

**🎯 Your Profile:**
- Personality: {student_profile['personality_type']}
- Preferred Role: {student_profile['preferred_role']}
- Current Engagement: {student_profile['engagement_score']}/10

**💡 Quick Suggestions:**
- Use the dashboard visualizations to track your progress
- Check the team formation tools for collaboration tips
- Explore the conflict resolution resources if needed

Please try your question again in a moment when the AI service is restored!
        """

def main():
    st.markdown('<h1 class="main-header">🎓 Student AI Learning Assistant</h1>', unsafe_allow_html=True)
    
    # Load data
    students_df, participation_df, motivation_df, gamification_df = load_student_data()
    
    # Student Selection (simulating login)
    st.sidebar.markdown("### 👤 Student Profile")
    selected_student = st.sidebar.selectbox(
        "Login as:",
        students_df['student_name'].tolist()
    )
    
    # Get student profile
    student_profile = students_df[students_df['student_name'] == selected_student].iloc[0].to_dict()
    
    # Display student dashboard
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 👤 Your Profile")
        st.markdown(f"""
        <div class="dashboard-card">
        <strong>Name:</strong> {student_profile['student_name']}<br>
        <strong>Major:</strong> {student_profile['major']}<br>
        <strong>Personality:</strong> {student_profile['personality_type']}<br>
        <strong>Preferred Role:</strong> {student_profile['preferred_role']}<br>
        <strong>Technical Skills:</strong> {student_profile['technical_skills']}/10<br>
        <strong>Collaboration Score:</strong> {student_profile['collaboration_score']}/10<br>
        <strong>Engagement:</strong> {student_profile['engagement_score']}/10
        </div>
        """, unsafe_allow_html=True)
        
        # Quick stats
        st.markdown("### 📊 Quick Stats")
        col1a, col1b = st.columns(2)
        with col1a:
            st.metric("Group Rank", f"{random.randint(1, 4)}/4")
            st.metric("Weekly Contributions", f"{random.randint(15, 40)}%")
        with col1b:
            st.metric("Peer Rating", f"{random.uniform(6.5, 9.5):.1f}/10")
            st.metric("Achievements", f"{random.randint(3, 12)}")
    
    with col2:
        # AI Chat Interface
        st.markdown("### 🤖 Chat with Your AI Assistant")
        
        # Initialize chat history
        if "student_messages" not in st.session_state:
            st.session_state.student_messages = [
                {"role": "assistant", "content": f"Hello {student_profile['student_name']}! I'm here to help you succeed in your group project. What would you like to know?"}
            ]
        
        # Chat history display
        chat_container = st.container()
        with chat_container:
            for message in st.session_state.student_messages:
                css_class = "user-message" if message["role"] == "user" else "assistant-message"
                st.markdown(f"""
                <div class="chat-message {css_class}">
                {message["content"]}
                </div>
                """, unsafe_allow_html=True)
        
        # Chat input
        if prompt := st.chat_input("Ask me anything about your group project..."):
            st.session_state.student_messages.append({"role": "user", "content": prompt})
            
            # Generate AI response
            context_data = {
                'participation': participation_df[participation_df['student_id'] == student_profile['student_id']],
                'motivation': motivation_df[motivation_df['student_id'] == student_profile['student_id']],
                'gamification': gamification_df[gamification_df['student_id'] == student_profile['student_id']]
            }
            
            response = generate_student_ai_response(prompt, student_profile, context_data)
            st.session_state.student_messages.append({"role": "assistant", "content": response})
            st.rerun()
    
    # Student Dashboard Features
    st.markdown("## 📊 Your Personal Dashboard")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Progress Tracking", "🤝 Team Dynamics", "🎮 Achievements", "📚 Learning Resources"])
    
    with tab1:
        # Progress tracking
        student_participation = participation_df[participation_df['student_id'] == student_profile['student_id']]
        
        if not student_participation.empty:
            col1, col2 = st.columns(2)
            
            with col1:
                # Weekly contribution trend
                fig_progress = px.line(student_participation, x='week', y='contribution_percentage',
                                     title="Your Weekly Contribution Trend")
                fig_progress.add_hline(y=25, line_dash="dash", line_color="red", 
                                     annotation_text="Target: 25% (Equal Share)")
                st.plotly_chart(fig_progress, use_container_width=True)
            
            with col2:
                # Contribution breakdown
                latest_week = student_participation['week'].max()
                latest_data = student_participation[student_participation['week'] == latest_week].iloc[0]
                
                contributions = {
                    'Type': ['Code Commits', 'Document Edits', 'Ideas Contributed', 'Meeting Participation'],
                    'Count': [latest_data['code_commits'], latest_data['document_edits'], 
                             latest_data['ideas_contributed'], latest_data['meeting_speaking_time']]
                }
                
                fig_breakdown = px.bar(x=contributions['Type'], y=contributions['Count'],
                                     title="This Week's Contribution Breakdown")
                st.plotly_chart(fig_breakdown, use_container_width=True)
    
    with tab2:
        # Team dynamics
        group_students = students_df[students_df['group_id'] == student_profile['group_id']]
        
        st.markdown(f"### 👥 Your Team: {group_students.iloc[0]['group_id']}")
        
        for _, teammate in group_students.iterrows():
            is_current_student = teammate['student_id'] == student_profile['student_id']
            border_color = "#007bff" if is_current_student else "#28a745"
            
            st.markdown(f"""
            <div style="border: 2px solid {border_color}; padding: 1rem; border-radius: 10px; margin: 0.5rem 0;">
            <strong>{'👤 You' if is_current_student else '👥 ' + teammate['student_name']}</strong><br>
            Role: {teammate['preferred_role']} | Skills: {teammate['technical_skills']}/10 | Engagement: {teammate['engagement_score']}/10<br>
            Personality: {teammate['personality_type']} | Communication: {teammate['communication_style']}
            </div>
            """, unsafe_allow_html=True)
        
        # Team compatibility analysis
        st.markdown("### 🤝 Team Compatibility Analysis")
        
        compatibility_metrics = {
            'Aspect': ['Skill Balance', 'Personality Diversity', 'Communication Styles', 'Work Preferences'],
            'Score': [random.uniform(7, 9), random.uniform(6, 8), random.uniform(7, 9), random.uniform(6, 8)]
        }
        
        fig_compatibility = px.bar(x=compatibility_metrics['Aspect'], y=compatibility_metrics['Score'],
                                 title="Team Compatibility Scores")
        fig_compatibility.update_layout(yaxis_range=[0, 10])
        st.plotly_chart(fig_compatibility, use_container_width=True)
    
    with tab3:
        # Achievements and gamification
        student_achievements = gamification_df[gamification_df['student_id'] == student_profile['student_id']]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🏆 Your Achievements")
            
            if not student_achievements.empty:
                for _, achievement in student_achievements.head(5).iterrows():
                    difficulty_colors = {'Bronze': '#cd7f32', 'Silver': '#c0c0c0', 'Gold': '#ffd700', 'Platinum': '#e5e4e2'}
                    color = difficulty_colors.get(achievement['difficulty_level'], '#e5e4e2')
                    
                    st.markdown(f"""
                    <div style="background-color: {color}; padding: 0.5rem; border-radius: 5px; margin: 0.3rem 0; color: black;">
                    <strong>{achievement['achievement_type']}</strong><br>
                    Level: {achievement['difficulty_level']} | Points: {achievement['points_earned']}
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown("No achievements yet. Keep collaborating to earn your first badge!")
        
        with col2:
            st.markdown("### 📊 Points & Progress")
            
            total_points = student_achievements['points_earned'].sum() if not student_achievements.empty else 0
            st.metric("Total Points", total_points)
            
            # Next level progress
            next_level_threshold = 500
            progress = (total_points % next_level_threshold) / next_level_threshold
            st.progress(progress)
            st.markdown(f"Progress to next level: {total_points % next_level_threshold}/{next_level_threshold}")
            
            # Leaderboard position
            st.metric("Class Rank", f"{random.randint(15, 45)}/80")
    
    with tab4:
        # Learning resources
        st.markdown("### 📚 Personalized Learning Resources")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            <div class="feature-card">
            <h4>🎯 Recommended for {student_profile['preferred_role']}s</h4>
            <ul>
                <li>Advanced Data Preprocessing Techniques</li>
                <li>Feature Engineering Best Practices</li>
                <li>Model Evaluation Strategies</li>
                <li>Hyperparameter Optimization Guide</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="feature-card">
            <h4>🧠 {student_profile['personality_type']} Learning Style</h4>
            <ul>
                <li>Structured problem-solving approaches</li>
                <li>Visual learning materials</li>
                <li>Hands-on coding exercises</li>
                <li>Peer discussion forums</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="feature-card">
            <h4>🤝 Collaboration Skills</h4>
            <ul>
                <li>Effective Communication in Tech Teams</li>
                <li>Conflict Resolution Strategies</li>
                <li>Peer Code Review Best Practices</li>
                <li>Project Management for Students</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="feature-card">
            <h4>📈 Skill Development</h4>
            <ul>
                <li>Python for Machine Learning</li>
                <li>Statistical Analysis Fundamentals</li>
                <li>Data Visualization Techniques</li>
                <li>Research Methodology</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    
    # Quick Action Buttons
    st.markdown("## 🚀 Quick Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🤝 Find Teammates"):
            st.session_state.student_messages.append({"role": "user", "content": "Help me find good teammates"})
            st.rerun()
    
    with col2:
        if st.button("📈 Check Progress"):
            st.session_state.student_messages.append({"role": "user", "content": "How am I doing in the project?"})
            st.rerun()
    
    with col3:
        if st.button("🆘 Get Help"):
            st.session_state.student_messages.append({"role": "user", "content": "I need help with my project"})
            st.rerun()
    
    with col4:
        if st.button("🎯 Set Goals"):
            st.session_state.student_messages.append({"role": "user", "content": "Help me set participation goals"})
            st.rerun()

if __name__ == "__main__":
    main()
