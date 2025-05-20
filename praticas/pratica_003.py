alunos=[]

for i in range (2):
    nome= input('Nome: ')
    idade= int(input('Idade: '))
    nota= float(input('Nota: '))
    alunos.append({'nome': nome, 'idade': idade, 'nota': nota})
    print()

for aluno in alunos:
    if aluno['nota'] > 7:
        print(
            f"O aluno {aluno['nome']} com a nota: {aluno['nota']:.1f}"
        )