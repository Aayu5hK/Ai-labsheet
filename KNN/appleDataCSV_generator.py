import pandas as pd
import random
import numpy as np

# Define category distributions based on size-texture patterns
def assign_category(size, texture):
    if size >= 4 and texture >= 6:
        return "Excellent"
    elif size <= 2 and texture <= 3:
        return "Bad" 
    elif (size == 3 and texture <= 2) or (size <= 1 and texture <= 3):
        return "Average"
    else:
        return random.choices(["Good", "Average"], weights=[0.7, 0.3])[0]

# Generate 200 apples with realistic patterns
data = []
for _ in range(200):
    size = random.choices(
        [0, 1, 2, 3, 4, 5, 6, 7],
        weights=[0.1, 0.15, 0.15, 0.2, 0.2, 0.1, 0.05, 0.05]
    )[0]
    
    texture = int(np.clip(
        random.gauss(
            mu=4 if size < 3 else 6,  # Mean texture based on size
            sigma=2
        ), 0, 10
    ))
    
    category = assign_category(size, texture)
    data.append([size, texture, category])

# Create DataFrame
df = pd.DataFrame(data, columns=["Size", "Texture", "Category"])

# Shuffle and save
df = df.sample(frac=1).reset_index(drop=True)
df.to_csv("apple_knn_data_200.csv", index=False)
print("Generated apple_knn_data_200.csv with 200 apples:")
print(df.head(10))