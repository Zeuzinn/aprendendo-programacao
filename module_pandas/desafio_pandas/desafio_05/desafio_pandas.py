import pandas as pd

client= "praticas-com-python/module_pandas/desafio_pandas/desafio_05/clientes.csv"
data = pd.read_csv(client)

pd.options.display.float_format = "R${:,.2f}".format

df = pd.DataFrame(data)

df["Total"] = df["Valor pago"]\
        .str.replace("R$ ","")\
        .str.replace(".","")\
        .str.replace(",", ".")\
        .astype(float)

df_faturamento = df["Total"].sum()


df["Total a receber"] = df["Valor a vencer"]\
        .str.replace("R$ ","")\
        .str.replace(".","")\
        .str.replace(",", ".")\
        .astype(float)

df_valor_a_receber = df["Total a receber"].sum()

print(f"Valor para receber: \nR${df_valor_a_receber:,.2f}")
print(f"Faturamento total da sua empresa: \nR${df_faturamento:,.2f}")
