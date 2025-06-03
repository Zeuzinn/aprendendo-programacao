#Agenda Telefônica
agenda={}
while True:
    print('1. Adicionar contato')
    print('2. Buscar contato')
    print('3. Remover contato')
    print('4. Listar')
    print('5. Sair')
    opcao= input('Escolha uma opção: ')
    
    if opcao == '1':
        nome=input('Nome: ')
        telefone=input('Telefone: ')
        agenda[nome]= telefone
    elif opcao == '2':
        nome= input('Contato: ')
        if nome in agenda:
            print('Telefone: ', agenda[nome])
        else:
            print('Este nome não está em sua agenda.')
    elif opcao == '3':
        nome=input('Qual contato deseja remover? ')
        if nome in agenda:
            del agenda[nome]
            print('Contato removido.')
    elif opcao == '4':
        if len(agenda)>0:
            for nomes, telefones in agenda.items():
                print(nomes + ": " + telefones)
        else:
            print('Agenda vazia')
    elif opcao == '5':
        print('Fechando agenda...')
        break