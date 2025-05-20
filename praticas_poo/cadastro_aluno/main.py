from cadastro_alunos import Aluno

def menu():
    print('=== MENU ===')
    print('1. Cadastrar aluno')
    print('2. Listar alunos')
    print('3. Sair')
    

def cadastrar_aluno():
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    nota = float(input('Nota: '))
    aluno = Aluno(nome, idade, nota)
    lista_aluno.append(aluno)
    print('Aluno cadastrado!')
    

def mostar_alunos():
    if not lista_aluno:
        print('Nenhum aluno cadastrado.')
    else:
        for i,aluno in enumerate(lista_aluno, 1):
            print(f'Aluno - {i}')
            aluno.mostrar_dados()


lista_aluno = []
while True:
    menu()
    opcao = input('Selecione a opção: ')
    print()
    if opcao == '1':
        cadastrar_aluno()
        print()
    elif opcao =='2':
        mostar_alunos()
        print()      
    elif opcao == '3':
        print('Fechando o programa...')
        break
    else:
        print('Opção errada!')


