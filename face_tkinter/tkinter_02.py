import tkinter as tk

# Criando Janela
janela = tk.Tk()
janela.title("App de usuários")
janela.geometry("300x200") 

# Função para responder ao botão
def show_text():
    texto = entrada.get()
    label_resposta.config(text=f"Você digitou {texto}")

# Widgets

entrada = tk.Entry(janela)
entrada.pack(pady=10)

botao = tk.Button(janela, text="Enviar", command=show_text)
botao.pack()

label_resposta = tk.Label(janela, text="")
label_resposta.pack(pady=10)

janela.mainloop()