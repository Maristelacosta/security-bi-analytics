"""Central de Conformidade de Segurança e BI.

Esta aplicação carrega logs de segurança em CSV, apresenta os dados em uma
interface Streamlit e usa a API do Gemini para gerar um relatório de auditoria
com riscos, severidade, evidências e recomendações de correção.
"""

import os

import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()


st.set_page_config(page_title="Central de Conformidade", page_icon="🛡️")
st.title("Central de Conformidade de Segurança e BI")


# Campo para o usuário inserir a chave da API do Gemini.
# A chave deve ser armazenada em variáveis de ambiente ou no arquivo .env.
api_key = st.text_input("Insira sua GEMINI_API_KEY:", type="password")

if not api_key:
    st.warning("⚠️ Insira a sua chave de API do Gemini para liberar as ferramentas de análise.")
    st.stop()

# Configura o cliente do SDK do Gemini.
genai.configure(api_key=api_key)


# Upload do arquivo CSV contendo logs de segurança e acessos.
uploaded_file = st.file_uploader(
    "Envie o relatório de logs ou acessos (CSV)",
    type="csv",
)


def build_security_audit_prompt(df: pd.DataFrame) -> str:
    """Cria um prompt estruturado para a IA analisar riscos de segurança nos logs."""
    return (
        "Você é um analista de segurança cibernética e compliance. "
        "Analise os registros abaixo e responda em português com:\n"
        "1. Resumo executivo;\n"
        "2. Riscos e anomalias detectados;\n"
        "3. Severidade de cada evento (baixo, médio, alto, crítico);\n"
        "4. Evidências baseadas nos dados fornecidos;\n"
        "5. Impacto operacional e de conformidade;\n"
        "6. Recomendações acionáveis para mitigação;\n\n"
        "Dados de entrada:\n"
        f"{df.to_string(index=False)}"
    )


if uploaded_file is not None:
    # Lê o CSV usando o padrão mais comum para registros separados por vírgula.
    df = pd.read_csv(uploaded_file)

    # Normaliza nomes de colunas para facilitar a análise e reduzir ruído.
    normalized_columns = {
        "carimbo de data/hora": "timestamp",
        "carimbo_de_data_hora": "timestamp",
        "timestamp": "timestamp",
        "usuário": "usuario",
        "usuario": "usuario",
        "tipo_de_ação": "tipo_acao",
        "tipo_de_acao": "tipo_acao",
        "tipo de ação": "tipo_acao",
        "tipo_acao": "tipo_acao",
        "endereço_ip": "endereco_ip",
        "endereco_ip": "endereco_ip",
        "http_status": "http_status",
        "status_http": "http_status",
    }
    df.columns = [normalized_columns.get(str(col).strip().lower(), str(col).strip()) for col in df.columns]

    st.success("Arquivo carregado com sucesso!")
    st.dataframe(df)

    if st.button("🤖 Executar Auditoria de Segurança com IA"):
        with st.spinner("Analisando logs..."):
            prompt = build_security_audit_prompt(df)

            # Utiliza o modelo Gemini suportado pelo SDK do Google GenAI.
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)

            st.subheader("📊 Relatório de Auditoria da IA")
            st.write(response.text)
