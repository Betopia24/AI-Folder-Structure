"""Service 1 - General AI Assistant

This service provides general AI assistance for any questions or tasks.
Just ask it anything and get helpful responses!
"""

import os
import openai
from dotenv import load_dotenv
from .service1_schema import service1_response
from ...utils.common_utils import sanitize_input, setup_logger, validate_openai_params

# Load environment variables
load_dotenv()

# Set up logging for this service
logger = setup_logger("Service1")

class Service1:
    """General AI assistant service."""
    
    def __init__(self):
        """Initialize the service with OpenAI client."""
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_service1(self, input_data: dict) -> service1_response:
        """
        Main method to process general questions.
        
        Args:
            input_data: Dictionary containing the user's input
            
        Returns:
            service1_response with the AI's answer
        """
        logger.info("Got a question for the AI assistant!")
        
        # Get the user's input
        user_input = input_data.get('example_field', '')
        
        # Clean the input to make it safe
        clean_input = sanitize_input(user_input)
        
        # Create a simple prompt
        prompt = self._create_simple_prompt(clean_input)
        
        # Get AI response
        answer = self._get_ai_response(prompt)
        
        logger.info("AI response generated successfully!")
        return service1_response(example_field=answer)

    def _create_simple_prompt(self, user_input: str) -> str:
        """
        Create a simple, helpful prompt.
        
        Args:
            user_input: The user's question or request
            
        Returns:
            A formatted prompt string
        """
        prompt = f"""You are a helpful AI assistant. Please provide a clear, helpful response.
        
        User asks: {user_input}
        
        Provide a comprehensive and friendly answer that addresses their needs.
        """
        
        return prompt

    def _get_ai_response(self, prompt: str) -> str:
        """
        Get response from OpenAI API with safe parameters.
        
        Args:
            prompt: The prompt to send to AI
            
        Returns:
            AI response string
        """
        # Use utility function to ensure safe parameters
        safe_config = validate_openai_params(
            model="gpt-3.5-turbo", 
            temperature=0.7, 
            max_tokens=1000
        )
        
        # Make the API call
        completion = self.client.chat.completions.create(
            model=safe_config["model"],
            messages=[{"role": "user", "content": prompt}],
            temperature=safe_config["temperature"],
            max_tokens=safe_config["max_tokens"]
        )
        
        return completion.choices[0].message.content.strip()
