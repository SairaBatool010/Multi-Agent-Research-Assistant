from app.agents.planner_agent import planner_agent
from app.agents.research_agent import research_agent
from app.agents.summarizer_agent import summarizer_agent
from app.agents.fact_checker_agent import fact_checker_agent
from app.agents.write_agent import writer_agent

def run(query):

    print("\n🧠 Planner running...")
    plan = planner_agent(query)

    print("\n🔎 Research running...")
    raw_research = research_agent(query, plan)

    print("\n🧹 Summarizing...")
    summary = summarizer_agent(query, raw_research)

    print("\n🛡️ Fact-checking...")
    verified = fact_checker_agent(query, summary)

    print("\n✍️ Writing report...")
    report = writer_agent(query, verified)

    return report


if __name__ == "__main__":
    query = input("Enter topic: ")
    output = run(query)

    print("\n" + "="*60)
    print(output)