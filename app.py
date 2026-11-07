import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.set_page_config(
    page_title="Security & BI Compliance Hub", 
    page_icon="🛡️", 
    layout="wide"
)

st.title("🛡️ Central de Conformidade de Segurança e BI")
st.subheader("Plataforma integrada de análise de logs, governança e detecção de riscos com IA")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = st.text_input("Insira sua GEMINI_API_KEY:", type="password")

if api_key:
    client = genai.Client(api_key=api_key)

    uploaded_file = st.file_uploader("Envie o relatório de logs ou acessos (CSV)", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("### 📊 Visão Geral dos Dados")
            st.dataframe(df.head())
        with col2:
            st.write("### 📈 Estatísticas Rápidas")
            st.write(f"- Total de Registros Analisados: {df.shape[0]}")
            st.write(f"- Atributos Monitorados: {df.shape[1]}")

        if st.button("🤖 Executar Auditoria de Segurança com IA"):
            with st.spinner("Analisando conformidade e riscos nos dados..."):
                dados_amostra = df.head(50).to_string()
                
                prompt = f"""
                Você é um Especialista Sênior em Governança de TI, Business Intelligence e Cibersegurança.
                Com base nos dados de auditoria e logs abaixo, faça uma análise crítica focada em:
                1. Riscos potenciais de vazamento de dados ou acessos indevidos.
                2. Indicadores operacionais relevantes para a tomada de decisão da diretoria.
                3. Recomendações práticas alinhadas às boas práticas de segurança da informação.

                Dados:
                {dados_amostra}
                """

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                st.markdown("### 🔍 Relatório Executivo de Auditoria & Segurança")
                st.markdown(response.text)
    else:
        st.info("💡 Por favor, faça o upload de um arquivo CSV para iniciar a auditoria.")
else:
    st.warning("⚠️ Insira a sua chave de API do Gemini para liberar as ferramentas de análise.")
