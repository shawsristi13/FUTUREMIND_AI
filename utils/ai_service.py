import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def get_ai_response(prompt):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "FUTUREMIND AI",
        "Content-Type": "application/json"
    }

    # Supports normal prompts and chat history
    if isinstance(prompt, list):
        messages = prompt
    else:
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 800
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=30
        )

        response.raise_for_status()

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except requests.exceptions.Timeout:
        return "⚠️ AI is taking too long to respond. Please try again."

    except requests.exceptions.ConnectionError:
        return "⚠️ Internet connection problem. Please check your network."

    except Exception as e:
        return f"⚠️ AI service error:\n\n{str(e)}"