from utils.ai_service import get_ai_response

def generate_career_roadmap(goal, current_level):
    prompt = f"""
    You are an experienced career mentor.

    Create a detailed career roadmap for a student.

    Career Goal:
    {goal}

    Current Level:
    {current_level}

    Include:

    1. Learning phases with timeline
    2. Important skills to learn
    3. Technologies and tools
    4. Projects to build
    5. Certifications (if useful)
    6. Internship/job preparation tips
    7. Common mistakes to avoid

    Make the roadmap practical, beginner-friendly,
    and well formatted with headings and bullet points.
    """

    roadmap = get_ai_response(prompt)

    return roadmap