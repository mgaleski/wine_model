import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, GridSearchCV


wine = pd.read_csv('winequality.csv')

#quality rating bins, with high quality wines being those above a 6.5 rating
bins = [2, 6.5, 9]
labels = ['bad', 'good']
wine['quality'] = pd.cut(wine['quality'], bins=bins, labels=labels)
wine = wine.dropna()

X = wine.drop(['Unnamed: 0', 'Unnamed: 0.1.1', 'color', 'quality', 'good', 'wine_id'], axis=1)
y = wine['quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

'''
These were the other types of model tested
'''
rfc = RandomForestClassifier(n_estimators=200)
rfc.fit(X_train, y_train)
rfc_pred = rfc.predict(X_test)
print(classification_report(y_test, rfc_pred))

sgd = SGDClassifier(penalty=None)
sgd.fit(X_train, y_train)
pred_sgd = sgd.predict(X_test)
print(classification_report(y_test, pred_sgd))

'''
Parameters here were determined by code below, not included to save time when running the program
'''
svc = SVC(C=1.2, gamma=0.9, kernel='rbf')
svc.fit(X_train, y_train)
pred_svc = svc.predict(X_test)
print(classification_report(y_test, pred_svc))

#
# param = {
#     'C': [0.1,0.8,0.9,1,1.1,1.2,1.3,1.4],
#     'kernel':['linear', 'rbf'],
#     'gamma' :[0.1,0.8,0.9,1,1.1,1.2,1.3,1.4]
# }
# grid_svc = GridSearchCV(svc, param_grid=param, scoring='accuracy')
#
# grid_svc.fit(X_train, y_train)

# print(grid_svc.best_params_)

import pickle
pickle.dump(svc, open('model.pkl', 'wb'))

import nltk
import sklearn
print('The scikit-learn version is {}.'.format(sklearn.__version__))
