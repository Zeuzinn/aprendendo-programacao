funcionarios = []

for _ in range(2):
    nome= input('Nome completo: ')
    cargo= input('Cargo: ')
    salario= float(input('Salário R$: '))
    funcionarios.append({'nome': nome, 'cargo': cargo,'salario': salario})
    print()

print('\n====LISTA DE FUNCIONÁRIOS:====\n')
for funcionario in funcionarios:
    print(f"Nome: {funcionario['nome']}") 
    print(f"Cargo: {funcionario['cargo']}") 
    print(f"Salário R${funcionario['salario']:,.2f}")

    if funcionario['salario'] < 2000: 
        print('Salário abaixo da média.')
        print()
    elif funcionario['salario'] < 5000:
        print('Salário dentro da média')
        print()
    else:
        print('Salário acima da média')
        print()
