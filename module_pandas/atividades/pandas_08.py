# 🔹 Junção e Mesclagem de Dados
# merge() – Une dois DataFrames com regras específicas.

# concat() – Concatena múltiplos DataFrames vertical ou horizontalmente.

import pandas as pd


df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})

df['A_dobrado'] = df['A'].apply(lambda x: x * 2)

df['B_formatado'] = df['B'].map(lambda x: f"Valor: {x}")

df['A'] = df['A'].replace({1: 'um', 2: 'dois'})

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Nome': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 4], 'Idade': [25, 30, 35]})

# Mesclando com merge()
df_merged = pd.merge(df1, df2, on='ID', how='outer')

# Concatenando DataFrames verticalmente com concat()
df_concat = pd.concat([df1, df2], axis=0)

print(df)
print('-'*30)
print(df_merged)
print('-'*30)
print(df_concat)

