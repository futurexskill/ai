# -*- coding: utf-8 -*-
"""using_classification_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pt8r3sSTjzugMAyRUZobF8f48XjQkEUE

## Import the libraries
"""

import pickle
import numpy as np

filename = "knnmodel.pickle"
filename2 = "sc.pickle"

"""## Load the Model and the Scaler"""

classifier = pickle.load(open(filename,'rb'))

sc = pickle.load(open(filename2,'rb'))

"""## Predict using the Model"""

new_pred = classifier.predict(sc.transform(np.array([[40,20000]])))
new_pred

new_pred_proba = classifier.predict_proba(sc.transform(np.array([[40,20000]])))[:,1]
new_pred_proba

new_pred = classifier.predict(sc.transform(np.array([[42,50000]])))
new_pred

new_pred_proba = classifier.predict_proba(sc.transform(np.array([[42,50000]])))[:,1]
new_pred_proba

