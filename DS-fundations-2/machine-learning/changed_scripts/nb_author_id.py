#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
# create a classifier
clf = GaussianNB()
# fit it with training features and training labels
t0 = time()
clf.fit(features_train, labels_train)
print("tempo de treinamento:", round(time()-t0, 3), "s")
# create a vector of predictions
t0 = time()
pred = clf.predict(features_test)
print("tempo de predicao:", round(time()-t0, 3), "s")
# quantify how well is doing
accuracy = accuracy_score(pred, labels_test)
print(accuracy) 
#########################################################


