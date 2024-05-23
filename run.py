from app import create_app

# Cria a aplicação Flask usando a fábrica de aplicativos
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # Executa a aplicação Flask no modo de depuração
