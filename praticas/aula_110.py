def soma():
    numero_1 = int(input('Digite um número: ')) 
    numero_2 = int(input('Outro numero: '))
    print('Resultado: ', numero_1 + numero_2)


def subtrair():
    numero_1 = int(input('Digite um número: ')) 
    numero_2 = int(input('Outro numero: '))
    print('Resultado: ', numero_1 - numero_2)


def multiplicar():
    numero_1 = int(input('Digite um número: ')) 
    numero_2 = int(input('Outro numero: '))
    print('Resultado: ', numero_1 * numero_2)


def dividir():
    numero_1 = int(input('Digite um número: ')) 
    numero_2 = int(input('Outro numero: '))
    print('Resultado: ', numero_1 / numero_2)


while True:
    print('\n=== CALCULADORA ===\n' )
    print('1- SOMA')
    print('2- SUBTRAIR')
    print('3- MULTIPLICAR')
    print('4- DIVIDIR')
    print('5- SAIR')
    opcao = input('Escolha uma operação: ')
    print('-'*30)
    if opcao == '1':
        soma()
    elif opcao == '2':
        subtrair()
    elif opcao == '3':
        multiplicar()
    elif opcao == '4':
        dividir()
    elif opcao == '5':
        print('Fechando calculadora')
        break
    else:
        print('OPÇÃO INVÁLIDA!')