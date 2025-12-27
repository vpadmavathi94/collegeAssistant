import os
from typing import Optional
from dotenv import load_dotenv
import google.generativeai as genai
from utils.config import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

class LLMClient:
    """Client for interacting with Gemini API for campus event Q&A."""
    
    def __init__(self, api_key: Optional[str] = None):
        # Initialize the API key
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model_Name = os.getenv("MODEL_NAME")
        # Raise ValueError if no API key found
        if not self.api_key:
            raise ValueError("API key not provided. Set GEMINI_API_KEY environment variable or pass api_key parameter.")
        
        # Initialize the genai Client
        genai.configure(api_key=self.api_key)
    
    def call_api(self, user_query: str) -> str:
        """Call Gemini API with system prompt and user query."""
        # Format the prompt with user query
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser Query: {user_query}"
        
        # Make API call to llm
        model = genai.GenerativeModel(self.model_Name)
        response = model.generate_content(full_prompt)
        
        # Handle empty or None response
        if not response or not response.text:
            return "Unable to generate a response. Please try again."
        
        # Return the response text
        return response.text


def answer_student_query(query: str) -> str:
    """Answer a student's query about campus events."""
    try:
        # Create llmClient instance
        client = LLMClient()
        # Call the API
        result = client.call_api(query)
        return result
    except ValueError as e:
        return f"Configuration Error: {str(e)}"
    except Exception as e:
        return f"Error processing query: {str(e)}"


def main():
    """Main function to demonstrate the API calling functionality."""
    test_queries = [
        "When is the Tech Fest happening?",
        "Where is the Career Fair located?",
        "Tell me about the Hackathon",
        "What's the schedule for the Music Concert?",
        "Tell me a joke",  # Non-event query
        "What's the weather like?"  # Non-event query
    ]
    
    print("Campus Event Q&A Assistant")
    print("=" * 40)
    
    for query in test_queries:
        print(f"\nQuery: {query}")
        result = answer_student_query(query)
        print(f"Response: {result}")
        print("-" * 40)


if __name__ == "__main__":
    main()
