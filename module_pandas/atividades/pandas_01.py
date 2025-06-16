import pandas as pd

# Criando um DataFrame
dados = {
    "Nome": ["Eliseu", "Guilherme", "Ingrid"],
    "Idade": [24, 22, 23],
    "Cidade": ["São Vicente", "São Vicente", "Praia Grande"],
}

df = pd.DataFrame(dados)

print(df)