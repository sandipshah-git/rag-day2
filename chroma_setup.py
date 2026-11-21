
import chromadb

# Create a persistent ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

# Create a collection
collection = client.get_or_create_collection(
    name="alice_book"
)

print("ChromaDB connected successfully!")
print("Collection created:", collection.name)
print("Total records:", collection.count())