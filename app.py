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

st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}
.card {
    padding: 25px;
    border-radius: 18px;
    background: white;
    box-shadow: 0 4px 20px rgba(0,0,0,0.06);
    border: 1px solid #eee;
}
.hero {
    padding: 35px;
    border-radius: 25px;
    background: linear-gradient(135deg, #f4f0ff, #ffffff);
    margin-bottom: 25px;
}
.action-card {
    padding: 22px;
    border-radius: 18px;
    background: white;
    border: 1px solid #e5e7eb;
    text-align: center;
    box-shadow: 0 4px 14px rgba(0,0,0,0.04);
}
.small {
    color: #6b7280;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chunks" not in st.session_state:
    st.session_state.chunks = None

with st.sidebar:
    st.markdown("## 🤖 AI Doc Assistant")
    st.caption("Upload a PDF and chat with it.")

    uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            file_path = tmp.name

        text = load_pdf(file_path)
        st.session_state.chunks = split_text(text)

        st.success("Document uploaded successfully!")
        st.info(f"File: {uploaded_file.name}")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("### About")
    st.caption("Built with Streamlit, Gemini AI, Python, and RAG concepts.")

st.markdown("""
<div class="hero">
<h1>📄 AI Document Assistant</h1>
<p>Upload PDFs and let AI help you understand, summarize, and study smarter.</p>
</div>
""", unsafe_allow_html=True)

if st.session_state.chunks is None:
    st.info("Upload a PDF from the sidebar to start.")
else:
    st.markdown("## ⚡ Quick Actions")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        summarize_btn = st.button("📄 Summarize", use_container_width=True)

    with col2:
        explain_btn = st.button("🧠 Explain Simply", use_container_width=True)

    with col3:
        flashcards_btn = st.button("📝 Flashcards", use_container_width=True)

    with col4:
        keypoints_btn = st.button("🎯 Key Takeaways", use_container_width=True)

    full_context = "\n".join(st.session_state.chunks[:3])

    if summarize_btn:
        answer = generate_answer("Summarize this document in bullet points.", full_context)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun()

    if explain_btn:
        answer = generate_answer("Explain this document in simple beginner-friendly language.", full_context)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun()

    if flashcards_btn:
        answer = generate_answer("Create 10 flashcards from this document in Q&A format.", full_context)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun()

    if keypoints_btn:
        answer = generate_answer("List the most important key takeaways from this document.", full_context)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun()

    st.markdown("---")
    st.markdown("## 💬 Chat with your document")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_input = st.chat_input("Ask something about your document...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        context = "\n".join(st.session_state.chunks[:2])
        answer = generate_answer(user_input, context)

        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun()

st.markdown("---")
st.caption("Built by Daniyal Munir • AI Document Assistant")