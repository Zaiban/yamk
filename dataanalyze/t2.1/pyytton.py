# Python harjoitukset tehtävä 2.1
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('titanic.csv')


# Histogrammi koko datasta (epäselvää, mitä x-akselille valitaan?)
# df.plot.bar(x='Age')
# plt.show()


# Miesten ja naisten määrät pylväinä
gender_count = df.groupby('GenderCode').count()

malefemalecomp = pd.DataFrame()
malefemalecomp['Count'] = gender_count['id']
malefemalecomp['Gender'] = ['Male', 'Female']

malefemalecomp.plot.bar(x='Gender')
plt.show()
