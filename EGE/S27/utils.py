import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import centroid
from scipy.spatial import ConvexHull


def plot_clusters(*datasets):
    plt.figure(figsize=(8, 6))
    colors = ['blue', 'red', 'green', 'purple', 'orange', 'blue', 'red', 'green', 'purple', 'orange', 'blue', 'red',
              'green', 'purple', 'orange']  # Extend as needed

    for idx, data in enumerate(datasets):
        data = np.array(data)
        plt.scatter(data[:, 0], data[:, 1], color=colors[idx % len(colors)], label=f'Cluster {idx}')

        # Draw convex hulls
        if len(data) > 2:
            hull = ConvexHull(data)
            for simplex in hull.simplices:
                plt.plot(data[simplex, 0], data[simplex, 1], color=colors[idx % len(colors)])

        # Compute and plot centroids
        # centroid_point = centroid(data)
        # plt.scatter(*centroid_point, color='black', marker='x', s=100, label=f'Centroid {idx}')

    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.title("Clusters with Convex Hulls and Centroids")
    plt.show()
