# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from datetime import datetime, timedelta

print("hello world")

# Luetaan data pandasin dataframeihin, luetaan puhelinnumerot merkkijonona
df_emp1 = pd.read_csv('employee1.csv', dtype={'phone1': str, 'phone2': str})
df_emp2 = pd.read_csv('employee2.csv', dtype={'phone1': str, 'phone2': str})
df_dep = pd.read_csv('department.csv')

# Tehdään uusi
df_emp = pd.concat([df_emp1, df_emp2], ignore_index=True)

# yhdistetään employee ja department data uudeksi dataframeksi employeen dep
df = pd.merge(df_emp, df_dep, how='inner', left_on='dep', right_on='id')

# Poistetaan turhat sarakkeet
df.drop(['id_y', 'dep'], inplace=True, axis=1)

# Käsitellään NULL arvot (eli tyhjät arvot) korvaamalla tyhjät puhelinnumero
df['phone2'].fillna(value='-', inplace=True)

# "Rikastetaan" dataa laskemalla tämän hetken ikä syntymäajan avulla
# // tarkoittaa kokonaislukujen jakoa, jossa tuloksena on jakolaskun kokonaisluku ilman desimaalia
df['age'] = (datetime.now() - pd.to_datetime(df['bdate'])
             ) // timedelta(days=365.2425)

df.columns = ['Id', 'Etunimi', 'Sukunimi', 'Palkka', 'Syntymäaika',
              'Sähköposti', 'Työpuhelin', 'Kotipuhelin', 'Kuva', 'Osasto', 'Ikä']

df.to_csv('emp-dep-python.csv', index=False)

print(df)

# Python tehtävä 1.1
df.drop(['Id', 'Kuva', 'Ikä', 'Kotipuhelin', 'Palkka', 'Syntymäaika'], inplace=True, axis=1)
df.to_csv('yhteystiedot.csv', index=False)

print(df)