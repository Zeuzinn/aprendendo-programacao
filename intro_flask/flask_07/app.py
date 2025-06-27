from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/', methods= ['GET'])
def Login():
    return render_template('Login.html')

@app.route('/details', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        output = 'Hi, Welcome ' +name+ ''
        resp = make_response(output)
        resp.set_cookie('username', name)
        return resp
    
if __name__ == "__main__":
    app.run(debug=True)