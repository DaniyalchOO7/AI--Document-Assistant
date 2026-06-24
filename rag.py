import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


# Split text into chunks
def split_text(text, chunk_size=200):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))

    return chunks


# Create vector index
def create_index(chunks):
    embeddings = model.encode(chunks)

    dim = len(embeddings[0])

    index = faiss.IndexFlatL2(dim)

    index.add(np.array(embeddings))

    return index, embeddings


# Search relevant chunks
def search(query, index, chunks, k=3):

    query_vec = model.encode([query])

    distances, indices = index.search(
        np.array(query_vec),
        k
    )

    results = [chunks[i] for i in indices[0]]

    return results