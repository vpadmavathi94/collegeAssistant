"""
Configuration file for Campus Event Q&A Assistant.
Handles loading the system prompt from prompt.txt file.
"""

import os


def load_system_prompt() -> str:
    """Load the system prompt from prompt.txt file."""
    try:
        # Get the path to prompt.txt file
        prompt_path = os.path.join(os.path.dirname(__file__), '..', 'prompt.txt')
        
        # Open and read the prompt file
        with open(prompt_path, 'r') as f:
            prompt_content = f.read()
        
        # Return the content stripped of whitespace
        return prompt_content.strip()
    except FileNotFoundError:
        return "You are a helpful assistant for campus events Q&A."
    except Exception as e:
        return f"Error loading prompt: {str(e)}"


def get_system_prompt() -> str:
    """Get the system prompt with user query placeholder."""
    return load_system_prompt()


# Export the system prompt as SYSTEM_PROMPT
SYSTEM_PROMPT = get_system_prompt()
