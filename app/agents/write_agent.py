from app.workflows.llm import OllamaLLM

llm = OllamaLLM()

def writer_agent(query, verified_notes):
    prompt = f"""
You are a professional report writer.

Write a structured research report.

Topic:
{query}

Verified Notes:
{verified_notes}

Format:
1. Summary
2. Key Findings
3. Analysis
4. Conclusion
"""
    return llm.generate(prompt)