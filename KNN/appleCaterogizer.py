import csv
import math
from collections import Counter
import os

def load_data(filename):
    data = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            
            # Check available columns
            available_columns = reader.fieldnames or []
            print(f"Available columns in CSV: {available_columns}")
            
            # Try common column name variations
            size_col = next((col for col in available_columns if 'size' in col.lower()), None)
            texture_col = next((col for col in available_columns if 'texture' in col.lower()), None)
            category_col = next((col for col in available_columns if 'category' in col.lower()), None)
            
            if not all([size_col, texture_col, category_col]):
                raise ValueError("CSV must contain size, texture, and category columns")
            
            for row in reader:
                try:
                    size = int(row[size_col])
                    texture = int(row[texture_col])
                    category = row[category_col]
                    data.append((size, texture, category))
                except (ValueError, KeyError) as e:
                    print(f"Skipping invalid row: {row}. Error: {e}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []
    return data

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def predict_category(data, new_item, k=5):
    if not data:
        return "No data available for prediction"
    
    distances = []
    for item in data:
        dist = calculate_distance((item[0], item[1]), new_item)
        distances.append((dist, item[2]))

    distances.sort(key=lambda x: x[0])
    nearest = distances[:k]
    categories = [category for _, category in nearest]
    most_common = Counter(categories).most_common(1)[0][0]
    return most_common

if __name__ == "__main__":
    # Use raw string or forward slashes for path
    data_path = r"KNN\appleData.csv"  # or "KNN/appleData.csv"
    
    dataset = load_data(data_path)
    
    if not dataset:
        print("Failed to load dataset. Please check:")
        print(f"1. File exists at: {os.path.abspath(data_path)}")
        print("2. CSV contains columns for size, texture, and category")
    else:
        try:
            size = int(input("Enter apple size (e.g., 1 to 5): "))
            texture = int(input("Enter apple texture (e.g., 1 to 9): "))
            test_apple = (size, texture)
            
            result = predict_category(dataset, test_apple, k=5)
            print("Predicted Category:", result)
        except ValueError:
            print("Invalid input. Please enter numbers only.")