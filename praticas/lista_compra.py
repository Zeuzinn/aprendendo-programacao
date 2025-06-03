#Lista de Compra
import os
lista_compra=[]

while True:
    print('Lista de Compra')
    print('1. Inserir \n2. Apagar \n3. Listar \n4. Sair ')
    opcao=input('Selecione uma opção: ')

    if opcao == '1':
        os.system('cls')
        inserir = input('Produto: ')
        lista_compra.append(inserir)

    elif opcao == '2':
        apagar=input('Escolha um indice para apagar: ')

        try:
            indice= int(apagar)
            del lista_compra[indice]
            print('Produto apagado.')
        except:
            print('Não foi possível apagar este indice.')
    

    elif opcao == '3':
        os.system('cls')
        for numero, item in enumerate(lista_compra):
            print(numero, item)
            
    elif opcao == '4':
        print('Fechando lista...')
        break
        