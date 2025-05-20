import json

ARQ_LIVROS = 'livros.json'

def carregar_livro():
    try:
        with open(ARQ_LIVROS, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
def salvar_livro(livros):
    with open(ARQ_LIVROS, 'w', encoding='utf-8')as arquivo:
        json.dump(livros, arquivo, indent= 4)
    

def menu():
    print('[1] Cadastrar novo livro')
    print('[2] Listar livros')
    print('[3] Busca por título')
    print('[4] Sair')
    print('-' *30)


def cadastrar_livro(livros):
    titulo = input('Título: ').upper()
    autor = input('Autor: ').upper()
    ano = int(input('Ano do livro: '))
    genero = input('Gênero: ').upper()
    livros.append({'titulo': titulo, 'autor': autor, 'ano': ano, 'genero': genero})
    print('✅ - Cadastro efetuado!')


def listar_livros(livros):
    if not livros:
        print('❌ - Sem livro cadastrado')
    else:
        print('\n=== 📚 LISTA DE LIVROS 📚 ===\n')
        for livro in livros:
            print(f'Titulo: {livro['titulo']} \nAutor:{livro['autor']} \nAno: {livro['ano']} \nGênero: {livro['genero']}')
            print('-'*30)
    print()


def buscar_livro(livros):
    titulo = input('Título: ').upper()
    titulo_encontrado = [
        livro for livro in livros
        if titulo in livro['titulo'].upper()
        ]
    
    if titulo_encontrado:
        for t in titulo_encontrado:
            print(f"🔍 {t['titulo']}")
    else:
        print("❌ Nenhum livro encontrado com este título.")
    print()

livros = carregar_livro()
while True:
    menu()
    opcao = input('Escolha uma opção: ')
    print()
    if opcao == '1':
        cadastrar_livro(livros)
        salvar_livro(livros)
    elif opcao == '2':
        listar_livros(livros)
    elif opcao == '3':
        buscar_livro(livros)
    elif opcao == '4':
        print('Fechando programa!')
        break
    else:
        print('❌ - OPÇÃO INVÁLIDA! ESCOLHA A OPÇÃO CORRETA.')


