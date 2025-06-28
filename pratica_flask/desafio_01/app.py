#🧠 Desafio 1 — Crie um contador de cliques com Flask e HTML
# Objetivo:
# Criar uma aplicação Flask com uma única rota (/) que exibe um botão “Clique aqui!”. 
# Cada vez que o botão for clicado, o número de cliques deve aumentar usando cookies para armazenar essa contagem no navegador do usuário.

# Requisitos:
# - Ao acessar a página, o usuário vê o número atual de cliques (inicialmente zero).
# - O botão “Clique aqui!” incrementa a contagem.
# - A contagem é armazenada no cookie, então mesmo que o usuário recarregue a página ou feche o navegador, o número anterior deve continuar.

from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def acess_page():

    count = int(request.cookies.get('Acessos', 0))
    count += 1

    output = 'Quantidade de acesso: '+str(count)
    resp = make_response(output)
    resp.set_cookie('Acessos', str(count))
    return resp


if __name__ == "__main__":
    app.run(debug=True)