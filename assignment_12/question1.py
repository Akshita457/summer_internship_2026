#Create numpy array and perform following operation

#1) Convert 1D array to 2D
import numpy as np
arr1=np.array([1,2,3,4,5,6])
arr2d=arr1.reshape(2,3)
print(arr2d)

# 2) Print Array Attributes (shape, dimension, data type, itemsize)
print("\nShape:", arr2d.shape)
print("Dimensions:", arr2d.ndim)
print("Data Type:", arr2d.dtype)
print("Item Size:", arr2d.itemsize)

# 3) Create a 3×3 NumPy array of all 9
arr3=np.full((3,3),9) 
print(arr3)

# 4) Create a 1D array of 10 evenly spaced values between 25 and 125
arr4 = np.linspace(25, 125, 10)
print( arr4)

# 5) cONVERT A PYTHON LIST TO NUMPY ARRAY
lst=[1,2,3,4,5,6]
arr5=np.array(lst)
print(arr5)

# 6) Reverse a 1D numpy array
arr6=[2,4,6,8,10]
print("Reversed array:", arr6[::-1])

# 7) Create a 4×4×3 array and extract value at its second set, first row and last column
arr7=np.array([
    [[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
    [[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
    [[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
    [[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
])
print(arr7)

print(arr7[1,0,2])

# 8) Create a 4×4 and Extract Odd Rows and Even Columns
arr8= np.arange(1, 17).reshape(4, 4)
print("\n4x4 Array:\n", arr8)
print(arr8[0,:])
print(arr8[2,:])
print(arr8[:,1])
print(arr8[:,3])

# 9) Slice the first two rows and first two columns of second set from a 4×4×3 array
arr9 = np.arange(48).reshape(4, 4, 3)
print("\nSlice:\n", arr9[1, :2, :2])

# 10) Replace all odd numbers in a NumPy array with -1 using for loop
arr = np.array([[23, 56, 78, 93], [71, 82, 13, 24]])

for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        if arr[i][j] % 2 != 0:
            arr[i][j] = -1

print( arr)

