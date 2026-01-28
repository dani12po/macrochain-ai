"""
Configuration settings for MacroChain AI.

This module contains all configuration parameters and settings
for the MacroChain AI system.
"""

import os
from typing import Dict, Any
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    # API Configuration
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_title: str = "MacroChain AI API"
    api_description: str = "AI-powered crypto market analysis agent"
    api_version: str = "1.0.0"
    
    # Analysis Configuration
    max_analysis_length: int = 2000
    analysis_timeout: int = 30
    
    # LLM Configuration (placeholder for future integration)
    llm_provider: str = "openai"  # Can be changed to other providers
    llm_model: str = "gpt-3.5-turbo"
    llm_temperature: float = 0.3
    llm_max_tokens: int = 1000
    
    # Data Sources (conceptual - no live APIs required)
    enable_onchain_data: bool = True
    enable_sentiment_data: bool = True
    enable_macro_data: bool = True
    
    # Risk Management
    max_risk_level: str = "medium"  # low, medium, high
    require_disclaimer: bool = True
    
    # Logging
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
settings = Settings()


def get_analysis_config() -> Dict[str, Any]:
    """
    Get analysis configuration parameters.
    
    Returns:
        Dictionary containing analysis configuration
    """
    return {
        "max_length": settings.max_analysis_length,
        "timeout": settings.analysis_timeout,
        "enable_onchain": settings.enable_onchain_data,
        "enable_sentiment": settings.enable_sentiment_data,
        "enable_macro": settings.enable_macro_data,
        "max_risk_level": settings.max_risk_level,
        "require_disclaimer": settings.require_disclaimer
    }


def get_llm_config() -> Dict[str, Any]:
    """
    Get LLM configuration parameters.
    
    Returns:
        Dictionary containing LLM configuration
    """
    return {
        "provider": settings.llm_provider,
        "model": settings.llm_model,
        "temperature": settings.llm_temperature,
        "max_tokens": settings.llm_max_tokens
    }


def get_api_config() -> Dict[str, Any]:
    """
    Get API configuration parameters.
    
    Returns:
        Dictionary containing API configuration
    """
    return {
        "host": settings.api_host,
        "port": settings.api_port,
        "title": settings.api_title,
        "description": settings.api_description,
        "version": settings.api_version
    }
