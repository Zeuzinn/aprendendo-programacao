# str.replace("R$", "") → Remove o "R$".
# str.replace(",", "") → Remove todas as vírgulas
# str.replace(",", ".") → Troca a vírgula decimal por ponto.

import pandas as pd


dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [23, 35, 31],
    'Valor pago': ["R$1.900,00", "R$800,00", "R$1.850,00"]
}

df = pd.DataFrame(dados)

# Transformação de dados:

# 📌 Se o valor está no formato "R$1.000,00", precisamos primeiro converter para número!
df["Valor pago"] = df["Valor pago"]\
    .str.replace("R$", "")\
    .str.replace(".", "")\
    .str.replace(",", ".")\
    .astype(float)

# Filtrar quem pagou mais de R$ 1.000,00:
df_filtrado = df[df["Valor pago"] > 1000]

print(df["Valor pago"])
print()
print(df_filtrado)

