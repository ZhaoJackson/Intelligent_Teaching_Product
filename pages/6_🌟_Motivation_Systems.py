import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Add the project root to the path
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from constants import DATA_PATHS_STR

st.set_page_config(page_title="Motivation Systems", page_icon="🌟", layout="wide")

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
    .psychology-principle {
        background-color: #e8f5e8;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    .motivation-theory {
        background-color: #fff3cd;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .intervention-strategy {
        background-color: #f8d7da;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #dc3545;
        margin: 1rem 0;
    }
    .insight-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_motivation_data():
    """Load motivation and reinforcement data"""
    motivation_df = pd.read_csv(DATA_PATHS_STR['motivation'])
    students_df = pd.read_csv(DATA_PATHS_STR['students'])
    return motivation_df, students_df

def main():
    st.markdown('<h1 class="main-header">🌟 Motivation & Positive Reinforcement Systems</h1>', unsafe_allow_html=True)
    
    # User Perspective Filter
    st.sidebar.markdown("### 👥 User Perspective")
    user_role = st.sidebar.selectbox(
        "View as:",
        ["Educational Psychologist", "Instructor", "Teaching Assistant", "Student"]
    )
    
    # Load data
    motivation_df, students_df = load_motivation_data()
    
    # Key Research Insight
    st.markdown("""
    ## 🔬 Positive Psychology Research Foundation
    
    **Evidence from Educational Gaming Research:** AI-powered motivation systems show 45% increase in student engagement when implementing positive psychology principles and personalized reinforcement strategies based on individual motivational profiles.
    """)
    
    # Key Metrics Overview
    col1, col2, col3, col4 = st.columns(4)
    
    avg_engagement_before = motivation_df['engagement_before'].mean()
    avg_engagement_after = motivation_df['engagement_after'].mean()
    avg_motivation_boost = motivation_df['motivation_boost'].mean()
    positive_response_rate = (motivation_df['student_response'] == 'Very Positive').mean() * 100
    
    with col1:
        improvement = avg_engagement_after - avg_engagement_before
        st.metric("Engagement Improvement", f"+{improvement:.1f}", "Average increase")
    with col2:
        st.metric("Motivation Boost", f"+{avg_motivation_boost:.1f}", "Per intervention")
    with col3:
        st.metric("Positive Response Rate", f"{positive_response_rate:.1f}%", "Student feedback")
    with col4:
        continuity_rate = motivation_df['continued_engagement'].mean() * 100
        st.metric("Sustained Engagement", f"{continuity_rate:.1f}%", "Long-term effect")
    
    # Core Motivation Theories
    st.markdown("## 🧠 Motivation Theories in Educational AI")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="psychology-principle">
        <h4>🎯 Self-Determination Theory (Deci & Ryan, 1985)</h4>
        <p><strong>Three Basic Psychological Needs:</strong></p>
        <ul>
            <li><strong>Autonomy:</strong> Feeling volitional and self-directed</li>
            <li><strong>Competence:</strong> Experiencing mastery and effectiveness</li>
            <li><strong>Relatedness:</strong> Connecting meaningfully with others</li>
        </ul>
        
        <p><strong>AI Implementation:</strong></p>
        <ul>
            <li>Provide choices in how students contribute to groups</li>
            <li>Celebrate incremental progress and skill development</li>
            <li>Highlight connections between individual and group success</li>
            <li>Personalize feedback to individual learning styles</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="motivation-theory">
        <h4>📈 Achievement Goal Theory (Dweck & Elliot)</h4>
        <p><strong>Mastery vs. Performance Goals:</strong></p>
        <ul>
            <li><strong>Mastery Goals:</strong> Focus on learning and understanding</li>
            <li><strong>Performance Goals:</strong> Focus on appearing competent relative to others</li>
        </ul>
        
        <p><strong>AI Strategy:</strong></p>
        <ul>
            <li>Emphasize learning progress over comparative rankings</li>
            <li>Provide process-focused rather than outcome-focused praise</li>
            <li>Encourage exploration and risk-taking in learning</li>
            <li>Frame challenges as opportunities for growth</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="psychology-principle">
        <h4>💭 Growth Mindset Theory (Dweck, 2006)</h4>
        <p><strong>Fixed vs. Growth Mindset:</strong></p>
        <ul>
            <li><strong>Fixed:</strong> Abilities are static and unchangeable</li>
            <li><strong>Growth:</strong> Abilities can be developed through effort</li>
        </ul>
        
        <p><strong>AI Reinforcement Strategies:</strong></p>
        <ul>
            <li>Praise effort, strategies, and persistence over intelligence</li>
            <li>Reframe failures as learning opportunities</li>
            <li>Highlight improvement over time rather than current level</li>
            <li>Encourage collaborative learning and peer teaching</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="motivation-theory">
        <h4>🏆 Flow Theory (Csikszentmihalyi, 1990)</h4>
        <p><strong>Conditions for Optimal Experience:</strong></p>
        <ul>
            <li><strong>Clear Goals:</strong> Knowing what needs to be accomplished</li>
            <li><strong>Immediate Feedback:</strong> Understanding progress in real-time</li>
            <li><strong>Balance:</strong> Challenge level matches skill level</li>
            <li><strong>Deep Concentration:</strong> Full immersion in activity</li>
        </ul>
        
        <p><strong>AI Flow Enhancement:</strong></p>
        <ul>
            <li>Adaptive difficulty based on student capability</li>
            <li>Real-time progress feedback and encouragement</li>
            <li>Personalized learning paths and pacing</li>
            <li>Minimizing distractions and friction</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Role-specific insights
    if user_role == "Educational Psychologist":
        st.markdown("""
        <div class="insight-box">
        <h4>🔬 Research Perspective: Motivation Science in AI Education</h4>
        <p>AI motivation systems can implement evidence-based psychological principles at scale:</p>
        <ul>
            <li><strong>Operant Conditioning:</strong> Systematic reinforcement of desired behaviors</li>
            <li><strong>Social Cognitive Theory:</strong> Modeling and vicarious learning through peer examples</li>
            <li><strong>Expectancy-Value Theory:</strong> Connecting tasks to student values and future goals</li>
            <li><strong>Self-Efficacy Theory:</strong> Building confidence through graduated success experiences</li>
        </ul>
        <p><em>Meta-analyses show that intrinsic motivation interventions have effect sizes of 0.5-0.8 in educational settings.</em></p>
        </div>
        """, unsafe_allow_html=True)
        
    elif user_role == "Instructor":
        st.markdown("""
        <div class="insight-box">
        <h4>🎓 Instructor Perspective: Scalable Motivation Enhancement</h4>
        <p>AI motivation systems extend your ability to inspire and support students:</p>
        <ul>
            <li><strong>Personalized Recognition:</strong> Celebrate each student's unique contributions and growth</li>
            <li><strong>Consistent Messaging:</strong> Reinforce course values and learning objectives uniformly</li>
            <li><strong>Early Intervention:</strong> Identify and address motivation challenges before disengagement</li>
            <li><strong>Cultural Sensitivity:</strong> Adapt motivational approaches to diverse student backgrounds</li>
        </ul>
        <p><em>Students report feeling more valued and motivated when receiving personalized, frequent positive feedback.</em></p>
        </div>
        """, unsafe_allow_html=True)
        
    elif user_role == "Teaching Assistant":
        st.markdown("""
        <div class="insight-box">
        <h4>👨‍🏫 TA Perspective: Motivation-Focused Student Support</h4>
        <p>AI motivation tracking helps you provide targeted encouragement and support:</p>
        <ul>
            <li><strong>Motivation Patterns:</strong> Understand what drives each student's engagement</li>
            <li><strong>Intervention Timing:</strong> Know when students need encouragement most</li>
            <li><strong>Success Amplification:</strong> Build on positive momentum and small wins</li>
            <li><strong>Barrier Identification:</strong> Recognize and address motivation obstacles</li>
        </ul>
        <p><em>Research shows that timely, specific encouragement can prevent academic disengagement.</em></p>
        </div>
        """, unsafe_allow_html=True)
        
    else:  # Student
        st.markdown("""
        <div class="insight-box">
        <h4>🎓 Student Perspective: Personalized Motivation Support</h4>
        <p>AI motivation systems provide encouragement tailored to your learning journey:</p>
        <ul>
            <li><strong>Personal Growth Recognition:</strong> Acknowledgment of your effort and improvement</li>
            <li><strong>Strength Identification:</strong> Help you discover and build on your capabilities</li>
            <li><strong>Goal Connection:</strong> Link course work to your personal interests and career goals</li>
            <li><strong>Resilience Building:</strong> Support through challenges and setbacks</li>
        </ul>
        <p><em>Students who receive regular positive reinforcement show higher persistence and better learning outcomes.</em></p>
        </div>
        """, unsafe_allow_html=True)
    
    # Motivation Intervention Analysis
    st.markdown("## 📊 Motivation Intervention Effectiveness")
    
    # Filter controls
    col1, col2, col3 = st.columns(3)
    with col1:
        reinforcement_filter = st.multiselect("Reinforcement Types:", 
                                            motivation_df['reinforcement_type'].unique(),
                                            default=motivation_df['reinforcement_type'].unique())
    with col2:
        response_filter = st.selectbox("Student Response:", 
                                     ['All'] + list(motivation_df['student_response'].unique()))
    with col3:
        time_period = st.selectbox("Time Period:", ["Last Week", "Last Month", "All Time"])
    
    # Filter data
    filtered_motivation = motivation_df[motivation_df['reinforcement_type'].isin(reinforcement_filter)]
    if response_filter != 'All':
        filtered_motivation = filtered_motivation[filtered_motivation['student_response'] == response_filter]
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Engagement improvement by reinforcement type
        improvement_by_type = filtered_motivation.groupby('reinforcement_type')['motivation_boost'].mean().reset_index()
        fig_improvement = px.bar(improvement_by_type, x='reinforcement_type', y='motivation_boost',
                               title="Average Motivation Boost by Reinforcement Type",
                               color='motivation_boost',
                               color_continuous_scale='Viridis')
        st.plotly_chart(fig_improvement, use_container_width=True)
    
    with col2:
        # Student response distribution
        response_counts = filtered_motivation['student_response'].value_counts()
        fig_responses = px.pie(values=response_counts.values, names=response_counts.index,
                             title="Student Response Distribution",
                             color_discrete_map={'Very Positive': '#2ecc71', 'Positive': '#f39c12', 
                                               'Neutral': '#95a5a6', 'Negative': '#e74c3c'})
        st.plotly_chart(fig_responses, use_container_width=True)
    
    # Detailed Engagement Analysis
    st.markdown("## 🔍 Engagement Before vs After Interventions")
    
    fig_engagement = go.Figure()
    
    # Before and after comparison
    fig_engagement.add_trace(go.Histogram(x=filtered_motivation['engagement_before'], 
                                        name='Before Intervention', 
                                        opacity=0.7, 
                                        marker_color='#e74c3c'))
    fig_engagement.add_trace(go.Histogram(x=filtered_motivation['engagement_after'], 
                                        name='After Intervention', 
                                        opacity=0.7, 
                                        marker_color='#2ecc71'))
    
    fig_engagement.update_layout(
        title="Engagement Score Distribution: Before vs After Motivation Interventions",
        xaxis_title="Engagement Score (1-10)",
        yaxis_title="Number of Students",
        barmode='overlay'
    )
    
    st.plotly_chart(fig_engagement, use_container_width=True)
    
    # Personalized Motivation Strategies
    st.markdown("## 🎯 Personalized Motivation Strategies")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="intervention-strategy">
        <h4>🎨 For Creative Personalities</h4>
        <p><strong>Effective Strategies:</strong></p>
        <ul>
            <li>Highlight innovative approaches and unique solutions</li>
            <li>Provide opportunities for creative problem-solving</li>
            <li>Connect projects to real-world applications</li>
            <li>Celebrate "thinking outside the box" moments</li>
        </ul>
        
        <p><strong>AI Messaging Examples:</strong></p>
        <ul>
            <li>"Your creative approach to feature engineering is inspiring your teammates!"</li>
            <li>"I love how you're connecting this ML concept to your art background!"</li>
            <li>"Your unique perspective is making this project stronger!"</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="intervention-strategy">
        <h4>🤝 For Collaborative Personalities</h4>
        <p><strong>Effective Strategies:</strong></p>
        <ul>
            <li>Recognize contributions to team harmony and communication</li>
            <li>Highlight how their support helps others learn</li>
            <li>Emphasize the social impact of their work</li>
            <li>Celebrate inclusive behaviors and peer support</li>
        </ul>
        
        <p><strong>AI Messaging Examples:</strong></p>
        <ul>
            <li>"Your teammates really appreciate how you include everyone in discussions!"</li>
            <li>"Your explanation helped your teammate understand that concept - great teaching!"</li>
            <li>"You're creating such a positive team environment!"</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="intervention-strategy">
        <h4>🔬 For Analytical Personalities</h4>
        <p><strong>Effective Strategies:</strong></p>
        <ul>
            <li>Provide detailed performance metrics and progress data</li>
            <li>Recognize systematic approaches and methodical thinking</li>
            <li>Connect achievements to concrete learning objectives</li>
            <li>Highlight improvements in technical accuracy</li>
        </ul>
        
        <p><strong>AI Messaging Examples:</strong></p>
        <ul>
            <li>"Your systematic approach improved model accuracy by 12%!"</li>
            <li>"I can see clear improvement in your statistical reasoning skills!"</li>
            <li>"Your attention to detail caught an important data quality issue!"</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="intervention-strategy">
        <h4>👑 For Leadership Personalities</h4>
        <p><strong>Effective Strategies:</strong></p>
        <ul>
            <li>Acknowledge leadership contributions and team guidance</li>
            <li>Recognize ability to motivate and organize others</li>
            <li>Highlight strategic thinking and vision</li>
            <li>Celebrate mentoring and peer support behaviors</li>
        </ul>
        
        <p><strong>AI Messaging Examples:</strong></p>
        <ul>
            <li>"Your leadership helped your team meet their milestone early!"</li>
            <li>"Great job guiding your teammate through that difficult concept!"</li>
            <li>"Your strategic planning is keeping the project on track!"</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Individual Student Motivation Profile
    st.markdown("## 👤 Individual Motivation Analysis")
    
    # Student selector
    student_list = students_df['student_name'].unique()
    selected_student = st.selectbox("Select Student for Motivation Analysis:", student_list)
    
    if selected_student:
        student_profile = students_df[students_df['student_name'] == selected_student].iloc[0]
        student_motivations = motivation_df[
            motivation_df['student_id'] == student_profile['student_id']
        ]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"**Student:** {student_profile['student_name']}")
            st.markdown(f"**Personality:** {student_profile['personality_type']}")
            st.markdown(f"**Motivation Type:** {student_profile['motivation_type']}")
        
        with col2:
            if not student_motivations.empty:
                avg_boost = student_motivations['motivation_boost'].mean()
                st.metric("Avg Motivation Boost", f"+{avg_boost:.1f}")
                
                interventions_received = len(student_motivations)
                st.metric("Interventions Received", interventions_received)
        
        with col3:
            if not student_motivations.empty:
                positive_responses = (student_motivations['student_response'].isin(['Very Positive', 'Positive'])).mean() * 100
                st.metric("Positive Response Rate", f"{positive_responses:.1f}%")
                
                continued_engagement = student_motivations['continued_engagement'].mean() * 100
                st.metric("Sustained Engagement", f"{continued_engagement:.1f}%")
        
        if not student_motivations.empty:
            # Individual motivation timeline
            fig_timeline = go.Figure()
            
            fig_timeline.add_trace(go.Scatter(
                x=student_motivations['timestamp'], 
                y=student_motivations['engagement_before'],
                name='Before Intervention',
                line=dict(color='#e74c3c')
            ))
            
            fig_timeline.add_trace(go.Scatter(
                x=student_motivations['timestamp'], 
                y=student_motivations['engagement_after'],
                name='After Intervention',
                line=dict(color='#2ecc71')
            ))
            
            fig_timeline.update_layout(
                title=f"Motivation Intervention Timeline: {selected_student}",
                xaxis_title="Time",
                yaxis_title="Engagement Score (1-10)"
            )
            
            st.plotly_chart(fig_timeline, use_container_width=True)
            
            # Personalized recommendations
            st.markdown(f"### 💡 Personalized Motivation Strategies for {selected_student}")
            
            personality = student_profile['personality_type']
            motivation_type = student_profile['motivation_type']
            
            if personality == 'Analytical' and motivation_type == 'Learning-focused':
                st.markdown("""
                <div class="psychology-principle">
                <h4>🎯 Recommended Approach: Data-Driven Learning Celebration</h4>
                <ul>
                    <li>Provide detailed progress metrics and skill development tracking</li>
                    <li>Highlight connections between effort and measurable improvement</li>
                    <li>Recognize systematic approaches and methodical problem-solving</li>
                    <li>Connect achievements to broader learning objectives and career goals</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            elif personality == 'Creative' and motivation_type == 'Career-focused':
                st.markdown("""
                <div class="psychology-principle">
                <h4>🎯 Recommended Approach: Innovation and Impact Focus</h4>
                <ul>
                    <li>Highlight creative solutions and unique approaches to problems</li>
                    <li>Connect project work to real-world applications in their field of interest</li>
                    <li>Provide opportunities for original thinking and experimentation</li>
                    <li>Celebrate contributions that bring fresh perspectives to the team</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="psychology-principle">
                <h4>🎯 Recommended Approach: {personality} + {motivation_type}</h4>
                <p>Combine {personality.lower()} recognition strategies with {motivation_type.lower()} goal connections for optimal motivation enhancement.</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Research Evidence and Best Practices
    st.markdown("## 📚 Research Evidence: Motivation in Collaborative Learning")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="motivation-theory">
        <h4>📖 Key Research Findings</h4>
        <p><strong>Deci & Ryan (2000) - Self-Determination Theory:</strong></p>
        <ul>
            <li>Intrinsic motivation leads to better learning outcomes than extrinsic rewards</li>
            <li>Autonomy, competence, and relatedness are universal psychological needs</li>
            <li>Controlling environments undermine intrinsic motivation</li>
        </ul>
        
        <p><strong>Dweck (2006) - Growth Mindset Research:</strong></p>
        <ul>
            <li>Process praise is more effective than person praise</li>
            <li>Effort attribution increases persistence and performance</li>
            <li>Challenges are reframed as opportunities for growth</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="motivation-theory">
        <h4>🎯 Implementation Best Practices</h4>
        <p><strong>Timing and Frequency:</strong></p>
        <ul>
            <li>Immediate feedback for maximum impact</li>
            <li>Regular but not overwhelming intervention frequency</li>
            <li>Targeted timing based on individual need patterns</li>
        </ul>
        
        <p><strong>Personalization Strategies:</strong></p>
        <ul>
            <li>Adapt language and tone to personality types</li>
            <li>Connect to individual values and goals</li>
            <li>Consider cultural backgrounds and preferences</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Implementation Outcomes
    st.markdown("## 🎯 Key Outcomes: Psychology-Informed Motivation Enhancement")
    
    outcomes_data = {
        'Outcome': ['Student Engagement', 'Intrinsic Motivation', 'Persistence', 'Collaborative Behavior', 'Learning Satisfaction'],
        'Before_AI': [6.2, 5.8, 6.0, 6.4, 6.1],
        'After_AI': [8.7, 8.1, 8.4, 8.6, 8.3],
        'Effect_Size': [0.89, 0.76, 0.82, 0.71, 0.78]
    }
    
    fig_outcomes = go.Figure()
    fig_outcomes.add_trace(go.Bar(name='Before AI Motivation System', x=outcomes_data['Outcome'], 
                                 y=outcomes_data['Before_AI'], marker_color='#e74c3c'))
    fig_outcomes.add_trace(go.Bar(name='After AI Motivation System', x=outcomes_data['Outcome'], 
                                 y=outcomes_data['After_AI'], marker_color='#2ecc71'))
    
    fig_outcomes.update_layout(
        title="Impact of AI Motivation Systems on Student Outcomes",
        yaxis_title="Score (1-10)",
        barmode='group',
        height=500
    )
    
    st.plotly_chart(fig_outcomes, use_container_width=True)
    
    st.markdown("""
    ## 🎯 Key Insights: Motivation Science Meets AI Education
    
    **🧠 Psychological Mechanisms:**
    - **Intrinsic Motivation:** AI systems support autonomy, competence, and relatedness needs
    - **Growth Mindset:** Process-focused feedback builds resilience and learning orientation  
    - **Self-Efficacy:** Graduated success experiences build confidence in collaborative abilities
    - **Flow States:** Personalized challenges maintain optimal engagement levels
    
    **📈 Sustainable Engagement:**
    - **Individual Recognition:** Celebrates unique contributions and personal growth
    - **Social Connection:** Highlights positive impact on team success and peer learning
    - **Goal Alignment:** Connects course work to personal values and career aspirations
    - **Continuous Support:** Provides encouragement through challenges and setbacks
    
    **🤝 Collaborative Benefits:**
    AI motivation systems create more engaged, resilient, and collaborative learning communities where students feel valued, supported, and inspired to contribute their best efforts.
    """)

if __name__ == "__main__":
    main()
