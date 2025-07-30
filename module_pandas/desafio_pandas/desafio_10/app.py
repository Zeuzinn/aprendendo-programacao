import pandas as pd

pd.options.display.float_format = "R${:,.2f}".format
csv_funcionarios = "praticas-com-python/module_pandas/desafio_pandas/desafio_10/funcionarios.csv"
df = pd.read_csv(csv_funcionarios)


df = df.fillna(0)

# Converta a coluna data_admissao
df['data_admissao'] = pd.to_datetime(df['data_admissao'])

# Qual é o salário médio da empresa?
df_salario_medio = df['salario'].mean()
print(f'R${df_salario_medio:,.2f}')
print()

# Quantos funcionários ativos e inativos existem?
ativos_inativos = df['ativo'].value_counts()
print("Funcionários ativos e inativos:")
print(ativos_inativos)
print()

# Qual departamento tem o maior número de funcionários ativos?
mais_ativos = df[df['ativo'] == 'Sim'].groupby('departamento')['id'].count().sort_values(ascending=False)
print("Departamentos com mais funcionários ativos:")
print(mais_ativos.head(3))
print()

# Qual é a média salarial por departamento?
media_salarial = df.groupby('departamento')['salario'].mean().sort_values(ascending=False)
print("Média salarial por departamento:")
print(media_salarial)
print()

# Quem são os 5 funcionários com maior salário?
top_salarios = df[['nome', 'salario']].sort_values(by='salario', ascending=False).head(5)
print("Top 5 funcionários com maior salário:")
print(top_salarios)

