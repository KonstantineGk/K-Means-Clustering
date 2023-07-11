from Init_Centroids import init_Centroids
from Cluster_Choice import choose_Cluster
from Centroid_Update import update_Centroids

def kmeans(X):
    Centroids = init_Centroids(X)

    for _ in range(50):                                       
        Clusters = choose_Cluster(X, Centroids)
        Centroids = update_Centroids(X, Clusters)
    
    return Clusters, Centroids