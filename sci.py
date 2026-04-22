# import numpy as np
# from scipy.linalg import det    
# matrix = np.array([[1, 2, 3],
#                    [0, 1, 4],
#                    [5, 6, 0]])

# determinant = det(matrix)

# print(f"Determinant of the matrix is: {determinant}")

# from scipy import integrate
# import numpy as np


# f = lambda x: x**2
# result, error = integrate.quad(f, 0, 1)
# print(result)

# import scipy.constants as const

# print("Pi:", const.pi)
# print("Golden ratio:", const.golden_ratio)
# print("Speed of light:", const.c)
# print("Gravitational constant:", const.G)
# print("Gas constant (R):", const.R)
# print("Boltzmann constant:", const.k)
# print("Proton mass:", const.proton_mass)

# import scipy
# res = scipy.constants.find("proton")
# print(res, end='\n')

import scipy.constants as const
# This return a tuple(vslue, unit, uncertainty)
print(const.physical_constants['alpha particle mass'])