import random

def dezena():
    numero = random.randint(0, 99)
    n1 = int(input('Digite sua dezena (00 a 99): '))
    
    if n1 == numero:
        print(f'NÚMERO SORTEADO (dezena): {numero:02d}')
        print('Parabéns! Você acertou a dezena!')
    else:
        print('Não foi dessa vez!')

def centena():
    numero = random.randint(0, 999)
    n1 = int(input('Digite sua centena (000 a 999): '))
    
    if n1 == numero:
        print(f'NÚMERO SORTEADO (centena): {numero:03d}')
        print('Parabéns! Você acertou a centena!')
    else:
        print('Não foi dessa vez!')


def milhar():
    numero = random.randint(0, 9999)
    print(f'NÚMERO SORTEADO (milhar): {numero:04d}')
    n1 = int(input('Digite sua milhar (0000 a 9999): '))

    if n1 == numero:
        print('Parabéns! Você acertou a milhar!')
        print(f'NÚMERO SORTEADO (milhar): {numero:04d}')
    else:
        
        print('Não foi dessa vez!')


while True:
    print('\n=== JOGO DO BICHO ===\n')
    print('[1] Realizar jogo')
    print('[2] Sair')
    opcao = input('Escolha uma opção: ')
    print()
    if opcao == '1':
        while True:
            print('[1] Dezena')
            print('[2] Centena')
            print('[3] Milhar')
            opcao_2 = input('Escolha o que deseja jogar')
            print()
            if opcao_2 == '1':
                dezena()
            elif opcao_2 == '2': 
                centena()
            elif opcao_2 == '3': 
                milhar()
            else:
                print('Opção inválida!')
    elif opcao == '2':
        print('Encerrando jogo.')
        break  
    else:
        print('Opção inválida!')