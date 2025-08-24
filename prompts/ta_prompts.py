"""
Prompt templates for TA AI Assistant in ML Course context
"""

SYSTEM_PROMPT = """
You are an AI Assistant for Teaching Assistants in Columbia University's "Introduction to Machine Learning" course.
You help TAs efficiently support 80 students in 20 groups working on collaborative ML projects.

Your role is to:
1. Prioritize TA tasks based on student needs and urgency
2. Provide evidence-based intervention strategies
3. Support conflict resolution using social psychology principles
4. Track TA effectiveness and suggest improvements
5. Optimize TA time for maximum student impact

Focus on:
- Social psychology and group dynamics
- Evidence-based intervention strategies  
- Student support and motivation
- Conflict resolution and mediation
- Collaborative learning facilitation

Course Context:
- 20 groups of 4 students each
- 8-week ML project with multiple milestones
- Diverse student backgrounds and personalities
- Mix of technical and collaboration challenges
- Both individual and group learning objectives

Provide practical, actionable guidance that enhances TA effectiveness.
"""

TASK_PRIORITIZATION_PROMPT = """
Help prioritize TA tasks for maximum student impact:

Current Situation:
- Active Conflicts: {active_conflicts}
- At-Risk Students: {at_risk_students} 
- Groups Needing Support: {struggling_groups}
- Routine Check-ins Needed: {routine_tasks}
- Office Hours Requests: {office_hours_requests}

Time Available: {available_hours} hours today

Student Needs Analysis:
{student_needs_data}

Group Dynamics Status:
{group_status_data}

Provide:
1. Prioritized task list with time estimates
2. Rationale for prioritization based on impact and urgency
3. Delegation suggestions for routine tasks
4. Efficiency strategies for high-impact activities
5. Follow-up planning for incomplete tasks

Base prioritization on educational triage principles and student support research.
"""

CONFLICT_MEDIATION_PROMPT = """
Guide TA through conflict resolution process:

Conflict Details:
- Group: {group_id}
- Conflict Type: {conflict_type}
- Participants: {participants}
- Duration: {conflict_duration}
- Impact on Learning: {learning_impact}

Background Information:
{background_context}

Student Personalities Involved:
{personality_profiles}

Provide:
1. Conflict analysis from social psychology perspective
2. Step-by-step mediation strategy
3. Communication techniques for different personality types
4. Success metrics and follow-up plans
5. When to escalate to instructor

Use evidence-based conflict resolution and group dynamics research.
"""

STUDENT_SUPPORT_PROMPT = """
Develop individualized student support plan:

Student Profile:
- Name: {student_name}
- Current Performance: {performance_metrics}
- Engagement Level: {engagement_score}/10
- Personality Type: {personality_type}
- Learning Challenges: {challenges}

Group Context:
- Group Dynamics: {group_dynamics}
- Role in Team: {team_role}
- Peer Feedback: {peer_feedback}

Recent Concerns:
{recent_issues}

Provide:
1. Root cause analysis of student difficulties
2. Targeted intervention strategies based on personality and learning style
3. Motivation and confidence building approaches
4. Group integration strategies
5. Progress monitoring plan

Apply educational psychology and student development research.
"""

INTERVENTION_STRATEGY_PROMPT = """
Design evidence-based intervention for struggling group:

Group Information:
- Group ID: {group_id}
- Risk Level: {risk_level}
- Main Issues: {primary_issues}
- Progress Status: {progress_status}

Group Composition:
{group_member_profiles}

Performance Data:
{performance_metrics}

Previous Interventions:
{intervention_history}

Provide:
1. Comprehensive intervention plan addressing root causes
2. Specific strategies for each identified issue
3. Timeline and milestones for improvement
4. Success metrics and evaluation methods
5. Contingency plans if initial interventions fail

Base on collaborative learning research and group development theory.
"""

EFFECTIVENESS_ANALYSIS_PROMPT = """
Analyze TA performance and suggest improvements:

TA Performance Metrics:
- Response Time: {response_time} minutes
- Student Satisfaction: {satisfaction_score}/10
- Intervention Success Rate: {success_rate}%
- Conflicts Resolved: {conflicts_resolved}
- Students Supported: {students_helped}

Feedback Data:
- Student Comments: {student_feedback}
- Instructor Observations: {instructor_feedback}
- Self-Assessment: {self_assessment}

Areas for Development:
{development_areas}

Provide:
1. Performance analysis with strengths and growth areas
2. Professional development recommendations
3. Skill-building strategies for identified gaps
4. Efficiency improvements through better practices
5. Goal setting for continuous improvement

Use educational effectiveness research and professional development principles.
"""

GROUP_FACILITATION_PROMPT = """
Guide effective group facilitation strategies:

Group Session Context:
- Group: {group_id}
- Session Purpose: {session_purpose}
- Current Group Dynamics: {group_dynamics}
- Participation Patterns: {participation_data}

Student Profiles:
{student_profiles}

Session Goals:
{session_objectives}

Provide:
1. Facilitation strategy tailored to group composition
2. Techniques to encourage equal participation
3. Methods to maintain focus and productivity
4. Conflict prevention and management during session
5. Follow-up actions to reinforce positive dynamics

Apply group facilitation research and collaborative learning best practices.
"""
