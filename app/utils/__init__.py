"""
Utility package for common functionality across services.

This package contains simple, reusable utility functions for:
- API response formatting
- Input validation and sanitization
- Logging setup
- OpenAI configuration validation
- Service configuration management

All functions are simple and don't require class instantiation.
"""

from .common_utils import (
    format_success_response,
    format_error_response,
    sanitize_input,
    validate_prompt_length,
    setup_logger,
    validate_openai_params
)

from .config_utils import (
    ServiceConfig,
    ConfigManager
)

__all__ = [
    "format_success_response",
    "format_error_response",
    "sanitize_input", 
    "validate_prompt_length",
    "setup_logger",
    "validate_openai_params",
    "ServiceConfig",
    "ConfigManager"
]