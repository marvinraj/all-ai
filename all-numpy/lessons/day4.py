# day 4 - joining array
import numpy as np

# join arrays using concatenate
arr_1 = np.array([1,2,3,4])
arr_2 = np.array([5,6,7,8])

arr_1and2 = np.concatenate((arr_1, arr_2))


# join arrays using stack
arr = np.stack((arr_1, arr_2), axis=1)

# stacking along rows 
arr_row = np.hstack((arr_1, arr_2))

# stacking along columns
arr_col = np.vstack((arr_1, arr_2))

# stacking along height/depth
arr_height = np.dstack((arr_1, arr_2))