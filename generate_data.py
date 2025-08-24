import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import json

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

def generate_student_data(n_students=80):
    """Generate synthetic student data for the ML class"""
    
    # Define possible values
    personality_types = ["Analytical", "Creative", "Collaborative", "Leadership"]
    preferred_roles = ["Data Scientist", "ML Engineer", "Project Manager", "Domain Expert"]
    majors = ["Computer Science", "Statistics", "Mathematics", "Business", "Psychology", "Engineering"]
    
    # Generate names (mix of common names)
    first_names = [
        "Alex", "Taylor", "Jordan", "Casey", "Morgan", "Riley", "Avery", "Cameron",
        "Emma", "Liam", "Olivia", "Noah", "Sophia", "Ethan", "Isabella", "Mason",
        "Ava", "William", "Mia", "James", "Charlotte", "Benjamin", "Amelia", "Lucas",
        "Harper", "Henry", "Evelyn", "Alexander", "Abigail", "Michael", "Emily", "Daniel",
        "Elizabeth", "Jacob", "Sofia", "Logan", "Madison", "Jackson", "Scarlett", "Sebastian",
        "Victoria", "Jack", "Aria", "Owen", "Grace", "Samuel", "Chloe", "Matthew", "Camila",
        "Joseph", "Penelope", "Levi", "Riley", "Mateo", "Layla", "David", "Lillian",
        "John", "Nora", "Wyatt", "Zoey", "Carter", "Mila", "Luke", "Aubrey",
        "Jayden", "Hannah", "Gabriel", "Lily", "Anthony", "Addison", "Isaac", "Eleanor",
        "Grayson", "Natalie", "Dylan", "Luna", "Leo", "Savannah", "Lincoln", "Brooklyn"
    ]
    
    last_names = [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
        "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas",
        "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White",
        "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young",
        "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
        "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
        "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker",
        "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy",
        "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey",
        "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson"
    ]
    
    students = []
    
    for i in range(n_students):
        # Generate correlated attributes for realism
        personality = random.choice(personality_types)
        
        # Personality influences preferred role and skills
        if personality == "Analytical":
            preferred_role = random.choice(["Data Scientist", "ML Engineer"])
            technical_skills = np.random.normal(8, 1.5)
            collaboration_score = np.random.normal(6, 1.5)
        elif personality == "Creative":
            preferred_role = random.choice(["Domain Expert", "Data Scientist"])
            technical_skills = np.random.normal(7, 1.5)
            collaboration_score = np.random.normal(7, 1.5)
        elif personality == "Collaborative":
            preferred_role = random.choice(["Project Manager", "Domain Expert"])
            technical_skills = np.random.normal(6, 1.5)
            collaboration_score = np.random.normal(8.5, 1)
        else:  # Leadership
            preferred_role = random.choice(["Project Manager", "ML Engineer"])
            technical_skills = np.random.normal(7.5, 1.5)
            collaboration_score = np.random.normal(8, 1.5)
        
        # Ensure scores are within bounds
        technical_skills = max(1, min(10, technical_skills))
        collaboration_score = max(1, min(10, collaboration_score))
        
        # Generate engagement score (correlated with collaboration)
        engagement_score = collaboration_score + np.random.normal(0, 1)
        engagement_score = max(1, min(10, engagement_score))
        
        # Academic performance (correlated with engagement and technical skills)
        academic_performance = (technical_skills * 0.4 + engagement_score * 0.6) + np.random.normal(0, 0.5)
        academic_performance = max(1, min(10, academic_performance))
        
        # Work style preferences
        work_styles = ["Morning", "Afternoon", "Evening"]
        availability = random.sample(work_styles, random.randint(1, 3))
        
        student = {
            'student_id': f"STU{i+1:03d}",
            'student_name': f"{random.choice(first_names)} {random.choice(last_names)}",
            'major': random.choice(majors),
            'personality_type': personality,
            'preferred_role': preferred_role,
            'technical_skills': round(technical_skills, 1),
            'collaboration_score': round(collaboration_score, 1),
            'engagement_score': round(engagement_score, 1),
            'academic_performance': round(academic_performance, 1),
            'communication_style': random.choice(["Direct", "Diplomatic", "Supportive", "Analytical"]),
            'work_preference': random.choice(["Individual first", "Collaborative", "Mixed approach"]),
            'availability': ", ".join(availability),
            'group_id': f"GRP{(i//4)+1:03d}",  # 4 students per group
            'previous_ml_experience': random.choice(["None", "Beginner", "Intermediate", "Advanced"]),
            'motivation_type': random.choice(["Grade-focused", "Learning-focused", "Career-focused", "Research-focused"])
        }
        
        students.append(student)
    
    return pd.DataFrame(students)

def generate_group_data(students_df):
    """Generate group-level data based on student composition"""
    
    groups = []
    n_groups = len(students_df['group_id'].unique())
    
    for i in range(n_groups):
        group_id = f"GRP{i+1:03d}"
        group_students = students_df[students_df['group_id'] == group_id]
        
        # Calculate group metrics
        avg_technical = group_students['technical_skills'].mean()
        avg_collaboration = group_students['collaboration_score'].mean()
        avg_engagement = group_students['engagement_score'].mean()
        
        # Diversity metrics
        personality_diversity = len(group_students['personality_type'].unique())
        role_diversity = len(group_students['preferred_role'].unique())
        major_diversity = len(group_students['major'].unique())
        
        # Calculate risk level based on various factors
        risk_factors = 0
        if avg_engagement < 6:
            risk_factors += 2
        if avg_collaboration < 6:
            risk_factors += 2
        if personality_diversity < 3:
            risk_factors += 1
        if role_diversity < 3:
            risk_factors += 1
        if group_students['engagement_score'].std() > 2:  # High variance in engagement
            risk_factors += 1
        
        if risk_factors >= 4:
            risk_level = "High"
        elif risk_factors >= 2:
            risk_level = "Medium"
        else:
            risk_level = "Low"
        
        # Progress percentage (influenced by group dynamics)
        base_progress = 60  # 8 weeks into semester
        if risk_level == "Low":
            progress_modifier = np.random.normal(15, 5)
        elif risk_level == "Medium":
            progress_modifier = np.random.normal(5, 5)
        else:
            progress_modifier = np.random.normal(-5, 5)
        
        progress_percentage = max(20, min(95, base_progress + progress_modifier))
        
        # ML project topics
        ml_topics = [
            "Customer Churn Prediction", "Image Classification for Medical Diagnosis",
            "Natural Language Processing for Sentiment Analysis", "Recommendation Systems",
            "Time Series Forecasting", "Fraud Detection", "Predictive Maintenance",
            "Speech Recognition", "Computer Vision for Autonomous Vehicles",
            "Drug Discovery with ML", "Financial Risk Assessment", "Climate Data Analysis",
            "Social Media Analytics", "E-commerce Price Optimization", "Healthcare Analytics",
            "Supply Chain Optimization", "Energy Consumption Prediction", "Stock Market Prediction",
            "Cybersecurity Threat Detection", "Sports Performance Analytics"
        ]
        
        group = {
            'group_id': group_id,
            'group_name': f"Team {i+1}",
            'project_topic': ml_topics[i % len(ml_topics)],
            'avg_technical_skills': round(avg_technical, 1),
            'avg_collaboration_score': round(avg_collaboration, 1),
            'avg_engagement_score': round(avg_engagement, 1),
            'personality_diversity': personality_diversity,
            'role_diversity': role_diversity,
            'major_diversity': major_diversity,
            'risk_level': risk_level,
            'progress_percentage': round(progress_percentage, 1),
            'last_meeting': datetime.now() - timedelta(days=random.randint(1, 7)),
            'meetings_per_week': round(np.random.normal(2.5, 0.5), 1),
            'code_commits_week': random.randint(5, 25),
            'documentation_quality': random.choice(["Excellent", "Good", "Needs Improvement", "Poor"])
        }
        
        groups.append(group)
    
    return pd.DataFrame(groups)

def generate_interaction_data(students_df, n_interactions=500):
    """Generate interaction data between students"""
    
    interactions = []
    interaction_types = [
        "Code Review", "Discussion", "Meeting", "Help Request", "Collaboration",
        "Conflict Resolution", "Knowledge Sharing", "Planning Session"
    ]
    
    for i in range(n_interactions):
        # Select random students (bias towards same group)
        if random.random() < 0.7:  # 70% chance same group
            group_id = random.choice(students_df['group_id'].unique())
            group_students = students_df[students_df['group_id'] == group_id]
            student1, student2 = random.sample(list(group_students['student_id']), 2)
        else:  # 30% chance different groups
            student1, student2 = random.sample(list(students_df['student_id']), 2)
        
        interaction = {
            'interaction_id': f"INT{i+1:04d}",
            'student1_id': student1,
            'student2_id': student2,
            'interaction_type': random.choice(interaction_types),
            'timestamp': datetime.now() - timedelta(
                days=random.randint(0, 30),
                hours=random.randint(0, 23),
                minutes=random.randint(0, 59)
            ),
            'duration_minutes': random.randint(15, 120),
            'quality_rating': round(np.random.normal(7, 1.5), 1),
            'follow_up_needed': random.choice([True, False]),
            'topic': random.choice([
                "Data Preprocessing", "Model Selection", "Feature Engineering",
                "Hyperparameter Tuning", "Results Interpretation", "Code Debugging",
                "Project Planning", "Documentation", "Presentation Prep"
            ])
        }
        
        # Ensure quality rating is within bounds
        interaction['quality_rating'] = max(1, min(10, interaction['quality_rating']))
        
        interactions.append(interaction)
    
    return pd.DataFrame(interactions)

def main():
    """Generate all synthetic data files"""
    print("Generating synthetic data for AI-Enhanced Teaching Assistant Dashboard...")
    
    # Generate data
    print("Creating student profiles...")
    students_df = generate_student_data(80)
    
    print("Creating group compositions...")
    groups_df = generate_group_data(students_df)
    
    print("Creating interaction histories...")
    interactions_df = generate_interaction_data(students_df)
    
    # Save to CSV files
    print("Saving data files...")
    students_df.to_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/students.csv', index=False)
    groups_df.to_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/groups.csv', index=False)
    interactions_df.to_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/interactions.csv', index=False)
    
    # Generate summary statistics
    print("\n=== DATA SUMMARY ===")
    print(f"Generated {len(students_df)} student profiles")
    print(f"Created {len(groups_df)} groups")
    print(f"Recorded {len(interactions_df)} interactions")
    
    print(f"\nGroup Risk Distribution:")
    print(groups_df['risk_level'].value_counts())
    
    print(f"\nPersonality Type Distribution:")
    print(students_df['personality_type'].value_counts())
    
    print(f"\nPreferred Role Distribution:")
    print(students_df['preferred_role'].value_counts())
    
    print("\nData generation completed successfully!")
    print("Files saved to /Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/")

if __name__ == "__main__":
    main()
