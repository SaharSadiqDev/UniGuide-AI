from crewai import Crew, Task, Process

from agents.requirements_agent import requirements_agent
from agents.eligibility_agent import eligibility_agent
from agents.recommendation_agent import recommendation_agent


def run_admission_system(student_profile, university_data):

    # Requirements Agent Task
    requirements_task = Task(
        description=f"""
        Analyze the university and program information.

        Student Profile:
        {student_profile}

        University Data:
        {university_data}

        Identify and explain the admission requirements
        for the relevant programs.

        Include:
        - Minimum academic percentage
        - Entry test requirements
        - Required subjects
        - Other stated requirements

        Use only the provided information.
        Do not invent requirements.
        """,

        expected_output=(
            "A clear explanation of the admission requirements "
            "for the relevant programs."
        ),

        agent=requirements_agent,
    )


    # Eligibility Agent Task
    eligibility_task = Task(
        description=f"""
        Evaluate the student's eligibility for the available programs.

        Student Profile:
        {student_profile}

        University Data:
        {university_data}

        Compare the student's academic information with
        the provided requirements.

        For each relevant program, explain whether the student is:

        - Eligible
        - Not Eligible
        - Missing Information

        Explain the reason.

        Use only the provided information.
        Do not invent requirements.
        """,

        expected_output=(
            "A clear eligibility assessment for each relevant program."
        ),

        agent=eligibility_agent,
    )


    # Recommendation Agent Task
    recommendation_task = Task(
        description=f"""
        Recommend suitable university programs for the student.

        Student Profile:
        {student_profile}

        University Data:
        {university_data}

        Consider:
        - Academic background
        - Desired field
        - Interests
        - Budget
        - Preferred city

        Recommend programs only from the provided university data.

        Explain briefly why each program is suitable.
        """,

        expected_output=(
            "A list of suitable university programs with reasons."
        ),

        agent=recommendation_agent,
    )


    # Create Crew
    admission_crew = Crew(
        agents=[
            requirements_agent,
            eligibility_agent,
            recommendation_agent,
        ],

        tasks=[
            requirements_task,
            eligibility_task,
            recommendation_task,
        ],

        process=Process.parallel,

        verbose=True,
    )


    # Run all agents
    result = admission_crew.kickoff()

    return result
