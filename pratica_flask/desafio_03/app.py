from flask import Flask, render_template, request
from datetime import datetime

year_actual = datetime.now().year

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def calculator_age():
    result_age = None

    if request.method == "POST":
        try:
            age = int(request.form['age'])
            result_age = year_actual - age        
        except ValueError:
            return 'ERRO: IDADE DEVE SER APENAS NÚMERO'
    return render_template('idade.html', result = result_age)    


if __name__ == "__main__":
    app.run(debug=True)