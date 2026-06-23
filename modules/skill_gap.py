from utils.gemini_api import get_gemini_response


def analyze_skill_gap(career_goal, current_skills):
    prompt = f"""
    You are an expert career coach.

    Analyze the student's current skills and compare them with the requirements for the target career.

    Target Career:
    {career_goal}

    Current Skills:
    {current_skills}

    Provide the following:

    1. Current strengths
    2. Missing skills and knowledge gaps
    3. Important tools and technologies to learn
    4. A step-by-step learning roadmap
    5. Project ideas to improve skills
    6. Advice for becoming job-ready

    Make your answer practical, motivating, and easy to understand.
    """

    analysis = get_gemini_response(prompt)

    return analysis