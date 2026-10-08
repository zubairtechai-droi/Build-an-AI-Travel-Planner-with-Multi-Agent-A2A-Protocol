"""Defines the AI Travel Planner agents."""

import os

from dotenv import load_dotenv
from google import genai
from google.adk.agents.llm_agent import Agent
from google.genai import types


load_dotenv()


def select_model():
    """Find a working Gemini Flash model automatically."""

    # Connect to Gemini using the API key from .env
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    # Get models available to our API key
    models = client.models.list()

    # Try available Flash models
    for model in models:

        # Skip models that cannot generate content
        if "generateContent" not in model.supported_actions:
            continue

        # Skip non-Flash models
        if "flash" not in model.name.lower():
            continue

        # Google returns "models/model-name"
        # ADK expects "model-name"
        model_name = model.name.replace("models/", "", 1)

        try:
            print(f"Trying model: {model_name}")

            # Check if the model actually responds
            client.models.generate_content(
                model=model_name,
                contents="Say hello."
            )

            print(f"Using model: {model_name}")

            return model_name

        except Exception:
            print(f"Model unavailable: {model_name}")

    raise RuntimeError(
        "No working Gemini Flash model was found."
    )


# Automatically choose a working model.
selected_model = select_model()


# Local ADK agent responsible for tourist attractions.
attractions_agent = Agent(
    # Model selected automatically at runtime.
    model=selected_model,

    # Unique agent name.
    name="attractions_agent",

    # Agent responsibility.
    description="Provides tourist attractions info for a given city.",

    # Agent instructions.
    instruction="""
        You are responsible for suggesting popular tourist attractions,
        sightseeing spots, and local activities for the given city.
        Provide concise and relevant recommendations to help the user plan their trip.
    """,

    # Gemini safety configuration.
    generate_content_config=types.GenerateContentConfig(
        safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.OFF,
            ),
        ]
    ),
)