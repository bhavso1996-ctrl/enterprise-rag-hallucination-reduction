import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from openai import OpenAI

INDEX_PATH = "data/faiss_index/index.faiss"
DOCS_PATH = "data/faiss_index/docs.pkl"

THRESHOLD = 0.55   # similarity threshold
TOP_K = 5

# Load OpenAI client
client = OpenAI()

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index and documents
index = faiss.read_index(INDEX_PATH)

with open(DOCS_PATH, "rb") as f:
    documents = pickle.load(f)

def search_docs(question):
    # Convert question to vector
    query_vector = model.encode(question).astype("float32")
    query_vector = np.array([query_vector])

    # Search similar chunks
    scores, indices = index.search(query_vector, TOP_K)

    results = []
    for score, idx in zip(scores[0], indices[0]):
        similarity = 1 / (1 + score)

        if similarity >= THRESHOLD:
            results.append(documents[idx])

    return results

def ask_llm(question, context):
    prompt = f"""
You are a policy assistant.

Answer ONLY using the context below.
If the answer is not found, say:
"I don't know. The documents do not contain enough information."

Context:
{context}

Question:
{question}
"""

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    return response.output_text.strip()

def main():
    while True:
        question = input("Ask a question (or type 'exit'): ")
        if question.lower() == "exit":
            break

        context_chunks = search_docs(question)

        if not context_chunks:
            print("\nAnswer:")
            print("I don't know. The documents do not contain enough information.\n")
            continue

        context = "\n".join(context_chunks)
        answer = ask_llm(question, context)

        print("\nAnswer:")
        print(answer)
        print()

main()
