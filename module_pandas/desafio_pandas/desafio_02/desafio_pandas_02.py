import pandas as pd

pd.options.display.float_format = "R${:.2f}".format

df = pd.read_csv('praticas-com-python/module_pandas/desafio_pandas/desafio_02/vendas.csv')

df["Preço"] = df["Preço"]\
    .str.replace("R$", "").str.strip()\
    .str.replace(r"\.", "", regex=True)\
    .str.replace(",", ".", regex=True)\
    .astype(float)

df['Total'] = df["Preço"] * df['Quantidade']

df_5k = df[df["Total"] > 5000]

df_ordenar = df_5k.sort_values(by="Total", ascending=False)

print(df_ordenar)
