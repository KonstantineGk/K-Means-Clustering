import numpy as np

def addDim(X):
    rows , cols = X.shape
    Z = np.zeros((rows,1))
    
    for i in range(0,rows):
        Z[i] = np.linalg.norm(X[i,:]) ** 2
    X = np.concatenate((X,Z), axis = 1)
    return X