#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:40:11 2019

@author: shanedaly



Sepsis Detection


"""
import time

import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

class dataset:
    """ 
    Read In The CSV Files, Delimited by | 
    """
    def read_file(filename):
        array = pd.read_csv(filename, delimiter=",")
        return array
    
    """
    Initially, I will focus on two readily available vital signs,
    that can be achieved by manual counting, or by using devices.
    
    small_data will contain:
        HR
        RR
        (Sepsis Label)
        
    big_data will contain:
        HR
        RR
        SPO2
        Temp
        Age
        Gender
        (Sepsis Label)
    """
    def data_cleaning(data):
        big_data = data.filter(['HR', 'O2Sat', 'Temp', 'Resp', 'Age', 'Gender', 'SepsisLabel'])
        small_data = data.filter(['HR', 'Resp', 'SepsisLabel'])
        
        # Impute the data to replace NaN with mean of the column.
        small_data = small_data.dropna() #fillna(small_data.mean())
        big_data = big_data.dropna() #fillna(big_data.mean())
        return small_data, big_data
    
    def pre_processing(data):
        num_columns = len(data.columns) -1 # makes method global
        X = data.iloc[:,:-1].values # the first n columns
        y = data.iloc[:, num_columns] # the results
        
        # Split the dataset using train/test split.
        X_train, X_test, y_train, y_test = tts(X, y, test_size=0.2) 
        
        # Perform feature scaling.
        # Allows for features to be uniformly evaluated.
        # scaler = StandardScaler()
        # scaler.fit(X_train)
        # X_train = scaler.transform(X_train)  
        # X_test = scaler.transform(X_test)
        
        return X_train, X_test, y_train, y_test
    # Alter method to allow for hyper-parameter tuning. 
    def knn(X_train, X_test, y_train, y_test, n):
        classifier = KNeighborsClassifier(n_neighbors=n)  
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        
        # Evaluate our model 
        return accuracy_score(y_test, y_pred)
        
    
health_data = dataset.read_file("vitals.csv")
small_data, big_data = dataset.data_cleaning(health_data)
# print(small_data.loc[small_data["SepsisLabel"] == 1])

# Perform pre-processing on the smaller of two dataframes. 
X_train, X_test, y_train, y_test = dataset.pre_processing(big_data)

best_acc = -1
best_n = 0

accuracies = []
ns = []
# Hyper param opto
# for n in range(10):
for n in range(1,101):
    accuracy = dataset.knn(X_train, X_test, y_train, y_test, n)
    
    if accuracy > best_acc:
        best_acc = accuracy
        best_n = n
    else:
        pass
accuracies.append(best_acc)
ns.append(best_n)
best_acc = -1
best_n = 0
    

avg1 = sum(accuracies) / len(accuracies) 
avg2 = sum(ns) / len(ns) 
    
print("Best Accuracy = ", avg1)
print("Best # Neighbours = ", avg2)
    


