# Filtragem de dados com base em valores ausentes
import pandas as pd

d = pd.read_csv("praticas-com-python/module_pandas/atividades/employees.csv")

# isnull() é usada na coluna "Gênero" para filtrar e imprimir linhas que contêm dados de gênero ausentes.
bool_series = pd.isnull(d["Gender"])
missing_gender_data = d[bool_series]

print(missing_gender_data)