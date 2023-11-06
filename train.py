#imports

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

import pickle

# data preparation

df = pd.read_csv("Maternal Health Risk Data Set.csv")
df['HighRisk'] = (df.RiskLevel == 'high risk')
del df['RiskLevel']
del df['DiastolicBP']
labels = df.drop(columns=['HighRisk']).columns

X = df.drop(columns=['HighRisk'])
y = df['HighRisk']

X_full_train, X_test, y_full_train, y_test = train_test_split( 
    X,y, test_size = 0.2, random_state = 1, shuffle = True, stratify = y)

# training final model

print('training the final model')

model = RandomForestClassifier(n_estimators=12, random_state=1)
model.fit(X_full_train, y_full_train)

y_pred = model.predict(X_test)
auc = roc_auc_score(y_test, y_pred)
round(auc, 5)

print(f'auc={auc}')

# save the model

with open('model.pkl', 'wb') as f_out:
    pickle.dump(model, f_out)

print(f'the model is saved')