import os
import json

CAMINHO_ARQUIVO = 'produtos.json'

def linha():
    print('-'*30)

def salvar_produtos(produtos):
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        json.dump(produtos, arquivo, ensure_ascii=False, indent=3)


def carregar_produtos():
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    return []


def cadastrar_produto(produtos):
    nome=input('Nome do produto: ')
    preco= float(input('Valor do produto R$'))
    produtos.append({'nome': nome.lower(), 'preco': preco})   # Cria um dicionáro com produtos
    salvar_produtos(produtos)       # Salva os produtos em um arquivo JSON
    print('Produto adicionado!')
    linha()


def remover_produto(produtos):
    remover = input('Produto que deseja remover: ').lower()
    for produto in produtos:
        if produto['nome'] == remover:
            produtos.remove(produto)
            salvar_produtos(produtos)
            print(f'Produto "{remover}" removido com sucesso.')
            linha()
            return
    print('Produto não encontrado.')
    linha()

def mostrar_produto(produtos):
    print('=== PRODUTOS ===')
    if not produtos:
        print('Sua lista de produtos está vazia.')
    else:
        for produto in produtos:
            nome = produto['nome'].capitalize()
            preco = f"R$ {produto['preco']:.2f}"
            print(f'{nome} - {preco}')
    linha()

def buscar_produto(produtos):
    buscar= input('Buscar produto: ').lower()
    for produto in produtos:
        if produto['nome'] == buscar:
            print(buscar)
            linha()
            return
    print('Produto não encontrado.')
    linha()

def menu():
    produtos = carregar_produtos()
    while True:
        print('1. Cadastro de produtos.')
        print('2. Remover produto.')
        print('3. Mostrar produtos.')
        print('4. Buscar produtos.')
        print('0. Sair')
        opcao = input('Opção: ')
        linha()
        if opcao =='1':
            cadastrar_produto(produtos)
        elif opcao == '2':
            remover_produto(produtos)
        elif opcao == '3':
            mostrar_produto(produtos)
        elif opcao == '4':
            buscar_produto(produtos)
        elif opcao == '0':
            print('Encerrando programa, ate logo!')
        else:
            print('Opção inválida!')

if __name__ == '__main__':
    menu()