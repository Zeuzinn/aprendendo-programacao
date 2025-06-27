# Função url_for() no Flask
# Outro método que você pode usar ao realizar redirecionamentos no Flask é a função url_for() para criação de URL. 
# Esta função aceita o nome da função como primeiro argumento, 
# e a função chamada user(name) aceita o valor por meio da URL de entrada. 
# Ela verifica se o argumento recebido corresponde ao argumento "admin" ou não. 
# Se corresponder, a função hello_admin() é chamada; 
# caso contrário, a função hello_guest() é chamada.

from flask import Flask, redirect, url_for

app = Flask(__name__)

# decorator for route(argument) function
@app.route('/admin')
# binding to hello_admin call
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
# binding to hello_guest call
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):

    # dynamic binding of URL to function
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest'
                                , guest=name))

if __name__ == '__main__':
    app.run(debug=True)