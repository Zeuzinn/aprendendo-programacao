# Lista numérica crescente e decrescente
lista = []

for i in range (5):
    n = int(input('Numero: '))
    lista.append(n)

print('Lista normal:', lista)
print('Lista crescente: ',sorted(lista))
print ('Lista decrescente: ', sorted(lista, reverse=True))
print()

lista_2 = [2, 6, 9, 7, 8, 1]

print('Lista normal:', lista_2)
print('Lista crescente: ',sorted(lista_2))
print ('Lista decrescente: ', sorted(lista_2, reverse=True))
print()

