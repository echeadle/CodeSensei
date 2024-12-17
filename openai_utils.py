# Wrapper for OpenAI API integration.
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get OpenAI API Key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please check your .env file.")

def generate_code(prompt, model="gpt-4", max_tokens=200):
    """
    Generates Python code based on a user-provided prompt.

    Args:
        prompt (str): User's input describing the task or code requirements.
        model (str): OpenAI model to use (default: gpt-4).
        max_tokens (int): Maximum number of tokens in the response.

    Returns:
        str: Generated code as a string.
    """
    try:
        response = openai.Completion.create(
            model=model,
            prompt=f"Write Python code for the following task:\n{prompt}",
            max_tokens=max_tokens,
            temperature=0.5
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error: {e}"

def explain_code(code, model="gpt-4", max_tokens=300):
    """
    Explains the provided Python code.

    Args:
        code (str): Python code to explain.
        model (str): OpenAI model to use (default: gpt-4).
        max_tokens (int): Maximum number of tokens in the response.

    Returns:
        str: Explanation of the code.
    """
    try:
        response = openai.Completion.create(
            model=model,
            prompt=f"Explain the following Python code in simple terms:\n{code}",
            max_tokens=max_tokens,
            temperature=0.5
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error: {e}"

def debug_code(code, model="gpt-4", max_tokens=300):
    """
    Provides debugging suggestions for the given Python code.

    Args:
        code (str): Python code to debug.
        model (str): OpenAI model to use (default: gpt-4).
        max_tokens (int): Maximum number of tokens in the response.

    Returns:
        str: Debugging suggestions or fixes for the code.
    """
    try:
        response = openai.Completion.create(
            model=model,
            prompt=f"Identify errors in the following Python code and suggest fixes:\n{code}",
            max_tokens=max_tokens,
            temperature=0.5
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error: {e}"

def optimize_code(code, model="gpt-4", max_tokens=300):
    """
    Suggests optimizations for the provided Python code.

    Args:
        code (str): Python code to optimize.
        model (str): OpenAI model to use (default: gpt-4).
        max_tokens (int): Maximum number of tokens in the response.

    Returns:
        str: Optimized version or suggestions for improvements.
    """
    try:
        response = openai.Completion.create(
            model=model,
            prompt=f"Optimize the following Python code for better performance or readability:\n{code}",
            max_tokens=max_tokens,
            temperature=0.5
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error: {e}"
