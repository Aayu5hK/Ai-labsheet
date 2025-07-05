import itertools

def step(x):
    return 1 if x >= 0 else 0

def generate_truth_table(n, gate_type):
    return [(list(bits), int(all(bits) if gate_type == "AND" else any(bits))) 
            for bits in itertools.product([0, 1], repeat=n)]

def train_perceptron(n, gate_type, lr=0.1, max_epochs=100):
    data = generate_truth_table(n, gate_type)
    weights = [0.0] * n
    bias = 0.0
    
    print(f"\nTraining {gate_type} Gate (n={n})")
    print(f"Initial weights: {weights}, bias: {bias:.2f}")

    for epoch in range(max_epochs):
        errors = 0
        for inputs, target in data:
            output = step(sum(w*x for w,x in zip(weights, inputs)) + bias)
            error = target - output
            
            if error != 0:
                errors += 1
                weights = [w + lr*error*x for w,x in zip(weights, inputs)]
                bias += lr * error
            
            print(f"Input: {inputs} Target: {target} Output: {output} Weights: {[f'{w:.2f}' for w in weights]} Bias: {bias:.2f}")
        
        if errors == 0:
            print("Training complete")
            break

    correct = sum(1 for inputs, target in data 
               if step(sum(w*x for w,x in zip(weights, inputs)) + bias) == target)
    
    print(f"\nFinal weights: {[f'{w:.4f}' for w in weights]}")
    print(f"Final bias: {bias:.4f}")
    print(f"Accuracy: {correct/len(data)*100:.1f}%")
    print("=" * 40)

test_configs = [(3, "AND"), (3, "OR"), (4, "AND"), (4, "OR")]
for n, gate in test_configs:
    train_perceptron(n, gate)