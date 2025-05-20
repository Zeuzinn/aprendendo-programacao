lista = []

print('CADASTRO DE PRODUTOS:')
for _ in range (3):
    nome = input('Nome do produto: ')
    estoque = int(input('Quantidade no estoque: '))
    preco = float(input('Preço do produto: '))
    lista.append({'produto': nome, 'quantidade':estoque,'preco':preco})
    print()


print('PRODUTOS:')
for i , p in enumerate(lista):
    print(f"{i} - Produto: {p['produto']}")
    print(f"Valor em estoque: R${p['quantidade'] * p['preco']:.2f}")
    
    if (p['quantidade'] * p['preco']) >= 1000:
        print('Estoque alto.')
        print()
    else:
        print('Estoque baixo.')
        print()