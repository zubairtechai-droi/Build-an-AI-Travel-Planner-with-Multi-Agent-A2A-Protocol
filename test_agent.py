import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Suppress ADK experimental warnings
warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    module=r"google\.adk\..*"
)

# Optional: suppress only function_call concatenation warnings
warnings.filterwarnings(
    "ignore",
    message=r".*non-text parts in the response.*"
)


from dotenv import load_dotenv
load_dotenv()  # loads .env into os.environ


import asyncio
from google.genai import types
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.artifacts.in_memory_artifact_service import InMemoryArtifactService
from google.adk.auth.credential_service.in_memory_credential_service import InMemoryCredentialService
from google.adk.apps.app import App
from agent import attractions_agent
#from agent import flight_agent # Comment it out when running the file in Task 2
#from agent import hotel_agent # Comment it out when running the file in Task 2 and 3
from google.adk.apps import App



# Task 2: Connect CLI with Attractions Agent
async def run_cli_attractions():
    artifact_service = InMemoryArtifactService()
    session_service = InMemorySessionService()
    credential_service = InMemoryCredentialService()

    session = await session_service.create_session(app_name="TravelPlanner", user_id="user_1")
    app = App(name="TravelPlanner", root_agent=attractions_agent)

    runner = Runner(
        app=app,
        artifact_service=artifact_service,
        session_service=session_service,
        credential_service=credential_service,
    )

    print("Welcome to Travel Planner CLI!")


    user_input = "Suggest three attractions in Paris that are good for photography."

    content = types.Content(role="user", parts=[types.Part(text=user_input)])
    agen = runner.run_async(user_id=session.user_id, session_id=session.id, new_message=content)

    async for event in agen:
        if event.content and event.content.parts:
            text = "".join(part.text for part in event.content.parts if part.text)
            if text:
                print(f"[{event.author}]: {text}")

    await runner.close()


# Comment it out when running the file in Task 2
# Task 3: Connect CLI with Flight Agent
async def run_cli_flights():
    artifact_service = InMemoryArtifactService()
    session_service = InMemorySessionService()
    credential_service = InMemoryCredentialService()

    app = App(name="TravelPlanner", root_agent=flight_agent)
    user_input = "Show flights from New York to London on 01-01"     
    session = await session_service.create_session(app_name="TravelPlanner", user_id="user_1")

    runner = Runner(
        app=app,
        artifact_service=artifact_service,
        session_service=session_service,
        credential_service=credential_service,
    )

    print("Welcome to Travel Planner CLI!")
    print(f"Query: {user_input}")

    content = types.Content(role="user", parts=[types.Part(text=user_input)])
    agen = runner.run_async(user_id=session.user_id, session_id=session.id, new_message=content)

    async for event in agen:
        if event.content and event.content.parts:
            text = "".join(part.text for part in event.content.parts if part.text)
            if text:
                print(f"[{event.author}]: {text}")

    await runner.close()



# Comment it out when running the file in Task 2 and 3
# Task 4: Connect CLI with Flight Agent
async def run_cli_hotels():
    artifact_service = InMemoryArtifactService()
    session_service = InMemorySessionService()
    credential_service = InMemoryCredentialService()


    app = App(name="TravelPlanner", root_agent=hotel_agent)

    # NOTE: The query below will be answered by the LLM's general knowledge 
    user_input = "Suggest hotels in Paris with at least 4 stars and under $120" 
    session = await session_service.create_session(app_name="TravelPlanner", user_id="user_1")

    runner = Runner(
        app=app,
        artifact_service=artifact_service,
        session_service=session_service,
        credential_service=credential_service,
    )

    print("Welcome to Travel Planner CLI!")
    print(f"Query: {user_input}")

    content = types.Content(role="user", parts=[types.Part(text=user_input)])
    agen = runner.run_async(user_id=session.user_id, session_id=session.id, new_message=content)

    async for event in agen:
        if event.content and event.content.parts:
            text = "".join(part.text for part in event.content.parts if part.text)
            if text:
                print(f"[{event.author}]: {text}")

    await runner.close()


if __name__ == "__main__":
    asyncio.run(run_cli_attractions())
