import pandas as pd

df = pd.read_csv('database/winequality.csv')

print(df.head())

id = []

#adds an id number for each record to be used as primary key
for i in range(1, len(df)+1):
    wine_id = i
    id.append(i)


df['wine_id'] = id
df.to_csv('./winequality.csv')