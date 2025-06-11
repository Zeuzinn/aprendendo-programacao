# Desafio: Números Pares e Ímpares Separados
# Descrição:

# Crie um programa que:

# Peça para o usuário digitar 10 números inteiros (um por vez).

# Armazene os números em uma lista.

# Separe esses números em duas listas: uma contendo apenas os pares e outra contendo apenas os ímpares.

# Ao final, exiba as três listas: a original, a de pares e a de ímpares.

numbers = []
for _ in range(10):
    while True:
        try:
            number = int(input("Número: "))
            numbers.append(number)
            break
        except ValueError:
            print("Erro: Digite apenas números inteiros.")

pares =[par for par in numbers if par % 2 == 0]
impares =[impar for impar in numbers if impar % 2 !=0]

print("Números digitados: ",numbers)
print("Números pares: ",pares)
print("Números impares: ",impares)