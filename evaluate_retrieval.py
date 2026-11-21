
import chromadb
from sentence_transformers import SentenceTransformer

# Step 1: Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="alice_book")

# Step 2: Load the same embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Step 3: Create a small evaluation dataset
test_cases = [
    {
        "question": "Why was Alice curious about the White Rabbit?",
        "relevant_chunk_ids": ["page_3_recursive_1"]
    }
]

# Step 4: Set Top-K
K = 5

# Step 5: Evaluate retrieval
for test in test_cases:

    question = test["question"]
    relevant_ids = set(test["relevant_chunk_ids"])

    # Convert question into embedding
    question_embedding = model.encode(question).tolist()

    # Retrieve top K chunks
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=K
    )

    retrieved_ids = results["ids"][0]

    # Calculate relevant retrieved chunks
    relevant_retrieved = set(retrieved_ids) & relevant_ids

    # Calculate Precision@K
    precision = len(relevant_retrieved) / len(retrieved_ids)

    # Calculate Recall@K
    recall = len(relevant_retrieved) / len(relevant_ids)

    print("\n===== RETRIEVAL EVALUATION =====")
    print("Question:", question)
    print("Retrieved chunks:", retrieved_ids)
    print("Relevant retrieved:", list(relevant_retrieved))
    print("Precision@K:", round(precision, 2))
    print("Recall@K:", round(recall, 2))
