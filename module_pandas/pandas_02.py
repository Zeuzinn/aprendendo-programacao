# Leitura de arquivos (entrada de dados)
import pandas as pd

# CSV
# read_csv() lê arquivos separados por vírgula (ou outro separador).
df = pd.read_csv("praticas-com-python/aulas_csv/aula_260.csv")   

print(df.head()) # head() mostra as primeiras linhas da tabela.

print()

# Carregar CSV
df_2 = pd.read_csv("praticas-com-python/aulas_csv/aula_260.csv", delimiter=",", names=["Nome", "cpf", "valor pago"])

# Exibir tabela
print(df_2)