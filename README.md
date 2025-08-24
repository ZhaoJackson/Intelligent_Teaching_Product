# AI-Enhanced Teaching Assistant Dashboard 🎓

A comprehensive Streamlit dashboard that explores how AI can replace or enhance the functionality of teaching assistants in student group settings, specifically enabling more consistent engagement among group members in targeted classes.

## Research Question

**How can AI replace or enhance the functionality of teaching assistants in student group settings, specifically enabling more consistent engagement among group members in targeted classes, without focusing on engineering considerations?**

## Project Overview

This dashboard demonstrates an AI-powered solution for managing student group dynamics in a Columbia University "Introduction to Machine Learning" course context. The system addresses common challenges in group projects through data-driven insights and psychology-based interventions.

### Course Context
- **Class Size**: 80 students organized into 20 groups of 4
- **Project Type**: End-to-end machine learning pipeline development
- **Key Components**: Data processing, feature engineering, model selection, training, hyperparameter tuning
- **Duration**: 8-week collaborative project
- **Challenges**: Diverse backgrounds, trust issues, free-rider problems, inconsistent TA availability

## Features

### 🔍 Page 1: Research Framework
- Comprehensive analysis of current TA limitations
- AI-enhanced solutions for group management
- Psychology-based intervention strategies
- Implementation roadmap with expected outcomes

### 📊 Page 2: Group Dynamics Dashboard
- Real-time monitoring of 20 student groups
- Risk assessment and early warning systems
- Performance analytics and engagement metrics
- Individual student progress tracking
- Interactive visualizations of group health

### 🤖 Page 3: AI Collaboration Assistant
- Intelligent teammate matching based on personality types
- Psychology-driven conflict resolution strategies
- Role assignment optimization
- Group health assessment tools
- Real-time collaboration guidance

## Key AI Capabilities

### 🎯 Smart Group Formation
- **Personality Compatibility**: Matches complementary personality types (Analytical, Creative, Collaborative, Leadership)
- **Skill Diversity**: Balances technical expertise across group members
- **Role Optimization**: Assigns roles based on natural strengths and interests
- **Communication Style Matching**: Pairs compatible interaction preferences

### 📈 Continuous Monitoring
- **Engagement Tracking**: 24/7 observation of group interactions
- **Early Warning System**: Identifies potential issues before they escalate
- **Performance Prediction**: Forecasts group success based on dynamics
- **Intervention Recommendations**: Suggests targeted support strategies

### 🧠 Psychology-Based Interventions
- **Trust Building**: Facilitates psychological safety in teams
- **Conflict Resolution**: Applies social psychology principles
- **Motivation Enhancement**: Addresses intrinsic vs. extrinsic motivation
- **Communication Improvement**: Provides structured dialogue frameworks

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Intelligent_Teaching_Product
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate synthetic data** (already done, but can be regenerated)
   ```bash
   python generate_data.py
   ```

4. **Run the Streamlit application**
   ```bash
   streamlit run app.py
   ```

5. **Access the dashboard**
   - Open your web browser and navigate to `http://localhost:8501`

## Data Structure

The dashboard uses three main datasets:

### Students Dataset (`data/students.csv`)
- **80 student profiles** with realistic diversity
- Personality types, technical skills, collaboration scores
- Learning preferences and availability patterns
- Academic performance and engagement metrics

### Groups Dataset (`data/groups.csv`)
- **20 group compositions** with 4 students each
- Risk assessment levels (Low, Medium, High)
- Progress tracking and meeting patterns
- Project topics and documentation quality

### Interactions Dataset (`data/interactions.csv`)
- **500+ interaction records** between students
- Communication patterns and collaboration quality
- Meeting histories and follow-up requirements
- Topic-specific discussion tracking

## Theoretical Framework

### Social Psychology Principles
- **Social Identity Theory**: Understanding group belonging and dynamics
- **Trust Building**: Creating psychological safety in teams
- **Communication Styles**: Matching compatible interaction preferences
- **Conflict Resolution**: Early intervention strategies based on behavioral patterns

### AI Enhancement Strategies
1. **Assessment Phase**: Personality profiling, skill assessment, learning style analysis
2. **Matching Phase**: Complementary skill pairing, personality compatibility, diverse perspective inclusion
3. **Monitoring Phase**: Real-time tracking, early warning systems, intervention recommendations

## Usage Guide

### For Instructors
1. **Monitor Group Health**: Use the dashboard to identify at-risk groups
2. **Intervention Planning**: Get AI-recommended strategies for struggling teams
3. **Performance Analytics**: Track engagement and collaboration metrics
4. **Resource Allocation**: Focus TA support where it's needed most

### For Students
1. **Find Compatible Teammates**: Use the AI matching system
2. **Resolve Conflicts**: Access psychology-based resolution strategies
3. **Optimize Roles**: Get recommendations for effective task distribution
4. **Track Progress**: Monitor group health and individual contributions

### For Researchers
1. **Analyze Group Dynamics**: Explore the relationship between personality and performance
2. **Test Interventions**: Use the simulated environment to test new strategies
3. **Study Collaboration Patterns**: Examine communication and engagement data
4. **Validate Theories**: Test social psychology principles in educational settings

## Technical Architecture

### Frontend
- **Streamlit**: Interactive web application framework
- **Plotly**: Advanced data visualizations
- **Custom CSS**: Enhanced user interface styling

### Data Management
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Synthetic Data Generation**: Realistic student and interaction patterns

### AI Components
- **Matching Algorithms**: Psychology-based compatibility scoring
- **Risk Assessment**: Multi-factor evaluation of group health
- **Intervention Systems**: Context-aware recommendation engine

## Expected Outcomes

### Improved Student Experience
- **Enhanced Engagement**: More consistent participation across all group members
- **Better Learning Outcomes**: Optimized group composition and support
- **Reduced Conflicts**: Early detection and resolution of interpersonal issues
- **Increased Satisfaction**: Higher quality collaborative experiences

### Enhanced TA Effectiveness
- **Scalable Support**: Consistent quality across all groups
- **Efficient Resource Use**: Focus on high-impact interventions
- **Data-Driven Decisions**: Objective assessment and guidance
- **Proactive Management**: Prevention rather than reaction

### Educational Innovation
- **Personalized Learning**: Tailored group experiences for diverse students
- **Evidence-Based Practice**: Psychology-informed educational strategies
- **Continuous Improvement**: Data-driven optimization of group dynamics
- **Institutional Benefits**: Improved course outcomes and student satisfaction

## Future Enhancements

### Advanced AI Features
- Natural language processing for communication analysis
- Predictive modeling for group success forecasting
- Adaptive intervention strategies based on real-time feedback
- Integration with learning management systems

### Extended Psychology Integration
- Cultural competency considerations
- Emotional intelligence assessments
- Stress and well-being monitoring
- Long-term relationship building strategies

### Scalability Improvements
- Multi-course deployment capabilities
- Cross-institutional collaboration features
- Mobile application development
- Real-time notification systems

## Contributing

We welcome contributions to improve the AI-Enhanced Teaching Assistant Dashboard. Please feel free to:
- Submit bug reports and feature requests
- Contribute code improvements
- Share educational insights and best practices
- Provide feedback on user experience

## License

This project is developed for educational and research purposes. Please refer to the license file for specific usage terms.

## Contact

For questions, suggestions, or collaboration opportunities, please contact the development team.

---

*This dashboard represents a comprehensive approach to enhancing educational group dynamics through AI-powered insights and psychology-based interventions, demonstrating the potential for technology to improve collaborative learning experiences without replacing the human elements that make education meaningful.*