#records: Lista de dicionários
# columns: Dicionário com rótulos de colunas
# index: Dicionário com índices de linha
# split: Dicionário com índice, colunas e dados
# table: Esquema de tabela JSON

import pandas as pd

df = pd.DataFrame(data=[
    ['15135', 'Alex', '25/4/2014'],
    ['23515', 'Bob', '26/8/2018'],
    ['31313', 'Martha', '18/1/2019'],
    ['55665', 'Alen', '5/5/2020'],
    ['63513', 'Maria', '9/12/2020']],
    columns=['ID', 'NAME', 'DATE OF JOINING'])

df.to_json('file1.json', orient='split', compression='infer')

df = pd.read_json('file1.json', orient='split', compression='infer')
print(df)