"""Common utilities for all services.

This module provides simple utility functions that can be reused across different services.
All functions are standalone and don't require instantiation.
"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime


def format_success_response(data: Any, message: str = "Success") -> Dict[str, Any]:
    """
    Format a successful API response with metadata.
    
    Args:
        data: The response data to include
        message: Success message (default: "Success")
        
    Returns:
        Dictionary with status, message, data, and timestamp
        
    Example:
        response = format_success_response({"result": "Hello"}, "Request completed")
    """
    return {
        "status": "success",
        "message": message,
        "data": data,
        "timestamp": datetime.now().isoformat()
    }


def format_error_response(error: str, details: Optional[str] = None) -> Dict[str, Any]:
    """
    Format an error API response with metadata.
    
    Args:
        error: The error message
        details: Additional error details (optional)
        
    Returns:
        Dictionary with status, message, details, and timestamp
        
    Example:
        error = format_error_response("Validation failed", "Missing required field")
    """
    return {
        "status": "error",
        "message": error,
        "details": details,
        "timestamp": datetime.now().isoformat()
    }


def sanitize_input(input_text: str) -> str:
    """
    Sanitize user input to prevent prompt injection and excessive length.
    
    This function:
    - Returns empty string if input is None or empty
    - Replaces multiple newlines and tabs with single spaces
    - Limits length to 1000 characters to prevent token overflow
    
    Args:
        input_text: The user input string to sanitize
        
    Returns:
        Cleaned and safe input string
        
    Example:
        clean = sanitize_input("Hello\n\nworld\t!")
        # Returns: "Hello world !"
    """
    if not input_text:
        return ""
    
    # Replace multiple whitespace characters with single spaces
    sanitized = input_text.replace('\n\n', ' ').replace('\t', ' ')
    
    # Limit length to prevent excessive token usage
    return sanitized[:1000] if len(sanitized) > 1000 else sanitized


def validate_prompt_length(prompt: str, max_length: int = 2000) -> bool:
    """
    Validate that a prompt doesn't exceed maximum length.
    
    Args:
        prompt: The prompt text to validate
        max_length: Maximum allowed length (default: 2000)
        
    Returns:
        True if prompt is within length limit, False otherwise
        
    Example:
        is_valid = validate_prompt_length("Short prompt")  # Returns: True
    """
    return len(prompt) <= max_length


def setup_logger(service_name: str) -> logging.Logger:
    """
    Set up a logger with consistent formatting for a service.
    
    This function:
    - Creates a logger with the service name
    - Adds a console handler if none exists
    - Sets up consistent formatting with timestamp, service name, level, and message
    - Sets log level to INFO
    
    Args:
        service_name: Name of the service for the logger
        
    Returns:
        Configured logger instance
        
    Example:
        logger = setup_logger("MyService")
        logger.info("Processing request")
    """
    logger = logging.getLogger(service_name)
    
    # Only add handler if none exists to avoid duplicates
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            f'%(asctime)s - {service_name} - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    
    return logger


def validate_openai_params(model: str, temperature: float, max_tokens: int) -> Dict[str, Any]:
    """
    Validate and sanitize OpenAI API parameters to ensure they're within safe limits.
    
    This function:
    - Clamps temperature between 0.0 and 2.0
    - Limits max_tokens between 1 and 4000
    - Validates model name against known models, defaults to gpt-3.5-turbo if invalid
    
    Args:
        model: OpenAI model name
        temperature: Sampling temperature (0.0 to 2.0)
        max_tokens: Maximum tokens to generate
        
    Returns:
        Dictionary with validated model, temperature, and max_tokens
        
    Example:
        config = validate_openai_params("gpt-4", 1.5, 2000)
        # Returns: {"model": "gpt-4", "temperature": 1.5, "max_tokens": 2000}
    """
    # Ensure temperature is within valid range (0.0 to 2.0)
    safe_temperature = max(0.0, min(2.0, temperature))
    
    # Ensure max_tokens is within reasonable limits
    safe_max_tokens = max(1, min(4000, max_tokens))
    
    # Validate model name against known models
    valid_models = ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo-preview"]
    safe_model = model if model in valid_models else "gpt-3.5-turbo"
    
    return {
        "model": safe_model,
        "temperature": safe_temperature,
        "max_tokens": safe_max_tokens
    }