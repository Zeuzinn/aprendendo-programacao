from functools import reduce

produtos = [
    {'nome': 'Produto 1', 'preco': 15.80},
    {'nome': 'Produto 3', 'preco': 45.66},
    {'nome': 'Produto 2', 'preco': 31.10},
    {'nome': 'Produto 4', 'preco': 2.60},
]

def funcao_do_reduce(acumulador, produto):
    print('Acumulador: ', acumulador)
    print('Produto: ', produto)
    return acumulador + produto['preco']

# Utilizando Função
total = reduce(
    funcao_do_reduce,
    produtos,
    0  # Valor inicial
)

# Utilizando função Lambda
total_2 = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0  # Valor inicial
)


print('Total é: ', total)
print()
print('Total: ', total_2)