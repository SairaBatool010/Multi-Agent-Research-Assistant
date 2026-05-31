from app.workflows.llm import OllamaLLM

llm = OllamaLLM()

def planner_agent(query):
    prompt = f"""
You are a research planner.

Break this task into steps:

{query}

Return bullet points only.
"""
    return llm.generate(prompt)