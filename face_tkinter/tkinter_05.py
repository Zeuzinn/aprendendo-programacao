import tkinter as tk
from tkinter import ttk

# Cria a janela principal
janela = tk.Tk()
icone = tk.PhotoImage(file="praticas-com-python/face_tkinter/download.png")
janela.iconphoto(False, icone)
janela.title("Santos Futebol Clube")
janela.geometry("400x200")
janela.configure(bg="#1e1e1e")  # Define uma cor de fundo escura


# Cria o estilo personalizado para o cabeçalho
estilo = ttk.Style()
estilo.theme_use("clam")    # Usa um tema que aceita bem personalizações
estilo.configure("Cabecalho.TLabel",    # Nome do estilo   
    background="#1e1e1e",             # Cor de fundo
    foreground="#00bfff",             # Cor do texto
    font=("Segoe UI", 18, "bold")       # Fonte grande e em negrito
)


# Cria o widget de cabeçalho com o estilo definido
cabecalho = ttk.Label(
    janela, 
    text="🐋 Bem-vindo ao Santos F.C. 🐋",     # Texto com emoji no início 
    style="Cabecalho.TLabel",           # Aplica o estilo criado
    anchor="center"                     # Centraliza o texto
    )
cabecalho.pack(pady=30)                 # Posiciona com espaço vertical


# Cria o estilo personalizado para o botão
estilo.configure("Neon.TButton",
    background="#00ff99",
    foreground="#101010",
    font=("Arial", 10, "bold"),
    borderwidth=0,
    padding=8
)

# Cria o widget de cabeçalho com o estilo definido
neon_botao = ttk.Button(janela, text="Clique Aqui", style="Neon.TButton")
neon_botao.pack()


janela.mainloop()