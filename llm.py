import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

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

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text