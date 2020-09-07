import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

wine = pd.read_csv('./database/winequality.csv')

#quality rating bins, 6.5-8 = good, less than 6.5 = bad
bins = [0, 6.5, 8]
labels = ['bad', 'good']
wine['quality'] = pd.cut(wine['quality'], bins=bins, labels=labels)
wine = wine.dropna()


X = wine.drop(['color', 'quality', 'good', 'density'], axis=1)
y = wine['quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)
rfc_pred = model.predict(X_test)
print(classification_report(y_test, rfc_pred))

import pickle
pickle.dump(model, open('model.pkl', 'wb'))
