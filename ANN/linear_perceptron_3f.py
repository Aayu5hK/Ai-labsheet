import numpy as np

np.random.seed(42)

def true_function(x1, x2, x3):
    return 2 * x1 + 3 * x2 - x3 + 5

X = np.random.rand(10, 3)
y_true = np.array([true_function(x[0], x[1], x[2]) for x in X])

print("Dataset (x1, x2, x3, y):")
for i in range(10):
    print(f"{X[i][0]:.3f}\t{X[i][1]:.3f}\t{X[i][2]:.3f}\t{y_true[i]:.3f}")

w1, w2, w3 = np.random.randn(3)
b = np.random.randn()

alpha = 0.01
epochs = 100

for epoch in range(1, epochs + 1):
    total_error = 0
    print(f"\nEpoch {epoch}:")
    print(f"Current weights: w1={w1:.4f}, w2={w2:.4f}, w3={w3:.4f}, b={b:.4f}")
    
    for i in range(len(X)):
        x1, x2, x3 = X[i]
        target = y_true[i]
        
        y_pred = w1 * x1 + w2 * x2 + w3 * x3 + b
        error = target - y_pred
        total_error += error ** 2
        
        w1 += alpha * error * x1
        w2 += alpha * error * x2
        w3 += alpha * error * x3
        b += alpha * error
        
        print(f"Sample {i}:")
        print(f"x: [{x1:.3f}, {x2:.3f}, {x3:.3f}]")
        print(f"Target: {target:.3f} | Pred: {y_pred:.3f} | Error: {error:.3f}")
        print(f"Updated weights: w1={w1:.4f}, w2={w2:.4f}, w3={w3:.4f}, b={b:.4f}")
    
    mse = total_error / len(X)
    print(f"Epoch {epoch} MSE: {mse:.6f}")

    if mse < 1e-6:
        print("\nConverged.")
        break

print(f"\nFinal weights: w1={w1:.4f}, w2={w2:.4f}, w3={w3:.4f}, b={b:.4f}")