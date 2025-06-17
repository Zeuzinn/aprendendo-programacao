# isnull() -> retorna um DataFrame com valor booleano 
# onde True representa dados ausentes (NaN)
import pandas as pd
import numpy as np

d = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}
df = pd.DataFrame(d)

mv = df.isnull()

print(mv)