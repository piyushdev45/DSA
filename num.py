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