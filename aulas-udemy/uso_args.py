def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


n1= int(input('Numero: '))
n2=int(input('Numero: '))
n3=int(input('Numero: '))
vezes=multiplicar(n1,n2,n3)
print(vezes)


def par_impar(numero):
    divisivel_de_dois = numero % 2 == 0

    if divisivel_de_dois:
        return f'{numero} é Par'
    return f'{numero} é Impar'


numero=int(input('Numero:'))
par_OU_impar=par_impar(numero)
print(par_OU_impar)