# 🔹 Manipulação de Dados Avançada
# apply() – Aplica funções personalizadas a colunas ou linhas.
# map() – Transforma elementos de uma Series usando uma função.
# replace() – Substitui valores específicos em um DataFrame.


import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})

df['A_dobrado'] = df['A'].apply(lambda x: x * 2)

df['B_formatado'] = df['B'].map(lambda x: f"Valor: {x}")

df['A'] = df['A'].replace({1: 'um', 2: 'dois'})

# Agrupando e somando valores
df_grouped = df.groupby('A_dobrado').sum()

# Criando tabela dinâmica (pivot_table)
df_pivot = df.pivot_table(values='B', index='A_dobrado', aggfunc='mean')

# Transformando o DataFrame de largo para longo com melt()
df_melted = pd.melt(df, id_vars=['A'], value_vars=['B', 'A_dobrado'])

print(df)
print()
print(df_grouped)
print()
print(df_pivot) 
print()
print(df_melted)


