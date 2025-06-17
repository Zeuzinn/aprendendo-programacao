# 🔹 Manipulação de Dados Avançada
# apply() – Aplica funções personalizadas a colunas ou linhas.
# map() – Transforma elementos de uma Series usando uma função.
# replace() – Substitui valores específicos em um DataFrame.

# 🔹 Filtragem e Seleção Otimizada
# query() – Filtra dados usando expressões.
# isin() – Filtra elementos que pertencem a uma lista.
# between() – Seleciona valores dentro de um intervalo.

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})

# Usando apply() para dobrar os valores da coluna 'A'
df['A_dobrado'] = df['A'].apply(lambda x: x * 2)

# Usando map() para transformar a coluna 'B' em string formatada
df['B_formatado'] = df['B'].map(lambda x: f"Valor: {x}")

# Substituindo valores com replace()
df['A'] = df['A'].replace({1: 'um', 2: 'dois'})

print(df)
print()
# Filtrando usando query()
df_filtrado = df.query("A_dobrado > 4")

# Filtrando valores específicos com isin()
df_selecionado = df[df['B'].isin([10, 40])]

# Selecionando valores dentro de um intervalo com between()
df_intervalo = df[df['A_dobrado'].between(4, 8)]

print(df_filtrado)
print()
print(df_selecionado)
print()
print(df_intervalo)
