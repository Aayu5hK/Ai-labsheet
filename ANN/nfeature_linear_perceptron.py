import numpy as np

class LinearPerceptron:
    def __init__(self, learning_rate=0.01, epochs=100):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0.0
        
        print(f"\nTraining with {n_features} features")
        print("="*50)
        
        for epoch in range(1, self.epochs + 1):
            total_error = 0
            for x_i, y_i in zip(X, y):
                y_pred = np.dot(x_i, self.weights) + self.bias
                error = y_i - y_pred
                
                self.weights += self.lr * error * x_i
                self.bias += self.lr * error
                total_error += error ** 2
            
            mse = total_error / n_samples
            print(f"Epoch {epoch:3d} | MSE: {mse:.6f}")
            
            if mse < 1e-6:
                break
                
        return self

if __name__ == "__main__":
    # Generate test datasets
    np.random.seed(42)
    
    for n in [4, 5]:
        # Create dataset
        X = np.random.rand(10, n)
        true_weights = np.random.uniform(-1, 1, size=n)
        true_bias = 5
        y = np.dot(X, true_weights) + true_bias
        
        # Train model
        model = LinearPerceptron(learning_rate=0.01, epochs=100)
        model.fit(X, y)
        
        # Display results
        print("\nFinal Learned Parameters:")
        print("-"*50)
        print(f"Weights: {np.array2string(model.weights, precision=4)}")
        print(f"Bias: {model.bias:.4f}")
        print("="*50 + "\n")