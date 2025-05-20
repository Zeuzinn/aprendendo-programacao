# Exercício: Contador de Palavras em um Texto
from collections import Counter

texto = input('Insira seu texto ou frase: ').lower()
contar_texto = Counter(texto.split())

print(contar_texto)

# Exercício: Verificador de Palíndromos

def palindromo(palavra):
    palavra_invertida = palavra [::-1]
    if palavra == palavra_invertida: 
        print('É palíndromo')
        return
    else:
        print('Não é palíndromo')
    
palavra = input('Digite uma palavra: ').lower()
palindromo(palavra)

# Exercício: Filtrando e Ordenando Nomes

nomes = ['Eliseu', 'Ana', 'Robson','Zorro','Caique','Abacuque','Reginaldo','Gaspar','Stuart','James','Alfredo']

# Filtrar nomes que começam com 'A' (maiúsculo ou minúsculo)
nomes_com_a = [nome for nome in nomes if nome.lower().startswith('a')]

# Ordenar a lista filtrada
nomes_com_a_ordenados = sorted(nomes_com_a)

print('Lista original: ', nomes)
print('Nomes que começam com "A" (ordenados): ', nomes_com_a_ordenados)