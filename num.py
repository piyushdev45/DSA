a1= ([1,2,3])
a2 =([3,4,5])
a3 =([7,8,9])
print(a1)
print(a2)
print(a3)
a4 = a1 + a2 + a3
print(a4)

import numpy as np

a0 = np.zeros((3, 3))
a1  = np.ones((2, 2))
ar  = np.arange(0, 10, 2)

print(a0)
print(a1)
print(ar)

a1= ([1,2,3])
a2 =([3,4,5])
a3 =([7,8,9])
print(a1[2])
print(a2[1])
print(a3[0])
print (a1[0:2])
print (a2[1:])


import numpy as np

a = np.array([10, 5, 40, 40, 90, 60])
idx = np.array([1, 3, 5])

print(a[idx])       # integer indexing

cond = a > 30
print(a[cond])      # boolean indexing


#numpy arrthemetic operations
a = np.array([7, 7, 3])                       # we also can perform this operations by using res 
b = np.array([4, 6, 6])
print(a + b)  # element-wise addition
print(a * b)  # element-wise multiplication

#numpy shorting array
import numpy as np

dtype = [('name', 'S10'), ('year', int), ('cgpa', float)]
vals  = [('piyush', 2028, 8.5),
         ('Ajay',    2027, 8.7),
         ('jp',  2027, 7.9),
         ('abhinav',  2028, 9.0)]

a = np.array(vals, dtype=dtype)

print(np.sort(a, order='name'))
print(np.sort(a, order=['year', 'cgpa']))


import numpy as np
 
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

arr2 = arr[:2, ::2]
print ("first 2 rows and alternate columns(0 and 2):\n", arr2)
 
arr3 = arr[[1, 1, 0, 3], 
                [3, 2, 1, 0]]
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", arr3) 

import numpy as np

a1= np.array([1, 2, 3])
a2 = np.array([3, 4, 5])
print(a1+1)  # add 1 to each element of a1
print(a1*2)  # multiply each element of a1 by 2
print (a1.sum())  # sum of all elements in a1

x = np.array([8, 2,8, 4, 5])  
print(x.dtype)         
 
x = np.array([1.0, 2.0]) 
print(x.dtype) 



import numpy as np

np.empty([4, 3],
         dtype = np.int32,
         order = 'f')
print(np.empty([4, 3],
         dtype = np.int32,
         order = 'f')
)


import numpy as np

vector_zeros = np.zeros(3)
print("Vector using np.zeros():", vector_zeros)

vector_ones = np.ones(8)
print("Vector using np.ones():", vector_ones)


a1= np.array([1, 2, 3, 4, 5])
v= a1.view()
a1[0] = 10
print("Original array:", a1) 
print ("views of the original array:", v)


a1= np.array([1, 2, 3, 4, 5])
c= a1.copy()
a1[0] = 10  
print("Original array:", a1)
print("Copy of the original array:", c)

#appending array
import numpy as np  
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])        
a3 = np.append(a1, a2)
print(a3)

a1 = np.append(a1, 4)
print(a1)