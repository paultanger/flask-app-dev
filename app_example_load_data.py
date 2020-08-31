# Here we train and pickle a logistic regression model on the iris dataset

# Based on:
# http://scikit-learn.org/stable/auto_examples/linear_model/plot_iris_logistic.html

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import pickle

# import data
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
Y = iris.target

# declare model
logreg = LogisticRegression(C=1e5, solver='lbfgs', multi_class='multinomial')

# fit the data
logreg.fit(X, Y)

# pickle the data (wouldn't normally do this but want to plot prediction vs the train data)
trainXY = np.hstack((X,Y.reshape(-1,1)))
with open('data/trainXY.pkl', 'wb') as f:
    pickle.dump(trainXY, f)

# pickle the model
with open('data/model_logreg.pkl', 'wb') as f:
    pickle.dump(logreg, f)