import streamlit as st
import tempfile

from pdf_loader import load_pdf
from rag import split_text
from llm import generate_answer


st.set_page_config(page_title="AI Doc Chat", layout="wide")

st.title("📄 AI Document Chatbot (RAG)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chunks" not in st.session_state:
    st.session_state.chunks = None


# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file and st.session_state.chunks is None:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    text = load_pdf(file_path)
    st.session_state.chunks = split_text(text)

    st.success("PDF processed! You can start chatting now.")


# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# User input
user_input = st.chat_input("Ask something about the document...")

if user_input and st.session_state.chunks:

    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # Get context (simple top chunks for now)
    context = "\n".join(st.session_state.chunks[:5])

    # Get AI response
    answer = generate_answer(user_input, context)

    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.write(answer)