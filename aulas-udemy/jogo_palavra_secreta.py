import random

def linha():
    print('-' *30)

lista_sec = ['carro', 'computador', 'tigre', 'controle', 'televisao', 'futebol', 'bandeira', 'torcida', 'velocidade']
num=random.randint(0, len(lista_sec))
palavra_secreta = lista_sec[num]
letras_acertadas = ''
letras_acertadas_2 = ''
jogador_1 = 0
jogador_2 = 0

print('Bem vindo ao jogo da Palavra Secreta.')
linha()
print(f'Dicas: \n1- Uma letra por jogador; \n2- Apenas letras minúsculas. \nTente se for capaz!')
linha()
nome1= input('Jogador 1: ')
nome2= input('Jogador 2: ')
linha()

while True:
    letra_d= input(f'{nome1} digite uma Letra: ')
    letra_d2= input(f'{nome2} digite uma Letra: ')
    jogador_1 += 1
    jogador_2 += 1

    if len(letra_d) > 1:
        print(f'{nome1} Digite apenas uma letra!')
        linha()
        continue

    if len(letra_d2) > 1:
        print(f'{nome2} Digite apenas uma letra!')
        linha()
        continue

    if letra_d in palavra_secreta:
        letras_acertadas += letra_d

    if letra_d2 in palavra_secreta:
        letras_acertadas_2 += letra_d2

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra formada de {nome1} =',palavra_formada)
    linha()

    palavra_formada_2 = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas_2:
            palavra_formada_2 += letra_secreta
        else:
            palavra_formada_2 += '*'

    print(f'Palavra formada de {nome2} =', palavra_formada_2)
    linha()

    if palavra_formada == palavra_secreta:
        print(f'Parabéns {nome1}! Você ganhou!')
        print(f'A palavra escondida era: {palavra_formada}')
        print(f'Tentativas: {jogador_1}')
    if palavra_formada_2 == palavra_secreta:
        print(f'Parabéns {nome2}! Você ganhou!')
        print(f'A palavra escondida era: {palavra_formada_2}')
        print(f'Tentativas: {jogador_2}')
        break