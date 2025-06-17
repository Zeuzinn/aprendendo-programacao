# pd.json_normalize() ->  é usado quando trabalhamos com estruturas JSON aninhadas. 
# JSON de APIs geralmente vem em formato aninhado, 
# e esse método ajuda a compactá- lo em um formato tabular mais fácil de trabalhar no Pandas. 
# Esse método é útil ao trabalhar com respostas JSON reais de APIs.

import pandas as pd
import json

data = {"One": {"0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60},
        "Two": {"0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102}}

json_data = json.dumps(data)

df_normalize = pd.json_normalize(json.loads(json_data))

print("\nDataFrame using JSON module and `pd.json_normalize()` method:")
print(df_normalize)
print()

# Usando pd.DataFrame com um dicionário
df = pd.DataFrame(data)
print(df)

# Esses métodos ajudam você a usar dados JSON no Pandas para análise e visualização. 
# Com apenas algumas linhas de código, 
# você pode transformar JSON bruto em um DataFrame limpo e utilizável.