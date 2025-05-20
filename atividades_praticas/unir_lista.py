# União de lista
def zipper(lista1 , lista2):
    intervalo = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(intervalo)   
    ]

lista1=['Salvador','São Vicente', 'Copacabana']
lista2=['BA', 'SP', 'RJ', 'MG']
print(zipper(lista1, lista2))
print()

# 2º Exemplo
print(list(zip(lista1,lista2)))