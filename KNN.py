import math
import random
from collections import Counter
from typing import List

# Constants
K = 5  # Number of neighbors to consider
DATA_SIZE = 200  # Total dataset size

class Person:
    def __init__(self, age: int, income: int, jeans_type: str):
        self.age = age
        self.income = income
        self.jeans_type = jeans_type

class Neighbor:
    def __init__(self, distance: float, jeans_type: str):
        self.distance = distance
        self.jeans_type = jeans_type

def generate_dataset(size: int) -> List[Person]:
    """Generate a larger dataset with realistic distributions"""
    dataset = []
    jeans_types = ["Skinny", "Regular", "Bootcut", "Relaxed", "Loose"]
    
    for _ in range(size):
        age = random.randint(16, 65)
        
        # Income roughly correlates with age
        base_income = 8000 + age * 500
        income = base_income + random.randint(-2000, 5000)
        
        # Jeans type distribution changes with age
        if age < 20:
            jeans_type = random.choices(jeans_types, weights=[60, 20, 10, 5, 5])[0]
        elif age < 30:
            jeans_type = random.choices(jeans_types, weights=[30, 40, 15, 10, 5])[0]
        elif age < 40:
            jeans_type = random.choices(jeans_types, weights=[10, 30, 30, 20, 10])[0]
        elif age < 50:
            jeans_type = random.choices(jeans_types, weights=[5, 20, 25, 30, 20])[0]
        else:
            jeans_type = random.choices(jeans_types, weights=[2, 10, 20, 30, 38])[0]
        
        dataset.append(Person(age, income, jeans_type))
    
    return dataset

def compute_distance(age1: int, income1: int, age2: int, income2: int) -> float:
    """Calculate Euclidean distance between two points"""
    return math.sqrt((age1 - age2)**2 + (income1 - income2)**2)

def predict_jeans_type(neighbors: List[Neighbor], k: int) -> str:
    """Predict jeans type based on k-nearest neighbors"""
    k_nearest = neighbors[:k]
    type_counts = Counter(n.jeans_type for n in k_nearest)
    return type_counts.most_common(1)[0][0]

def main():
    # Generate larger dataset
    dataset = generate_dataset(DATA_SIZE)
    
    # Get user input
    try:
        input_age = int(input("Enter age (16-65): "))
        if not 16 <= input_age <= 65:
            raise ValueError("Age must be between 16 and 65")
            
        input_income = int(input("Enter monthly income (NPR): "))
        if input_income < 0:
            raise ValueError("Income must be positive")
            
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # Find all neighbors with their distances
    neighbors = [
        Neighbor(
            compute_distance(input_age, input_income, person.age, person.income),
            person.jeans_type
        ) for person in dataset
    ]
    
    # Sort by distance (ascending)
    neighbors.sort(key=lambda x: x.distance)
    
    # Make prediction
    predicted = predict_jeans_type(neighbors, K)
    
    # Show results
    print(f"\nPredicted jeans type: {predicted}")
    print(f"Based on {K} nearest neighbors:")
    for i, neighbor in enumerate(neighbors[:K], 1):
        print(f"{i}. Age: {dataset[i].age}, Income: {dataset[i].income}, Jeans: {neighbor.jeans_type}, Distance: {neighbor.distance:.2f}")

if __name__ == "__main__":
    main()