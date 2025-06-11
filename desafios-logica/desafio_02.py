import random

number_secret= random.randint(1,10)
tentativa = 0

while True:

    print("Adivinhe o número secreto")
    try:
        number = int(input("Número: "))
        tentativa +=1
    except ValueError:
        print("Digite apenas número")
    print()
    if number == number_secret:
        print("Você acertou o número secreto, parabéns!")
        print('Tentativas:', tentativa)
        break
    elif number < number_secret:
        print("Tente um número maior")
    elif number > number_secret:
        print("Tente um número menor")
