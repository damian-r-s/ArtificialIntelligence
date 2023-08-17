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
df_can_t = df[years].transpose()
df_can_t.index = map(int, df_can_t.index)
df_can_t.index.name = 'Year'
df_can_t.reset_index(inplace=True)

norm_brazil = (df_can_t['Brazil'] - df_can_t['Brazil'].min()) / (df_can_t['Brazil'].max() - df_can_t['Brazil'].min())
norm_argentina = (df_can_t['Argentina'] - df_can_t['Argentina'].min()) / (df_can_t['Argentina'].max() - df_can_t['Argentina'].min())

ax0 = df_can_t.plot(kind='scatter', x='Year', y='Brazil', figsize=(14,8), alpha=0.5, color='green', s=norm_brazil*2000 + 10, xlim=(1975, 2015))
ax1 = df_can_t.plot(kind='scatter', x='Year', y='Argentina', alpha=0.5, color='blue', s=norm_argentina*2000 + 10, ax=ax0)
ax0.set_ylabel('Number of Immigrants')
ax0.set_title('Immigration from Brazil and Argentina from 1980 to 2013')
ax0.legend(['Brazil', 'Argentina'], loc='upper left', fontsize='x-large')
plt.show()




