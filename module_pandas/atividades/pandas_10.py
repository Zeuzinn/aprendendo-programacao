# HEATMAP -> MAPA DE CALOR COM PANDAS

import pandas as pd

# defining index for the dataframe
idx = ['1', '2', '3', '4']

# defining columns for the dataframe
cols = list('ABCD')

# entering values in the index and columns  
# and converting them into a panda dataframe
df = pd.DataFrame([
    [10, 20, 30, 40], 
    [50, 30, 8, 15],
    [25, 14, 41, 8], 
    [7, 14, 21, 28]],
    columns = cols, index = idx)

# displaying dataframe as an heatmap 
# with diverging colourmap as virdis
df.style.background_gradient(cmap ='viridis')\
        .set_properties(**{'font-size': '20px'})


