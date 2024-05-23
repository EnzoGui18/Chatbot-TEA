import openai
import os

# Obtém a chave da API do OpenAI das variáveis de ambiente
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_gpt4_response(prompt):
    # Cria uma requisição para a API do OpenAI GPT-4
    response = openai.Completion.create(
        engine="text-davinci-003",  # Especifica o modelo a ser usado
        prompt=prompt,  # Passa o prompt do usuário
        max_tokens=150  # Define o máximo de tokens na resposta
    )
    return response.choices[0].text.strip()  # Retorna a resposta gerada pelo modelo
