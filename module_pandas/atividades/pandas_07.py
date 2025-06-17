# 🔹 Tratamento de Dados Faltantes
# fillna() – Preenche valores ausentes com uma estratégia específica.

# dropna() – Remove linhas ou colunas com valores nulos.

import pandas as pd


df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})

df['A_dobrado'] = df['A'].apply(lambda x: x * 2)

df['B_formatado'] = df['B'].map(lambda x: f"Valor: {x}")

df['A'] = df['A'].replace({1: 'um', 2: 'dois'})

df_missing = pd.DataFrame({'A': [1, None, 3, None], 'B': [10, 20, None, 40]})

# Preenchendo valores ausentes com fillna()
df_missing_filled = df_missing.fillna(0)

# Removendo linhas com valores nulos com dropna()
df_cleaned = df_missing.dropna()

print(df_missing_filled)
print()
print(df_cleaned)
