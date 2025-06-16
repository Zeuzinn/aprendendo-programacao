# Principais operações com um DataFrame

# df.head() → Mostra as primeiras linhas
# df.info() → Exibe informações sobre os tipos de dados
# df.describe() → Resumo estatístico das colunas numéricas
# df["Nome"] → Seleciona apenas a coluna "Nome"
# df.iloc[0] → Seleciona a primeira linha

import pandas as pd

dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [23, 35, 31],
    'CPF': ['13899566836', '46698736446','99115662815']
}

df = pd.DataFrame(dados)

# Escolher uma única coluna:
print('\nEscolher uma única coluna:')
print(df['Nome'])

# Escolher várias colunas:
print('\nEscolher várias colunas:')
print(df[['Nome', 'CPF']])

# Escolher uma linha específica:
print('\nEscolher uma linha específica:')
print(df.iloc[2]) # Retorna a terceira linha (index 2)