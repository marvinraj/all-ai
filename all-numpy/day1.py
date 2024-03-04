# day 1
import numpy as np


# array dimensions
arr_1d = np.array([1,2,3,4,5])
arr_2d = np.array([[1,2,3],[4,5,6]])
arr_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(arr_1d)
print(arr_2d)
print(arr_3d)

# accessing arrays
print("accessing 1d array: ", arr_1d[0])
print("accessing 2d array: ", arr_2d[1,1])
print("accessing 3d array: ", arr_3d[0,0,0])

# slicing arrays
print("slicing 1d array: ", arr_1d[0:5:2])
print("slicing 2d array: ", arr_2d[0:2, 0:3])

# check datatype
print(arr_1d.dtype)
animal_arr = np.array(["dog", "cat", "tiger", "lion"])
print(animal_arr)
print(animal_arr.dtype)