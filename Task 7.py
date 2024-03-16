import numpy as np

# Create a sample array
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Compute the mean along the second axis
mean = np.mean(array, axis=1)

# Compute the standard deviation along the second axis
std_deviation = np.std(array, axis=1)

# Compute the variance along the second axis
variance = np.var(array, axis=1)

print("Array:")
print(array)
print("\nMean along the second axis:", mean)
print("Standard deviation along the second axis:", std_deviation)
print("Variance along the second axis:", variance)
