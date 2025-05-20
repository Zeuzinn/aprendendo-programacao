def cadastro_produto(produtos):
    nome = input('Nome: ').lower()
    preco= float(input('Preço: '))
    categoria = input('Categoria: ').lower()
    produtos.append({'nome': nome, 'preco': preco, 'categoria': categoria})
    print('Cadastro concluído.')


def listar_produtos(produtos):
    if not produtos:
        print('Primeiro você precisa cadastrar. Sua lista está vazia')
    else:
        print('== LISTA ==')
        for produto in produtos:
            print(f"Nome: {produto['nome']} - R${produto['preco']:,.2f} - [{produto['categoria']}]")


def buscar_produto(produtos):
    buscar = input('Nome: ').lower()
    encontrado = False
    
    for produto in produtos:
        if produto['nome'] == buscar:
            print(f"Nome: {produto['nome']} - R${produto['preco']:,.2f} - [{produto['categoria']}]")
            encontrado = True

    if not encontrado:
        print('Produto não encontrado.')


def editar_produto(produtos):
    
    editar= input('Nome do produto que deseja editar: ').lower()
    encontrado = False
    
    for produto in produtos:
        if produto['nome'] == editar:
            alterar_produto = input('O que deseja alterar? (nome, preço, categoria) ').lower()
            
            if alterar_produto == 'nome':
                novo_nome = input('Digite o novo nome: ')
                produto['nome'] = novo_nome
                print('Novo nome registrado.')

            elif alterar_produto == 'preco' or alterar_produto == 'preco':
                novo_preco = float(input('Digite o novo valor R$: '))
                produto['preco'] = novo_preco
                print('Novo preço registrado.')

            elif alterar_produto == 'categoria':
                nova_categoria = input('Digite a nova categoria: ')
                produto['categoria'] = nova_categoria
                print('Nova categoria registrada.')
            
            else:
                print('Opção de edição inválida.')
            
            encontrado = True
            break  # já encontrou e editou, pode sair do loop

    if not encontrado:
        print('Produto não encontrado.')

    
    if not encontrado:
        print('Produto não encontrado.')

def menu():
    print('1. Cadastrar')
    print('2. Listar')
    print('3. Buscar')
    print('4. Editar produto')
    print('0. Sair')
    

produtos = []
while True:
    menu()
    opcao= input('Escolha uma opção: ')
    print('-'*30)
    if opcao == '1':
        cadastro_produto(produtos)
        print()
    elif opcao =='2':
        listar_produtos(produtos)
        print()
    elif opcao =='3':
        buscar_produto(produtos)
        print()
    elif opcao == '4':
        editar_produto(produtos)
        print()
    elif opcao =='0':
        print('Encerrando programa.')
        break
    else:
        print('Opção inválida!')
