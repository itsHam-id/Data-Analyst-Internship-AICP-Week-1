import numpy as np

# Define a square matrix as a NumPy array
matrix = np.array([[1, 2],
                   [3, 4]])

# Compute the determinant of the matrix
determinant = np.linalg.det(matrix)

print("Determinant of the matrix:", determinant)
