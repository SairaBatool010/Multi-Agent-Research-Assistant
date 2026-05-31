from app.agents.planner_agent import planner_agent
from app.agents.research_agent import research_agent
from app.agents.summarizer_agent import summarizer_agent
from app.agents.fact_checker_agent import fact_checker_agent
from app.agents.write_agent import writer_agent


def plan_node(state):
    state["plan"] = planner_agent(state["query"])
    return state


def research_node(state):
    state["research"] = research_agent(state["query"], state["plan"])
    return state


def summarize_node(state):
    state["summary"] = summarizer_agent(state["query"], state["research"])
    return state


def factcheck_node(state):
    state["verified"] = fact_checker_agent(state["query"], state["summary"])
    return state


def writer_node(state):
    state["report"] = writer_agent(state["query"], state["verified"])
    return state