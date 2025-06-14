import string
import re
# O que ele faz:

# r"\w+" significa: pegue letras, números ou underlines seguidos.
# Ou seja, pegou todas as palavras, ignorando a pontuação.

texto = "Hoje é sábado! Amanhã será domingo."
resultado = re.findall(r"\w+", texto)

print(resultado)

# Outra forma com import string
texto = "Hoje é sábado! Amanhã será domingo."
palavras = texto.split()
limpas = [p.strip(string.punctuation) for p in palavras]
# Resultado: ['Hoje', 'é', 'sábado', 'Amanhã', 'será', 'domingo']
print(limpas)

sem_letras = re.findall(r"[^a-zA-Z]", "abc123!@#")
print(sem_letras)
# Nesse caso, [^a-zA-Z] significa: qualquer caractere que NÃO seja letra.
# Resultado: ['1', '2', '3', '!', '@', '#']