def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2
    else:
        print('Operacao invalida!')

n1= int(input('1° numero: '))
n2= int(input('2° numero: '))
op= input('Operacao: ')
resultado=calculadora(n1, n2, op)
print(resultado)