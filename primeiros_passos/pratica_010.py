turma_1 = []
distancia_1 = []
maior = distancia_1[0]
#Turma 1 
soma_km1=0
for t_1 in range(3):
    nome= input(f"{t_1+1} Nome: ")
    km_1 = int(input('Distância percorrida: '))
    soma_km1 +=km_1
    turma_1.append(nome)
    distancia_1.append(km_1)
print(f'Maior distância percorrida é {maior}')



