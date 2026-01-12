import os

# Folder that contains raw extracted text files
INPUT_DIR = "data/parsed_docs"

# Folder where cleaned text will be saved
OUTPUT_DIR = "data/cleaned_docs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Loop through each text file
for file_name in os.listdir(INPUT_DIR):
    if not file_name.endswith(".txt"):
        continue

    input_path = os.path.join(INPUT_DIR, file_name)
    output_path = os.path.join(OUTPUT_DIR, file_name)

    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Basic cleaning:
    # remove extra spaces and new lines
    text = text.replace("\n", " ")
    text = " ".join(text.split())

    # Save cleaned text
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

print("Text cleaning complete.")
