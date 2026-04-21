# import numpy as np
# from scipy.linalg import det    
# matrix = np.array([[1, 2, 3],
#                    [0, 1, 4],
#                    [5, 6, 0]])

# determinant = det(matrix)

# print(f"Determinant of the matrix is: {determinant}")

from scipy import integrate
import numpy as np


f = lambda x: x**2
result, error = integrate.quad(f, 0, 1)
print(result)