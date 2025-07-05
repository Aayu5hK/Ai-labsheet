import csv
import random

# Define possible values
categories = ['A', 'B', 'C']
texture_mapping = {
    1: 'Low',
    5: 'Medium',
    9: 'High'
}

# Generate data matching your exact example pattern
def generate_apples(num):
    apples = []
    for i in range(1, num + 1):
        texture_value = random.choice([1, 5, 9])
        apples.append({
            'ID': i,
            'Size': random.randint(1, 4),  # Sizes 1-4 like your example
            'TextureValue': texture_value,
            'TextureLabel': texture_mapping[texture_value],
            'Category': random.choice(categories)
        })
    return apples

# Write to CSV
with open('apple_data_custom_200.csv', 'w', newline='') as csvfile:
    fieldnames = ['ID', 'Size', 'TextureValue', 'TextureLabel', 'Category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for apple in generate_apples(200):  # Generate 200 rows
        writer.writerow(apple)

print("Generated apple_data_custom_200.csv with 200 entries!")