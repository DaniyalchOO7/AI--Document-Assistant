AI Document Assistant (RAG Chatbot)
🚀 Overview

AI Document Assistant is a ChatGPT-style RAG (Retrieval-Augmented Generation) chatbot that allows users to upload PDF documents and ask questions about them in natural language.

The system extracts text from documents, splits it into chunks, and uses an LLM (Google Gemini) to generate context-aware answers based only on the uploaded content.

✨ Features
📄 Upload PDF documents
💬 ChatGPT-style conversational UI
🧠 Retrieval-Augmented Generation (RAG)
🔎 Context-aware question answering
⚡ Fast responses using Google Gemini API
🗂️ Automatic text extraction from PDFs
🧩 Chunk-based document processing
🛠️ Tech Stack
Python
Streamlit
Google Gemini API
Natural Language Processing (NLP)
RAG (Retrieval-Augmented Generation)
PyPDF / PDF text extraction
Basic vector-style chunk retrieval
📁 Project Structure
ai-doc-assistant/
│
├── app.py              # Streamlit frontend (Chat UI)
├── llm.py              # Gemini LLM integration
├── pdf_loader.py      # PDF text extraction
├── rag.py             # Text chunking logic
├── requirements.txt   # Dependencies
└── .gitignore
⚙️ How It Works
User uploads a PDF document
Text is extracted from the file
Document is split into chunks
User asks a question
Relevant context is passed to Gemini LLM
AI generates an answer based only on document content
▶️ Run Locally
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-doc-assistant.git
cd ai-doc-assistant
2. Install dependencies
pip install -r requirements.txt
3. Add API key

Create a .env file:

GEMINI_API_KEY=your_api_key_here
4. Run the app
streamlit run app.py
🔐 Environment Variables

This project requires a Google Gemini API key:

GEMINI_API_KEY=your_api_key_here
📌 Future Improvements
🔍 FAISS-based semantic search (advanced RAG)
📚 Multi-document support
🧾 Citation highlighting in answers
💾 Chat history storage per user
🔐 Authentication system (Firebase)
🌐 Full web deployment (Vercel / AWS)
💡 Use Cases
Study notes assistant
Research paper Q&A
Exam preparation tool
Legal/financial document analysis
AI-powered document search tool
👨‍💻 Author

Daniyal Munir
Computer Science (AI Concentration)
University of Massachusetts Dartmouth

⭐ Note

This project is built for learning and portfolio purposes and demonstrates real-world applications of LLMs and RAG systems.