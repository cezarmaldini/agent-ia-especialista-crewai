from crewai import Crew
from agents import crewai_agent, langchain_agent
from tasks import crewai_task, langchain_task

def criar_crew(pergunta: str):
    if "langchain" in pergunta.lower():
        return Crew(
            agents=[langchain_agent],
            tasks=[langchain_task],
            verbose=True
        )
    else:
        return Crew(
            agents=[crewai_agent],
            tasks=[crewai_task],
            verbose=True
        )