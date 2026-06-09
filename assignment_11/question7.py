#Find the sum of values in a 2D array using for loop
import numpy as np

arr = np.array([[1, 2],
                [3, 4]])

total = 0

for row in arr:
    for item in row:
        total += item

print(total)