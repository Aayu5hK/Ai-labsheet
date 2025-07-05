# k-Means Clustering Implementation

## Overview
This project implements two versions of k-Means Clustering:
1. Basic version for 2 features with k=2 clusters
2. Generalized version for arbitrary features and clusters

## 2-Feature k-Means (k=2)

### Implementation
- Dataset: 10 samples with 2 features  
- Uses Euclidean distance  
- Random centroid initialization  
- Runs until convergence or max 100 iterations  

### Output
![2-feature clustering result](https://github.com/user-attachments/assets/fa7a0889-86ff-42f3-8bd8-56fece36739b)  
*Final cluster assignments and centroids*

![2-feature visualization](https://github.com/user-attachments/assets/003b51ef-d352-4b4a-ac81-2771ad395f68)  
*Cluster visualization (2D scatter plot)*

## Generalized k-Means (4 features, k=3) 

### Implementation  
- Dataset: 12 samples with 4 features  
- Projects to 2D for visualization  
- Computes WCSS metric  

### Output
![Generalized clustering steps](https://github.com/user-attachments/assets/e1cd314d-29f1-44d9-93f6-31b549a2273e)  
*Cluster assignment process*

![4-feature visualization](https://github.com/user-attachments/assets/52c6102f-f965-4cbd-8372-353d5c3a6efe)  
*Projected cluster visualization*

![WCSS calculation](https://github.com/user-attachments/assets/982dc09f-1238-4548-9d18-f40f4541af35)  
*Projected cluster visualization*

