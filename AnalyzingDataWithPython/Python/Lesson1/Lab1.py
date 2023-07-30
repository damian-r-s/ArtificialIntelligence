# import pandas library
import pandas as pd
import numpy as np

other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)

print("The first 5 rows!")
print(df.head(5))
print("The last 10 rows!")
print(df.tail(10))

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

print("headers\n", headers)

df.columns = headers
print(df.head(5))

df1 = df.replace('?', np.NaN)

df = df1.dropna(subset=["price"], axis=0)

df.to_csv('automobile.csv', index=False)

print(df[['length', 'width', 'height']])
print(df[['length', 'width', 'height']].describe())
print(df.info())