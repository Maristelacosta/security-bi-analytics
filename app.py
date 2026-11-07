import streamlit as st
import pandas as pd
from google import genai
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente locais se houver
load_dotenv()

st.title("Central de Conformidade de Segurança e BI")

# Campo para o usuário inserir a chave de API na barra lateral ou tela principal
api_key = st.text_input("Insira sua GEMINI_API_KEY:", type="password")

if not api_key:
    st.warning("⚠️ Insira a sua chave de API do Gemini para liberar as ferramentas de análise.")
    st.stop()

# Inicializa o cliente moderno do Google GenAI corretamente
client = genai.Client(api_key=api_key)

# O restante do seu código para upload de CSV e auditoria continua aqui...
uploaded_file = st.file_uploader("Envie o relatório de logs ou acessos (CSV)", type="csv")
