# notnull()-> retorna um DataFrame com valores booleanos, 
# onde True indica dados não ausentes (válidos).

import pandas as pd
import numpy as np

d = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}
df = pd.DataFrame(d)

nmv = df.notnull()

print(nmv)