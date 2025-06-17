# replace() -> para substituir valores NaN por um valor específico.
import pandas as pd
import numpy as np

data = pd.read_csv("praticas-com-python/module_pandas/atividades/employees.csv")

data.replace(to_replace=np.nan, value=-99)