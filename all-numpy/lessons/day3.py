# day 3 - array iteration

import numpy as np

# iterate through 1d
array_one = np.array([1,2,3,4,5])
for x in array_one:
    print(x)

# iterate through 2d
array_two = np.array([[1,2,3],[4,5,6]])
for x in array_two:
    for y in x:
        print(y)

# iterate through 3d
# 1 
array_three = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for x in array_three:
    for y in x:
        for z in y:
            print(z)   
# 2
for x in np.nditer(array_three):
    print(x)
