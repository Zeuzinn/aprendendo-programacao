# Crie uma lista de 10 números
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função para exibir uma lista ao quadrado '**2'
def exibir_lista_quadrado(lista):
    return [
        n ** 2 for n in lista
]

# Função para exibir uma nova lista com números pares
def exibir_pares(lista_q):
    return [
    p for p in lista_q
    if p % 2 == 0
]

# Passa a primeira lista criada para função
lista_de_quadrado = exibir_lista_quadrado(lista)

# Passa o retorno da lista ao quadrado para a função
lista_pares= exibir_pares(lista_de_quadrado)

print('Lista normal: ', lista)
print('Lista ao quadrado: ',lista_de_quadrado)
print('Lista de números pares: ', lista_pares)