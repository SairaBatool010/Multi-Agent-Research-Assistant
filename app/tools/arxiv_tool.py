import arxiv

def search_arxiv(query, max_results=3):
    client = arxiv.Client()

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    papers = []

    # IMPORTANT: v4 uses client.results()
    for result in client.results(search):
        papers.append({
            "title": result.title,
            "summary": result.summary
        })

    return papers