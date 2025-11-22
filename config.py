"""
Configuration module for Claude Alsokkary
"""

import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Model Configuration
DEFAULT_MODEL = "claude-3-5-sonnet-20241022"
MAX_TOKENS = 2048
TEMPERATURE = 0.7

# Application Settings
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = "DEBUG" if DEBUG else "INFO"

# System Prompt
SYSTEM_PROMPT = """
You are Claude Alsokkary, an intelligent assistant specialized in:
- GitHub automation and repository management
- Code analysis and suggestions
- Development workflow optimization
- Problem-solving and technical guidance

Provide helpful, accurate, and practical advice. Always consider best practices and security.
"""