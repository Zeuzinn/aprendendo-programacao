produtos = [
    {'nome': 'Camiseta', 'preco': 25.00},
    {'nome': 'Calça', 'preco': 50.00},
    {'nome': 'Sapato', 'preco': 80.00},
    {'nome': 'Meias', 'preco': 10.00}
]

produtos_ordenados = sorted(produtos, key=lambda produto: produto['preco'])

for p in produtos_ordenados:
    print(p['preco'])

palavras = ['maçã', 'banana', 'laranja', 'uva', 'kiwi', 'abacate']

