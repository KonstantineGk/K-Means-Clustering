import numpy as np
from random import randint

# Find the initial Centroids randomly
def init_Centroids(X):
    row, col = X.shape
    Centroid0 = X[randint(0,199), :]
    Centroid1 = X[randint(0,199), :]
    initial_Centroids = np.reshape( np.concatenate((Centroid0, Centroid1), axis = 0),(2,col) )
    return initial_Centroids