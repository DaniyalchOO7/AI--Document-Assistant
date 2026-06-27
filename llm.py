import streamlit as st
from google import genai

api_key = st.secrets["GEMINI_API_KEY"]

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

    except   Exception as e:
        return f"Gemini error: {e}"