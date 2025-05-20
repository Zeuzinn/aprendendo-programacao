def menu():
    print('[1] adicionar tarefa')
    print('[2] Listar tarefa')
    print('[3] Marcar tarefa concluída')
    print('[4] Excluir tarefa')
    print('[5] Sair')
    print()


def adicionar_tarefa(tarefas):
    tarefa = input('Digite sua tarefa: ').lower()
    descricao = input('Digite a descrição: ').lower()
    tarefas.append({'tarefa': tarefa, 'descricao' : descricao, 'concluida': False})
    print('Tarefa adicionada! ')


def mostrar_tarefa(tarefas):
    if not tarefas:
        print('Lista de tarefa está vazia.')
        adicionar_tarefa(tarefas)
    else:
        for tarefa in tarefas:
            print(f'Tarefa: {tarefa['tarefa']} \nDescrição: {tarefa['descricao']} \nConluída: {tarefa['concluida']}')


def concluir_tarefa(tarefas):
    if not tarefas:
        adicionar_tarefa(tarefas)
    else:
        tarefa = input('Nome da tarefa: ').lower()
        for t in tarefas:
            if tarefa not in t['tarefa']:
                print('Não tem essa tarefa')
            if t['tarefa'] == tarefa:
                t['concluida'] = True
                print(f'A tarefa: {t['tarefa']} foi marcada como concluída - {t['concluida']}')
            

tarefas=[]
while True:
    menu()
    opcao = input('Escolha uma opção: ')
    print()
    if opcao == '1':
        adicionar_tarefa(tarefas)
        print()
    elif opcao == '2':
        mostrar_tarefa(tarefas)
        print()
    elif opcao == '3':
        concluir_tarefa(tarefas)
        print()
    elif opcao == '4':
        ...
    elif opcao == '5':
        break
    else:
        print('Opção inválida!')