from app.workflows.llm import OllamaLLM

llm = OllamaLLM()

def fact_checker_agent(query, notes):
    prompt = f"""
You are a strict fact-checking agent.

Task:
- Identify incorrect or unsupported claims
- Remove hallucinations
- Keep only reliable statements

Topic:
{query}

Notes:
{notes}

Return corrected verified notes only.
"""
    return llm.generate(prompt)