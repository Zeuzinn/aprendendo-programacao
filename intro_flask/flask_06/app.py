from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/', methods =['GET'])
def login():
    return render_template('Login.html')