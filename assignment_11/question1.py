# 1) Combining a one and a two-dimensional NumPy Array
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([[10,20,30],[40,50,60]])
result=np.vstack((arr1,arr2))
print(result)


