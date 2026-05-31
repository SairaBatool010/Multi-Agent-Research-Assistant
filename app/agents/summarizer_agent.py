from app.workflows.llm import OllamaLLM

llm = OllamaLLM()

def summarizer_agent(query, raw_research):
    prompt = f"""
You are a summarization agent.

Your job:
- Remove noise
- Keep only key technical facts
- Structure clearly

Topic:
{query}

Raw Research:
{raw_research}

Return clean bullet-point notes.
"""
    return llm.generate(prompt)