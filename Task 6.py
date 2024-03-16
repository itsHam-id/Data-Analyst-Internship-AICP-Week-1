import numpy as np

# Create a 5x5 array with random values
random_array = np.random.rand(5, 5)

print("5x5 array with random values:")
print(random_array)

# Find the minimum and maximum values in the array
minimum_value = np.min(random_array)
maximum_value = np.max(random_array)

print("\nMinimum value:", minimum_value)
print("Maximum value:", maximum_value)
