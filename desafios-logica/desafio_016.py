# 🚦 Desafio: Semáforo de Números
# Crie uma função que recebe uma lista de números inteiros e classifica cada número como:

# 'verde' se o número for par e positivo

# 'amarelo' se o número for ímpar

# 'vermelho' se o número for negativo


def semafaro(numbers:list):
    for number in numbers:
        if number < 0:
            msg = f'{number} - Vermelho'
            print(msg)
        elif number % 2 != 0:
            msg = f'{number} - Amarelo'
            print(msg)
        else:
            msg = f'{number} - Verde' 
            print(msg)

numbers = [5,-9,15,6,117,-115,-21,36]
semafaro(numbers)
