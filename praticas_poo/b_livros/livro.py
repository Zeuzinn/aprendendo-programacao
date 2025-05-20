class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
    
    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True
        
    def exibir_info(self):
        print(f'Titulo: {self.titulo} - Autor: {self.autor} - Disponibilidade: {self.disponivel}')




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

livros = []
while True:
    print('1 - Cadastrar novo livro')
    print('2 - Listar todos os livros')
    print('3 - Emprestar livro')
    print('4 - Devolver livro')
    opcao = input('Selecione uma opção:')
    print()
    if opcao == '1':
        cadastrar()
        print()
    elif opcao =='2':
        listar_livros()
        print()
    elif opcao =='3':
        ...
    elif opcao =='4':
        ...