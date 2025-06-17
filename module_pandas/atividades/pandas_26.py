# dropna() -> é usada para remover linhas ou colunas com valores NaN. 
# Ela pode ser usada para remover dados com base em diferentes condições.

# Eliminando linhas com pelo menos um valor nulo
# Remova as linhas que contêm pelo menos um valor ausente.

import pandas as pd
import numpy as np

dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score': [52, 40, 80, 98],
        'Fourth Score': [np.nan, np.nan, np.nan, 65]}
df = pd.DataFrame(dict)

df.dropna()