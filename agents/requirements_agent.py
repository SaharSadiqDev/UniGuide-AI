import os
from crewai import Agent, LLM


llm = LLM(
    model="openai/gpt-oss-120b",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY"),
    temperature=0.2,
)


requirements_agent = Agent(
    role="University Admission Requirements Specialist",

    goal=(
        "Identify and explain the admission requirements "
        "for the university programs provided by the system."
    ),

    backstory=(
        "You are a university admission requirements specialist. "
        "You carefully analyze the provided university and program "
        "information and clearly explain the requirements. "
        "Never invent requirements that are not provided."
    ),

    llm=llm,

    verbose=True,

    allow_delegation=False,
)
