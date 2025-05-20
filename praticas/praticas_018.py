# List Comprehension 

# Números pares
pares = [ x for x in range(20) if x % 2 == 0]
print(pares)
print()

# Palavras com mais de 4 letras
palavras = ['cão', 'girassol','sol','montanha','lua','computador','macaco']
letras = [palavra for palavra in palavras if len(palavra) >= 4]
print(letras)
print()

# Quadrado dos ímpares
quadrado = [x**2 for x in range(1,16) if x % 2 != 0]
print(quadrado)
print()

# Dobro dos números multiplos de 3
dobro = [ x*2 for x in range(0,30) if x % 3 == 0]
print(dobro)
print()

# Palavras com letra "a"
frutas = ["maçã", "banana", "kiwi", "abacaxi", "pera", "melão", "ameixa"]

letra_a = [ palavra for palavra in frutas if 'a' in palavra]
print(letra_a)

# Letras maiúsculas da string
texto = "Programar em Python é divertido"
maiusculas = [letra for letra in texto if letra.isupper()]
print (maiusculas)


palavras = ["python", "java", "go", "typescript"]

comprimento = [(palavras['palavras'])]