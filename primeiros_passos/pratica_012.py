#Simulador Caixa Eletrônico
def lin():
    print('')

saldo = 0
while True:
    nome = input("Digite seu nome: ")
    lin()
    print(f'Olá, {nome}! Seja bem vindo ao caixa eletrônico.')
    print(f'Seu saldo atual é R${saldo:.2f}')
    lin()
    print("Escolha a operação que deseja fazer:")
    print("1- Depositar dinheiro.")
    print("2- Sacar dinheiro.")
    print("3- Verificar saldo.")
    print("4- Sair do sistema.")
    lin()
    op = input("Escolha uma operação: ")
    if op == '1':
        deposito = float(input("Digite o valor do deposito R$ "))
        saldo = saldo + deposito
        print('Depósito efetuado. Encerrando...')
    elif op == '2':
        saque= float(input("Digite o valor do saque R$ "))
        saldo = saldo - saque
        if saldo <= saque:
            print("Não é possível sacar o valor maior que seu saldo atual.")
    elif op == '3':
        print(f'Saldo atual R${saldo:.2f}')
    elif op == '4':
        print("Saindo do sistema.")
        break
