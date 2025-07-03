from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'santos12'


@app.route('/', methods=["GET", "POST"])
def number_secrets():
    # Inicializa se não existir ainda
    if 'number_secret' not in session:
        session['number_secret'] = random.randint(1, 100)
        session['attempt'] = 0

    msg = None
    number = None

    if request.method == "POST":
        try:
            number = int(request.form['number'])
            session['attempt'] += 1

            if number == session['number_secret']:
                msg = f"Parabéns! Você acertou o número secreto ({session['number_secret']}) em {session['attempt']} tentativas."
                # Reinicia o jogo
                session['number_secret'] = random.randint(1, 100)
                session['attempt'] = 0

            elif number < session['number_secret']:
                msg = "Tente um número maior"

            elif number > session['number_secret']:
                msg = "Tente um número menor"

        except ValueError:
            msg = "Erro: digite apenas um número válido."

    return render_template('number.html',
                           mensagem=msg,
                           attempt=session.get('attempt', 0),
                           number=number)

if __name__ == "__main__":
    app.run(debug=True)