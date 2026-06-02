from langchain_chroma import Chroma

DB_PATH = "chroma_db"


def create_vector_db(chunks, embeddings):

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH
    )

    return db


def load_vector_db(embeddings):

    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )


def add_documents(chunks, embeddings):

    db = load_vector_db(embeddings)

    db.add_documents(chunks)

    return db