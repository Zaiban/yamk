# Python harjoitukset tehtävä 2.2
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('titanic.csv')

count_survived = df.groupby('Survived').count()

data = ['', '']
data = [count_survived['id'][1], count_survived['id'][0]]
labels = ['Survived', 'Perished']

plt.pie(data, labels=labels, autopct='%.0f%%')
plt.show()
