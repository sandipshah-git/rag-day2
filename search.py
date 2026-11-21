
import chromadb
from sentence_transformers import SentenceTransformer

# Step 1: Connect to our existing database
client = chromadb.PersistentClient(path="./chroma_db")

# Step 2: Access our existing collection
collection = client.get_collection(name="alice_book")

# Step 3: Load the same embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 4: Ask a question
question = "Why was Alice curious about the White Rabbit?"

# Step 5: Convert question into an embedding
question_embedding = model.encode(question).tolist()

# Step 6: Search ChromaDB
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=5
)

# Step 7: Display results
print("\n===== SEARCH RESULTS =====")

for i in range(len(results["documents"][0])):

    print(f"\nResult {i + 1}")

    print("Document:")
    print(results["documents"][0][i])

    print("\nMetadata:")
    print(results["metadatas"][0][i])

    print("\nDistance:")
    print(results["distances"][0][i])

    print("-" * 60)
