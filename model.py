import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
wine = pd.read_csv('./database/winequality.csv')

#quality rating bins, 6.5-8 = good, less than 6.5 = bad
bins = [2, 6.5, 8]
labels = ['bad', 'good']
wine['quality'] = pd.cut(wine['quality'], bins=bins, labels=labels)
wine = wine.dropna()

X = wine.drop(['Unnamed: 0', 'color', 'quality', 'good', 'density', 'wine_id'], axis=1)
print(X.columns)
y = wine['quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.fit_transform(X_test)

rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train, y_train)
rfc_pred = rfc.predict(X_test)
print(classification_report(y_test, rfc_pred))

sgd = SGDClassifier(penalty=None)
sgd.fit(X_train, y_train)
pred_sgd = sgd.predict(X_test)
print(classification_report(y_test, pred_sgd))

svc = SVC(C=1.2, gamma=0.9, kernel= 'rbf')
svc.fit(X_train, y_train)
pred_svc2 = svc.predict(X_test)
print(classification_report(y_test, pred_svc2))

import pickle
pickle.dump(svc, open('model.pkl', 'wb'))
