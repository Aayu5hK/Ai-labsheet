import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

try:
    df = pd.read_csv("KNN/appleData.csv")
    
    if df.empty:
        raise ValueError("CSV file is empty")
    if not {'Size', 'Texture', 'Category'}.issubset(df.columns):
        raise ValueError("CSV missing required columns")

    def manhattan_distance(x1, x2):
        return abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])

    class_labels = df['Category'].unique()
    class_to_int = {label: idx for idx, label in enumerate(class_labels)}
    df['CategoryInt'] = df['Category'].map(class_to_int)

    def knn_classify_fixed(new_item, k, dataset):
        distances = []
        for i, row in dataset.iterrows():
            features = [row['Size'], row['Texture']]
            dist = manhattan_distance(new_item, features)
            distances.append((i, dist))
        distances.sort(key=lambda x: x[1])
        top_k = distances[:k]
        categories = [dataset.iloc[i]['Category'] for i, _ in top_k]
        freq = Counter(categories)
        return freq.most_common(1)[0][0]

    x_min, x_max = df['Size'].min() - 1, df['Size'].max() + 1
    y_min, y_max = df['Texture'].min() - 1, df['Texture'].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.2),
                         np.arange(y_min, y_max, 0.2))

    Z = np.array([class_to_int[knn_classify_fixed([x, y], 3, df)] 
                 for x, y in zip(xx.ravel(), yy.ravel())])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(10, 7))
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='Accent')

    for label in class_labels:
        subset = df[df['Category'] == label]
        plt.scatter(subset['Size'], subset['Texture'], label=label, edgecolor='k')

    new_apple = [2, 0]
    predicted_class = knn_classify_fixed(new_apple, 3, df)
    plt.scatter(new_apple[0], new_apple[1], c='red', s=100, marker='X',
                label=f'New Apple → {predicted_class}', edgecolor='black')

    plt.title("KNN Decision Boundary for Apples (k=3, Manhattan Distance)")
    plt.xlabel("Size")
    plt.ylabel("Texture")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Error: File not found at 'KNN/appleData.csv'")
except Exception as e:
    print(f"An error occurred: {str(e)}")