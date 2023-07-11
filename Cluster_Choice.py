import numpy as np
from Euc_distance import distance_Euc

def choose_Cluster(X, cent):
    # Calc distances from Centroids
    DistfromCen0 = distance_Euc(X,cent[0,:] )
    DistfromCen1 = distance_Euc(X,cent[1,:] )
    
    # Assign closest Centroid to point
    Clusters = np.where(DistfromCen0 >= DistfromCen1, 1, 0)
    
    # Return the array
    return Clusters