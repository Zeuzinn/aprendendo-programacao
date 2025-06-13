import tkinter as tk
from tkinter import ttk


janela = tk.Tk()
janela.title("🧮 Calculadora")
janela.geometry("350x350")

def calculate():
    valores = check_numbers()
    if not check_numbers():
        return
    
    number_1, number_2 = valores
    operation = combo.get()

    try:
        if operation == "somar":
            result = int(number_1) + int(number_2)
        elif operation == "subtrair":
            result = int(number_1) - int(number_2)
        elif operation == "multiplicar":
            result = int(number_1) * int(number_2)    
        elif operation == "dividir":     
            result = int(number_1) / int(number_2)
    except ZeroDivisionError:
        label_resposta.config(text="Erro: Divisão por zero")

    label_resposta.config(text=f"Resultado: {result}")

def check_numbers():
    try:
        number_1 = int(number_one.get())
        number_2 = int(number_two.get())
        return number_1, number_2
    except ValueError:
        label_resposta.config(text="Erro: Insira apenas números")
        return
                
# Widgets

tk.Label(janela, text="Digite um número").pack()
number_one = tk.Entry(janela)
number_one.pack(pady=5)

number_two = tk.Entry(janela)
number_two.pack(pady=5)

tk.Label(janela, text="Escola uma operação: ").pack()
operations = ["somar", "subtrair", "multiplicar", "dividir"]
combo = ttk.Combobox(janela, values=operations)
combo.pack(pady=5)

button = tk.Button(janela, text="Enviar", command=calculate)
button.pack()

label_resposta = tk.Label(janela, text="")
label_resposta.pack(pady=10)

janela.mainloop()