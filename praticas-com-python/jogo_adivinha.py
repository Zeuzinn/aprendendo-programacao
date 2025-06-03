import random

num=random.randint(1,100)
contador = 0

print("Seja bem vindo ao jogo do adivinha.")
print("Você deve acertar o numero escondido entre 1 e 100.")
print()
while True:
    palpite = int(input("Palpite: "))
    if palpite < num:
        contador += 1
        print("Tente um numero maior!")
    elif palpite > num:
        contador += 1
        print("Tente um numero menor!")
    else:
        print(f'Parabens! Você acertou em {contador} tentativas')
        break
