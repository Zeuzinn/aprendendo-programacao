tarefas= []
tarefas_removidas = []
while True:
    
    print('Comandos: listar, desfazer, refazer')
    nome_tarefa= input('Digite uma tarefa ou comando: ')
    tarefa = nome_tarefa.lower()
    print()

    if tarefa != 'listar' and tarefa != 'desfazer' and tarefa != 'refazer':
        tarefas.append(tarefa)
        print('Tarefa adicionada.')

    elif tarefa == 'listar':    
        if not tarefas:
            print('Lista vazia.')
        else:
            for t in tarefas:
                print (t)

    elif tarefa == 'desfazer':
        if not tarefas:
            print('Não posso desfazer essa tarefa, sua lista está vazia.')

        else:
            tarefas_removida = tarefas.pop()
            tarefas_removidas.append(tarefas_removida)
            print(f'Removemos: {tarefas_removida}')
            print(f'Ultima tarefa removida com sucesso.')

    elif tarefa == 'refazer':
        if not tarefas_removidas:
            print('Não foi removida nenhuma tarefa')
        else:
            tarefa_refeita = tarefas_removidas.pop()
            tarefas.append(tarefa_refeita)
            print(f'Tarefa refeita: {tarefa_refeita}')
            print('Tarefa refeita com sucesso.')
