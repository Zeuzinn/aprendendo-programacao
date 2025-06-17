# requests.get(url) busca dados da URL.
# response.json() converte a resposta em um dicionário/lista Python.
# json_normalize() converte JSON aninhado em uma tabela plana.

import pandas as pd
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

data = pd.json_normalize(response.json())
print(data.head())