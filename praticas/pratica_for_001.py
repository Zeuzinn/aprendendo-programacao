# Mostra o maior número digitado
maior = 0 
for n in range (5):
    numero= int(input('Numero: '))
    if numero > maior:
        maior = numero
print(maior)


lista = ["maçã", "banana", "laranja"]
for i in range(len(lista)):  # Itera sobre os índices da lista
    print(i, lista[i])  # [0] maçã, [1] banana, [2] laranja


lista_1 = ["maçã", "banana", "laranja"]
for fruta in lista_1:  # Itera sobre os elementos da lista
    print(fruta)  # maçã, banana, laranja