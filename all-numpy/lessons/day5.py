# day 5 - split array
import numpy as np

# splitting 1d array
array1 = np.array([1,2,3,4,5])
array2 = np.array_split(array1, 3)
print(array2)

# accessing split array
split_arr = array2[0]
print(split_arr)

# split 2d array
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
new_arr = np.array_split(arr, 3)
print(arr)
print(new_arr)