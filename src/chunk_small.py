import os

INPUT_DIR = "data/cleaned_docs"
OUTPUT_DIR = "data/chunks"

os.makedirs(OUTPUT_DIR, exist_ok=True)

CHUNK_SIZE = 150  # approx words per chunk

for file_name in os.listdir(INPUT_DIR):
    if not file_name.endswith(".txt"):
        continue

    with open(os.path.join(INPUT_DIR, file_name), "r", encoding="utf-8") as f:
        words = f.read().split()

    chunk_count = 0

    for i in range(0, len(words), CHUNK_SIZE):
        chunk_words = words[i:i + CHUNK_SIZE]
        chunk_text = " ".join(chunk_words)

        chunk_file = f"{file_name}_chunk_{chunk_count}.txt"
        chunk_path = os.path.join(OUTPUT_DIR, chunk_file)

        with open(chunk_path, "w", encoding="utf-8") as f:
            f.write(chunk_text)

        chunk_count += 1

print("150-word chunking complete.")
