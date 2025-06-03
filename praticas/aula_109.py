def eh_primo (numero):
    if numero % 2 == 0:
        print(True)
    else:
        print(False)
eh_primo(8)

# Crie uma função que recebe uma string e retorna um dicionário com a contagem de cada palavra.
from collections import Counter

def string(entrada):
    strings=Counter(entrada.split())
    print(strings)

entrada = "gato cachorro gato cavalo cachorro cachorro"
string(entrada)