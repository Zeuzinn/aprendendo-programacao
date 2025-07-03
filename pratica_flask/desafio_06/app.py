# 🚀 Desafio Flask: Conversor de Temperatura

# 🧠 O que você vai praticar:
# Rotas com @app.route
# Uso de request.form para pegar dados de um formulário
# Lógica simples com if
# Renderização com render_template

# ✅ O Desafio:
# Crie uma aplicação web em Flask que permita o usuário converter temperaturas de Celsius para Fahrenheit ou Fahrenheit para Celsius.

# 📝 Requisitos:
# Página com um formulário onde o usuário:
# Digita o valor da temperatura.
# Escolhe se quer converter de Celsius para Fahrenheit ou o contrário.
# Clica em um botão para converter.
# Após o envio do formulário, a aplicação mostra o resultado da conversão.

# 🧮 Fórmulas:
# Celsius → Fahrenheit: F = C × 1.8 + 32

# Fahrenheit → Celsius: C = (F - 32) / 1.8
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    result = None
    msg = None
    if request.method == "POST":
        try:
            graus = float(request.form['graus'])
            tipo = request.form['tipo']
            if tipo == "C":
                result = f"{graus * 1.8 + 32:.1f}ºF"
            else: 
                result = f"{(graus - 32) / 1.8:.1f}ºC"

        except ValueError:
            msg = "ERRO: DIGITE APENAS NÚMERO"
        

    return render_template(
        'index.html',
        result = result,
        msg= msg
        )


if __name__ == "__main__":
    app.run(debug=True)