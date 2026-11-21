
import json
from statistics import mean

# Load recursive chunks
with open("recursive_chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

# Calculate character count of every chunk
lengths = [len(chunk["text"]) for chunk in chunks]

print("===== CHUNK QUALITY REPORT =====")

print("Total chunks:", len(chunks))
print("Average characters:", round(mean(lengths), 2))
print("Shortest chunk:", min(lengths))
print("Longest chunk:", max(lengths))

# Find chunks smaller than 200 characters
small_chunks = [
    chunk for chunk in chunks
    if len(chunk["text"]) < 200
]

print("\nChunks smaller than 200 characters:", len(small_chunks))

# Find chunks larger than 1000 characters
large_chunks = [
    chunk for chunk in chunks
    if len(chunk["text"]) > 1000
]

print("Chunks larger than 1000 characters:", len(large_chunks))

# Display the 5 shortest chunks
print("\n===== 5 SHORTEST CHUNKS =====")

shortest_chunks = sorted(chunks, key=lambda chunk: len(chunk["text"]))

for chunk in shortest_chunks[:5]:
    print("\nChunk ID:", chunk["metadata"]["chunk_id"])
    print("Characters:", len(chunk["text"]))
    print("Content:", chunk["text"][:200])
