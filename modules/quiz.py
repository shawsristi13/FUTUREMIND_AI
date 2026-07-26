import json
from utils.ai_service import get_ai_response


def generate_quiz(topic, difficulty, number_of_questions):

    prompt = f"""
You are an expert quiz generator.

Generate EXACTLY {number_of_questions} multiple-choice questions about "{topic}".

Difficulty: {difficulty}

IMPORTANT RULES:

- Return ONLY a valid JSON array.
- Do NOT return markdown.
- Do NOT write ```json
- Do NOT write any introduction.
- Do NOT write any conclusion.
- Every question must contain exactly 4 options.
- Answer must be only A, B, C or D.
- Keep explanations under 20 words.
- Keep questions concise.

Return this format ONLY:

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

    if response.startswith("⚠️"):
        return None

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        quiz_data = json.loads(response)

        if not isinstance(quiz_data, list):
            return None

        if len(quiz_data) != number_of_questions:
            return None

        return quiz_data

    except Exception as e:
        print("\n========== QUIZ JSON ERROR ==========")
        print(e)
        print("\n========== AI RESPONSE ==========")
        print(response)
        print("====================================\n")

        return None