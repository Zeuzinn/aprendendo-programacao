notas= []
contador = 1
while contador <=3:
    cda= input("Nome aluno: ")
    nota= float(input("Nota do aluno: "))
    result= [cda, nota]
    notas.append(result)
    contador= contador + 1
print("Quantidade de notas: ",len(notas))
print(notas)