#Atividade 1 
nome = str(input('Nome completo: ')).strip()
divido = nome.split()
print(f'Nome maiúsculo: {nome.upper()}')
print(f'Nome minúsculo: {nome.lower()}')

#Remoção dos espaços
print(f'Quantidade de letras: {len(nome)- nome.count(' ')} letras')
print(f'Primeiro nome tem: {len(divido[0])}letras')

#Atividade 2 
frase = input('Frase: ')
frase_invertida = frase[::-1]
print(frase.lower())
print(frase_invertida)

#Atividade 3
#Mostrando numeros
num = int(input('Numero: '))
print(f'Unidade: {num // 1 %10}')
print(f'Dezena: {num // 10 %10}')
print(f'Centena: {num // 100 %10}')
print(f'Milhar: {num // 1000 %10}')
