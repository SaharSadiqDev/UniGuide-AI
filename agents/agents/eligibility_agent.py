import os
from crewai import Agent, LLM


llm = LLM(
    model="openai/gpt-oss-120b",
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API_KEY"),
    temperature=0.2,
)


eligibility_agent = Agent(
    role="Student Eligibility Evaluator",

    goal=(
        "Evaluate whether a student meets the admission "
        "requirements of the provided university programs."
    ),

    backstory=(
        "You are an academic eligibility specialist. "
        "You compare the student's academic information "
        "with the provided admission requirements and "
        "clearly explain whether the student is eligible. "
        "Never invent requirements or student information."
    ),

    llm=llm,

    verbose=True,

    allow_delegation=False,
)
