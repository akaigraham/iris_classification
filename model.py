# import necessary libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pickle


# load dataset
iris = datasets.load_iris()

# load feature names and target names
feature_names = iris.feature_names
target_names = iris.target_names

# separate target from features
X = iris.data 
y = iris.target

# separate into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=23)

# scale data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# instantiate KNN classifier with three neighbors
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train_scaled, y_train)

# generate test predictions
test_preds = clf.predict(X_test)

# produce accuracy score
test_acc = accuracy_score(y_test, test_preds)

# pickle model
pickle.dump(clf, open('model.pkl', 'wb'))




