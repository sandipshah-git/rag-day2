
import json
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter


# STEP 1: Load our existing PDF data

input_file = Path("documents.json")

documents = json.loads(
    input_file.read_text(encoding="utf-8")
)


# STEP 2: Configure recursive splitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150,
    separators=["\n\n", "\n", " ", ""]
)


# STEP 3: Create lists for our chunks

fixed_chunks = []
recursive_chunks = []


# STEP 4: Process each PDF page

for document in documents:

    text = document["text"]
    metadata = document["metadata"]

    if not text.strip():
        continue

    # Fixed-size chunking
    fixed_parts = []

    start = 0
    chunk_size = 1000
    overlap = 150

    while start < len(text):

        end = start + chunk_size

        chunk_text = text[start:end]

        fixed_parts.append(chunk_text)

        start += chunk_size - overlap

    for i, part in enumerate(fixed_parts, start=1):

        fixed_chunks.append({
            "text": part,
            "metadata": {
                **metadata,
                "chunk_id": f"page_{metadata['page']}_fixed_{i}"
            }
        })


    # Recursive character splitting
    recursive_parts = splitter.split_text(text)

    for i, part in enumerate(recursive_parts, start=1):

        recursive_chunks.append({
            "text": part,
            "metadata": {
                **metadata,
                "chunk_id": f"page_{metadata['page']}_recursive_{i}"
            }
        })


# STEP 5: Save both results

Path("fixed_chunks.json").write_text(
    json.dumps(fixed_chunks, indent=4, ensure_ascii=False),
    encoding="utf-8"
)

Path("recursive_chunks.json").write_text(
    json.dumps(recursive_chunks, indent=4, ensure_ascii=False),
    encoding="utf-8"
)


# STEP 6: Display results

print("Chunking completed successfully!")

print("Original PDF pages:", len(documents))
print("Fixed-size chunks:", len(fixed_chunks))
print("Recursive chunks:", len(recursive_chunks))

print("\nFirst recursive chunk:")
print(recursive_chunks[0]["text"])

print("\nMetadata:")
print(recursive_chunks[0]["metadata"])
