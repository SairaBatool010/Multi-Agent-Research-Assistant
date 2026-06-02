from app.workflows.llm import OllamaLLM

from app.tools.wikipedia_tool import search_wikipedia
from app.tools.web_search_tool import web_search
from app.tools.arxiv_tool import search_arxiv
from app.tools.rag_tool import rag_search

llm = OllamaLLM()
def research_agent(query, plan):

    tool_prompt = f"""
You are a tool routing agent.

QUERY:
{query}

PLAN:
{plan}

Available tools:
- wikipedia
- web
- arxiv
- pdf

Return only tool names.
"""

    tool_decision = llm.generate(tool_prompt)

    wiki_data = ""
    web_data = ""
    papers = ""
    pdf_results = ""

    if "wikipedia" in tool_decision.lower():
        wiki_data = search_wikipedia(query)

    if "web" in tool_decision.lower():
        web_data = web_search(query)

    try:
        if "pdf" in tool_decision.lower():
            pdf_results = rag_search(query)
    except Exception:
        pdf_results = ""

    synthesis_prompt = f"""
You are a research synthesis agent.

QUESTION:
{query}

PLAN:
{plan}

PDF DOCUMENTS:
{pdf_results}

WIKIPEDIA:
{wiki_data}

WEB:
{web_data}

ARXIV:
{papers}

Create comprehensive structured research notes.

Sections:
1. Key Findings
2. Supporting Evidence
3. Important Facts
4. Sources Summary
"""

    return llm.generate(synthesis_prompt)



#    if "arxiv" in tool_decision.lower():
#        papers = search_arxiv(query)
#ARXIV:
#{papers}