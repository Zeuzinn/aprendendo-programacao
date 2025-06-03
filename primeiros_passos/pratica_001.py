nota = []
contador = 0
soma = 0
while contador <= 4:
    contador = contador + 1
    nota= int(input("Nota: "))
    soma = nota + soma
print(f'A media e: {soma/contador:.2f}')
