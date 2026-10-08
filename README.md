\# ✈️ AI Travel Planner — Multi-Agent A2A System



An AI-powered travel planner built with \*\*Python, Google Gemini, Google Agent Development Kit (ADK), and Agent-to-Agent (A2A) communication\*\*.



The system uses multiple specialized AI agents to collaboratively plan a trip. Instead of relying on one large agent to perform every task, each agent focuses on a specific travel domain and communicates with a \*\*Root Agent\*\* that coordinates the overall planning process.



\## 🏗️ Architecture



```text

&#x20;                        ┌──────────────────┐

&#x20;                        │      User        │

&#x20;                        │      CLI         │

&#x20;                        └────────┬─────────┘

&#x20;                                 │

&#x20;                                 ▼

&#x20;                      ┌────────────────────┐

&#x20;                      │    Root Agent      │

&#x20;                      │ Gemini + ADK       │

&#x20;                      │   Coordinator      │

&#x20;                      └─────────┬──────────┘

&#x20;                                │

&#x20;                   A2A Communication

&#x20;                                │

&#x20;            ┌───────────────────┼───────────────────┐

&#x20;            │                   │                   │

&#x20;            ▼                   ▼                   ▼

&#x20;     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐

&#x20;     │   Flights   │     │   Hotels    │     │ Attractions │

&#x20;     │    Agent    │     │    Agent    │     │    Agent    │

&#x20;     └──────┬──────┘     └──────┬──────┘     └──────┬──────┘

&#x20;            │                   │                   │

&#x20;            ▼                   ▼                   ▼

&#x20;      Mock Dataset        Mock Dataset         Mock Dataset



&#x20;                        ┌──────────────────┐

&#x20;                        │  Weather Agent   │

&#x20;                        │   Remote A2A     │

&#x20;                        └────────┬─────────┘

&#x20;                                 │

&#x20;                                 ▼

&#x20;                        OpenWeatherMap API

```



The \*\*Root Agent\*\* receives the user's travel request, determines which specialized agents are required, delegates tasks, collects their responses, and produces the final travel plan.



\## 🎯 Project Description



Traditional AI applications often rely on a single model to handle multiple responsibilities. As the number of tasks increases, this can make systems harder to maintain and potentially less reliable.



This project demonstrates an alternative approach using a \*\*multi-agent architecture\*\*.



Each specialized agent has a clearly defined responsibility:



\- ✈️ \*\*Flights Agent\*\* — searches available flights using mock flight data.

\- 🏨 \*\*Hotels Agent\*\* — recommends hotels using city-specific mock data.

\- 🏛️ \*\*Attractions Agent\*\* — suggests tourist attractions and activities.

\- 🌤️ \*\*Weather Agent\*\* — retrieves weather information using the OpenWeatherMap API.

\- 🧠 \*\*Root Agent\*\* — coordinates the specialized agents and creates the final travel plan.



The Weather Agent is implemented as a \*\*remote agent\*\* and communicates with the Root Agent using the \*\*A2A protocol\*\*.



\## 📚 You Will Learn



\- Use the \*\*Google Agent Development Kit (ADK)\*\* to create specialized AI agents.

\- Design agents with clearly defined responsibilities.

\- Create and register agents for flights, hotels, attractions, and weather.

\- Build a \*\*Root Agent\*\* that delegates tasks to specialized agents.

\- Understand \*\*Agent-to-Agent (A2A)\*\* communication.

\- Define agent capabilities using \*\*Agent Cards\*\*.

\- Integrate external APIs with AI agents.

\- Work with mock datasets for external services.

\- Build asynchronous Python applications.

\- Run a multi-agent AI system through a command-line interface.

\- Understand patterns used in distributed AI and agentic systems.



\## 🧠 Skills



\- Generative AI

\- Multi-Agent Systems

\- Agentic AI

\- AI Chatbots

\- AI Orchestration

\- API Integration

\- Asynchronous Python

\- Distributed AI Systems



\## 🛠️ Technologies



\- \*\*Python\*\*

\- \*\*Google Gemini\*\*

\- \*\*Google Agent Development Kit (ADK)\*\*

\- \*\*Agent-to-Agent (A2A) Protocol\*\*

\- \*\*OpenWeatherMap API\*\*

\- JSON

\- Asynchronous Python

\- Command Line Interface (CLI)



\## 📋 Prerequisites



Before starting, you should have:



\- Basic Python knowledge

\- Familiarity with APIs and JSON

\- Basic understanding of generative AI

\- A Google Gemini API key

\- An OpenWeatherMap API key



Python \*\*3.11+\*\* is recommended.



\## 📁 Project Structure



```text

travel-planner/

│

├── agent.py

│

├── agents/

│   └── weather\_agent/

│       ├── agent.py

│       ├── agent.json

│       └── mock\_weather.json

│

├── cli.py

│

├── flights\_dataset.json

├── mock\_hotels.json

│

├── .env

├── .gitignore

├── requirements.txt

└── README.md

```



\### Main Components



| Component | Responsibility |

|---|---|

| `agent.py` | Defines the root and local specialized agents |

| `agents/weather\_agent/` | Contains the remote Weather Agent |

| `weather\_agent/agent.py` | Weather Agent implementation |

| `weather\_agent/agent.json` | Weather Agent capability/card definition |

| `mock\_weather.json` | Weather/mock weather data |

| `flights\_dataset.json` | Mock flight dataset |

| `mock\_hotels.json` | Mock hotel dataset |

| `cli.py` | Command-line interface |

| `.env` | API keys and environment variables |



\## 🔄 How It Works



A user might enter:



```text

Plan a 5-day trip from Lahore to Istanbul.

My budget is $1,500.

I am interested in history and food.

```



The Root Agent analyzes the request and delegates the required work:



```text

User

&#x20;│

&#x20;▼

Root Agent

&#x20;│

&#x20;├──► Flights Agent

&#x20;│

&#x20;├──► Hotels Agent

&#x20;│

&#x20;├──► Attractions Agent

&#x20;│

&#x20;└──► Weather Agent

&#x20;         │

&#x20;         ▼

&#x20;   OpenWeatherMap

```



The specialized agents return their results to the Root Agent.



The Root Agent then combines the information into a single travel recommendation:



```text

✈️ Flights

🏨 Hotels

🌤️ Weather

🏛️ Attractions

💰 Estimated Budget

📅 Suggested Itinerary

```



\## 🤝 Why A2A?



The \*\*Agent-to-Agent (A2A)\*\* approach allows agents to communicate through a structured protocol rather than requiring the Root Agent to directly control every implementation detail.



This provides better separation of responsibilities:



```text

Root Agent

&#x20;   │

&#x20;   │ A2A

&#x20;   ▼

Specialized Agent

&#x20;   │

&#x20;   ▼

External API / Dataset

```



A specialized agent can therefore evolve independently while maintaining a defined communication interface with other agents.



\## 🌐 Remote Weather Agent



The Weather Agent demonstrates how a remote agent can expose its capabilities to other agents.



Its Agent Card describes:



\- Agent identity

\- Capabilities

\- Supported operations

\- Communication endpoint



The Root Agent can discover the Weather Agent and communicate with it through A2A.



\## 🚀 Example Use Case



Input:



```text

Plan a 4-day trip from Lahore to Dubai

with a budget of $1,200.

```



The system can coordinate:



1\. Flight recommendations.

2\. Hotel recommendations.

3\. Weather information.

4\. Tourist attractions.

5\. A final combined itinerary.



\## 🔐 Environment Variables



Create a `.env` file containing your API credentials:



```text

GOOGLE\_API\_KEY=your\_google\_api\_key

OPENWEATHER\_API\_KEY=your\_openweathermap\_api\_key

```



\*\*Never commit `.env` to Git.\*\*



The project `.gitignore` excludes it from version control.



\## ▶️ Running the Project



After setting up the environment and installing dependencies:



```bash

python cli.py

```



Then enter a travel request through the CLI.



\## 🎓 Learning Outcome



By completing this project, you will move from building a single AI agent toward understanding how \*\*multiple specialized agents can collaborate as a distributed AI system\*\*.



The architecture demonstrates concepts that can also be applied beyond travel planning, including:



\- Enterprise AI automation

\- Customer support systems

\- Research assistants

\- Data-processing pipelines

\- AI workflow orchestration

\- Production agent platforms

\- Distributed AI applications



\---



\## 📌 Project Goal



The primary goal is not simply to build a travel chatbot.



It is to understand how to design, connect, and orchestrate \*\*specialized AI agents using ADK and A2A communication\*\*.

