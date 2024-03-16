import numpy as np

# Define two matrices (2x3 and 2x3) as NumPy arrays
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

matrix2 = np.array([[7, 8, 9],
                    [10, 11, 12]])

# Compute the cross-product of the two matrices
cross_product = np.cross(matrix1, matrix2)

print("Cross-product of the two matrices:")
print(cross_product)
