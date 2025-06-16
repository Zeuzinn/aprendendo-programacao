# Imagine que você recebeu os resultados de uma pesquisa de satisfação de clientes em um arquivo CSV. Sua missão é: 
# 1️⃣ Carregar o arquivo CSV contendo os dados da pesquisa. 
# 2️⃣ Calcular a média de satisfação para cada categoria. 
# 3️⃣ Identificar as categorias com média de satisfação abaixo de 3.0 (possíveis problemas). 
# 4️⃣ Ordenar as categorias de satisfação do menor para o maior. 
# 5️⃣ Salvar os resultados em um novo arquivo CSV chamado "categorias_insatisfacao.csv".

import pandas as pd

df = pd.read_csv("praticas-com-python/module_pandas/desafio_pandas/desafio_03/pesquisa.csv")

media_satisfacao = df["Satisfação"].mean()

df_menor_3 = df[df["Satisfação"] < 3]
df_menor_3 = df_menor_3.reset_index(drop=True)

df_order = df.sort_values(by="Satisfação")


print(df)
print(f"\nMédia geral da satisfação: {media_satisfacao:.2f}")

print('\nSatisfações abaixo de 3.0')
print(df_menor_3)

print('\nOrdenar as categorias de satisfação do menor para o maior.')
print(df_order)

# Cria um arquivo CSV e salva informações
df_menor_3.to_csv("categorias_insatisfacao.csv", index=False)


