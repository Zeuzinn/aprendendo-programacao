import pandas as pd

# Ajustando a exibição global dos floats
pd.options.display.float_format = "R${:.2f}".format

# Carrega um arquivo CSV 
df = pd.read_csv('praticas-com-python/module_pandas/desafio_pandas/desafio_01/planilha_pandas.csv')

# Converte o preço para Números
df["preco"] = df["preco"]\
    .str.replace("R$", "")\
    .str.replace(",", ".")\
    .astype(float)

# Calcula o valor total de cada produto
df['total'] = df["preco"] * df["quantidade"]

# Filtra se o total é maior que 1100
filter_df = df[df['total'] > 1100]

# Ordena de forma decrescente do maior valor para o menor
order_df = filter_df.sort_values(by='total', ascending=False)
print(order_df)

media_total = df["total"].mean()
print(f"Média de gastos por produto: R$ {media_total:.2f}")
