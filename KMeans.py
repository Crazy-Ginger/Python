#!/usr/bin/env  python3
# import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

# initial inputs
num_of_coords = 10000
initial_cluster_means = [(1, 1), (1, 0), (0, 1), (1, 1), (1, 0), (0, 1), (1, 1), (1, 0), (0, 1), (1, 1), (1, 0), (0, 1), (1, 1), (1, 0), (0, 1), (1, 1)]
num_clusters = len(initial_cluster_means)
print("num_clusters: ", num_clusters)
dataset = make_blobs(n_samples=num_of_coords, centers=initial_cluster_means, n_features=num_clusters, cluster_std=2)

# print("dataset: ",dataset)

random_data = dataset[0]
# print(random_data)

k = KMeans(n_clusters=num_clusters)
print(k)

cluster_data = k.fit_predict(random_data)
print(cluster_data)
centers = k.cluster_centers_


plt.scatter(random_data[:, 0], random_data[:, 1], c=cluster_data, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()
