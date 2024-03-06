# day 6 - searching arrays & sorting arrays
import numpy as np

# 1 - where(), search array for a value and return index
array_one = np.array([1,2,4,6,4,7,4])
x = np.where(array_one == 4)
print(x)

# 2 - searchsorted(), performs binary search in the array and returns index on where the value would be inserted
array_two = np.array([12,13,14,15,16])
y = np.searchsorted(array_two, 14)
print(y)

# 3 - sorting arrays
array_three = np.array([1,4,2,5,6,7,3,9,8])
print(np.sort(array_three))

array_four = np.array(["banana", "apple", "cherry", "durian"])
print(np.sort(array_four))