import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import seaborn as sb

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url, header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers

# print(df.corr())
# print(df[['wheel-base', 'length', 'engine-size', 'fuel-system']].corr())
# print(df[['engine-size', 'price']].corr())
# sb.regplot(x='engine-size', y='highway-mpg', data=df)
# plt.ylim(0, )
# plt.show()
# sb.regplot(x='stroke', y='price')

# print(df['drive-wheels'].unique())
# print(df['fuel-type'].unique())

df_group_one = df[['drive-wheels', 'body-style', 'price']]
df_group_one = df_group_one.groupby(['drive-wheels'], as_index=False).mean()

print(df_group_one)
