def adicionar_aluno(alunos):
    nome=input('Nome completo: ')
    idade= int(input('Idade do aluno: '))
    curso= input('Curso do aluno: ')
    aluno = {'nome': nome, 'idade': idade, 'curso': curso}
    alunos.append(aluno)


def listar_alunos(alunos):
    if not alunos:
        print('Nenhum aluno cadastrado.')
    else:
        for aluno in alunos:
            print(f'Nome: {aluno['nome']}, idade: {aluno['idade']}, curso: {aluno['curso']}')


def buscar_aluno(alunos):
    buscar_nome = input('Nome: ')
    for aluno in alunos:
        if aluno['nome'] == buscar_nome:
            print(f'Nome: {aluno['nome']}, idade: {aluno['idade']}, curso: {aluno['curso']}') 
    
    print('Aluno não encontrado')


def remover_aluno(alunos):
    excluir_aluno = input('Aluno que deseja remover: ')
    for aluno in alunos:
        if aluno['nome'] == excluir_aluno:
            alunos.remove(aluno)
            print('Aluno removido com sucesso.')
        if not aluno['nome']:
            print('Não é possível remover aluno que não existe')


def exibir_menu():        
    print('1. Adicionar aluno.')
    print('2. Listar aluno.')
    print('3. Buscar aluno.')
    print('4. Remover aluno.')
    print('5. Atualizar curso.')


def main():
    alunos = []
    while True:
        exibir_menu()
        opcao = input('Escolha uma opção: ')
        if opcao == "1":
            adicionar_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            buscar_aluno(alunos)
        elif opcao == "4":
            remover_aluno(alunos)
        elif opcao == "5":
            ...
        else:
            print('Opção Inválida.')

main()