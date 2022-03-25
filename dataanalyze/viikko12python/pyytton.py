import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from file to dataframe
df = pd.read_csv('kyselydataa.csv',sep=';')

print("-- dataframe")
print(df)

# Data description
description = df.describe()

print("-- description")
print(description)

# Show histogram
#df.hist()
#plt.show()

# Data info
print("-- info")
df.info()

# Get 5 oldest by row index
oldest5index = df['ikä'].nlargest(5)
oldest5 = df.loc[oldest5index.index]

print("-- oldest5")
print(oldest5)

# Frequency distribution for amount (frekvenssijakauma)
df_freq = pd.crosstab(df['koulutus'], 'f')
print("-- df_freq")
print(df_freq)

# Give labels to the eduation values
education = ['Peruskoulu', '2. aste', 'Korkeakoulu', 'Ylempi korkeakoulu']

# Replace education numerical values with text values
df_freq.index = education

print("-- df_freq 2")
print(df_freq)

# Show bar chart and save the chart as file
#df_freq.plot.barh(zorder=2)
plt.savefig('frekvenssijakauma.png', bbox_inches='tight')
#plt.show()

# Frequency distribution with education and sex (frekvenssijakauma)
df_freq_sex = pd.crosstab(df['koulutus'], df['sukup'])
print("-- df_freq_sex")
print(df_freq_sex)

# Add text labels for sex
sex = ['Mies', 'Nainen']

# Add text labels for the table
df_freq_sex.index = education
df_freq_sex.columns = sex

print("-- df_freq_sex 2")
print(df_freq_sex)

# Show bar chart and save the chart as file
#df_freq_sex.plot.barh(zorder=2)
#plt.show()

plt.savefig('koulutus_ja_sukupuoli.png', bbox_inches='tight')

# Create separate df for the columns listed
df_corr = df[['sukup', 'ikä', 'perhe', 'koulutus', 'palkka']]

# Show correlation heatmap
heatmap = sns.heatmap(df_corr.corr(), annot=True)
plt.show()

# Save the heatmap
heatmap.get_figure().savefig("heatmap.png")