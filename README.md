# Enhanced-K-means-Clustering-with-an-Additional-Dimension
Developed a customized K-means clustering algorithm to differentiate between two datasets.
By augmenting the 2D vectors with an additional dimension representing the distance from the origin, the algorithm achieved significant enhancements in clustering performance.
It utilized both the coordinates and distances from the origin to achieve improved results.

This Project was developed for the Machine Learning course (University of Patras).
TO RUN Kmeans_Clustering:
1) pip install numpy, math, matplotlib, scipy, random.
2) Put "data33.mat" in the same file with script.
3) Run :D

Description:
1) Load: Loads data from data33.mat.
2) distance_Euc: Calculate the Euclidean distance from two 2D points.
3) init_Centroids: Choose 2 random centroids from the dataset.
4) choose_Cluster: Assing datapoints to closest centroid and create clusters.
5) update_Centroids: Update centroids based on the mean of data points assigned to each cluster.
6) kmeans: Execute Kmeans
7) main: Execute functions in order. Calculate mistakes using the secret info that the dataset is split in half.
8) Finally plot datapoints with true label and circle around them with the cluster assigned from kmeans.

TO RUN Kmeans_Clustering:
1) pip install numpy, math, matplotlib, scipy, random, mpl_toolkits.
2) Put "data33.mat" in the same file with script.
3) Run :D

The only difference is that during the Load we add a 3rd dimension to the dataset with ||X[:]||**2
and modify all other functions to support it.
Finall we can also plot in 3D.

Thank you!
