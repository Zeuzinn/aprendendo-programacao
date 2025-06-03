def soma_numeros():
    soma = 0
    while True:
        numero = int(input("Digite um número (ou um número negativo para parar): "))
        if numero < 0:
            break  # Sai do loop se o número for negativo
        soma += numero  # Adiciona o número à soma
    return soma

# Chama a função e exibe o resultado
resultado = soma_numeros()
print("A soma dos números digitados é:", resultado)