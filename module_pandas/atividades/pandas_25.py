# interpolate() -> preenche valores ausentes usando técnicas de interpolação, 
# como o método linear.
import pandas as pd
   
df = pd.DataFrame({"A": [12, 4, 5, None, 1], 
                   "B": [None, 2, 54, 3, None], 
                   "C": [20, 16, None, 3, 8], 
                   "D": [14, 3, None, None, 6]})  
print(df)