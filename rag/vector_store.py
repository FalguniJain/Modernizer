import faiss
import numpy as np

index = faiss.IndexFlatL2(384)
documents = []

def store_embedding(embedding, text):
    index.add(np.array([embedding]))
    documents.append(text)

def search_embedding(query_embedding, k=1):
    D, I = index.search(np.array([query_embedding]), k)
    return [documents[i] for i in I[0]]
