import pandas as pd

df = pd.read_csv('winequality.csv')

print(df.head())
print(df.columns)
id = []

#adds an id number for each record to be used as primary key
for i in range(1, len(df)+1):
    wine_id = i
    id.append(i)

df['wine_id'] = id
df = df.drop(['Unnamed: 0', 'Unnamed: 0.1.1'], axis=1)
df.to_csv('./database/wine_sql_data.csv')

print(df.columns)