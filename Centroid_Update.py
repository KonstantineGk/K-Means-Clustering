import numpy as np

# Update centroids based on the mean of data points assigned to each cluster
def update_Centroids(X, Clusters):
    row, col = X.shape
    
    Cluster0_points = X[ Clusters == 0]
    Cluster1_points = X[ Clusters == 1]
    
    Centroid0 = np.mean(Cluster0_points, axis=0)
    Centroid1 = np.mean(Cluster1_points, axis=0)
    
    New_Centroids = np.reshape( np.concatenate( (Centroid0,Centroid1), axis = 0), (2,col) )
    return New_Centroids