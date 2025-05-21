import streamlit as st
from crew import criar_crew
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

st.set_page_config(page_title="Chatbot de Estudo", page_icon="🤖")
st.title("🤖 Chatbot de Estudo")
st.markdown("<p>Pergunte algo sobre <b>CrewAI</b> ou <b>LangChain</b></p>", unsafe_allow_html=True)

pergunta = st.chat_input("Faça sua pergunta...")

if pergunta:
    with st.chat_message("user"):
        st.markdown(pergunta)

    try:
        crew = criar_crew(pergunta)
        resposta = resposta = crew.kickoff()

        with st.chat_message("assistant"):
            st.markdown(resposta)

    except Exception as e:
        st.error(f"Erro: {e}")