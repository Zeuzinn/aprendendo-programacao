# O método HTTP é fornecido pelo Flask
# GET -> Isso é usado para enviar os dados em um formato sem criptografia para o servidor.
# HEAD -> fornece corpo de resposta ao formulário
# PUT -> Substitui a representação atual do recurso de destino pela URL.
# POST -> Envia os dados do formulário para o servidor. Os dados recebidos pelo método POST não são armazenados em cache pelo servidor.
# DELETE -> Exclui o recurso de destino de uma URL fornecida

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)