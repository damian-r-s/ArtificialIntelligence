import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx'

df = pd.read_excel(url, sheet_name='Canada by Citizenship', skiprows=range(20), skipfooter=2)

# print(df.head())
# print(df.tail())
# print(df.info(verbose=True))
# print(df.columns)
# print(df.index)
# print(type(df.columns))
# print(type(df.index))

df.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
df.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)

# print(df.isnull().sum())
# print(df.describe())
# print(df[['Country', 'Continent', 1980, 1981, 1982, 1983, 1984, 1985]])

df.set_index('Country', inplace=True)
# print(df.head())

# df.loc['Japan']
# print(df.loc['Japan', 2013])
# print(df.iloc[87, [3, 4, 5, 6, 7, 8]])

# print(df[(df['Continent']=='Asia') & (df['Region'] == 'Southern Asia')])

# print('data dimensions:', df.shape)
# print(df.columns)

df.columns = list(map(str, df.columns))
years = list(map(str, range(1980, 2014)))

haiti = df.loc['Haiti', years]
haiti.index = haiti.index.map(int)
haiti.plot(kind='line')
plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.text(2000, 6000, '2010 Earthquake')
plt.show()