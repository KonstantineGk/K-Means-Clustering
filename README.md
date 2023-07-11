# Enhanced-K-means-Clustering-with-an-Additional-Dimension
Developed a customized K-means clustering algorithm to differentiate between two datasets.
By augmenting the 2D vectors with an additional dimension representing the distance from the origin, the algorithm achieved significant enhancements in clustering performance.
It utilized both the coordinates and distances from the origin to achieve improved results.

This Project was developed for the Machine Learning course (University of Patras).
TO RUN main.py or main3d.py:
1) pip install numpy, math, matplotlib, scipy, random.
2) Put "data33.mat" in the same file with script and file your adress in Load_file.
3) Run main.py or main3d.py. 

Description:
1) Load_data.py: Loads data from data33.mat.
2) Euc_distance.py: Calculate the Euclidean distance from two points.
3) Init_Centroids.py: Choose 2 random centroids from the dataset.
4) Cluster_Choice.py: Assing datapoints to closest centroid and create clusters.
5) Centroid_Update.py: Update centroids based on the mean of data points assigned to each cluster.
6) Kmeans_algo.py: Execute Kmeans
7) main.py: Execute functions in order. Calculate mistakes using the secret info that the dataset is split in half. Finally plot datapoints with true label and circle around them with the cluster assigned from kmeans.
8) main3d.py: Same with main but with added dimension.
