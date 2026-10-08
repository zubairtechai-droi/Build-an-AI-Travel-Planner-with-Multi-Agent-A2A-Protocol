"""Defines the AI Travel Planner agents."""

# Gemini API client
from google.genai import Client

# ADK local agent
from google.adk.agents.llm_agent import Agent

# Remote agent and standard A2A Agent Card path
from google.adk.agents.remote_a2a_agent import (
    AGENT_CARD_WELL_KNOWN_PATH,
    RemoteA2aAgent,
)

# Example tool for agents
from google.adk.tools.example_tool import ExampleTool

# Gemini message/content types
from google.genai import types

# Environment variables and JSON data
import os
import json

# Optional type hints
from typing import Optional