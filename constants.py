"""
Global constants and paths for the AI-Enhanced Teaching Assistant Dashboard
"""

import os
from pathlib import Path

# Base paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
PAGES_DIR = PROJECT_ROOT / "pages"
PROMPTS_DIR = PROJECT_ROOT / "prompts"

# Data file paths
STUDENTS_CSV = DATA_DIR / "students.csv"
GROUPS_CSV = DATA_DIR / "groups.csv"
INTERACTIONS_CSV = DATA_DIR / "interactions.csv"
MONITORING_CSV = DATA_DIR / "monitoring.csv"
TUTORING_CSV = DATA_DIR / "tutoring.csv"
PARTICIPATION_CSV = DATA_DIR / "participation.csv"
MOTIVATION_CSV = DATA_DIR / "motivation.csv"
GAMIFICATION_CSV = DATA_DIR / "gamification.csv"
CONFLICTS_CSV = DATA_DIR / "conflicts.csv"
TEAM_FORMATION_CSV = DATA_DIR / "team_formation.csv"

# User roles
USER_ROLES = {
    "STUDENT": "student",
    "PROFESSOR": "professor", 
    "TA": "teaching_assistant",
    "ADMIN": "administrator",
    "RESEARCHER": "educational_researcher"
}

# Course context
COURSE_INFO = {
    "name": "Introduction to Machine Learning",
    "institution": "Columbia University",
    "total_students": 80,
    "total_groups": 20,
    "group_size": 4,
    "project_duration_weeks": 8,
    "project_components": [
        "Data preprocessing and cleaning",
        "Feature engineering and selection", 
        "Model selection and training",
        "Hyperparameter optimization",
        "Results interpretation and presentation"
    ]
}

# AI model configuration
AZURE_OPENAI_CONFIG = {
    "api_version": "2024-12-01-preview",
    "deployment_name": "gpt-4o",
    "max_tokens": 1500,
    "temperature": 0.7
}

# Social psychology principles
PSYCHOLOGY_PRINCIPLES = {
    "SOCIAL_LOAFING": {
        "name": "Social Loafing Theory",
        "researchers": "Latané, Williams & Harkins (1979)",
        "description": "Individuals exert less effort when working in groups due to reduced accountability"
    },
    "SELF_DETERMINATION": {
        "name": "Self-Determination Theory", 
        "researchers": "Deci & Ryan (1985)",
        "description": "Three basic psychological needs: autonomy, competence, and relatedness"
    },
    "EQUITY_THEORY": {
        "name": "Equity Theory",
        "researchers": "Adams (1963)", 
        "description": "People seek fairness in the ratio of their contributions to rewards"
    },
    "SOCIAL_COMPARISON": {
        "name": "Social Comparison Theory",
        "researchers": "Festinger (1954)",
        "description": "Human drive to evaluate self through comparison with others"
    },
    "COOPERATIVE_LEARNING": {
        "name": "Cooperative Learning Theory",
        "researchers": "Johnson & Johnson",
        "description": "Structured approach to collaborative learning with positive interdependence"
    }
}

# Dashboard color scheme
COLORS = {
    "PRIMARY": "#1f77b4",
    "SUCCESS": "#2ecc71", 
    "WARNING": "#f39c12",
    "DANGER": "#e74c3c",
    "INFO": "#3498db",
    "LIGHT": "#f8f9fa",
    "DARK": "#2c3e50"
}

# Engagement thresholds
ENGAGEMENT_THRESHOLDS = {
    "HIGH": 8.5,
    "MEDIUM": 6.5,
    "LOW": 4.0
}

# Risk level definitions
RISK_LEVELS = {
    "LOW": {"threshold": 8.0, "color": COLORS["SUCCESS"]},
    "MEDIUM": {"threshold": 6.0, "color": COLORS["WARNING"]}, 
    "HIGH": {"threshold": 0.0, "color": COLORS["DANGER"]}
}

# AI enhancement areas
AI_ENHANCEMENT_AREAS = [
    {
        "id": "team_formation",
        "name": "Forming Well-Balanced Teams",
        "description": "AI analyzes student profiles for optimal group composition",
        "evidence": "Khan Academy's Khanmigo shows 40% improvement in group satisfaction"
    },
    {
        "id": "real_time_monitoring", 
        "name": "Real-Time Facilitation and Monitoring",
        "description": "Continuous observation with immediate intervention capabilities",
        "evidence": "NSF iSAT Institute research shows 35% increase in equal participation"
    },
    {
        "id": "ai_tutoring",
        "name": "AI Tutoring and Question Answering", 
        "description": "24/7 availability for content support and feedback",
        "evidence": "Georgia Tech's Jill Watson handled 97% of routine questions effectively"
    },
    {
        "id": "equal_participation",
        "name": "Encouraging Equal Participation",
        "description": "Data-driven tracking with targeted interventions", 
        "evidence": "FeedbackFruits shows 60% reduction in free-riding behavior"
    },
    {
        "id": "motivation_systems",
        "name": "Motivation and Positive Reinforcement",
        "description": "Psychology-based engagement strategies",
        "evidence": "Gamified AI systems show 45% increase in student motivation"
    },
    {
        "id": "gamification",
        "name": "Gamification and Engagement Incentives",
        "description": "Game mechanics for collaborative behavior",
        "evidence": "Classcraft reports 50% improvement in collaborative behaviors"
    },
    {
        "id": "conflict_resolution",
        "name": "Conflict Mediation and Social Coaching", 
        "description": "Early detection with evidence-based resolution",
        "evidence": "Robot TA studies show improved conflict resolution in 70% of cases"
    }
]
