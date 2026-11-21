
from sentence_transformers import SentenceTransformer, util

# Load our embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Three sentences
sentences = [
    "Alice followed the White Rabbit.",
    "The White Rabbit ran into a rabbit hole.",
    "Python is a programming language."
]

# Convert sentences into vectors
embeddings = model.encode(sentences)

# Compare sentence A with sentence B
similarity_ab = util.cos_sim(
    embeddings[0],
    embeddings[1]
)

# Compare sentence A with sentence C
similarity_ac = util.cos_sim(
    embeddings[0],
    embeddings[2]
)

print("Sentence A:", sentences[0])
print("Sentence B:", sentences[1])
print("Similarity A-B:", similarity_ab.item())

print("\nSentence A:", sentences[0])
print("Sentence C:", sentences[2])
print("Similarity A-C:", similarity_ac.item())
