import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

CHUNK_DIR = "data/chunks"
INDEX_DIR = "data/faiss_index"

os.makedirs(INDEX_DIR, exist_ok=True)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

texts = []
embeddings = []

# Read all chunk files
for file_name in os.listdir(CHUNK_DIR):
    with open(os.path.join(CHUNK_DIR, file_name), "r", encoding="utf-8") as f:
        text = f.read()
        texts.append(text)

        # Convert text into vector
        vector = model.encode(text)
        embeddings.append(vector)

# Convert list to numpy array
embedding_array = np.array(embeddings).astype("float32")

# Create FAISS index
index = faiss.IndexFlatL2(embedding_array.shape[1])
index.add(embedding_array)

# Save index and documents
faiss.write_index(index, os.path.join(INDEX_DIR, "index.faiss"))

with open(os.path.join(INDEX_DIR, "docs.pkl"), "wb") as f:
    pickle.dump(texts, f)

print("FAISS index created successfully.")
