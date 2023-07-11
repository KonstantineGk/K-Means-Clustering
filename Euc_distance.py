import numpy as np
# Calculate the Euclidean distance of 2 points.

def distance_Euc(X,Y):
    # Find dimensions
    row, col = X.shape
    sum = 0
    for i in range(0,col):
        sum += (X[:,i] - Y[i]) ** 2
    
    Distance = np.sqrt(sum)
    return Distance