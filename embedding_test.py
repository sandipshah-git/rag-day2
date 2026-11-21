
from sentence_transformers import SentenceTransformer

# Load an embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample text
sentences = [
    "Alice followed the White Rabbit.",
    "The White Rabbit ran into a rabbit hole.",
    "Python is a programming language."
]

# Convert text into numerical vectors
embeddings = model.encode(sentences)

# Display results
print("Number of sentences:", len(sentences))
print("Embedding shape:", embeddings.shape)

print("\nFirst sentence:")
print(sentences[0])

print("\nIts embedding:")
print(embeddings[0])

print("\nVector dimensions:")
print(len(embeddings[0]))
