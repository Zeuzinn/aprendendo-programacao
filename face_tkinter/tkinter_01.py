import tkinter as tk

# Janela principal
janela = tk.Tk()
janela.title("Conversor de Moedas")
janela.geometry("300x300")  # Largura x Altura

# Função que será chamada ao clicar no botão
def click():
    label.config(text="Você clicou no botão!")


# Criando widgets
label = tk.Label(janela, text="Olá Guys!")
label.pack(pady=10)

buttom =tk.Button(janela, text="Clique aqui", command=click)
buttom.pack()

# Mantém Janela aberta
janela.mainloop()