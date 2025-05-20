vendedores= []
for _ in range (3):
    nome=input('Nome: ')
    qtd_vendas = int(input('Quantidade de vendas: '))
    valor_vendido = float(input('Valor vendido, R$'))
    vendedores.append({'nome': nome, 'vendas': qtd_vendas, 'preco': valor_vendido})
    print()

print('\n==== VENDEDORES ====\n')
total_vendas_geral = 0
maior_venda = 0
top_vendedor = ''

for vendedor in vendedores:
    print(f'Vendedor: {vendedor['nome']}')
    print(f'Quantidade de vendas: {vendedor['vendas']}')
    print(f'Valor vendido R$: {vendedor['preco']:.2f}')
    print()
    
    total_vendas_geral += vendedor['preco']

    if vendedor['preco'] > maior_venda:
        maior_venda = vendedor['preco']
        top_vendedor = vendedor['nome']
        media = total_vendas_geral / len(vendedores)

print(f'Média geral de vendas: R${media:.2f}')
print(f'Melhor vendedor: {top_vendedor}')
print(f'Maior valor vendido: R${maior_venda:.2f}')