saldo = 0

while True:

    print('Conta Bancária')
    print('1. Depósito.')
    print('2. Saque.')
    print('3. Verificar saldo.')
    op=input('Operação: ')
    if op == "1":
        deposito= float(input('Depósito: '))
        saldo = saldo + deposito
        print(f'Depósito de R${deposito:,.2f} reais efetuado')  
    elif op == "2":
        saque= float(input('Saque: '))
        if saque <= saldo:
            saldo= saldo - saque
            print('Saque realizado')
        else:
            print('Não será possível realizar essa operação.')
    elif op == "3":
        print(f'Saldo R${saldo:,.2f}')
        