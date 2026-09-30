import os
from crewai import Agent, LLM


llm = LLM(
    model="openai/gpt-oss-120b",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY"),
    temperature=0.4,
)


recommendation_agent = Agent(
    role="University Program Recommendation Specialist",

    goal=(
        "Recommend suitable university programs based on "
        "the student's academic profile, interests, budget, "
        "and preferred location."
    ),

    backstory=(
        "You are a university program advisor. "
        "You help students identify programs that match "
        "their academic background and interests. "
        "Only recommend programs from the information provided. "
        "Do not invent universities or programs."
    ),

    llm=llm,

    verbose=True,

    allow_delegation=False,
)
