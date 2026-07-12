import pandas as pd

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], columns=["A","B","C"], index=["x","y","z","xz"])
print(df.head(1))
print(df.tail())
print(df.index.tolist())
print(df.info())
print(df.describe())
print(df.nunique()) # unique value in each col
print(df['A'].unique())
print(df.shape)
print(df.size)

coffee = pd.read_csv('./Pandas/warmup-data/coffee.csv') # we can also paste the url directly
print(coffee)