# -*- coding: utf-8 -*-

# Python tehtävä 2.1
# Esa Parkkila

import os
import pandas as pd
from datetime import datetime, timedelta

print("Hello world")
print("Visit https://www.imdb.com/title/tt0118615/")

resultpath = './results'

start = '2021-12-13T00:00:00'
end = '2021-12-15T23:59:59'
api = f'http://smart-iot-00.project.tamk.cloud/api/dump/start/{start}/end/{end}'
print('API:', api)

# Read IOT data from API
df_raw = pd.read_csv(api)

print('Raw data:')
print(df_raw)


# Separate class A3-16 CO2, Humidity and Temp values, all with date_time, as separate dataframes
df_co2 = df_raw.loc[:, ['date_time','A3_16_Vais_CO2']]
df_hum = df_raw.loc[:, ['date_time','A3_16_Vais_Rel_HUM']]
df_temp = df_raw.loc[:, ['date_time','A3_16_Vais_TEMP']]

# Filter/remove nan values from these dfs
df_co2 = df_co2.loc[df_co2['A3_16_Vais_CO2'].notna()]
df_hum = df_hum.loc[df_hum['A3_16_Vais_Rel_HUM'].notna()]
df_temp = df_temp.loc[df_temp['A3_16_Vais_TEMP'].notna()]

# Converting date_time to pandas datetime
df_co2['date_time'] = pd.to_datetime(df_co2['date_time'])
df_hum['date_time'] = pd.to_datetime(df_hum['date_time'])
df_temp['date_time'] = pd.to_datetime(df_temp['date_time'])

# interval for group by, i.e. all rows within interval will be grouped into one row
# Other options like 'S' for secondly, 'T' or 'min' for minutely, 'L' or 'ms' for microseconds, etc.
interval = '15min'

# Group by interval, i.e. combine rows within time interval into one row by mean value of the comnibed rows
df_co2 = df_co2.groupby(pd.Grouper(key='date_time', freq=interval))['A3_16_Vais_CO2'].mean().reset_index()
df_hum = df_hum.groupby(pd.Grouper(key='date_time', freq=interval))['A3_16_Vais_Rel_HUM'].mean().reset_index()
df_temp = df_temp.groupby(pd.Grouper(key='date_time', freq=interval))['A3_16_Vais_TEMP'].mean().reset_index()

print('separates:')
print(df_co2)
print(df_hum)
print(df_temp)

# Merge separate CO2 and Humidity dataframes into one dataframe by outer join based on date_time
df_all = pd.merge(df_co2, df_hum, how='inner', on='date_time')
# Merge TEMP dataframe into the same dataframe by outer join based on date_time
df_all = pd.merge(df_all, df_temp, how='inner', on='date_time')


print('merged:')
print(df_all)



# If result dir does not exist, create it
if not os.path.exists('./results'):
    os.makedirs('./results')
    print('New dir created')

# Create output file
df_all.to_csv('./results/smart_data_CO2-HUM-TEMP--A3-16--' + start + '-' + end + '.csv', index=False, sep=';', decimal=',')
