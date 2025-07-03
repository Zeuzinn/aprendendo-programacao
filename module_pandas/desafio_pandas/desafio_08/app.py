# 📄 Descrição da atividade
# Imagine que você recebeu um arquivo CSV com informações de uma pequena loja de e-commerce. A tarefa é analisar os dados de vendas usando pandas.

# 🧠 Objetivos
# Use pandas para:
# - Ler os dados do CSV
# - Visualizar os primeiros registros
# - Calcular o total de vendas (quantidade × preço)
# - Agrupar vendas por categoria
# - Filtrar vendas feitas por 'Ana Silva'
# - Ordenar os produtos por total de vendas

import pandas as pd

pd.options.display.float_format = 'R${:.2f}'.format

# - Ler os dados do CSV
data = "praticas-com-python/module_pandas/desafio_pandas/desafio_08/dados.csv"
df = pd.read_csv(data)

# - Visualizar os primeiros registros
print(df.head())

# - Calcular o total de vendas (quantidade × preço)
df ['total_sale'] = df['quantity'] * df['price']

# - Agrupar vendas por categoria
sale_category = df.groupby('category')['total_sale'].sum()

print(sale_category)

# - Filtrar vendas feitas por 'Ana Silva'
name_ana_silva = df[df['customer_name'] == "Ana Silva"]

# - Ordenar os produtos por total de vendas
df_order_sale = df.groupby('product')['total_sale'].sum().sort_values(ascending=False)
print(df_order_sale)
