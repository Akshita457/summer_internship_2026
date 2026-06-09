#Adding, Subtracting, Multiplying, Dividing arrays in NumPy
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# 6) Calculate average, mean, median and mode of two NumPy 2D arrays
import numpy as np
from scipy import stats

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6],
                 [7, 8]])

avg = (arr1 + arr2) / 2

print("Average Array:\n", avg)
print("Mean:", np.mean(avg))
print("Median:", np.median(avg))
print("Mode:", stats.mode(avg, axis=None, keepdims=False).mode)