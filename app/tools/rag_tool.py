from app.rag.retriever import search_documents


def rag_search(query):

    docs = search_documents(query)

    if not docs:
        return "No relevant documents found."

    context = []

    for doc in docs:

        source = doc.metadata.get(
            "source",
            "Unknown PDF"
        )

        context.append(
            f"Source: {source}\n{doc.page_content}"
        )

    return "\n\n".join(context)