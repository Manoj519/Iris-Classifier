#!/usr/bin/env python
# coding: utf-8

# # Iris classification Model Using KNeighborsClassifier



# import all necessary all library like pandas, numpy, nltk, string and sklearn.
import pandas as pd
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error
from sklearn import metrics
from sklearn.model_selection import train_test_split
import pickle




# Load iris dataset.
data = datasets.load_iris()




# data.keys gives all key value in datset.
data.keys()




# data.feature_names gives all column names from data in dataset.
data.feature_names




# data.DESCR gives description of dataset.
print(data.DESCR)




# Create dataframe by data.data as feature.
feature = pd.DataFrame(data.data)
feature.rename(columns={0: 'sepal length', 1: 'sepal width', 2: 'petal length', 3: 'petal width'}, inplace=True)




# Create dataframe by data.target as label.
label = pd.DataFrame(data.target)
label.rename(columns={0: 'target'}, inplace=True)




# Count total number of null values in dateset in each column.
feature.isna().sum()




# Info() function is use for information about data like index, column name, values,NaN value, memory used and datatype.
feature.info()




# Describe function() is use for statistic details for all variables.
feature.describe()




# Divide feature and test dataset into training and testing.
feature_train, feature_test, lable_train, lable_test = train_test_split(feature, label, test_size = 0.2, random_state = 42)




# Create the model and fit data of feature_train and lable_train.
model = KNeighborsClassifier(n_neighbors=4)
model.fit(feature_train,lable_train)




# Saving model to disk
pickle.dump(model,open('model.pkl','wb'))




# Predict label_text by model from feature_test values and display.
model_pkl = pickle.load(open('model.pkl','rb'))
y = model.predict(feature_test)




# Display accuracy score between predict label_text(y), lable_test that is tell us how accurate our model.
print(metrics.accuracy_score(y, lable_test))


# Display the error between lable and predict label_text(y)
print(metrics.mean_squared_error(lable_test, y))




# Display the cunfusion matrix that represent how much data checked by model.
metrics.confusion_matrix(y, lable_test)




# Classification_report represent precision, recall, f1-score, support etc.
print(metrics.classification_report(y, lable_test))

