from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/', methods=['GET'])
def index():
    msg = "Nenhuma nota adicionada."
    return render_template('index.html', notes=notes, msg = msg)


@app.route('/add', methods= ['GET', 'POST'])
def add_note():
    if request.method == "POST":
        note = request.form['note']

        if len(note) <= 0:
            msg = 'Você precisa escrever uma nota'
            return render_template('add.html', msg= msg)
        else:    
            notes.append(note)    
        return redirect(url_for('index'))    
    
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)