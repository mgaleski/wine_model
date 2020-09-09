import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

fig = plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='fixed acidity', data=df)
plt.savefig('visualizations/fixed acidity.png')

fig = plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='residual sugar', data=df)
plt.savefig('visualizations/residual sugar.png')

fig = plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='chlorides', data=df)
plt.savefig('visualizations/chlorides.png')

fig = plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='volatile acidity', data=df)
plt.savefig('visualizations/volatile acidity.png')

fig = plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='citric acid', data=df)
plt.savefig('visualizations/citric acid.png')

fig = plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='free sulfur dioxide', data=df)
plt.savefig('visualizations/free sulfur dioxide.png')

fig = plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='total sulfur dioxide', data=df)
plt.savefig('visualizations/total sulfur dioxide.png')

fig = plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='pH', data=df)
plt.savefig('visualizations/pH.png')

fig = plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='sulphates', data=df)
plt.savefig('visualizations/sulphates.png')

fig = plt.figure(figsize=(10, 6))
sns.barplot(x='quality', y='alcohol', data=df)
plt.savefig('visualizations/alcohol.png')

