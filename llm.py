import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def generate_answer(question, context):
    prompt = f"""
You are an AI assistant.

Use ONLY the context below:

CONTEXT:
{context}

QUESTION:
{question}

If not found, say: "I don't know from the document."
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return "The AI model is currently busy or unavailable. Please try again in a few moments."