def step_activation(x, threshold=0):
    return 1 if x >= threshold else 0

def train_perceptron(gate_name, dataset, learning_rate=0.1, max_epochs=100):
    # Initialize weights and bias
    weights = [0.0] * (len(dataset[0]) - 1)  # Number of inputs
    bias = 0.0
    
    print(f"\n=== Training {gate_name} Gate Perceptron ===")
    print(f"Initial Configuration:")
    print(f"Weights: {[f'w{i+1}: {w:.2f}' for i, w in enumerate(weights)]}")
    print(f"Bias: {bias:.2f}\n")
    
    for epoch in range(max_epochs):
        errors = 0
        print(f"Epoch {epoch + 1}:")
        
        for sample in dataset:
            inputs = sample[:-1]
            target = sample[-1]
            
            # Calculate weighted sum
            weighted_sum = sum(w * x for w, x in zip(weights, inputs)) + bias
            output = step_activation(weighted_sum)
            error = target - output
            
            if error != 0:
                errors += 1
                # Update weights and bias
                for i in range(len(weights)):
                    weights[i] += learning_rate * error * inputs[i]
                bias += learning_rate * error
            
            print(f"  Inputs: {inputs} | Target: {target} | Output: {output} | ", end='')
            print(f"Weights: {[f'{w:.2f}' for w in weights]} | Bias: {bias:.2f}")
        
        if errors == 0:
            print("\nTraining converged successfully!")
            break
    else:
        print("\nMaximum epochs reached without full convergence.")
    
    # Final evaluation
    correct = 0
    for sample in dataset:
        inputs = sample[:-1]
        target = sample[-1]
        output = step_activation(sum(w * x for w, x in zip(weights, inputs)) + bias)
        correct += (output == target)
    
    accuracy = (correct / len(dataset)) * 100
    
    print("\n=== Training Results ===")
    print(f"Final Weights: {[f'w{i+1}: {w:.2f}' for i, w in enumerate(weights)]}")
    print(f"Final Bias: {bias:.2f}")
    print(f"Classification Accuracy: {accuracy:.2f}%")
    print("=" * 40 + "\n")
    
    return weights, bias

# Test cases
def test_perceptron(n):
    print(f"\n{'#' * 20}")
    print(f"TESTING WITH n = {n}")
    print(f"{'#' * 20}")
    
    # Generate all possible binary inputs of length n
    from itertools import product
    binary_inputs = list(product([0, 1], repeat=n))
    
    # Test AND-like function (all inputs must be 1)
    and_data = [(*inputs, int(all(inputs))) for inputs in binary_inputs]
    print("\nTraining AND-like function:")
    train_perceptron(f"{n}-input AND", and_data)
    
    # Test OR-like function (any input must be 1)
    or_data = [(*inputs, int(any(inputs))) for inputs in binary_inputs]
    print("\nTraining OR-like function:")
    train_perceptron(f"{n}-input OR", or_data)

# Run tests
test_perceptron(3)  # 3-input perceptron
test_perceptron(4)  # 4-input perceptron