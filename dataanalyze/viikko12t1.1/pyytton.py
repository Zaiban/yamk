import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from file to dataframe
df = pd.read_csv('emp-dep-python.csv')

# Create separate df for the columns listed
df_corr = df[['Palkka', 'Osaston tulos', 'Ikä']]

# Show correlation heatmap
heatmap = sns.heatmap(df_corr.corr(), annot=True)
plt.show()