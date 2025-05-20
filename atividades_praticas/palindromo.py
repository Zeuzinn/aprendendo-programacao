def palindromo(mensagem):
    palavra_invertida = mensagem [::-1]
    if mensagem == palavra_invertida:
        print(f'A palavra {mensagem} palíndromo.')
        print(f'Palavra invertida: {palavra_invertida}')
    else:
        print(f'A palavra {mensagem} não é palíndromo.')
        print(f'Palavra invertida: {palavra_invertida}')


mensagem= input('Palavra: ').lower()
palindromo(mensagem)
