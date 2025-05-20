def adicionar_tarefa(tarefas, tarefa):
    tarefas.append(tarefa)
    print('Tarefa adicionada.')


def exibir_tarefas(tarefas):
    if not tarefas:
        print('Lista vazia.')
        return
    
    print('TAREFAS:')
    for t in tarefas:
        print(t)


def desfazer_tarefa(tarefas, tarefas_removidas):
    if not tarefas:
        print('Não posso desfazer essa tarefa, sua lista está vazia.')
        return
    
    tarefa_removida = tarefas.pop()
    tarefas_removidas.append(tarefa_removida)
    print('TAREFAS:')
    for t in tarefas:
        print(t)
    quebra_linha()
    print(f'Ultima tarefa removida com sucesso.')


def refazer_tarefa(tarefas, tarefas_removidas):
    if not tarefas_removidas:
        print('Não foi removida nenhuma tarefa')
        return
    
    tarefa_refeita = tarefas_removidas.pop()
    tarefas.append(tarefa_refeita)
    print('TAREFAS: ')
    for t in tarefas:
        print(t)
    quebra_linha()
    print('Tarefa refeita com sucesso.')


def quebra_linha():
    print()


def obter_comando():
    print('\nComandos: listar, desfazer, refazer')
    return input('Digite uma tarefa ou comando: ').lower()


def executar_comando(tarefas, tarefas_removidas, comando):
    
    if comando == 'listar':
        exibir_tarefas(tarefas)

    elif comando == 'desfazer':
        desfazer_tarefa(tarefas, tarefas_removidas)
        exibir_tarefas(tarefas)

    elif comando == 'refazer':
        refazer_tarefa(tarefas, tarefas_removidas)
        exibir_tarefas(tarefas)
    else:
        adicionar_tarefa(tarefas, comando)


def menu():
    tarefas = []
    tarefas_removidas = []

    while True:
        comando = obter_comando()
        executar_comando(tarefas, tarefas_removidas, comando)
        quebra_linha() 


if __name__ == "__main__":
    menu()