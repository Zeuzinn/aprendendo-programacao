# Exportando Pandas DataFrame para JSON

import pandas as pd

df = pd.DataFrame([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],
                  index=['row 1', 'row 2', 'row 3'],
                  columns=['col 1', 'col 2', 'col 3'])

df.to_json('file.json', orient='split', compression='infer', index=True, indent=2)

df = pd.read_json('file.json', orient='split', compression='infer')
print(df)