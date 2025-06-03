extrato = []
class ContaBancaria:
    def __init__(self,titular, numero_conta, saldo):
        self.titular = str(titular)
        self.numero_conta = int(numero_conta)
        self.saldo= float(saldo)


    def deposito(self):
        v_deposito = float(input('Deposito: '))
        if v_deposito > 0:
            self.saldo += v_deposito            
            extrato.append(v_deposito)
            print(f'Deposito de R${self.saldo:.2f} efetuado')
        else:
            print('O valor deve ser positivo.')
        print('-'*30)
        

    def saque(self):
        v_saque= float(input('Saque: '))
        if v_saque > 0:
            if (v_saque <= self.saldo): 
                self.saldo -= v_saque
                extrato.append(v_saque)
                print('Saque realizado!')
            else:
                print(f'Saldo indisponível para saque.')
                print(f'Saldo disponível R${self.saldo:.2f}')
        print('-'*30)


    def dados_conta(self):
        print(f'Titular: {self.titular}')
        print(f'Conta: {self.numero_conta}')
        print(f'Saldo atual R${self.saldo:.2f}')
        print('-'*30)


    def extratos(self):
        print('Histórico de transação')
        for ex in extrato:
            print(f'R${ex:.2f}')    


user = ContaBancaria("Eliseu", 7070, 0.0)

user.deposito()
user.saque()
user.dados_conta()
user.extratos()
