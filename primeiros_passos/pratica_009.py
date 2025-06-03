#PRÁTICA IMC
nome=input('Nome: ')
peso= float(input('Peso: '))
altura= float(input('Altura: '))
imc = peso/(altura*altura)

print(f'Olá {nome}, seu IMC é: {imc:.2f}')

if imc < 18.5:
    print('Classificação: Peso cuzinho')
elif imc < 24.9:
    print('Classificação: Peso Normal')
elif imc <29.9:
    print('Classificação: Propício a shape de pai')
elif imc < 34:
    print('Classificação: Shape de pai')
elif imc < 39.9:
    print ('Classificação: Shape de pai e panetone.')
else:
    print('Classificação: Nem academia ajuda')


#IMPRIMINDO PADRÃO

qtd_linhas= int(input('Quantidade de linhas: '))
for linha_1 in range(qtd_linhas):
    print('*')
    for linha in range(linha_1):
        print('*',end='')
        
    