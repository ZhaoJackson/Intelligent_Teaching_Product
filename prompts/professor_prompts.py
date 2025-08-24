"""
Prompt templates for Professor AI Dashboard in ML Course context
"""

SYSTEM_PROMPT = """
You are an AI Teaching Assistant for the instructor of Columbia University's "Introduction to Machine Learning" course.
You provide data-driven insights and evidence-based recommendations for managing 80 students in 20 groups working on 8-week ML projects.

Your expertise includes:
1. Educational psychology and learning science
2. Group dynamics and collaborative learning research  
3. Data-driven intervention strategies
4. Course design optimization
5. Student support and engagement strategies

Focus on:
- Social psychology principles in education
- Evidence-based teaching practices
- Collaborative learning optimization
- Student engagement and motivation
- Equitable learning outcomes

Course Context:
- 80 students in 20 groups of 4
- 8-week ML project (data preprocessing → model deployment)
- Mix of personalities: Analytical, Creative, Collaborative, Leadership
- Diverse academic backgrounds and skill levels
- Focus on both individual and group learning outcomes

Provide strategic, research-backed recommendations that enhance teaching effectiveness.
"""

CLASS_ANALYTICS_PROMPT = """
Provide a comprehensive class performance analysis:

Current Metrics:
- Average Engagement: {avg_engagement}/10
- Participation Equality: {participation_equality}/10  
- Groups at Risk: {at_risk_groups}
- Recent Interventions: {recent_interventions}
- Student Satisfaction: {student_satisfaction}/10

Class Composition:
- Personality Distribution: {personality_distribution}
- Skill Level Distribution: {skill_distribution}
- Engagement Trends: {engagement_trends}

Provide:
1. Overall class health assessment with key insights
2. Identification of concerning patterns or trends
3. Comparison with educational research benchmarks
4. Specific areas needing instructor attention
5. Recommendations for immediate and long-term actions

Base analysis on educational psychology research and collaborative learning principles.
"""

INTERVENTION_RECOMMENDATIONS_PROMPT = """
Recommend evidence-based interventions for struggling students/groups:

At-Risk Groups: {at_risk_groups}
Struggling Students: {struggling_students}
Common Issues: {common_issues}

Recent Data:
- Engagement Trends: {engagement_data}
- Participation Patterns: {participation_data}
- Conflict Incidents: {conflict_data}

Provide:
1. Prioritized intervention strategies based on research evidence
2. Specific approaches for different types of challenges
3. Resource allocation recommendations
4. Timeline and success metrics for interventions
5. Prevention strategies for future cohorts

Focus on social psychology interventions and collaborative learning research.
"""

COURSE_OPTIMIZATION_PROMPT = """
Analyze course effectiveness and suggest improvements:

Current Course Data:
- Learning Outcomes: {learning_outcomes}
- Student Engagement: {engagement_metrics}
- Group Collaboration Quality: {collaboration_metrics}
- Assignment Effectiveness: {assignment_data}
- Student Feedback: {feedback_data}

Challenges Identified:
{identified_challenges}

Provide:
1. Evidence-based course design improvements
2. Modifications to enhance collaborative learning
3. Assessment strategy optimization
4. Student support system enhancements
5. Implementation timeline and expected outcomes

Draw from educational research, learning science, and collaborative learning literature.
"""

STUDENT_SUPPORT_STRATEGY_PROMPT = """
Develop targeted support strategies for individual students:

Student Categories:
- High Performers: {high_performers}
- Average Performers: {average_performers}  
- At-Risk Students: {at_risk_students}

Detailed Analytics:
{student_analytics}

Diversity Considerations:
- Cultural Backgrounds: {cultural_diversity}
- Learning Styles: {learning_styles}
- Academic Preparation: {academic_backgrounds}

Provide:
1. Differentiated support strategies for each student category
2. Inclusive practices for diverse learners
3. Peer support and mentoring recommendations
4. Early intervention protocols
5. Success measurement approaches

Base on educational equity research and inclusive pedagogy principles.
"""

RESOURCE_ALLOCATION_PROMPT = """
Optimize teaching resources and TA assignments:

Current Resources:
- TA Hours Available: {ta_hours}
- Student Needs Assessment: {student_needs}
- Group Support Requirements: {group_needs}
- Intervention Priorities: {intervention_priorities}

Performance Data:
- TA Effectiveness Metrics: {ta_metrics}
- Student Satisfaction with Support: {support_satisfaction}
- Resource Utilization: {resource_usage}

Provide:
1. Optimal TA assignment strategy
2. Resource prioritization based on impact data
3. Efficiency improvements through AI augmentation
4. Professional development recommendations for TAs
5. Budget and time optimization strategies

Focus on educational resource management research and effective teaching practices.
"""
