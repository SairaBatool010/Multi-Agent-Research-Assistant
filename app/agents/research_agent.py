from app.workflows.llm import OllamaLLM
from app.tools.wikipedia_tool import search_wikipedia
from app.tools.arxiv_tool import search_arxiv
from app.tools.web_search_tool import web_search

llm = OllamaLLM()

def research_agent(query, plan):

    # Step 1: Decide which tools to use
    tool_prompt = f"""
You are a tool routing agent.

Given this query:
{query}

Decide which tools to use:
- wikipedia
- web
- arxiv

Return only tool names as a list.
"""

    tool_decision = llm.generate(tool_prompt)

    wiki_data = ""
    web_data = ""
    papers = ""

    # Step 2: Conditional tool execution
    if "wikipedia" in tool_decision.lower():
        wiki_data = search_wikipedia(query)

    if "web" in tool_decision.lower():
        web_data = web_search(query)

    if "arxiv" in tool_decision.lower():
        papers = search_arxiv(query)

    # Step 3: Synthesis
    prompt = f"""
You are a research synthesis agent.

QUERY:
{query}

PLAN:
{plan}

WIKIPEDIA:
{wiki_data}

WEB:
{web_data}

ARXIV:
{papers}

Create structured research notes.
"""

    return llm.generate(prompt)