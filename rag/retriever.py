from rag.embeddings import generate_embedding
from rag.vector_store import search_embedding

def retrieve_context(question):
    query_embedding = generate_embedding(question)
    return search_embedding(query_embedding)
