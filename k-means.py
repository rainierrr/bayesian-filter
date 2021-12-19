import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = np.array([[1, 1], [1, 2], [1, 3], [1, 5], [2, 3], [2, 4],
                 [3, 1], [4, 1], [4, 4], [5, 3], [6, 3], [6, 5]])
init_cluster_centers = np.array([[1, 2], [4, 1], [4, 4]])

for i in range(1, 3):
    kmeans = KMeans(n_clusters=3, init=init_cluster_centers, max_iter=i)
    kmeans.fit(data)
    print(i)
    print(kmeans.cluster_centers_)

kmeans = KMeans(n_clusters=3, init=init_cluster_centers)
kmeans.fit(data)
y_kmeans = kmeans.predict(data)

plt.scatter(data[:, 0], data[:, 1], c=y_kmeans)
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], s=250, marker='*', c='red')
plt.show()

print(kmeans.n_iter_)
