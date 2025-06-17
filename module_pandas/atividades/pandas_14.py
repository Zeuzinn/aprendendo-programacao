# Criando um DataFrame e Convertendo para JSON
# orient='split': separa colunas, índices e dados claramente.
# orient='index': mostra cada linha como um par chave-valor com seu índice.
import pandas as pd 

df = pd.DataFrame([['a', 'b'], ['c', 'd']],
                  index=['row 1', 'row 2'],
                  columns=['col 1', 'col 2'])

print(df.to_json(orient='split')) 
print(df.to_json(orient='index'))