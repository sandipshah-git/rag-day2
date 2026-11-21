
import json
import chromadb

# Step 1: Load our embedded chunks
with open("embedded_chunks.json", "r", encoding="utf-8") as file:
    chunks = json.load(file)

# Step 2: Connect to our persistent database
client = chromadb.PersistentClient(path="./chroma_db")

# Step 3: Get our existing collection
collection = client.get_or_create_collection(
    name="alice_book"
)

# Step 4: Prepare data for ChromaDB
ids = []
documents = []
metadatas = []
embeddings = []

for chunk in chunks:
    ids.append(chunk["metadata"]["chunk_id"])
    documents.append(chunk["text"])
    metadatas.append(chunk["metadata"])
    embeddings.append(chunk["embedding"])

# Step 5: Insert or update records
collection.upsert(
    ids=ids,
    documents=documents,
    metadatas=metadatas,
    embeddings=embeddings
)

# Step 6: Verify insertion
print("Insertion completed successfully!")
print("Total records in ChromaDB:", collection.count())

# Display one stored record
result = collection.get(
    ids=["page_1_recursive_1"],
    include=["documents", "metadatas"]
)

print("\nFirst stored document:")
print(result["documents"][0][:300])

print("\nMetadata:")
print(result["metadatas"][0])
