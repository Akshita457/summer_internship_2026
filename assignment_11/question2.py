# 2) Flatten a 2D NumPy array into 1D array
import numpy as np
arr_before=np.array([[10,20,30],[20,40,60]])
print("Before flattening:",arr_before)

arr_after=np.array(arr_before.reshape(-1))
print("After flattening:",arr_after)