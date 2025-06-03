soma = 0
n = int(input("Quantos números você deseja somar? "))
for i in range(n):
    num = int(input("Informe o número: ".format(i+1)))
    soma += num
print("Soma:", soma)


alunos = ["João", "Maria", "Pedro"]
distancias = [100, 200, 300]

for i in range(len(alunos)):
    print("Aluno:", alunos[i])
    print("Distância percorrida:", distancias[i], "metros")
    print("-------------------------")


alunos = ["João", "Maria", "Pedro"]
distancias = [100, 200, 300]

for aluno, distancia in zip(alunos, distancias):
    print("Aluno:", aluno)
    print("Distância percorrida:", distancia, "metros")
    print("-------------------------")
    

#Exemplo 1: Encontrar o número maior em uma lista

numeros = [12, 45, 7, 23, 56, 89, 34]
maior = numeros[0]
for numero in numeros:
    if numero > maior: 
        maior = numero
print("O número maior é:", maior)

