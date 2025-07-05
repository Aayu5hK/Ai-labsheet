import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class KMeans4D:
    def __init__(self, k=3, max_iters=100, random_state=42):
        self.k = k
        self.max_iters = max_iters
        self.random_state = random_state
        self.centroids = None
        self.labels = None
        self.wcss = None

    def fit(self, data):
        np.random.seed(self.random_state)
        self.centroids = data[np.random.choice(len(data), self.k, replace=False)]
        
        for iteration in range(self.max_iters):
            # Assign clusters
            distances = np.linalg.norm(data[:, np.newaxis] - self.centroids, axis=2)
            self.labels = np.argmin(distances, axis=1)
            
            # Update centroids
            new_centroids = np.array([
                data[self.labels == j].mean(axis=0) if np.any(self.labels == j) else self.centroids[j]
                for j in range(self.k)
            ])
            
            if np.allclose(self.centroids, new_centroids):
                print(f"Converged after {iteration + 1} iterations")
                break
                
            self.centroids = new_centroids
        
        # Calculate WCSS
        self.wcss = sum(np.sum((data[self.labels == j] - self.centroids[j])**2) 
                       for j in range(self.k))
        return self

    def visualize_3d(self, data):
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        colors = ['red', 'green', 'blue', 'purple', 'orange'][:self.k]
        
        for j in range(self.k):
            cluster_data = data[self.labels == j]
            ax.scatter(cluster_data[:, 0], cluster_data[:, 1], cluster_data[:, 2],
                       color=colors[j], label=f'Cluster {j}', alpha=0.7)
            
        ax.scatter(self.centroids[:, 0], self.centroids[:, 1], self.centroids[:, 2],
                   marker='X', s=200, color='black', label='Centroids')
        
        ax.set_title(f"3D Projection of 4D K-Means (k={self.k})")
        ax.set_xlabel("Feature 1")
        ax.set_ylabel("Feature 2")
        ax.set_zlabel("Feature 3")
        ax.legend()
        plt.show()

if __name__ == "__main__":
    # 4D dataset
    data = np.array([
        [1.0, 1.5, 0.8, 1.2], [1.2, 1.7, 0.9, 1.1],
        [1.1, 1.4, 0.7, 1.3], [1.3, 1.6, 0.85, 1.15],
        [4.0, 4.5, 3.8, 4.2], [4.2, 4.7, 3.9, 4.1],
        [4.1, 4.4, 3.7, 4.3], [4.3, 4.6, 3.85, 4.15],
        [2.0, 2.2, 1.8, 2.1], [2.1, 2.3, 1.9, 2.0],
        [4.5, 4.8, 4.0, 4.4], [4.4, 4.9, 3.95, 4.35]
    ])
    
    # Initialize and fit model
    kmeans = KMeans4D(k=3, max_iters=100)
    kmeans.fit(data)
    
    # Display results
    print("\nFinal Cluster Assignments:")
    for idx, point in enumerate(data):
        print(f"Sample {idx}: {point.round(2)} → Cluster {kmeans.labels[idx]}")
    
    print("\nFinal Centroids:")
    print(np.array2string(kmeans.centroids, precision=4, suppress_small=True))
    
    print(f"\nWCSS (Within-Cluster Sum of Squares): {kmeans.wcss:.4f}")
    
    # 3D Visualization (projecting first 3 features)
    kmeans.visualize_3d(data)
    
    # 2D Visualization (projecting first 2 features)
    plt.figure(figsize=(8, 6))
    colors = ['red', 'green', 'blue']
    for j in range(kmeans.k):
        cluster_data = data[kmeans.labels == j]
        plt.scatter(cluster_data[:, 0], cluster_data[:, 1], 
                    color=colors[j], label=f'Cluster {j}', alpha=0.7)
    plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1],
                marker='X', s=200, color='black', label='Centroids')
    plt.title(f"2D Projection (Features 1 & 2)\nK-Means Clustering (k={kmeans.k})")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.grid(True)
    plt.show()