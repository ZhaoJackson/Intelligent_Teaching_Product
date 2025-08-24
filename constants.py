"""
Global constants and paths for the Intelligent Teaching Product
"""
import os
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent

# Data directory paths
DATA_DIR = PROJECT_ROOT / "data"

# Data file paths
DATA_PATHS = {
    'students': DATA_DIR / "students.csv",
    'groups': DATA_DIR / "groups.csv",
    'interactions': DATA_DIR / "interactions.csv",
    'monitoring': DATA_DIR / "monitoring.csv",
    'tutoring': DATA_DIR / "tutoring.csv",
    'participation': DATA_DIR / "participation.csv",
    'motivation': DATA_DIR / "motivation.csv",
    'gamification': DATA_DIR / "gamification.csv",
    'conflicts': DATA_DIR / "conflicts.csv",
    'team_formation': DATA_DIR / "team_formation.csv"
}

# Convert to strings for compatibility
DATA_PATHS_STR = {k: str(v) for k, v in DATA_PATHS.items()}

# Course configuration
COURSE_CONFIG = {
    'name': 'Introduction to Machine Learning',
    'institution': 'Columbia University',
    'total_students': 80,
    'groups_count': 20,
    'students_per_group': 4,
    'project_duration_weeks': 8
}

# User roles
USER_ROLES = ['Student', 'TA', 'Professor']

# Personality types
PERSONALITY_TYPES = ['Analytical', 'Creative', 'Collaborative', 'Leadership']

# Social psychology principles
PSYCHOLOGY_PRINCIPLES = {
    'social_facilitation': 'Performance enhancement in the presence of others',
    'social_loafing': 'Tendency to exert less effort in group tasks',
    'groupthink': 'Pressure for consensus that can suppress dissent',
    'social_identity': 'Sense of self derived from group membership',
    'positive_interdependence': 'Success depends on all members contributing'
}

# Research-based best practices
BEST_PRACTICES = {
    'group_formation': [
        'Balance personality types and skill levels',
        'Ensure diversity of perspectives and backgrounds',
        'Consider communication styles and work preferences',
        'Promote positive interdependence through role assignment'
    ],
    'engagement_strategies': [
        'Use structured discussion formats',
        'Implement peer accountability systems',
        'Provide regular feedback and recognition',
        'Address conflicts early through mediation'
    ],
    'assessment_methods': [
        'Individual and group component balance',
        'Peer evaluation and self-reflection',
        'Process-focused as well as outcome-focused',
        'Continuous feedback rather than summative only'
    ]
}