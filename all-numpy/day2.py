# day 2
import numpy as np

# copy vs view
# 1 - copy
arr = np.array([1,2,3,4,5])
x = arr.copy() # make a copy of the array
arr[0] = 66 # change value in the original array

print(arr)
print(x)


# 2 - view
rand_nums = np.array([10,11,12,13,14,15])
y = rand_nums.view()
y[0] = 99

print(rand_nums)
print(y)


# array shape
even_nums = np.array([[3,5,7,9],[11,13,15,17]])
print(even_nums.shape) # returns 2,4 = 2 rows, 4 columns


# reshape array
# 1d - 2d
lucky_nums = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
not_so_lucky_nums = lucky_nums.reshape(4, 3)

# 1d - 3d
okok_nums = lucky_nums.reshape(2,3,2)

# 2d - 1d (flattening an array)
cool_nums = np.array([[1,2,3], [4,5,6]])
hot_nums = cool_nums.reshape(-1)