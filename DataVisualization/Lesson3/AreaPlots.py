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

df.sort_values(['Total'], ascending=False, axis=0, inplace=True)

dfTop5 = df.head()
dfTop5Transposed = dfTop5[years].transpose()
dfTop5Transposed.index = dfTop5Transposed.index.map(int)

dfTop5Transposed.plot(kind='area', stacked=False, figsize=(20, 10))
plt.title('Imigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()
