"""Service 2 - Simple Fitness Helper

This service provides simple fitness advice and workout suggestions.
Just ask it anything fitness-related and get helpful answers!
"""

import os
import openai
from dotenv import load_dotenv
from .service2_schema import service2_response
from ...utils.common_utils import sanitize_input, setup_logger, validate_openai_params

# Load environment variables
load_dotenv()

# Set up logging for this service
logger = setup_logger("Service2")

class Service2:
    """Simple fitness helper service."""
    
    def __init__(self):
        """Initialize the service with OpenAI client."""
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_service2(self, input_data: dict) -> service2_response:
        """
        Main method to process fitness questions.
        
        Args:
            input_data: Dictionary containing the user's question
            
        Returns:
            service2_response with the fitness advice
        """
        logger.info("Got a fitness question!")
        
        # Get the user's question
        question = input_data.get('question', 'Give me a simple workout')
        
        # Clean the input to make it safe
        clean_question = sanitize_input(question)
        
        # Create a simple prompt
        prompt = self._create_simple_prompt(clean_question)
        
        # Get AI response
        answer = self._get_ai_response(prompt)
        
        logger.info("Fitness advice generated successfully!")
        return service2_response(answer=answer)

    def _create_simple_prompt(self, question: str) -> str:
        """
        Create a simple, friendly prompt for fitness advice.
        
        Args:
            question: The user's fitness question
            
        Returns:
            A formatted prompt string
        """
        prompt = f"""You are a friendly fitness coach. Give simple, practical advice.
        
User asks: {question}
        
Provide a helpful, encouraging response. Keep it simple and actionable!
        If they want a workout, suggest 3-5 easy exercises they can do at home.
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
            max_tokens=800
        )
        
        # Make the API call
        completion = self.client.chat.completions.create(
            model=safe_config["model"],
            messages=[{"role": "user", "content": prompt}],
            temperature=safe_config["temperature"],
            max_tokens=safe_config["max_tokens"]
        )
        
        return completion.choices[0].message.content.strip()