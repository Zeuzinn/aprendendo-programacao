# Desafio: Alunos Aprovados
# Descrição:

# Crie um programa que:

# Peça ao usuário para informar o nome de 3 alunos.

# Para cada aluno, peça duas notas (valores de 0 a 10).

# Armazene as informações de cada aluno (nome e média das notas).

# Ao final, exiba:

# A lista de alunos com suas médias.

# Apenas os alunos com média maior ou igual a 7, marcados como "Aprovado"

def calcular_media(nota_1:float, nota_2:float):
    return (nota_1 + nota_2) / 2


alunos = []
for _ in range(3):
    while True:
        try:
            nome = input('Nome: ').title()
            nota_1 = float(input("Nota: "))
            nota_2 =float(input("Nota: "))
            
            if nota_1 <= 10 and nota_2 <= 10:
                total_nota = calcular_media(nota_1, nota_2)
                alunos.append({'nome':nome, 'notas': total_nota})
                print("Aluno cadastrado!")
                print()
                break
            else:   
                print("Erro: as notas devem ser entre 0 e 10")  

        except ValueError:
            print("Erro: Deve ser digitados apenas números.")

for aluno in alunos:
    status = "Reprovado" if aluno['notas'] < 7 else "Aprovado"    
    print(f"Aluno: {aluno['nome']} | Média: {aluno['notas']} - Status: {status}")
        
        