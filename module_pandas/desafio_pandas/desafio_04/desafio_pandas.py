# 💡 Sua tarefa:
# 1️⃣ Carregue o arquivo no pandas.
# 2️⃣ Crie uma nova coluna chamada Valor_Total que seja Quantidade * Preco_Unitario.
# 3️⃣ Filtre as vendas apenas da categoria Papelaria.
# 4️⃣ Calcule e exiba o faturamento total da categoria Papelaria.
# 5️⃣ Mostre as 5 datas com maior faturamento diário (agrupando por Data).
# 6️⃣ Salve o resultado do agrupamento em um novo arquivo CSV chamado faturamento_diario.csv.

import pandas as pd

pd.options.display.float_format = "R${:.2f}".format

df = pd.read_csv("praticas-com-python/module_pandas/desafio_pandas/desafio_04/vendas.csv")

# Cria uma nova coluna
df['Total'] = df['Quantidade'] * df['Preco_Unitario']

# Filtra pela categoria
df_papelaria = df[df['Categoria'] == 'Papelaria']

# Soma o faturamento da papelaria 
faturamento_papelaria = df_papelaria['Total'].sum()

# Agrupamento por data
df_datas = df.groupby('Data')['Total'].sum()


print(f'Faturamento total da categoria Papelaria: R${faturamento_papelaria:.2f}')

print('Salvando faturamento diário...')
df_datas.to_csv("faturamento_diario.csv")
