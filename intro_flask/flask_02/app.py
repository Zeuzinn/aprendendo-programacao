# Variáveis ​​no Flask, além do tipo de string padrão, o Flask também suporta int, float e path
# O parâmetro do decorador 'route ()' contém a parte variável anexada à URL ' /hello ' como argumento.
# Portanto, se uma URL como " http://localhost:5000/hello/Eliseu" for inserida, 
# " Eliseu " será passado para a função hello (name) como argumento.

from flask import Flask 
app = Flask(__name__) 


@app.route('/')
def home():
    return 'Olá, você está na página inicial!'


@app.route('/hello/<name>') 
def hello_name(name): 
    return 'Hello %s!' % name 


@app.route('/blog/<int:postID>')
def show_blog(postID): 
    return 'Blog Number %d' % postID  
    # blog/555 captura 555 como um inteiro e retorna "Número do blog 555".


@app.route('/rev/<float:revNo>')
def revision(revNo): 
    return 'Revision Number %f' % revNo  
    # /rev/1.1 captura 1.1 como um float e retorna "Número de revisão 1.100000" (formato float padrão).


if __name__ == '__main__': 
    app.run(debug = True)