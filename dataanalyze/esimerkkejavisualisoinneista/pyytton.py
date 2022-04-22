import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from file to dataframe
df = pd.read_csv('emp-dep.csv', sep=',')
print("Emp-dep.csv:")
print(df)

#df.plot.scatter(x='Ikä', y='Palkka')

#sns.scatterplot(data=df, x='Ikä', y='Palkka')

# Show bar chart with employee counts in departments, calculate first the counts and show th echart

df_counts = df['Osasto'].value_counts()
print(df_counts)

#df_counts.plot.bar()


# Labels
labels = ['miehet', 'naiset']

#colors
colors = ['blue', 'green']

# Count the values etc.

gender_counts = df['Sukupuoli'].value_counts()
gender_counts.plot.pie(labels=labels, autopct='%1.1%%', colors=colors)


plt.show()