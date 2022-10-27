import pandas as pd
df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
df.set_index('date', inplace=True)
df.drop('state', axis=1, inplace=True)

print(df.loc['31.12.20']) # or print(df.iloc[-1]) as it is the last entry