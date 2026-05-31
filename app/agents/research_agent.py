from app.workflows.llm import OllamaLLM
from app.tools.wikipedia_tool import search_wikipedia
from app.tools.arxiv_tool import search_arxiv
from app.tools.web_search_tool import web_search

llm = OllamaLLM()

def research_agent(query, plan):

    wiki_data = search_wikipedia(query)
    web_data = web_search(query)
    papers = search_arxiv(query)

    prompt = f"""
You are a research agent.

TASK:
{query}

PLAN:
{plan}

WIKIPEDIA:
{wiki_data}

WEB RESULTS:
{web_data}

ARXIV PAPERS:
{papers}

Now synthesize all information into structured research notes.
"""

    return llm.generate(prompt)