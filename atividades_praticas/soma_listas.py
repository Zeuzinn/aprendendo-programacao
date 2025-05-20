# 1º Solução
lista1= [3, 5, 1, 19, 10, 15]
lista2= [1, 3, 6, 2]

soma = [
    x + y for x, y in zip(lista1, lista2)
    ]
print(soma)
print()

# 2º Solução
lista_somada=[]
for i in range(len(lista2)):
    lista_somada.append(lista1[i] + lista2[i])
print(lista_somada)
print()

#3º Solução
lista_somada_2=[]
for i, _ in enumerate(lista2):
    lista_somada_2.append(lista1[i] + lista2[i])
print(lista_somada_2)