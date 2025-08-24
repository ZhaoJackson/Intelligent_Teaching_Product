"""
Utilities package for AI-Enhanced Teaching Assistant Dashboard
"""

from .azure_openai import azure_openai_client, get_ai_response, format_context_data

__all__ = ['azure_openai_client', 'get_ai_response', 'format_context_data']
