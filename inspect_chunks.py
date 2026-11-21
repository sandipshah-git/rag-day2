
import json

# Load recursive chunks
with open("recursive_chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

print("Total chunks:", len(chunks))

# Inspect first 5 chunks
for chunk in chunks[:5]:

    print("\n" + "=" * 60)

    print("Chunk ID:", chunk["metadata"]["chunk_id"])
    print("Page:", chunk["metadata"]["page"])

    print("Character count:", len(chunk["text"]))

    print("\nContent:")
    print(chunk["text"])
