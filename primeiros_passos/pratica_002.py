n1=int(input('Digite um numero: '))
n2= int(input('Digite outro numero: '))
operacao= input('Digite uma operacao[+, -, *, /]: ')

if operacao == '+':
    operacao= n1 + n2
    print(f'Resultaddo {operacao}')
elif operacao == '-':
    operacao= n1 -n2
    print(f'Resultaddo {operacao}')
elif operacao == '*':
    operacao= n1 * n2
    print(f'Resultaddo {operacao}')
elif operacao == '/':
    operacao= n1 / n2
    print(f'Resultaddo {operacao}')