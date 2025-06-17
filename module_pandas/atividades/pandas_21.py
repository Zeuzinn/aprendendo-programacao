import pandas as pd
d = pd.read_csv("praticas-com-python/module_pandas/atividades/employees.csv")

# notnull() é usada na coluna "Gênero" para filtrar e imprimir linhas contendo dados de gênero ausentes.
nmg = pd.notnull(d["Gender"])


nmgd= d[nmg]

print(nmgd)