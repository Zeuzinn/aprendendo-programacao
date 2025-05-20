# Tabuada
numero=int(input('Numero: '))
for t in range (1,11):
    print(f'{numero} x {t} = {t*numero}')
print('-'*30)

#Pares
soma = 0
for n in range (5):
    num = int(input('Numero: '))
    if num % 2 == 0:
        soma+=num
print(soma)
print('-'*30)

# Contegem regressiva
contagem_regressiva = int(input('Numero: '))
for c_r in range (contagem_regressiva):
    print(contagem_regressiva - c_r)
print('-'*30)

# Lista de compra
lista_compras = []
for l in range(1,4):
    compras = input('Lista de compras: ')
    lista_compras.append(compras)
    print('Adicionado!')
    for l_c in lista_compras:
        print(l_c)
print('-'*30)

