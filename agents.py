import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from crewai import Agent

# Carrega as variáveis do .env
load_dotenv()

# Inicializa a LLM com a chave do ambiente
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Agente para CrewAI
crewai_agent = Agent(
    role="Especialista em CrewAI",
    goal="Ensinar sobre a ferramenta CrewAI",
    backstory="Você é um expert em CrewAI e ajuda pessoas a entenderem como ela funciona.",
    verbose=True,
    llm=llm
)

# Agente para LangChain
langchain_agent = Agent(
    role="Especialista em LangChain",
    goal="Ensinar sobre a biblioteca LangChain",
    backstory="Você é um expert em LangChain e está sempre pronto para ensinar seus conceitos e aplicações.",
    verbose=True,
    llm=llm
)