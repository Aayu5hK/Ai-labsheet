import numpy as np
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, k=2, max_iters=100, random_state=42):
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
            new_centroids = np.array([data[self.labels == j].mean(axis=0) for j in range(self.k)])
            
            if np.allclose(self.centroids, new_centroids):
                print(f"Converged after {iteration + 1} iterations")
                break
                
            self.centroids = new_centroids
        
        # Calculate WCSS
        self.wcss = sum(np.sum((data[self.labels == j] - self.centroids[j])**2) 
                       for j in range(self.k))
        
        return self

    def plot_results(self, data):
        plt.figure(figsize=(8, 6))
        colors = ['red', 'blue', 'green', 'purple', 'orange'][:self.k]
        
        for j in range(self.k):
            cluster_data = data[self.labels == j]
            plt.scatter(cluster_data[:, 0], cluster_data[:, 1], 
                        color=colors[j], label=f'Cluster {j}', alpha=0.7)
            
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1],
                    marker='X', s=200, color='black', label='Centroids')
        
        plt.title(f"K-Means Clustering (k={self.k})")
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.legend()
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    # Sample 2D dataset
    data = np.array([
        [1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6],
        [9, 11], [8, 2], [10, 2], [9, 3], [4, 9]
    ])
    
    # Initialize and fit model
    kmeans = KMeans(k=2, max_iters=100)
    kmeans.fit(data)
    
    # Display results
    print("\nFinal Cluster Assignments:")
    for idx, point in enumerate(data):
        print(f"Point {point} → Cluster {kmeans.labels[idx]}")
    
    print("\nFinal Centroids:")
    print(np.array2string(kmeans.centroids, precision=4))
    
    print(f"\nWCSS (Within-Cluster Sum of Squares): {kmeans.wcss:.4f}")
    
    # Visualization
    kmeans.plot_results(data)