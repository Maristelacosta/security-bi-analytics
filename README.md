# 🛡️ Security & BI Compliance Hub

Uma aplicação interativa desenvolvida em Python e Streamlit que une **Business Intelligence (BI)**, **Cibersegurança** e **Inteligência Artificial (Google Gemini API)** para realizar auditoria de acessos, análise de conformidade de dados e detecção de anomalias em tempo real.

---

## 🎯 Objetivo do Projeto

O objetivo principal desta ferramenta é preencher a lacuna entre a análise de dados operacionais e a governança de cibersegurança. A aplicação permite que analistas de BI e SOC (Security Operations Center):
- Auditem logs de acesso a dados sensíveis.
- Identifiquem desvios de comportamento e acessos fora de padrão usando IA.
- Gerem relatórios executivos para tomada de decisão alinhada a diretrizes de segurança e privacidade (ex.: LGPD).

---

## 🚀 Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Interface Web:** [Streamlit](https://streamlit.io/)
- **Análise e Manipulação de Dados:** [Pandas](https://pandas.pydata.org/)
- **Inteligência Artificial:** [Google GenAI SDK](https://github.com/google-gemini/generative-ai-python) (Modelo Gemini 2.5 Flash)
- **Gerenciamento de Variáveis:** Python Dotenv

---

## 🛠️ Estrutura do Repositório

```text
security-bi-analytics/
├── app.py                   # Código principal da aplicação Streamlit
├── sample_security_logs.csv # Massa de dados simulada para testes
├── .env                     # Variáveis de ambiente (chave de API)
├── requirements.txt         # Dependências do projeto
├── LICENSE                  # Licença MIT
└── README.md                # Documentação técnica do projeto
