# 🧠 Desafio: Números Mágicos
# Crie um programa que:

# Peça ao usuário para digitar um número inteiro positivo.
# Verifique se o número é par ou ímpar.
# Verifique se o número é múltiplo de 3.
# Exiba uma mensagem personalizada com base nas verificações.

# 💡 Exemplo de saída:
# Se o usuário digitar 9, o programa deve imprimir:
# O número 9 é ímpar e múltiplo de 3. Isso é mágico!

# Se digitar 8, o programa deve imprimir:
# O número 8 é par e não é múltiplo de 3.


def colect_number():
    try:
        number = int(input('Digite um número: '))
        if number <0:
            print('Erro: Digite um número positivo.')
            return
    except ValueError:
        print('Erro: dígite apenas números')
        return
    
    verify_number(number)


def verify_number(number):
    par_or_impar = "par" if number % 2 == 0 else "ímpar"
    multiple_3 = number % 3 == 0

    if multiple_3:
        print(f'O número {number} é {par_or_impar} e múltiplo de 3. Isso é mágico!\n')
    else:
        print(f'O número {number} é {par_or_impar} e não é múltiplo de 3.\n')

while True:
    colect_number()