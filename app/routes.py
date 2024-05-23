from flask import Blueprint, request, jsonify
from .gpt4 import get_gpt4_response
from .bert import get_bert_response

# Cria um blueprint chamado 'main'
main = Blueprint('main', __name__)

# Define a rota '/chat' que aceita requisições POST
@main.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['input']  # Obtém a entrada do usuário da requisição JSON
    context = open('data/context.txt').read()  # Lê o contexto para o modelo BERT de um arquivo

    # Classifica a intenção (exemplo simples)
    if "what is autism" in user_input.lower():
        response = get_gpt4_response(user_input)  # Usa GPT-4 se a pergunta for "o que é autismo"
    else:
        response = get_bert_response(user_input, context)  # Usa BERT para outras perguntas

    return jsonify({"response": response})  # Retorna a resposta como um JSON
