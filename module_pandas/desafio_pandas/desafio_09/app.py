import pandas as pd
import matplotlib.pyplot as plt


pd.options.display.float_format = 'R${:,.2f}'.format
# Leitura de arquivo
vendas_loja = 'praticas-com-python/module_pandas/desafio_pandas/desafio_09/vendas_loja.csv'
df = pd.read_csv(vendas_loja)

# Verificar se há valores ausentes
df = df.fillna(0)

# Criar nova coluna "VALOR TOTAL"
df['valor_total'] = df['quantidade'] * df['preco_unitario']

#  3 Produtos mais vendidos em quantidade?
produtos_vendidos = df.groupby('produto')['quantidade'].sum().sort_values(ascending=False)

# Gráfico de barras
produtos_vendidos.plot(kind='bar', title='Produtos mais vendidos', figsize=(10,5), color='skyblue')
plt.ylabel('Quantidade Vendida')
plt.xlabel('Produto')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Qual categoria gerou mais receita total?
df_categoria = df.groupby('categoria')['valor_total'].sum().sort_values(ascending=False)

# Qual estado teve o maior faturamento?
df_estado_faturamento = df.groupby('estado')['valor_total'].sum().sort_values(ascending=False)

# Converter "data_venda" para datetime
df['data_venda'] = pd.to_datetime(df['data_venda'])

# Criar uma coluna com o mês
df['mes'] = df['data_venda'].dt.to_period('M')

# Total de vendas por mês
vendas_mensais = df.groupby('mes')['valor_total'].sum()

# Exibindo gráficos de vendas mensais
vendas_mensais.plot(kind='line', marker='o', title='Faturamento Mensal', figsize=(10,5))
plt.ylabel('Total em R$')
plt.xlabel('Mês')
plt.grid(True)
plt.tight_layout()
plt.show()


