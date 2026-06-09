#Select each element and specific element from array
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print(arr[0][1])      
print(arr[1][2])      

for row in arr:
    for item in row:
        print(item)