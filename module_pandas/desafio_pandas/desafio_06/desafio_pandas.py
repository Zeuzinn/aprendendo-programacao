import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

caminho = "praticas-com-python/module_pandas/desafio_pandas/desafio_06/vendas.csv"

# Carregar dados
df = pd.read_csv(caminho)

# Limpar dados
df = df.dropna().drop_duplicates()

# Calcular vendas por produto
vendas_por_produto = df.groupby("Produto")["Valor"].sum().reset_index()

# Visualizar dados
sns.barplot(x="Produto", y="Valor", data=vendas_por_produto)
plt.show()
