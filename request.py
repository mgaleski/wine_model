import requests
import json
import pandas as pd

df = pd.read_csv('database/winequality.csv')
df = df.reset_index().drop(['index','Unnamed: 0', 'wine_id', 'color', 'good', 'density','quality'], axis=1)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

# Flask URL
url = 'http://0.0.0.0:5000/'

#Feeds first 10 records to the app to give test predictions
for i in range(0, 10):
    data = [[df['fixed acidity'][i], df['volatile acidity'][i], df['citric acid'][i], df['residual sugar'][i],
             df['chlorides'][i], df['free sulfur dioxide'][i], df['total sulfur dioxide'][i], df['pH'][i],
             df['sulphates'][i], df['alcohol'][i]]]
    j_data = json.dumps(data)
    r = requests.post(url, data=j_data, headers=headers)
    print(r, r.text)



