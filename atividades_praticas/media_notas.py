media = 0
contador = 0
while True:
    
    nota= int(input(f"Nota {contador+1} : "))
    
    if nota <= 10:
        contador +=1
        media += nota
        print('Nota registrada!')
        print()
    else:
        print('Nota deve ser entre 10 e 0')
        print()

    if contador == 3 : 
        break
    

resultado = media /contador
if resultado >=7:
    print(f'Sua média é {resultado:.1f}')
    print('Aprovado')
else:
    print(f'Média: {resultado:.1f}')
    print('Reprovado')