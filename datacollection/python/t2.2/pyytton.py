# -*- coding: utf-8 -*-

# Python tehtävä 2.2
# Esa Parkkila

import os
import pandas as pd
from datetime import datetime, timedelta

print("Hello world")
print("Visit https://www.imdb.com/title/tt0118615/")

resultpath = './results'

start = '2021-12-06T00:00:00'
end = '2021-12-06T23:59:59'
api = f'http://smart-iot-00.project.tamk.cloud/api/dump/start/{start}/end/{end}'
print('API:', api)

# Read IOT data from API
df_raw = pd.read_csv(api)

print('Raw data:')
print(df_raw)
print(df_raw.columns)


# Separate class A3-16 Temp, Humidity  and light values, all with date_time, as separate dataframes
df_temp = df_raw.loc[:, ['date_time','A3_16_Vais_TEMP']]
df_hum = df_raw.loc[:, ['date_time','A3_16_Vais_Rel_HUM']]
df_light = df_raw.loc[:, ['date_time','Ref_light']]

# Filter/remove nan values from these dfs
df_temp = df_temp.loc[df_temp['A3_16_Vais_TEMP'].notna()]
df_hum = df_hum.loc[df_hum['A3_16_Vais_Rel_HUM'].notna()]
df_light = df_light.loc[df_light['Ref_light'].notna()]

# Converting date_time to pandas datetime
df_temp['date_time'] = pd.to_datetime(df_temp['date_time'])
df_hum['date_time'] = pd.to_datetime(df_hum['date_time'])
df_light['date_time'] = pd.to_datetime(df_light['date_time'])

# interval for group by, i.e. all rows within interval will be grouped into one row
# Other options like 'S' for secondly, 'T' or 'min' for minutely, 'L' or 'ms' for microseconds, etc.
interval = '5min'

# Group by interval, i.e. combine rows within time interval into one row by mean value of the comnibed rows
df_temp = df_temp.groupby(pd.Grouper(key='date_time', freq=interval))['A3_16_Vais_TEMP'].max().reset_index()
df_hum = df_hum.groupby(pd.Grouper(key='date_time', freq=interval))['A3_16_Vais_Rel_HUM'].max().reset_index()
df_light = df_light.groupby(pd.Grouper(key='date_time', freq=interval))['Ref_light'].max().reset_index()

print('separates:')
print(df_temp)
print(df_hum)
print(df_light)

# Merges
df_all = pd.merge(df_temp, df_hum, how='inner', on='date_time')
df_all = pd.merge(df_all, df_light, how='inner', on='date_time')


print('merged:')
print(df_all)



# If result dir does not exist, create it
if not os.path.exists('./results'):
    os.makedirs('./results')
    print('New dir created')

# Create output file
df_all.to_csv('./results/smart_data_HUM-TEMP-LIGHT--A3-16--' + start + '-' + end + '.csv', index=False, sep=';', decimal=',')
