# -*- coding: utf-8 -*-

# Python tehtävä 1.2
# Esa Parkkila

import pandas as pd
from datetime import datetime, timedelta

print("Hello world")
print("Visit https://www.imdb.com/title/tt0118615/")

# Read inputs
df_emp1 = pd.read_csv('employee1.csv', dtype={'phone1': str, 'phone2': str})
df_emp2 = pd.read_csv('employee2.csv', dtype={'phone1': str, 'phone2': str})
df_dep = pd.read_csv('department.csv')
df_rev = pd.read_csv('department-revenue.csv')

# Merge tables
df_emp = pd.concat([df_emp1, df_emp2], ignore_index=True)
df_empdep = pd.merge(df_emp, df_dep, how='inner', left_on='dep', right_on='id')
df = pd.merge(df_empdep, df_rev, how='inner', left_on='dname', right_on='dname')

print('Original DF:')
print(df)

# Delete unneeded columns
df.drop([ 'id_y', 'id', 'image', 'phone1', 'phone2', 'dep', 'email'], inplace=True, axis=1)
print('Pruned DF:')
print(df)

# Rename columns
df.columns = ['Id', 'Etunimi', 'Sukunimi', 'Palkka', 'Syntymäaika', 'Osasto', 'Osaston tulos']

print(df)
df.to_csv('results/tyontekijoiden-tulosdata.csv', index=False)