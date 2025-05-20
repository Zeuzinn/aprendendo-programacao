from itertools import groupby

alunos = [
    {'nome': 'Zeuzin', 'nota':'10'},
    {'nome': 'Cuzin', 'nota':'3'},
    {'nome': 'Antedeguemon', 'nota':'10'},
    {'nome': 'Robson', 'nota':'7'},
    {'nome': 'Flabeu', 'nota':'10'},
    {'nome': 'Soldier', 'nota':'5'},
    {'nome': 'Flakes', 'nota':'7'},
]

# Essa função ordena os alunos pela chave 'nota'
def ordena(aluno):  
    return aluno['nota']


# 'Key' é a chave que vou usar do dicionário, ou seja, 'nota' passar pra função 'ordena'
alunos_agrupados= sorted(alunos, key=ordena)  

# 'Groupby' serve para agrupar os alunos ordenados por 'nota'. 
# Novamente, a função ordena é usada como chave para o agrupamento. 
# Isso agrupará os alunos que têm a mesma nota.
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)