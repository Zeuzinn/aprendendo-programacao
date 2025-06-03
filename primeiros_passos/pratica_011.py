usuarios = {
        "Eliseu": {"senha": "123" , "saldo": 0}
}

login= input('Login: ') 
senha= input('Senha: ')

user = usuarios["Eliseu"]
password = usuarios["Eliseu"]["senha"]


if login == "Eliseu" and senha == "123":
    print('Acesso liberado.')
    while True:
        print(f'Olá, {login}! Seja bem vindo ao caixa eletrônico.')
        print('1. Saldo \n2. Deposito \n3. Saque \n4. Sair')
        operacao=input('Escolha uma operação: ')
    
        if operacao == '1':
            print(usuarios)
        elif operacao == '2':
            print('Deposito')
        elif operacao == '3':
            print('Saque')
        elif operacao == '4':
            print('Encerrando...')
            break    
elif login != "Eliseu":
    print('Login inválido!')
elif senha != "123":
    print('Senha inválida!')
    

    
