lista= []
for n in range(3):
    nome = input('Nome: ')
    nota_1 = float(input('Nota: '))
    nota_2 = float(input('Nota: '))
    nota_3 = float(input('Nota: '))
    lista.append({'nome': nome, 'nota1': nota_1, 'nota2': nota_2,'nota3': nota_3})
    print()

print('\nRESULTADOS:')
for aluno in lista:
    notas = [aluno['nota1'], aluno['nota2'], aluno['nota3']]
    media = sum(notas) / 3
    print(notas)

    print(f"Aluno: {aluno['nome']}")
    print(f"Notas: {notas[0]}, {notas[1]}, {notas[2]}")
    print(f"Média: {media:.2f}")

    if media < 5:
        print("❌ Reprovado\n")
    elif media < 7:
        print("⚠ Recuperação\n")
    else:
        print("✅ Aprovado\n")
