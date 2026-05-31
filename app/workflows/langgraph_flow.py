from langgraph.graph import StateGraph, END

from app.workflows.lg_state import AgentState
from app.workflows.lg_nodes import (
    plan_node,
    research_node,
    summarize_node,
    factcheck_node,
    writer_node
)

# Create graph
graph = StateGraph(AgentState)

# Add nodes
graph.add_node("planner", plan_node)
graph.add_node("research", research_node)
graph.add_node("summarizer", summarize_node)
graph.add_node("factcheck", factcheck_node)
graph.add_node("writer", writer_node)

# Define flow (edges)
graph.set_entry_point("planner")

graph.add_edge("planner", "research")
graph.add_edge("research", "summarizer")
graph.add_edge("summarizer", "factcheck")
graph.add_edge("factcheck", "writer")
graph.add_edge("writer", END)

# Compile graph
app = graph.compile()