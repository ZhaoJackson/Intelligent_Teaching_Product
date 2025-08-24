"""
Azure OpenAI integration utility for the AI-Enhanced Teaching Assistant Dashboard
"""

import streamlit as st
from openai import AzureOpenAI
from typing import Dict, List, Optional
import json
import time

class AzureOpenAIClient:
    """Client for Azure OpenAI API integration"""
    
    def __init__(self):
        """Initialize Azure OpenAI client with secrets from streamlit"""
        try:
            self.api_key = st.secrets["openai"]["AZURE_OPENAI_4O_API_KEY"]
            self.endpoint = st.secrets["openai"]["AZURE_OPENAI_4O_ENDPOINT"]
            self.api_version = st.secrets["openai"]["AZURE_OPENAI_4O_API_VERSION"]
            self.deployment = st.secrets["openai"]["AZURE_OPENAI_4O_DEPLOYMENT"]
            
            # Initialize Azure OpenAI client
            self.client = AzureOpenAI(
                api_key=self.api_key,
                api_version=self.api_version,
                azure_endpoint=self.endpoint
            )
            
        except Exception as e:
            st.error(f"Failed to initialize Azure OpenAI client: {e}")
            self.client = None
            self.api_key = None
    
    def is_available(self) -> bool:
        """Check if Azure OpenAI client is properly configured"""
        return self.client is not None
    
    def generate_response(
        self, 
        system_prompt: str, 
        user_prompt: str, 
        context_data: Optional[Dict] = None,
        max_tokens: int = 1500,
        temperature: float = 0.7,
        retry_attempts: int = 3
    ) -> str:
        """
        Generate AI response using Azure OpenAI
        
        Args:
            system_prompt: System role and instructions
            user_prompt: User's question or request
            context_data: Additional context for the conversation
            max_tokens: Maximum tokens in response
            temperature: Response creativity (0-1)
            retry_attempts: Number of retry attempts on failure
            
        Returns:
            Generated response string
        """
        if not self.is_available():
            return self._fallback_response(user_prompt)
        
        try:
            # Prepare messages
            messages = [
                {"role": "system", "content": system_prompt}
            ]
            
            # Add context if provided
            if context_data:
                context_message = f"Context Data: {json.dumps(context_data, indent=2)}"
                messages.append({"role": "system", "content": context_message})
            
            messages.append({"role": "user", "content": user_prompt})
            
            # Make API call with retry logic
            for attempt in range(retry_attempts):
                try:
                    response = self.client.chat.completions.create(
                        model=self.deployment,
                        messages=messages,
                        max_tokens=max_tokens,
                        temperature=temperature,
                        top_p=0.95,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    
                    return response.choices[0].message.content.strip()
                    
                except Exception as e:
                    if "rate_limit" in str(e).lower():
                        if attempt < retry_attempts - 1:
                            time.sleep(2 ** attempt)  # Exponential backoff
                            continue
                        else:
                            return self._rate_limit_response()
                    else:
                        if attempt < retry_attempts - 1:
                            time.sleep(1)
                            continue
                        else:
                            return self._api_error_response(str(e))
            
        except Exception as e:
            st.error(f"Error generating AI response: {e}")
            return self._fallback_response(user_prompt)
    
    def _fallback_response(self, user_prompt: str) -> str:
        """Provide fallback response when AI is unavailable"""
        return f"""
I apologize, but I'm currently unable to access the AI system to provide a personalized response to your question: "{user_prompt[:100]}..."

However, I can direct you to some helpful resources:

🎓 **For Students:**
- Review the participation guidelines and team formation strategies
- Check the course materials for collaboration best practices
- Reach out to your TA during office hours for personalized support

👨‍🏫 **For TAs:**
- Refer to the conflict resolution frameworks in the dashboard
- Use the student analytics to identify priority interventions
- Consult with the instructor for complex situations

🎓 **For Instructors:**
- Review the class performance analytics for insights
- Consider the evidence-based intervention strategies
- Leverage the peer support network recommendations

The dashboard contains comprehensive information and tools that can help address most questions about collaborative learning and group dynamics.
        """
    
    def _rate_limit_response(self) -> str:
        """Response when rate limited"""
        return """
I'm currently experiencing high demand and need to limit responses. Please try again in a few moments.

In the meantime, you can:
- Explore the interactive visualizations in the dashboard
- Review the research-based recommendations for your role
- Use the data filters to find relevant insights
- Check the evidence-based strategies for your specific situation
        """
    
    def _api_error_response(self, error: str) -> str:
        """Response when API error occurs"""
        return f"""
I'm experiencing a temporary issue connecting to the AI service. 

The dashboard still provides valuable insights through:
- Interactive data visualizations and analytics
- Evidence-based research findings and recommendations
- Role-specific guidance and best practices
- Comprehensive resources for collaborative learning

Please try again later or explore the dashboard features directly.

Technical details: {error}
        """

# Global instance
azure_openai_client = AzureOpenAIClient()

def get_ai_response(
    system_prompt: str,
    user_prompt: str, 
    context_data: Optional[Dict] = None,
    **kwargs
) -> str:
    """Convenience function for getting AI responses"""
    return azure_openai_client.generate_response(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        context_data=context_data,
        **kwargs
    )

def format_context_data(
    student_profile: Optional[Dict] = None,
    group_data: Optional[Dict] = None,
    performance_metrics: Optional[Dict] = None,
    additional_context: Optional[Dict] = None
) -> Dict:
    """Format context data for AI prompts"""
    context = {}
    
    def clean_data(data):
        """Clean data for JSON serialization"""
        if isinstance(data, dict):
            return {k: clean_data(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [clean_data(item) for item in data]
        elif hasattr(data, 'to_dict'):  # pandas objects
            return data.to_dict()
        elif hasattr(data, 'tolist'):  # numpy arrays
            return data.tolist()
        else:
            return str(data)  # Convert everything else to string
    
    if student_profile:
        context["student_profile"] = clean_data(student_profile)
    
    if group_data:
        context["group_data"] = clean_data(group_data)
        
    if performance_metrics:
        context["performance_metrics"] = clean_data(performance_metrics)
        
    if additional_context:
        context.update(clean_data(additional_context))
        
    return context
