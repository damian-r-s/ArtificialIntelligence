import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

year = list(map(str, range(1980, 2014)))

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx'
df = pd.read_excel(url, sheet_name='Canada by Citizenship', skiprows=range(20), skipfooter=2)

df.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
df.rename(columns={'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace=True)

df.columns=list(map(str, df.columns))
df.set_index('Country', inplace=True)
df['Total'] = df.iloc[:, 5:].sum(axis=1)
years = list(map(str, range(1980, 2014)))
df_continents = df.groupby('Continent', axis=0).sum()
df_continents.drop(['Region', 'DevName'], axis=1, inplace=True)

colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.1, 0, 0, 0, 0.1, 0.1] # ratio for each continent with which to offset each wedge.
# df_continents['Total'].plot(kind='pie', 
#                             figsize=(8, 9), 
#                             colors=colors_list,
#                             autopct='%1.1f%%', 
#                             labels=None,
#                             pctdistance=1.12,
#                             startangle=90,
#                             explode=explode_list,
#                             shadow=True)
# plt.title('Immigration to Canada by Continent [1980 - 2013]')
# plt.axis('equal')
# plt.legend(labels=df_continents.index, loc='upper left')

df_continents['2010'].plot(kind='pie', figsize=(15,6), autopct='%1.1f%%', startangle=90, shadow=True, labels=None, pctdistance=1.13, explode=explode_list)
plt.title('Immigration to Canada by Continent 2010')
plt.axis('equal')
plt.legend(labels=df_continents.index, loc='upper left')
plt.show()
