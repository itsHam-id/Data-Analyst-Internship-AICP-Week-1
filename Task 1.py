import numpy as np

# Create an array of all integers from 30 to 70
arr = np.arange(30, 71)

# Filter out the even integers
even_arr = arr[arr % 2 == 0]

print(even_arr)
