def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 1', 'preco': 15.80},
    {'nome': 'Produto 3', 'preco': 45.66},
    {'nome': 'Produto 2', 'preco': 31.10},
    {'nome': 'Produto 4', 'preco': 2.60},
]

def filtrar_preco(produto):
    return produto['preco'] > 35

# Filtro de produtos com IF
novos_produtos = [
    p for p in produtos
    if p ['preco'] > 30
]

# Filtro de produtos com 'filter'
novos_produtos_2 = filter(
    lambda p:p['preco'] > 10,
    produtos
)

# Filtro de preço com 'função'
novos_produtos_3 = filter(
    filtrar_preco,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)
print_iter(novos_produtos_2)
print_iter(novos_produtos_3)