# Desafio: Contador de Vogais e Consoantes
# Descrição:

# Crie um programa que:

# Peça ao usuário que digite uma palavra ou frase.

# Conte e exiba:

# Quantas vogais existem no texto.

# Quantas consoantes existem no texto.

# Ignore espaços, números e pontuações — considere apenas letras do alfabeto.

# Não diferencie maiúsculas de minúsculas (ou seja, A e a contam como vogal).


vogais =""
consoantes =""

frase= input("Frase ou Palavra: ").lower()
for f in frase:
    
    if f.isalpha():
        if f in "aeiou":
            vogais += f
        else:
            consoantes += f

print("vogais:",len(vogais))
print("consoantes:",len(consoantes))