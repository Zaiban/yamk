import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from file to dataframe
df = pd.read_csv('titanic-data.csv')

# Create separate df for the columns listed
df_corr = df[['Survived', 'Pclass', 'Sex']]

def myfunc(x):
    val = x[2]
    if val == 'male':
        val = 0
    elif val == 'female':
        val = 1
    x.Sex = val
    return x

df_final = df_corr.apply(myfunc, axis=1)

# Show correlation heatmap
heatmap = sns.heatmap(df_final.corr(), annot=True)
plt.show()