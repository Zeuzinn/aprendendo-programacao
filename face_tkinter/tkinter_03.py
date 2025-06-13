import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# Janela
janela = tk.Tk()
janela.title("Elementos visuais no Tkinter")
janela.geometry("400x400")

# --- Lista suspensa (Combobox) ---
tk.Label(janela, text="Escolha uma cor:").pack()
cores = ["Vermelho", "Verde", "Azul"]
combo = ttk.Combobox(janela, values=cores)
combo.current(0)  # Valor inicial
combo.pack(pady=5)

# --- Checkbox ---
var_check = tk.BooleanVar()
check = tk.Checkbutton(janela, text="Aceito os termos", variable=var_check)
check.pack(pady=5)

# --- Imagem ---
img = Image.open("praticas-com-python/face_tkinter/8899bc16-28f5-4e4b-986a-0c49c6698089.png")  # Substitua pelo caminho da sua imagem
img = img.resize((200, 200))
foto = ImageTk.PhotoImage(img)
img_label = tk.Label(janela, image=foto)
img_label.pack(pady=10)

# --- Botão para mostrar seleção ---
def mostrar_info():
    cor = combo.get()
    aceito = var_check.get()
    print(f"Cor: {cor}, Aceitou os termos: {aceito}")

tk.Button(janela, text="Enviar", command=mostrar_info).pack(pady=10)

janela.mainloop()