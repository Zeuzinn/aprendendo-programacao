# Rastreamento de visitantes do site usando cookies

from flask import Flask, request, make_response

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def vistors_count():

    # Obtém o valor do cookie 'visitors count', ou usa 0 se o cookie não existir
    count = int(request.cookies.get('visitors count', 0))

    # Incrementa o contador de visitas
    count = count + 1

    # Gera a resposta com o número de visitas
    output = 'You visited this page for ' +str(count) + ' times'

    # Cria a resposta e define o cookie atualizado
    resp = make_response(output)
    resp.set_cookie('visitors count', str(count))

    return resp 

@app.route('/get')
def get_vistors_count():
    # Retorna o valor atual do cookie 'visitors count'
    count = request.cookies.get('visitors count')
    return count

app.run()