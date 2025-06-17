# Python program to generate heatmap which 
# represents panda dataframe in color-coding schemes
# along with values mentioned in each cell

# import required libraries
import pandas as pd
import seaborn as sns
# import seaborn as sns % matplotlib inline
import matplotlib.pyplot as plt
# % matplotlib inline  # Apenas para exibir no Jupyter Notebook


# Defining figure size  
# for the output plot 
fig, ax = plt.subplots(figsize = (12, 7))

# Defining index for the dataframe
idx = ['1', '2', '3', '4']

# Defining columns for the dataframe
cols = list('ABCD')

# Entering values in the index and columns  
# and converting them into a panda dataframe
df = pd.DataFrame([
    [10, 20, 30, 40], 
    [50, 30, 8, 15],
    [25, 14, 41, 8], 
    [7, 14, 21, 28]],
    columns = cols, index = idx)

# Displaying dataframe as an heatmap 
# with diverging colourmap as RdYlGn
sns.heatmap(df, cmap ='RdYlGn', linewidths = 0.30, annot = True)
