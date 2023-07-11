#_____________ 1066600 _________________#
import matplotlib.pyplot as plt

from Load_data import Load
from Kmeans_algo import kmeans

def main():
    X = Load()
    clusters, centroids = kmeans(X)

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

    # Plots Points
    plt.figure(2)
    ax2 = plt.gca()
    ax2.plot(X[:100,0],X[:100,1],'.',color = 'b') # 0
    ax2.plot(X[100:,0],X[100:,1],'.',color = 'r') # 1

    # Plot circles
    for i in range(0,200):
        if clusters[i] == 0:
            ax2.add_patch( plt.Circle( (X[i,0], X[i,1]) , 0.1, color = 'b', fill=False) ) # Cluster 0
        elif clusters[i] == 1:
            ax2.add_patch( plt.Circle( (X[i,0], X[i,1]) , 0.1, color = 'r', fill=False) ) # Cluster 1
    plt.show()

if __name__ == "__main__":
    main()

