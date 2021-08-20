# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 09:51:50 2021

@author: User
"""
#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load parkinson dataset and separate target variable
data = pd.read_csv("pd_speech_features.csv")
print(data.head())
x= data.iloc[1:757,0:753]
y = data.iloc[1:757 , 754]

#split dataset into train and test data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x, y,test_size = 0.25,random_state =0)

#standardization
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

#creating the classifier object
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy',random_state=0)

#perform training
classifier = classifier.fit(x_train , y_train)

#prediction on test data
y_pred = classifier.predict(x_test)
print(y_pred)

#to calculate accuracy
from sklearn import metrics
print("accuracy:",metrics.accuracy_score(y_test,y_pred))

#construct confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

#plot decision tree with plot_tree
from sklearn import tree
fig = plt.subplots(figsize = (30,20))
tree.plot_tree(classifier,fontsize =10,filled = True)
plt.show()

