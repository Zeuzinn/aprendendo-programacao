# Cookie em Flask 
# Um Cookie é um tipo de arquivo de texto armazenado no computador do cliente, 
# cuja finalidade é lembrar e rastrear dados referentes ao uso do cliente 
# para melhorar o site de acordo com a experiência do usuário e as estatísticas da página.

from flask import Flask, request, render_template, make_response

app = Flask(__name__) 
@app.route('/') 

def index(): 
    return render_template('index.html') 

@app.route('/setcookie', methods = ['POST', 'GET']) 
def setcookie(): 
    if request.method == 'POST': 
        user = request.form['nm'] 
        resp = make_response(render_template('cookie.html')) 
        resp.set_cookie('userID', user) 
        return resp 

@app.route('/getcookie') 
def getcookie(): 
    name = request.cookies.get('userID') 
    return '<h1>welcome '+name+'</h1>'
if __name__ == "__main__":
    app.run()