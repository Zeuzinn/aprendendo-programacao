# Flask(__name__): Cria o aplicativo Flask.
# @app.route('/'): Define a rota inicial (/).
# def hello(): cria uma função que é vinculada à rota ' / ' e retorna "HELLO" quando a página raiz é acessada.
# app.run(debug=True): executa o aplicativo em modo de depuração. Isso garante que o aplicativo não precise ser reiniciado manualmente caso sejam feitas alterações no código.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'HELLO'

@app.route('/hello')
def hello_name():
    return 'HELLO ELISEU'


if __name__ == '__main__':
    app.run(debug=True)