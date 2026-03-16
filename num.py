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