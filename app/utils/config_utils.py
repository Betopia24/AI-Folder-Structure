"""
Configuration utilities for services.

This module provides configuration management utilities that can be reused
across different services in the application.
"""

import os
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class ServiceConfig:
    """Configuration class for service settings"""
    service_name: str
    openai_model: str = "gpt-3.5-turbo"
    temperature: float = 0.7
    max_tokens: int = 1000
    log_level: str = "INFO"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary"""
        return {
            "service_name": self.service_name,
            "openai_model": self.openai_model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "log_level": self.log_level
        }

class ConfigManager:
    """Utility class for managing configuration across services"""
    
    @staticmethod
    def get_service1_config() -> ServiceConfig:
        """Get configuration for Service1"""
        return ServiceConfig(
            service_name="Service1",
            openai_model=os.getenv("SERVICE1_MODEL", "gpt-3.5-turbo"),
            temperature=float(os.getenv("SERVICE1_TEMPERATURE", "0.7")),
            max_tokens=int(os.getenv("SERVICE1_MAX_TOKENS", "1000")),
            log_level=os.getenv("SERVICE1_LOG_LEVEL", "INFO")
        )
    
    @staticmethod
    def get_service2_config() -> ServiceConfig:
        """Get configuration for Service2"""
        return ServiceConfig(
            service_name="Service2",
            openai_model=os.getenv("SERVICE2_MODEL", "gpt-3.5-turbo"),
            temperature=float(os.getenv("SERVICE2_TEMPERATURE", "0.8")),
            max_tokens=int(os.getenv("SERVICE2_MAX_TOKENS", "1200")),
            log_level=os.getenv("SERVICE2_LOG_LEVEL", "INFO")
        )
    
    @staticmethod
    def get_default_config(service_name: str) -> ServiceConfig:
        """Get default configuration for any service"""
        return ServiceConfig(
            service_name=service_name,
            openai_model=os.getenv(f"{service_name.upper()}_MODEL", "gpt-3.5-turbo"),
            temperature=float(os.getenv(f"{service_name.upper()}_TEMPERATURE", "0.7")),
            max_tokens=int(os.getenv(f"{service_name.upper()}_MAX_TOKENS", "1000")),
            log_level=os.getenv(f"{service_name.upper()}_LOG_LEVEL", "INFO")
        )