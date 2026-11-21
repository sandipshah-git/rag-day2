import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("alice_book")

print("Collection configuration:")
print(collection.configuration)