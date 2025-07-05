# An Apple Categorizer Using K-Nearest Neighbors.

It features a very simple Python implementation of a KNN classifier that aims to categorize apples based on size and texture.

# Overview:
The CSV file reads the apple data, which entails attributes such as:

- **Size (int)**

- **Texture (int)**

- **Category (string label, e.g., Good, Bad, Excellent)**

Then, it calculates a Euclidean distance from this apple to every entry in that dataset once given a new apple's size and texture. It further selects the top k of those nearest neighbors and bases the prediction of the category of it on majority voting.
 # How It Works

- **Loads the apple data from a CSV file.**

- **The size and texture of the new apple are taken as user input.**

- **Calculate Euclidean distances of the new apple to
each apple in the dataset.**

- **Sort all the distances and choose the k-nearest neighbors.**

- **Estimate the category prediction by the majority votes received by the neighbors' categories.**

- **Prints the predicted category to the screen.**

  # Result
![image](https://github.com/user-attachments/assets/35b2c183-7072-4c9d-9155-e9915660a421)
![image](https://github.com/user-attachments/assets/9eb83b06-1415-4e86-8e93-ac2bf756f04a)
