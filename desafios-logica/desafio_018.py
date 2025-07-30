class Livro:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.available = True  
    
    def return_book(self):
        self.available = True

    def borrow_book(self):
        self.available = False
    
    def show_info(self):
        status = "✅" if self.available else "❌"
        print(f'Titulo: {self.title} \nAutor: {self.author} \nAno de publicação: {self.year} \nDisponível: {status}')


class Biblioteca:
    def __init__(self):
        self.bookcase = []

    def add_book(self, book: Livro):
        self.bookcase.append(book)
        print('✅ - Livro Adicionado!\n')

    def list_book(self):
        if not self.bookcase:
            print('Biblíoteca vazia.\n')
        else:
            for book in self.bookcase:
                book.show_info()
                print('-'*30)

    def search_book(self, name: str):
        found = False
        for book in self.bookcase:
            if name.lower() in book.title.lower() or name.lower() in book.author.lower():
                book.show_info()
                print('📚 Livro encontrado!')
                print('-'*30)
                found = True
        if not found:
            print('🚫 Nenhum livro encontrado com esse título ou autor.')

    def search_borrow_book(self, name: str):
        for book in self.bookcase:
            if name.lower() in book.title.lower() or name.lower() in book.author.lower():
                if book.available:
                    book.borrow_book()
                    print(f'📕 Você emprestou o livro: {book.title}\n')
                else:
                    print('⚠️ Este livro já foi emprestado.\n')
                return
        print('🚫 Livro não encontrado.\n')

    def search_return_book(self, name: str):
        for book in self.bookcase:
            if name.lower() in book.title.lower() or name.lower() in book.author.lower():
                if not book.available:
                    book.return_book()
                    print(f'📗 Você devolveu o livro: {book.title}\n')
                else:
                    print('⚠️ Este livro já está disponível.\n')
                return
        print('🚫 Livro não encontrado.\n')


class LoginAdmin:
    def __init__(self):
        self.login = 'admin'
        self.password = '1234'
 

    def verify_login(self, login:str, password:str):
        if login.lower() == self.login and password.lower() == self.password:
            print('✅ Acesso permitido.\n')
            return True
        else:
            print('❌ Login incorreto.\n')
            return False
            

class Pessoa:
    def __init__(self, name:str, age:int, cpf: str):
        self.name = name
        self.age = age
        self.cpf = cpf
        
    def show_people(self):
        print(f'Nome: {self.name} \nCPF:{self.cpf} \nIdade:{self.age}')


class Usuario:
    def __init__(self, pessoa: Pessoa, password: str):
        self.pessoa = pessoa
        self.password = password

    def show_user(self):
        self.pessoa.show_people()


class SistemaUsuarios:
    def __init__(self):
        self.list_users = []

    def add_users(self, people: Pessoa, password:str):
        new_user = Usuario(people, password)
        self.list_users.append(new_user)
        print('✅ - Usuário cadastrado!\n')
    
    def list_user(self):
        if not self.list_users:
            print('Nenhum usuário cadastrado.\n')
            return
        else:
            for user in self.list_users:
                user.show_user()


def home():
    while True:
        print('\n==== SEJA BEM VINDO A BIBLIOTECA! ====\n')
        print('[1] - Sou cliente.')
        print('[2] - Sou bibliotecário.')
        print('[0] - Sair do sistema.')
        print('======================================')
        option = input('Escolha uma opção: ')
        print()
        if option == '1':
            menu_1()
        elif option == '2':
            login_adm()
        elif option == '0':
            print('Encerrando Sistema...')
            break

def menu_1():
    while True:
        print('[1] - Criar cadastro')
        print('[2] - Efetuar login')
        option = input('Escolha uma opção: ')
        
        if option == '1':
            create_login()
        elif option == '2':
            ...


def create_login():
    name = input('Nome completo: ').title()
    cpf = input('CPF(Apenas digitos): ')
    if len(cpf) < 11:
        return
    
    try:
        age = int(input('Idade:'))
        if age < 0:
            print('Idade deve ser maior que 0')
            return
    except ValueError:
        print('⚠️ - Idade deve ser apenas números')
        return
    
    password = create_password()
    
    p = Pessoa(name, age, cpf)
    sistem_users.add_users(p, password)


def create_password():
    print('Crie uma senha.')
    print('A senha deve ter mínimo 8 digitos.')
    password = input('Senha:')
    if len(password) < 8:
        print('A senha deve ter mínimo 8 digitos.\n')
    else:
        return password
    

def login_adm():
    login = input('Login: ')
    password = input('Senha: ')
    admin = LoginAdmin()
    if admin.verify_login(login, password):
        menu_2()


def menu_2():
    while True:
        print('[1] - Adicionar livro')
        print('[2] - Exibir livros')
        print('[3] - Buscar livro')
        print('[4] - Emprestar livro')
        print('[5] - Devolver livro')
        print('[6] - Sair')
        option = input('Escolha uma opção: ')
        print()
        if option == '1':
            book = new_book()
            b.add_book(book)
            
        elif option == '2':
            b.list_book()
        
        elif option == '3':
            name = search()      
            b.search_book(name)
        
        elif option == '4':
            name = search()
            b.search_borrow_book(name)

        elif option == '5':
            name = search()
            b.search_return_book(name)

        
        elif option == '6':
            print('Fechando Biblioteca...')
            break        
        else:
            print('⚠️ - OPÇÃO INVÁLIDA')


def new_book():
    title = input('Título: ').title()
    author = input('Autor: ').title()
    try:
        year = int(input('Ano de lançamento: '))
        if year < 0:
            print('Ano deve ser maior que 0')
            return
    except ValueError:
        print('ERRO: O ANO DEVE SER EM NÚMEROS')
    
    book = Livro(title, author, year)
    return book


def search():
    name = input('\nTítulo ou Autor: ')
    return name


sistem_users = SistemaUsuarios()
b = Biblioteca()
home()
    
    