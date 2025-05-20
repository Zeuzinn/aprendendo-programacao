def cadastrar():
    titulo = input('Titulo do livro: ')
    autor = input('Nome do autor: ')
    livro = Livro(titulo, autor)
    livros.append(livro)
    print('Cadastro feito com sucesso! ')


def listar_livros():
    if not livros:
        print('Biblioteca vazia')
    else:
        for i, livro in enumerate(livros, 1):
            print(f'Nº: {i}')
            livro.exibir_info()