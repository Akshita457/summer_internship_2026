#Iterate 3D array using for loop and nditer
import numpy as np

arr = np.array([[[1, 2], [3, 4]],
                [[5, 6], [7, 8]]])

# Using for loop
for x in arr:
    for y in x:
        for z in y:
            print(z)

# Using nditer
for i in np.nditer(arr):
    print(i)