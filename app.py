from google import genai

# Inicializando o cliente com a chave que você insere no app
client = genai.Client(api_key=api_key)

# Exemplo de chamada para análise
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=f"Analise os seguintes logs de segurança: {dados_csv}"
)
