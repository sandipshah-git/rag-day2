
import json
from pathlib import Path
from sentence_transformers import SentenceTransformer

# Load our recursive chunks
with open("recursive_chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Extract text from chunks
texts = [chunk["text"] for chunk in chunks]

# Generate embeddings
embeddings = model.encode(
    texts,
    show_progress_bar=True
)

# Prepare data for saving
embedded_chunks = []

for chunk, embedding in zip(chunks, embeddings):
    embedded_chunks.append({
        "text": chunk["text"],
        "metadata": chunk["metadata"],
        "embedding": embedding.tolist()
    })

# Save embeddings
Path("embedded_chunks.json").write_text(
    json.dumps(embedded_chunks, ensure_ascii=False, indent=4),
    encoding="utf-8"
)

print("\nEmbedding generation completed!")
print("Total chunks:", len(embedded_chunks))
print("Vector dimensions:", len(embedded_chunks[0]["embedding"]))
print("Saved to: embedded_chunks.json")
