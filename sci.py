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

# import scipy.constants as const
# # This return a tuple(vslue, unit, uncertainty)
# print(const.physical_constants['alpha particle mass'])


# import scipy.constants as const

# # Area of a circle using pi
# def area_of_circle(r):
#     return const.pi * r * r

# # Gravitational force
# def force_gravity(M, m, dist):
#     return (const.G * M * m) / (dist ** 2)

# print("Area of Circle:", area_of_circle(5))
# print("Gravitational Force:", force_gravity(10, 5, 1))


#integration using scipy
# from scipy.integrate import quad

# def f(x):
#     return 3 * x**2 + 1
    
# I, err = quad(f, 0, 1)
# print(I)
# print(err)

# from scipy.integrate import dblquad

# A = dblquad(lambda x, y: x * y, 0, 0.5,              
#                lambda x: 0, lambda x: 1 - 2*x)        
# print(A)

#special function 
# from scipy.special import cbrt

# print(cbrt(64))    
# print(cbrt(78))

# from scipy.special import comb
# print(comb(4, 1))

# numpy and scipy are often used together for scientific computing. Here's an example of how to perform matrix addition using both libraries:
# import numpy as np
# from scipy.sparse import csr_matrix

# d = np.array([3, 4, 5, 7, 2, 6])     # data
# r = np.array([0, 0, 1, 1, 3, 3])     # rows
# c = np.array([2, 4, 2, 3, 1, 2])     # cols

# csr = csr_matrix((d, (r, c)), shape=(4, 5))
# print(csr.toarray())

# import numpy as np
# from scipy.sparse import csc_matrix

# d = np.array([3, 4, 5, 7, 2, 6])     
# r = np.array([0, 0, 1, 1, 3, 3])     
# c = np.array([2, 4, 2, 3, 1, 2])     

# csc = csc_matrix((d, (r, c)), shape=(4, 5)) 
# print(csc.toarray())

#lil matrix
import numpy as np
from scipy.sparse import lil_matrix

lil = lil_matrix((4, 5))
lil[0, 2] = 3
lil[0, 4] = 4
lil[1, 2] = 5
lil[1, 3] = 7
lil[3, 1] = 2
lil[3, 2] = 6

print(lil.toarray())