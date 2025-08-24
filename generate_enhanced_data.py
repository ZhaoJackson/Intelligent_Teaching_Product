import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import json

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

def generate_team_formation_data():
    """Generate data for team formation analysis"""
    formation_methods = ['Random', 'Self-Selected', 'AI-Optimized']
    
    data = []
    for method in formation_methods:
        for i in range(50):  # 50 groups per method
            if method == 'Random':
                satisfaction = np.random.normal(6.5, 1.5)
                skill_balance = np.random.normal(5.5, 1.8)
                diversity_score = np.random.normal(6.0, 1.2)
                completion_rate = np.random.normal(75, 15)
            elif method == 'Self-Selected':
                satisfaction = np.random.normal(7.2, 1.2)
                skill_balance = np.random.normal(4.8, 2.0)
                diversity_score = np.random.normal(5.2, 1.5)
                completion_rate = np.random.normal(78, 12)
            else:  # AI-Optimized
                satisfaction = np.random.normal(8.4, 0.8)
                skill_balance = np.random.normal(8.2, 1.0)
                diversity_score = np.random.normal(8.0, 0.9)
                completion_rate = np.random.normal(89, 8)
            
            data.append({
                'formation_method': method,
                'group_id': f"{method[:3]}{i+1:02d}",
                'satisfaction_score': max(1, min(10, satisfaction)),
                'skill_balance_score': max(1, min(10, skill_balance)),
                'diversity_score': max(1, min(10, diversity_score)),
                'completion_rate': max(50, min(100, completion_rate)),
                'weeks_to_completion': np.random.normal(8 if method == 'AI-Optimized' else 9, 1),
                'conflict_incidents': np.random.poisson(1 if method == 'AI-Optimized' else 3)
            })
    
    return pd.DataFrame(data)

def generate_monitoring_data():
    """Generate real-time monitoring data"""
    data = []
    group_ids = [f"GRP{i:03d}" for i in range(1, 21)]
    
    for group_id in group_ids:
        for week in range(1, 9):  # 8 weeks of data
            for day in range(1, 8):  # Daily monitoring
                # Simulate engagement patterns
                base_engagement = np.random.normal(7.5, 1.2)
                ai_intervention = random.choice([True, False])
                
                if ai_intervention:
                    engagement_boost = np.random.normal(1.5, 0.5)
                    participation_equality = np.random.normal(8.2, 0.8)
                else:
                    engagement_boost = 0
                    participation_equality = np.random.normal(6.8, 1.5)
                
                data.append({
                    'group_id': group_id,
                    'week': week,
                    'day': day,
                    'timestamp': datetime.now() - timedelta(days=(8-week)*7 + (7-day)),
                    'avg_engagement': max(1, min(10, base_engagement + engagement_boost)),
                    'participation_equality': max(1, min(10, participation_equality)),
                    'ai_intervention': ai_intervention,
                    'intervention_type': random.choice(['Prompt quiet member', 'Redirect discussion', 'Suggest break', 'Encourage idea sharing']) if ai_intervention else None,
                    'meeting_duration': np.random.normal(90, 20),
                    'active_speakers': random.randint(2, 4),
                    'off_topic_minutes': np.random.exponential(5) if not ai_intervention else np.random.exponential(2)
                })
    
    return pd.DataFrame(data)

def generate_tutoring_data():
    """Generate AI tutoring and Q&A data"""
    question_types = [
        'Data Preprocessing', 'Feature Engineering', 'Model Selection', 
        'Hyperparameter Tuning', 'Model Evaluation', 'Code Debugging',
        'Project Planning', 'Documentation', 'Presentation'
    ]
    
    data = []
    for i in range(1000):  # 1000 tutoring interactions
        response_quality = np.random.normal(8.2, 1.1)  # AI typically performs well
        resolution_time = np.random.exponential(15)  # Fast response times
        
        data.append({
            'interaction_id': f"TUT{i+1:04d}",
            'student_id': f"STU{random.randint(1, 80):03d}",
            'group_id': f"GRP{random.randint(1, 20):03d}",
            'question_type': random.choice(question_types),
            'timestamp': datetime.now() - timedelta(minutes=random.randint(0, 10080)),  # Last week
            'response_time_minutes': max(0.5, resolution_time),
            'response_quality': max(1, min(10, response_quality)),
            'student_satisfaction': max(1, min(10, response_quality + np.random.normal(0, 0.5))),
            'follow_up_needed': random.choices([True, False], weights=[0.2, 0.8])[0],
            'complexity_level': random.choice(['Basic', 'Intermediate', 'Advanced']),
            'ai_confidence': np.random.beta(8, 2) * 100  # AI typically confident
        })
    
    return pd.DataFrame(data)

def generate_participation_data():
    """Generate equal participation tracking data"""
    students_df = pd.read_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/students.csv')
    
    data = []
    for _, student in students_df.iterrows():
        for week in range(1, 9):
            # Simulate contribution patterns
            base_contribution = student['engagement_score'] * 10  # Convert to percentage
            weekly_variation = np.random.normal(0, 5)
            
            # AI intervention effect
            if student['engagement_score'] < 6:  # Low engagement student
                ai_boost = np.random.normal(15, 5) if random.random() < 0.7 else 0
            else:
                ai_boost = np.random.normal(2, 3)
            
            contribution_pct = max(5, min(50, base_contribution + weekly_variation + ai_boost))
            
            data.append({
                'student_id': student['student_id'],
                'group_id': student['group_id'],
                'week': week,
                'contribution_percentage': contribution_pct,
                'code_commits': random.randint(2, 15),
                'document_edits': random.randint(1, 8),
                'meeting_speaking_time': np.random.normal(contribution_pct/4, 5),
                'ideas_contributed': random.randint(1, 6),
                'ai_prompts_received': random.randint(0, 5),
                'peer_rating': max(1, min(10, np.random.normal(7, 1.2))),
                'improvement_flag': contribution_pct > base_contribution
            })
    
    return pd.DataFrame(data)

def generate_motivation_data():
    """Generate motivation and positive reinforcement data"""
    reinforcement_types = [
        'Achievement Badge', 'Progress Celebration', 'Peer Recognition', 
        'Skill Improvement Note', 'Team Contribution Highlight', 'Goal Achievement'
    ]
    
    data = []
    for i in range(500):
        data.append({
            'reinforcement_id': f"MOT{i+1:04d}",
            'student_id': f"STU{random.randint(1, 80):03d}",
            'group_id': f"GRP{random.randint(1, 20):03d}",
            'reinforcement_type': random.choice(reinforcement_types),
            'timestamp': datetime.now() - timedelta(hours=random.randint(0, 336)),  # Last 2 weeks
            'engagement_before': np.random.normal(6.5, 1.5),
            'engagement_after': np.random.normal(7.8, 1.2),
            'motivation_boost': np.random.normal(1.3, 0.8),
            'student_response': random.choice(['Very Positive', 'Positive', 'Neutral', 'Negative']),
            'continued_engagement': random.choices([True, False], weights=[0.8, 0.2])[0],
            'message_content': f"Great work on {random.choice(['data analysis', 'model implementation', 'team collaboration', 'documentation'])}!"
        })
    
    return pd.DataFrame(data)

def generate_gamification_data():
    """Generate gamification and engagement incentive data"""
    achievement_types = [
        'Data Detective', 'Code Collaborator', 'Model Master', 'Team Player',
        'Documentation Champion', 'Innovation Leader', 'Debugging Hero', 'Presentation Pro'
    ]
    
    data = []
    for i in range(300):
        data.append({
            'achievement_id': f"GAM{i+1:04d}",
            'student_id': f"STU{random.randint(1, 80):03d}",
            'group_id': f"GRP{random.randint(1, 20):03d}",
            'achievement_type': random.choice(achievement_types),
            'points_earned': random.randint(10, 100),
            'timestamp': datetime.now() - timedelta(hours=random.randint(0, 504)),  # Last 3 weeks
            'difficulty_level': random.choice(['Bronze', 'Silver', 'Gold', 'Platinum']),
            'team_bonus': random.choice([True, False]),
            'engagement_increase': np.random.normal(12, 4),  # Percentage increase
            'time_to_earn_hours': np.random.exponential(24),
            'shared_with_team': random.choices([True, False], weights=[0.7, 0.3])[0]
        })
    
    return pd.DataFrame(data)

def generate_conflict_resolution_data():
    """Generate conflict mediation and resolution data"""
    conflict_types = [
        'Unequal Contribution', 'Communication Style Clash', 'Technical Disagreement',
        'Scheduling Conflict', 'Leadership Dispute', 'Quality Standards Disagreement'
    ]
    
    resolution_strategies = [
        'Structured Discussion', 'Role Redistribution', 'Mediated Compromise',
        'Skill-Based Task Assignment', 'Communication Training', 'Goal Realignment'
    ]
    
    data = []
    for i in range(150):
        intervention_time = np.random.exponential(2)  # AI detects conflicts quickly
        resolution_success = random.choices([True, False], weights=[0.85, 0.15])[0]
        
        data.append({
            'conflict_id': f"CON{i+1:04d}",
            'group_id': f"GRP{random.randint(1, 20):03d}",
            'conflict_type': random.choice(conflict_types),
            'detection_method': random.choice(['Communication Analysis', 'Participation Metrics', 'Student Report']),
            'timestamp': datetime.now() - timedelta(hours=random.randint(0, 672)),  # Last 4 weeks
            'severity_level': random.choice(['Low', 'Medium', 'High']),
            'intervention_time_hours': max(0.5, intervention_time),
            'resolution_strategy': random.choice(resolution_strategies),
            'resolution_success': resolution_success,
            'group_satisfaction_before': np.random.normal(5.2, 1.5),
            'group_satisfaction_after': np.random.normal(7.8, 1.2) if resolution_success else np.random.normal(5.8, 1.8),
            'human_ta_involved': random.choices([True, False], weights=[0.3, 0.7])[0],
            'follow_up_needed': random.choices([True, False], weights=[0.4, 0.6])[0]
        })
    
    return pd.DataFrame(data)

def main():
    """Generate all enhanced datasets"""
    print("Generating enhanced datasets for AI TA analysis...")
    
    # Generate enhanced datasets
    print("1. Team Formation Analysis...")
    team_formation_df = generate_team_formation_data()
    team_formation_df.to_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/team_formation.csv', index=False)
    
    print("2. Real-time Monitoring...")
    monitoring_df = generate_monitoring_data()
    monitoring_df.to_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/monitoring.csv', index=False)
    
    print("3. AI Tutoring & Q&A...")
    tutoring_df = generate_tutoring_data()
    tutoring_df.to_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/tutoring.csv', index=False)
    
    print("4. Equal Participation Tracking...")
    participation_df = generate_participation_data()
    participation_df.to_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/participation.csv', index=False)
    
    print("5. Motivation & Reinforcement...")
    motivation_df = generate_motivation_data()
    motivation_df.to_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/motivation.csv', index=False)
    
    print("6. Gamification & Engagement...")
    gamification_df = generate_gamification_data()
    gamification_df.to_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/gamification.csv', index=False)
    
    print("7. Conflict Resolution...")
    conflict_df = generate_conflict_resolution_data()
    conflict_df.to_csv('/Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/conflicts.csv', index=False)
    
    print("\n=== ENHANCED DATA SUMMARY ===")
    print(f"Team Formation Analysis: {len(team_formation_df)} records")
    print(f"Real-time Monitoring: {len(monitoring_df)} records")
    print(f"AI Tutoring Interactions: {len(tutoring_df)} records")
    print(f"Participation Tracking: {len(participation_df)} records")
    print(f"Motivation Events: {len(motivation_df)} records")
    print(f"Gamification Achievements: {len(gamification_df)} records")
    print(f"Conflict Resolutions: {len(conflict_df)} records")
    
    print("\nEnhanced data generation completed successfully!")
    print("Files saved to /Users/jacksonzhao/Desktop/Intelligent_Teaching_Product/data/")

if __name__ == "__main__":
    main()
