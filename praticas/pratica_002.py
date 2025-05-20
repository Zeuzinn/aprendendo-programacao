def contar_ate_dez():
    for n in range(1,11):
        print(n)

contar_ate_dez()
print()


def tabuada(numero):
    for n in range(1,11):
        print(f'{numero} x {n} = {n*numero}')

numero=int(input('Numero: '))
tabuada(numero)
print()


def somar_numeros():
    soma = 0
    for n in range(5):
        num_1 = int(input('Números: '))
        soma += num_1
    print(soma)

somar_numeros()
print()


def caracteres_palavra():
    palavra = input('Palavra: ')
    for p in palavra:
        print(p)

caracteres_palavra()


def contar_pares():
    lista=[]
    for _ in range(1,11):
        numeros= int(input('Número: '))
        lista.append(numeros)
    
    print('números pares digitados:')
    for pares in lista:
        if pares % 2 == 0:
            print(pares)
        

contar_pares()
