import numpy as np
import scipy.io

# Load files
def Load():
    # Load .mat file
    mat = scipy.io.loadmat(r"C:\Users\Eygenia\Desktop\kmeans\data33.mat")
    X = np.array(mat['X'])
    # Reshape matrix 
    Xs = np.reshape( X[0,:], (200,1))
    Ys = np.reshape( X[1,:], (200,1))
    X = np.concatenate( (Xs,Ys), axis = 1)
    return X