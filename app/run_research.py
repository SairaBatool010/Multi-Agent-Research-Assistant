from app.workflows.langgraph_flow import app


def generate_report(query):

    result = app.invoke({
        "query": query,
        "plan": "",
        "research": "",
        "summary": "",
        "verified": "",
        "report": ""
    })

    return result["report"]