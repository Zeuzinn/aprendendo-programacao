contagem_letra ={}
s = 'mamaco'
for l in s:
    if 'a' <= l <= 'z':
        contagem_letra['letra']= contagem_letra.get(l, 0) +1

letras = []
for letra, contagem in contagem_letra.items():
    if contagem == 1:
        letras.append(letra)
    
print(letra)