def verificar_numero(numero):
    if numero > 0:
        print('Número positivo.')
    elif numero == 0:
        print('Número é zero')
    else:
        print('Número negativo')


num= int(input("Número: "))
verificar_numero(num)
print()


def par_impar(numero):
    if numero % 2 == 0:
        print('Par')
    else:
        print('Impar')

num_2= int(input("Número: "))
par_impar(num_2)
print()


def comparar_numero(numero_1, numero_2):
    if numero_1 == numero_2:
        print('Os números são iguais.')
    elif numero_1 > numero_2:
        print(f'O número {numero_1} é maior.')
    else:
        print(f'O número {numero_2} é maior')

num_3= int(input("Número: "))
num_4= int(input("Número: "))
comparar_numero(num_3, num_4)
print()


def votar(idade):
    if idade >= 16:
        print('Você já pode votar')
    else:
        print('Você não pode votar.')

num_5= int(input("Número: "))
votar(num_5)
print()


def verificar_senha(s):
    senha = "1234"
    if s != senha:
        print('Senha inválida.')
    else:
        print('Senha válida.')

s = input('Senha: ')
verificar_senha(s)