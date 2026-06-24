from utils.ai_service import get_ai_response


def generate_interview(role, experience_level):
    prompt = f"""
    You are an expert technical interviewer.

    Create a realistic mock interview for the following candidate.

    Job Role:
    {role}

    Experience Level:
    {experience_level}

    Include:

    1. Introduction of the interview
    2. 5 technical questions
    3. 3 HR questions
    4. 2 problem-solving questions
    5. Tips to improve interview performance

    Make the questions practical, realistic, and suitable for the candidate's experience level.
    """

    interview = get_ai_response(prompt)

    return interview