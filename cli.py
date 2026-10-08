"""CLI for running the AI Travel Planner."""

# Async program execution
import asyncio

# Gemini message types
from google.genai import types

# Executes ADK agents
from google.adk.runners import Runner

# Stores sessions in memory
from google.adk.sessions.in_memory_session_service import InMemorySessionService

# Stores artifacts in memory
from google.adk.artifacts.in_memory_artifact_service import InMemoryArtifactService

# Manages credentials in memory
from google.adk.auth.credential_service.in_memory_credential_service import InMemoryCredentialService

# Defines the ADK application
from google.adk.apps.app import App

# Main travel-planning agent
from agent import root_agent
