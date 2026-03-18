from sentence_transformers import SentenceTransformer
import numpy as np

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Read data from file
with open("data.txt", "r") as f:
    docs = f.readlines()

docs = [doc.strip() for doc in docs]

# Convert to embeddings
doc_embeddings = model.encode(docs)

def search(query):
    query_embedding = model.encode([query])[0]
    scores = np.dot(doc_embeddings, query_embedding)
    return docs[np.argmax(scores)]

# Chat loop
while True:
    query = input("Ask: ")
    result = search(query)
    print("Answer:", result)