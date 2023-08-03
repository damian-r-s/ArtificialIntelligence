import pandas as pd
import matplotlib.pylab as plt
import matplotlib as plt
from matplotlib import pyplot
import numpy as np


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]


df = pd.read_csv(url, names=headers)
df.replace("?", np.nan, inplace=True)

missing_data = df.isnull()

# for column in missing_data.columns.values.tolist():
#     print(column)
#     print(missing_data[column].value_counts())
#     print("")

# Calculate the mean value for the "normalized-losses" column
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses: ", avg_norm_loss)
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

# Calculate mean value for "bore" column
avg_bore = df["bore"].astype('float').mean(axis=0)
print("Averaget of bore: ", avg_bore)
df["bore"].replace(np.nan, avg_bore, inplace=True)

# Calculate mean value for "stroke" column
avg_stroke = df['stroke'].astype('float').mean(axis=0)
print("Stroke avg: ", avg_stroke)
df['stroke'].replace(np.nan, avg_stroke, inplace=True)

# Calculte mean value for "horsepower" column
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print("Average horsepower: ", avg_horsepower)
df['horsepower'].replace(np.nan, avg_horsepower, inplace=True)

# Calculate the mean value for "peak-rpm" column
avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

print("Num of doors values: ")
print(df['num-of-doors'].value_counts())
print(df['num-of-doors'].value_counts().idxmax())
df['num-of-doors'].replace(np.nan, 'four', inplace=True)

# Drop all rows that do not have price data:
df.dropna(subset=['price'], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

print(df.head())
print(df.dtypes)

df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]
df.head()

# Transform mpg to L/100km by mathematical operation (235 divided by mpg)
df["highway-mpg"] = 235/df["highway-mpg"]
df.rename(columns={'highway-mpg':'highway-L/100km'}, inplace=True)
df.head()

# Data Normalization - normalize: length, width, heigh
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()
df['height'] = df['height']/df['height'].max()

print(df[["length","width","height"]].head())

# Binning
df["horsepower"]=df["horsepower"].astype(int, copy=True)

plt.pyplot.hist(df['horsepower'])
plt.pyplot.xlabel('horsepower')
plt.pyplot.ylabel('count')
plt.pyplot.title('horsepower bins')

bins = np.linspace(min(df['horsepower']), max(df['horsepower']), 4)
group_names = ['Low', 'Medium', 'High']
df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True)
print(df[['horsepower', 'horsepower-binned']].head(20))
print(df['horsepower-binned'].value_counts())

pyplot.bar(group_names, df['horsepower-binned'].value_counts())
plt.pyplot.xlabel('horsepower')
plt.pyplot.ylabel('count')
plt.pyplot.title('horsepower bins')

# draw historgram of attribute "horsepower" with bins = 3
plt.pyplot.hist(df["horsepower"], bins = 3)

# set x/y labels and plot title
plt.pyplot.xlabel("horsepower")
plt.pyplot.ylabel("count")
plt.pyplot.title("horsepower bins")

# Dummy Variable
dummy_variable_1 = pd.get_dummies(df['fuel-type'])
dummy_variable_1.rename(columns={'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace=True)
df = pd.concat([df, dummy_variable_1], axis=1)
df.drop('fuel-type', axis=1, inplace=True)

dummy_aspiration = pd.get_dummies(df['aspiration'])
dummy_aspiration.rename(columns={'std':'aspiration-std', 'turbo':'aspiration-turbo'}, inplace=True)
df = pd.concat([df, dummy_aspiration], axis=1)
df.drop('aspiration', axis=1, inplace=True)

df.to_csv('clean_df.csv')

