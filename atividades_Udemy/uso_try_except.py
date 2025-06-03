numero_str=input('Numero: ')

try:
    numero1= float(numero_str)
    print (f'O dobro de {numero_str} e {numero1* 2:.0f}')
except:
    print('Nao e um numero')