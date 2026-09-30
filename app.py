import streamlit as st

from program import run_admission_system


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="UniGuide AI",
    page_icon="🎓",
    layout="wide",
)


# -----------------------------
# App Title
# -----------------------------

st.title("🎓 UniGuide AI")

st.write(
    "A simple multi-agent university admission assistant "
    "powered by CrewAI and Groq."
)


# -----------------------------
# Student Information
# -----------------------------

st.header("Student Information")


col1, col2 = st.columns(2)


with col1:

    student_name = st.text_input(
        "Student Name",
        placeholder="Enter your name"
    )

    intermediate_percentage = st.number_input(
        "Intermediate / A-Level Percentage",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=0.1,
    )

    entry_test_percentage = st.number_input(
        "Entry Test Percentage",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        step=0.1,
    )


with col2:

    desired_field = st.text_input(
        "Desired Field",
        placeholder="Computer Science"
    )

    interests = st.text_input(
        "Interests",
        placeholder="AI, Programming, Software Development"
    )

    preferred_city = st.text_input(
        "Preferred City",
        placeholder="Lahore"
    )


annual_budget = st.number_input(
    "Annual Budget (PKR)",
    min_value=0,
    value=200000,
    step=10000,
)


# -----------------------------
# Demo University Data
# -----------------------------

university_data = """
University: Demo Technology University

Program 1:
BS Computer Science

Minimum Intermediate Percentage: 60%
Minimum Entry Test Percentage: 50%
Required Subject: Mathematics
Annual Fee: 180000 PKR
City: Lahore


Program 2:
BS Software Engineering

Minimum Intermediate Percentage: 60%
Minimum Entry Test Percentage: 50%
Required Subject: Mathematics
Annual Fee: 180000 PKR
City: Lahore


Program 3:
BS Artificial Intelligence

Minimum Intermediate Percentage: 65%
Minimum Entry Test Percentage: 55%
Required Subject: Mathematics
Annual Fee: 220000 PKR
City: Islamabad
"""


# -----------------------------
# Student Profile
# -----------------------------

student_profile = f"""
Student Name:
{student_name}

Intermediate / A-Level Percentage:
{intermediate_percentage}%

Entry Test Percentage:
{entry_test_percentage}%

Desired Field:
{desired_field}

Interests:
{interests}

Preferred City:
{preferred_city}

Annual Budget:
{annual_budget} PKR
"""


# -----------------------------
# Analyze Button
# -----------------------------

if st.button(
    "🔍 Analyze Admission Options",
    type="primary",
):

    if not student_name:
        st.warning("Please enter your name.")

    elif not desired_field:
        st.warning("Please enter your desired field.")

    else:

        with st.spinner(
            "Three AI agents are analyzing your profile..."
        ):

            try:

                result = run_admission_system(
                    student_profile,
                    university_data,
                )

                st.success(
                    "Admission analysis completed!"
                )

                st.header("📋 Admission Analysis")

                st.write(result)

            except Exception as error:

                st.error(
                    "An error occurred while running the AI agents."
                )

                st.exception(error)
