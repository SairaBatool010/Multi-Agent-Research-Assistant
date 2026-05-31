from app.workflows.llm import OllamaLLM

llm = OllamaLLM()

def writer_agent(query, research_notes):
    prompt = f"""
You are a report writer.

Topic:
{query}

Notes:
{research_notes}

Write a professional report with:
- Summary
- Key Points
- Conclusion
"""
    return llm.generate(prompt)