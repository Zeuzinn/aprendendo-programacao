# PRÁTICA COM USUÁRIOS E JSON
import json

ARQ = 'usuarios.json'

def carregar_usuarios():  # Carrega o arquivo JSON
    try:
        with open(ARQ, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_usuarios(usuarios):      # Salva os usuários cadastrados
    with open(ARQ, 'w', encoding='utf-8') as arquivo:
        json.dump(usuarios, arquivo, indent=4)


def cadastro(usuarios):
    nome = input('Nome: ').lower()
    idade = int(input('Idade: '))
    email = input('E-mail: ').lower()
    usuarios.append({'nome': nome, 'idade' : idade, 'email' : email})
    print('✅ - Cadastro realizado! \n')
    

def lista_de_usuarios(usuarios):
    if not usuarios:
        print('Nenhum usuário encontrado!')
    else:
        print('\n=== LISTA DE USUÁRIOS ===\n')
        for i, usuario in enumerate(usuarios, 1):
            print(f"{i} - Nome: {usuario['nome']} \nE-mail: {usuario['email']} \n")
            

def buscar_usuario(usuarios):
    palavra = input('Digite o nome ou e-mail que deseja buscar: ')
    encontrados = [u for u in usuarios if palavra in u['nome'].lower() or palavra in u['email'].lower()]
    if encontrados:
        for u in encontrados:
            print(f"🔍 {u['nome']} - {u['email']}")
    else:
        print("❌ Nenhum usuário encontrado com esse termo.")


usuarios = carregar_usuarios()    # Carrega os usuários salvos no arquivo JSON
while True:
    print('[1] Cadastrar usuário.')
    print('[2] Listar usuários.')
    print('[3] Buscar usuários(NOME OU E-MAIL).')
    print('[4] Sair.')
    opcao = input('Escolha uma opção: ')
    print('-'*30)
    if opcao == '1':
        cadastro(usuarios)
        salvar_usuarios(usuarios)
    elif opcao == '2':
        lista_de_usuarios(usuarios)
    elif opcao == '3':
        buscar_usuario(usuarios)
    else:
        print('Opção inválida!')