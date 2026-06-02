from app.rag.embeddings import get_embeddings
from app.rag.vectordb import load_vector_db

def search_documents(query):

    embeddings = get_embeddings()

    db = load_vector_db(embeddings)

    docs = db.similarity_search(
        query,
        k=5
    )

    return docs