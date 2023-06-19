#_____________ 1066600 _________________#
import numpy as np
from math import pi
import matplotlib.pyplot as plt
import scipy.io
from random import randint
from mpl_toolkits import mplot3d
#------------------------------------------#
# Load files
def Load():
    # Load .mat file
    mat = scipy.io.loadmat('data33.mat')
    X = np.array(mat['X'])
    
    # Reshape
    Xs = np.reshape( X[0,:], (200,1))
    Ys = np.reshape( X[1,:], (200,1))
    X = np.concatenate( (Xs,Ys), axis = 1)
    
    # Add Z
    Z = np.zeros((200,1))
    for i in range(0,200):
        Z[i] = np.linalg.norm(X[i,:])**2
    X = np.concatenate((X,Z), axis = 1)
    
    # Return Arrays
    return X
#------------------------------------------------------------------------#

#------------------------------------------------------------------------#
# Calculate the Euclidean distance of 2 points.
def distance_Euc(X,Y):
    Distance = np.sqrt( (X[:,0]-Y[0])**2 + (X[:,1]-Y[1])**2 + (X[:,2]-Y[2])**2)
    return Distance
#------------------------------------------------------------------------#

#------------------------------------------------------------------------#
# Find the initial Centroids randomly
def init_Centroids(X):
    Centroid0 = X[randint(0,199), :]
    Centroid1 = X[randint(0,199), :]
    initial_Centroids = np.reshape( np.concatenate((Centroid0, Centroid1), axis = 0),(2,3) )
    return initial_Centroids
#------------------------------------------------------------------------#

#------------------------------------------------------------------------#
def choose_Cluster(X, cent):
    # Calc distances from Centroids
    DistfromCen0 = distance_Euc(X,cent[0,:] )
    DistfromCen1 = distance_Euc(X,cent[1,:] )
    
    # Assign closest Centroid to point
    Clusters = np.where(DistfromCen0 >= DistfromCen1, 1, 0)
    
    # Return the array
    return Clusters
#------------------------------------------------------------------------#

#------------------------------------------------------------------------#
# Update centroids based on the mean of data points assigned to each cluster
def update_Centroids(X, Clusters):
    Cluster0_points = X[ Clusters == 0]
    Cluster1_points = X[ Clusters == 1]
    
    Centroid0 = np.mean(Cluster0_points, axis=0)
    Centroid1 = np.mean(Cluster1_points, axis=0)
    
    New_Centroids = np.reshape( np.concatenate( (Centroid0,Centroid1), axis = 0), (2,3) )
    return New_Centroids
#------------------------------------------------------------------------#

#------------------------------------------------------------------------#
def kmeans(X):
    Centroids = init_Centroids(X)
    Cluster0_metric = []
    Cluster1_metric = []
    
    for _ in range(50):                                     
        prev_Centroids = Centroids    
        Clusters = choose_Cluster(X, Centroids)
        Centroids = update_Centroids(X, Clusters)
        
        Cluster0_metric.append( np.sqrt( (Centroids[0,0]-prev_Centroids[0,0])**2 + (Centroids[0,1]-prev_Centroids[0,1])**2 + (Centroids[0,2]-prev_Centroids[0,2])**2) )
        Cluster1_metric.append( np.sqrt( (Centroids[1,0]-prev_Centroids[1,0])**2 + (Centroids[1,1]-prev_Centroids[1,1])**2 + (Centroids[1,2]-prev_Centroids[1,2])**2) )
    return Clusters, Centroids, np.array( Cluster0_metric ), np.array( Cluster1_metric )
#------------------------------------------------------------------------#

#------------------------------------------------------------------------#
# Main
X = Load()
clusters, centroids, Cluster0_metric, Cluster1_metric = kmeans(X)

# Use of Secret Info to calculate mistake percentage
mistakes0 = 0
mistakes1 = 0
for i in range(0,100):
    if clusters[i] == 1:
        mistakes1+=1
for i in range(100,200):
    if clusters[i] == 0:
        mistakes0+=1

print(mistakes1/200, mistakes0/200)

#------ Plot ---------------#

# Plot Convergence
plt.figure(1)
ax1 = plt.gca()
ax1.plot(Cluster1_metric)
ax1.plot(Cluster0_metric)

# Plots Points
plt.figure(2)
ax2 = plt.axes(projection = '3d')
ax2.plot(X[:100,0],X[:100,1],X[:100,2], '.',color = 'b') # 0
ax2.plot(X[100:,0],X[100:,1],X[100:,2], '.',color = 'r') # 1

plt.figure(3)
ax3 = plt.gca()
ax3.plot(X[:100,0],X[:100,1], '.',color = 'b') # 0
ax3.plot(X[100:,0],X[100:,1], '.',color = 'r') # 1
# Plot circles
for i in range(0,200):
    if clusters[i] == 0:
        ax3.add_patch( plt.Circle( (X[i,0], X[i,1]) , 0.1, color = 'b', fill=False) ) # Cluster 0
    elif clusters[i] == 1:
        ax3.add_patch( plt.Circle( (X[i,0], X[i,1]) , 0.1, color = 'r', fill=False) ) # Cluster 1

plt.show()
