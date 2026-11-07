import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.title("Central de Conformidade de Segurança e BI")

# Campo para o usuário inserir a chave de API na interface
api_key = st.text_input("Insira sua GEMINI_API_KEY:", type="password")

if not api_key:
    st.warning("⚠️ Insira a sua chave de API do Gemini para liberar as ferramentas de análise.")
    st.stop()

# Inicializa o cliente moderno do Google GenAI corretamente
client = genai.Client(api_key=api_key)

# Upload do arquivo CSV de logs
uploaded_file = st.file_uploader("Envie o relatório de logs ou acessos (CSV)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Arquivo carregado com sucesso!")
    st.dataframe(df)
    
    if st.button("🤖 Executar Auditoria de Segurança com IA"):
        with st.spinner("Analisando logs..."):
            prompt = f"Analise estes logs de segurança e aponte riscos:\n\n{df.to_string()}"
            
            response = client.models.generate_content(
                model='gemini-3.8-flash',
                contents=prompt
            )
            
            st.subheader("📊 Relatório de Auditoria da IA")
            st.write(response.text)
