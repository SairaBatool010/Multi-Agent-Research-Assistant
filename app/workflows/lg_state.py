from typing import TypedDict

class AgentState(TypedDict):
    query: str
    plan: str
    research: str
    summary: str
    verified: str
    report: str