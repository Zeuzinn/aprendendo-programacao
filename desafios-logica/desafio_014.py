# 💡 Desafio: Somando Dígitos Pares
# Crie uma função em Python que recebe um número inteiro positivo e retorna a soma de todos os dígitos pares desse número.

# 📋 Regras:
# O número será sempre inteiro positivo.

# Os dígitos ímpares devem ser ignorados.

# A função deve retornar a soma dos dígitos pares encontrados.


def numeros_positivos():
    try:
        numero = int(input('Entrada: '))
        soma = par_impar(numero)
    except ValueError:
        print('ERRO: DIGITE APENAS NÚMEROS')
    
    resultado(soma)

def par_impar(numero):
    soma = 0

    for digito in str(numero):
        if int(digito) % 2 == 0:
            soma += int(digito)
    return soma

def resultado(soma:int):
    print('RESULTADO:', soma)


if __name__ == "__main__":
    numeros_positivos()