import pandas as pd
import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url, header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers

# df.dropna(subset=["price"], axis=0, inplace=True)

# df["city-mpg"] = 235/df["city-mpg"]
# df.rename(columns={"city_mpg", "city-L/100km"}, inplace=True)

# df["price"] = df["price"].astype("int")

# print(df.dtypes())

# Normalization
print("Original")
print(df["length"].head(4))

# Divide by maximum
print("Divide by maximum ")
# df["length"] = df["length"]/df["length"].max()

# Min-Max
print("Min-Max")
df["length"] = (df["length"] - df["length"].min()) / (df["length"].max() - df["length"].min())

# Z-score
print("Z-score")
df["length"] = (df["length"] - df["length"].mean()) / df["length"].std()

print(df["length"].head(4))

