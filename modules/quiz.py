import json
from utils.gemini_api import get_ai_response


def generate_quiz(topic, difficulty, number_of_questions):

    prompt = f"""
    You are a professional teacher.

    Create a {difficulty} level multiple-choice quiz about {topic}.

    Generate exactly {number_of_questions} questions.

    Return ONLY valid JSON.
    Do not write any introduction or markdown.

    Use this exact format:

    [
      {{
        "question": "Question text",
        "options": {{
          "A": "Option A",
          "B": "Option B",
          "C": "Option C",
          "D": "Option D"
        }},
        "answer": "A",
        "explanation": "Short explanation"
      }}
    ]
    """

    response = get_ai_response(prompt)

    # Remove possible markdown formatting
    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        quiz_data = json.loads(response)
        return quiz_data

    except Exception:
        return None