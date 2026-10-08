
"""Defines the AI Travel Planner agents."""

# Gemini client and message types
from google.genai import Client, types

# Local LLM-based agent
from google.adk.agents.llm_agent import Agent

# Remote agent using A2A protocol
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent

# Example tool for agent capabilities
from google.adk.tools.example_tool import ExampleTool

# Environment variables and file paths
import os

# Read JSON datasets
import json