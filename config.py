import os

class Config:
    # Obtém a chave da API do OpenAI das variáveis de ambiente
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
