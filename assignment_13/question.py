# NUMPY ASSIGNMENT
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


# 1) Replace NaN with 0 and interchange rows
#    and columns of 2D array

print("\n1) Replace NaN with 0 and interchange rows/columns")

arr = np.array([
    [6, -8, 73, -110],
    [np.nan, -8, 0, 94]
])

print("Original Array:")
print(arr)

# Replace NaN with 0
arr_no_nan = np.nan_to_num(arr, nan=0)

print("\nAfter Replacing NaN with 0:")
print(arr_no_nan)

# Interchange rows
row_swapped = arr_no_nan[::-1]

print("\nRows Interchanged:")
print(row_swapped)

# Interchange columns
col_swapped = arr_no_nan[:, ::-1]

print("\nColumns Interchanged:")
print(col_swapped)


# 2) Move axes of 3D array to new positions

print("\n2) Move axes of 3D array")

arr3d = np.arange(24).reshape(2, 3, 4)

print("Original Shape:", arr3d.shape)

moved = np.moveaxis(arr3d, 0, 2)

print("New Shape:", moved.shape)
print(moved)


# 3) Replace NaN values with average of columns

print("\n3) Replace NaN with column averages")

arr = np.array([
    [1, np.nan, 3],
    [4, 5, np.nan],
    [7, 8, 9]
])

print("Original Array:")
print(arr)

col_means = np.nanmean(arr, axis=0)

inds = np.where(np.isnan(arr))

arr[inds] = np.take(col_means, inds[1])

print("\nAfter Replacement:")
print(arr)


# 4) Replace negative values with zero

print("\n4) Replace Negative Values with Zero")

arr = np.array([10, -5, 20, -15, 30])

print("Original Array:")
print(arr)

arr[arr < 0] = 0

print("Modified Array:")
print(arr)


# 5) Average, Mean, Median, Mode of two
#    NumPy 2D arrays

print("\n5) Average, Mean, Median, Mode")

arr1 = np.array([
    [3, 4],
    [5, 6]
])

arr2 = np.array([
    [1, 0],
    [7, 8]
])

avg = (arr1 + arr2) / 2

print("Array 1:")
print(arr1)

print("Array 2:")
print(arr2)

print("\nAverage Array:")
print(avg)

combined = np.concatenate((arr1.flatten(), arr2.flatten()))

mean_val = np.mean(combined)
median_val = np.median(combined)

mode_val = Counter(combined).most_common(1)[0][0]

print("Mean =", mean_val)
print("Median =", median_val)
print("Mode =", mode_val)


# 6) Solve equations using linalg and inverse

print("\n6) Solve Linear Equations")

# x - 2y + 3z = 9
# -x + 3y - z = -6
# 2x - 5y + 5z = 17

A = np.array([
    [1, -2, 3],
    [-1, 3, -1],
    [2, -5, 5]
])

B = np.array([9, -6, 17])

# Method 1: linalg.solve()
solution = np.linalg.solve(A, B)

print("Using np.linalg.solve():")
print("x =", solution[0])
print("y =", solution[1])
print("z =", solution[2])

# Method 2: Inverse Matrix Method
A_inv = np.linalg.inv(A)

solution2 = np.dot(A_inv, B)

print("\nUsing Inverse Matrix:")
print("x =", solution2[0])
print("y =", solution2[1])
print("z =", solution2[2])


# 7) Compare semester results using matplotlib


print("\n7) Semester Result Comparison Graph")

subjects = [
    "Maths",
    "Physics",
    "Chemistry",
    "Programming",
    "English"
]

semester1 = [75, 80, 78, 85, 82]
semester2 = [82, 85, 80, 90, 88]

plt.figure(figsize=(8, 5))

plt.plot(
    subjects,
    semester1,
    marker='o',
    linewidth=2,
    label="Semester 1"
)

plt.plot(
    subjects,
    semester2,
    marker='s',
    linewidth=2,
    label="Semester 2"
)

plt.title("Semester Result Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.legend()

plt.show()