import streamlit as st
import tempfile

from pdf_loader import load_pdf
from rag import split_text
from llm import generate_answer


st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📄",
    layout="wide"
)

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chunks" not in st.session_state:
    st.session_state.chunks = None


# Sidebar
with st.sidebar:
    st.title("📄 AI Doc Assistant")
    st.write("Upload a PDF and chat with it.")

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            file_path = tmp.name

        text = load_pdf(file_path)
        st.session_state.chunks = split_text(text)
        st.success("Document uploaded successfully!")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()


# Main title
st.title("📄 AI Document Assistant")
st.caption("Upload PDFs and chat with your documents using AI")


# If no PDF uploaded
if st.session_state.chunks is None:
    st.info("Upload a PDF from the sidebar to start.")

else:
    # Quick Actions
    st.markdown("### Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:
        summarize_btn = st.button("📄 Summarize")

    with col2:
        explain_btn = st.button("🧠 Explain Simply")

    with col3:
        flashcards_btn = st.button("📝 Flashcards")

    full_context = "\n".join(st.session_state.chunks[:8])

    if summarize_btn:
        answer = generate_answer(
            "Summarize this document in clear bullet points.",
            full_context
        )

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        st.rerun()

    if explain_btn:
        answer = generate_answer(
            "Explain this document in simple beginner-friendly language.",
            full_context
        )

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        st.rerun()

    if flashcards_btn:
        answer = generate_answer(
            "Create 10 flashcards from this document in Question and Answer format.",
            full_context
        )

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        st.rerun()

    # Chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    user_input = st.chat_input("Ask something about your document...")

    if user_input:
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        context = "\n".join(st.session_state.chunks[:5])

        answer = generate_answer(user_input, context)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        st.rerun()