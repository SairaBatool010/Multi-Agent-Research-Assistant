from app.agents.planner_agent import planner_agent
from app.agents.research_agent import research_agent
from app.agents.write_agent import writer_agent

def run(query):
    print("\n🧠 Planner running...")
    plan = planner_agent(query)

    print("\n🔎 Research running...")
    research = research_agent(query, plan)

    print("\n✍️ Writing report...")
    report = writer_agent(query, research)

    return report


if __name__ == "__main__":
    query = input("Enter topic: ")
    output = run(query)

    print("\n" + "="*60)
    print(output)