import pandas as pd

pd.options.display.float_format = 'R${:,.2f}'.format

path_ = "praticas-com-python/module_pandas/desafio_pandas/desafio_07/vendas.csv"

df = pd.read_csv(path_)

df['Total Vendas'] = df["Valor"] * df["Quantidade"]

df_sales = df.groupby("Vendedor")["Total Vendas"].sum()

df_media= df.groupby("Produto")["Valor"].mean()

df["Data"]= pd.to_datetime(df["Data"])

df_sale_march = df[df["Data"].dt.month == 3]
df_sale_march = df_sale_march.reset_index(drop=True)

df['Comissão'] = df["Valor"] * 0.10


print('-'*75)
print(df.head(5))
print('-'*75)

print('VENDAS EM MARÇO:')
print('-'*75)
print(df_sale_march)
print('-'*75)


df.to_csv("vendas com comissão.csv", index=False)
print("Registro de vendas com comissão salvo!")
