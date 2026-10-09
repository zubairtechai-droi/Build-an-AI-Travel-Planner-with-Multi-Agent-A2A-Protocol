import os

from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.genai import types
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

selected_model = LiteLlm(
    model="openrouter/openrouter/free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

attractions_agent = Agent(
    model=selected_model,
    name="attractions_agent",
    description="Provides tourist attractions info for a given city.",
    instruction="""
        You are responsible for suggesting popular tourist attractions,
        sightseeing spots, and local activities for the given city.

        Provide concise and relevant recommendations to help the user
        plan their trip.
    """,
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)