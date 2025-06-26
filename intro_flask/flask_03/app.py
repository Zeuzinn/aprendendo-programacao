# O código abaixo possui uma função chamada user(name), 
# que aceita o valor por meio da URL de entrada.
#  
# Ele verifica se o argumento recebido dentro de '/user/<name>' 
# corresponde ao argumento "admin" ou não. 
# Se corresponder, a função hello_admin() é chamada, 
# caso contrário, a função hello_guest() é chamada.

from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/admin')  
def hello_admin():  
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):  
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin' or 'ADMIN':  
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


if __name__ == '__main__':
    app.run(debug=True)