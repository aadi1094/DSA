
#To find the maximum product of two integers in an array

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def maxProduct(arr):
    max_prod = -np.inf
    max_indices = (-1, -1)  # Initialize with invalid indices
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_prod:
                max_prod = product
                max_indices = (1, j)
    return max_prod, max_indices

max_prod, indices = maxProduct(arr)
print("Maximum product:", max_prod)
print("Indices:", indices)
