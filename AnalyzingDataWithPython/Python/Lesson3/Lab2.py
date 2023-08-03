import pandas as pd
import numpy as np
import matplotlib as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url, header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers

df_test = df[["drive-wheels", "body-style", "price"]]
df_grp = df_test.groupby(['drive-wheels', 'body-style'], as_index=False).mean()
df_pivot = df_grp.pivot(index = 'drive-wheels', columns='body-style')

print(df_grp)
print(df_pivot)