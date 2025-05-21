from crewai import Task
from agents import crewai_agent, langchain_agent

# Tarefa para responder sobre CrewAI
crewai_task = Task(
    description="Responda perguntas sobre CrewAI, fornecendo explicações detalhadas, exemplos e contexto.",
    expected_output="Uma explicação clara, direta e bem estruturada sobre CrewAI.",
    agent=crewai_agent
)

# Tarefa para responder sobre LangChain
langchain_task = Task(
    description="Responda perguntas sobre LangChain, explicando seus componentes e funcionamento com LLMs.",
    expected_output="Uma explicação clara, didática e aprofundada sobre LangChain.",
    agent=langchain_agent
)