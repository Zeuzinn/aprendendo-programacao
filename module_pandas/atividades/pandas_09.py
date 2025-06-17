# 🔹 Desempenho e Otimização
# astype() – Converte tipos de dados para otimizar armazenamento.
# memory_usage() – Analisa o consumo de memória do DataFrame.
# eval() – Executa expressões em um DataFrame de forma eficiente.

import pandas as pd


df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})

df['A_dobrado'] = df['A'].apply(lambda x: x * 2)

df['B_formatado'] = df['B'].map(lambda x: f"Valor: {x}")

df['A'] = df['A'].replace({1: 'um', 2: 'dois'})


# Convertendo tipos de dados com astype()
df['A_dobrado'] = df['A_dobrado'].astype(float)

# Analisando consumo de memória
print(df.memory_usage())

# Executando expressões de forma eficiente com eval()
df['Nova_Coluna'] = df.eval("A_dobrado * B")

print(df)
