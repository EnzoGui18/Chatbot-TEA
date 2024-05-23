from flask import Flask

def create_app():
    app = Flask(__name__)  # Cria uma instância do Flask

    from .routes import main  # Importa o blueprint das rotas
    app.register_blueprint(main)  # Registra o blueprint no aplicativo Flask

    return app  # Retorna a aplicação Flask configurada
