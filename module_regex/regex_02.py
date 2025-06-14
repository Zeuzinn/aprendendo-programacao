import re

# [^...] significa: qualquer caractere que NÃO seja letra.
# \w = letras/números, \s = espaços.
# Resultado: remove pontuação, mas mantém palavras e espaços.

texto = "A vida, é bela!"
limpo = re.sub(r"[^\w\s]", "", texto)
print(limpo)  # Saída: 'A vida é bela'


# Usando re.sub() para limpar e só então .split()
texto = "Hoje é sábado! Amanhã será domingo."
sem_pontuacao = re.sub(r"[^\w\s]", "", texto)
palavras = sem_pontuacao.split()
print(palavras)