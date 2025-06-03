# Métodos úteis em PYTHON

texto = "PyThon"

print(texto.upper())    # Converte os caracteres para maiúsculo

print(texto.lower())    # Converte os caracteres para minúsculo

print(texto.title())    # A primeira letra de cada palavra ficará em maiúsculo

print()

# Eliminando espaços em branco

palavra = " EU AMO PYTHON  "

print(palavra.strip())      # Remove os espaços em branco de ambos os lados

print(palavra.lstrip())     # Remove os espaços em branco da esquerda

print(palavra.rstrip())     # Remove os espaços em branco da direita

print()
# Junções e centralização

palavra = " EU AMO PYTHON  "

print(texto.upper().center(20, "="))    # 

print("-".join(texto))    # Insere um caracete entre as strings