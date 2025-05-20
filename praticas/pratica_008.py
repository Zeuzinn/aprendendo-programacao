def chegada(pessoas):
    for _ in range(2):
        pessoa = input('Nome: ')
        pessoas.append(pessoa)
    print('Pessoas adicionadas à fila.')


def atender(pessoas):
    if pessoas > 1:    
        print(f'{pessoas[0]} pessoa atendida.')
        del pessoas[0]
    elif pessoas:
        del pessoas[0], pessoas[1]
    else:
        print('Fila vazia! Ninguem para atender.')


def fila(pessoas):
    print('=== FILA ===')
    for pessoa in pessoas:
        print(pessoa)


def inicio():
    pessoas = []
    while True:
        chegada(pessoas)
        print()
        atender(pessoas)
        print()
        fila(pessoas)
        print()

inicio()