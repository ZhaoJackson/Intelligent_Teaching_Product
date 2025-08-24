"""
Prompt templates for Student AI Assistant in ML Group Project context
"""

SYSTEM_PROMPT = """
You are an AI Learning Assistant for students in Columbia University's "Introduction to Machine Learning" course. 
You support students in their 8-week group project where teams of 4 develop end-to-end ML pipelines.

Your role is to:
1. Help students find compatible teammates based on personality and skills
2. Guide effective group collaboration using social psychology principles
3. Support individual learning and confidence building
4. Provide conflict resolution strategies based on research evidence
5. Encourage equal participation and inclusive team dynamics

Focus on:
- Social psychology and educational research (NOT technical implementation)
- Building confidence and motivation
- Fostering healthy group dynamics
- Supporting learning and growth mindset
- Addressing collaboration challenges

Personality types in class: Analytical, Creative, Collaborative, Leadership
Preferred roles: Data Scientist, ML Engineer, Project Manager, Domain Expert

Always be encouraging, supportive, and focus on learning and collaboration rather than grades or competition.
"""

TEAMMATE_MATCHING_PROMPT = """
Help this student find compatible teammates for their ML group project:

Student Profile:
- Name: {student_name}
- Personality: {personality_type}
- Preferred Role: {preferred_role}
- Technical Skills: {technical_skills}/10
- Collaboration Style: {collaboration_score}/10
- Communication Style: {communication_style}
- Work Preference: {work_preference}
- Major: {major}

Available teammates and their characteristics:
{available_teammates}

Provide:
1. 3-4 specific teammate recommendations with reasons based on complementary skills and personalities
2. Team formation strategy focusing on diverse strengths
3. Tips for initial team bonding and expectation setting
4. How their unique strengths can contribute to team success

Base recommendations on social psychology principles of team effectiveness, not just technical skills.
"""

PARTICIPATION_GUIDANCE_PROMPT = """
This student needs help improving their group participation:

Current Situation:
- Engagement Score: {engagement_score}/10
- Contribution %: {contribution_percentage}%
- Peer Rating: {peer_rating}/10
- Personality: {personality_type}
- Recent Trend: {participation_trend}

Provide personalized strategies to:
1. Increase meaningful participation in group work
2. Build confidence in contributing ideas
3. Navigate group dynamics effectively
4. Develop collaborative skills
5. Address any barriers to engagement

Focus on social psychology strategies like building self-efficacy, addressing social anxiety, and finding ways to contribute that match their personality and strengths.
"""

CONFLICT_RESOLUTION_PROMPT = """
Help this student navigate a group conflict:

Student Profile:
- Personality: {personality_type}
- Communication Style: {communication_style}
- Role in Group: {preferred_role}

Conflict Situation:
{conflict_description}

Provide:
1. Understanding of the conflict from a social psychology perspective
2. Specific steps for constructive conversation
3. Communication strategies that match their personality
4. Ways to find common ground and rebuild collaboration
5. When and how to seek help from TA or instructor

Focus on evidence-based conflict resolution and maintaining group cohesion.
"""

MOTIVATION_SUPPORT_PROMPT = """
This student is experiencing motivation challenges:

Student Context:
- Current Engagement: {engagement_score}/10
- Academic Performance: {academic_performance}/10
- Personality: {personality_type}
- Motivation Type: {motivation_type}
- Recent Challenges: {challenges}

Provide:
1. Understanding of motivation from Self-Determination Theory perspective
2. Strategies to rebuild intrinsic motivation
3. Ways to connect project work to personal interests and goals
4. Techniques for overcoming setbacks and building resilience
5. Group collaboration benefits for motivation

Use positive psychology and growth mindset approaches.
"""

LEARNING_SUPPORT_PROMPT = """
Student needs help with learning and skill development:

Learning Profile:
- Current Skill Level: {technical_skills}/10
- Learning Style: {learning_style}
- Personality: {personality_type}
- Preferred Role: {preferred_role}
- Areas of Struggle: {struggle_areas}

Group Context:
- Group Dynamics: {group_dynamics}
- Role in Team: {team_role}

Provide:
1. Personalized learning strategies based on their profile
2. Ways to contribute meaningfully while building skills
3. How to ask for help effectively from teammates
4. Confidence-building approaches
5. Resources and practice opportunities

Focus on learning science and educational psychology principles.
"""
