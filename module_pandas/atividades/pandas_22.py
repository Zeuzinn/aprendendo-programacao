# fillna() -> é usado para substituir valores ausentes (NaN) por um valor fornecido.
# df.fillna(method='bfill') -> é usada para preenchê-lo com o próximo valor.
# df.fillna(method='pad') -> é usado para preencher valores ausentes com o valor anterior.
import pandas as pd
import numpy as np

d = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}
df = pd.DataFrame(d)

df.fillna(0)