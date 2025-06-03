lista_tarefa = []

while True:
    print('Menu:')
    print('1. Adicionar tarefa')
    print('2. Tarefa Concluída')
    print('3. Listar tarefas pendentes')
    print('4. Sair')
    
    menu= input('Opção: ')
    if menu == '1':
        adicionar_tarefa= input('Descrição da tarefa: ')
        lista_tarefa.append(adicionar_tarefa)
    elif menu == '2':
        apagar= input('Qual tarefa deseja apagar: ')
        
        try:
            numero= int(apagar)
            del lista_tarefa[numero]
            print('Tarefa concluída.')
        except IndexError:
            print('Você não tem essa tarefa numerada, por favor verifique sua lista de tarefas.')
        except ValueError:
            print('DIGITE APENAS NÚMEROS')   

    elif menu == '3':
        print('Tarefas pendentes: ')
        for tarefa in enumerate(lista_tarefa):
            print(f'- {tarefa}')
    else:    
        print('Fechando programa...')
