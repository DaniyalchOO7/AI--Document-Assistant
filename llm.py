import streamlit as st
from google import genai

api_key = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)


def generate_answer(question, context):

    prompt = f"""
Use ONLY the context below.

Context:
{context}

Question:
{question}

Answer clearly:
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Gemini error: {e}"
