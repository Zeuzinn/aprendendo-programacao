# 🧩 Desafio: Detectar Palíndromos Numéricos
# Crie uma função que receba um número inteiro positivo e verifique se ele é um palíndromo — ou seja, se ele permanece o mesmo quando seus dígitos são invertidos.

# 🔍 Regras:
# O número será sempre inteiro positivo.

# A função deve retornar True se for palíndromo, False caso contrário.


def main():
    while True:
        try:
            numero =int(input('ENTRADA:'))
            msg = palindromo(numero)
        except ValueError:
            print('ERRO: DIGITE APENAS NÚMEROS.')
        
        print(msg)


def palindromo(numero):
    num_str = str(numero)
    if num_str == num_str[::-1]:
        msg = f'O {num_str} é palindromo'
    else:
        msg = f'O {num_str} não é palindromo'

    return msg


if __name__ =="__main__":
    main()