import scikit  as sk    
import numpy as np
from scipy.sparse import csr_matrix
d = np.array([3, 4, 5, 7, 2, 6])     # data
r = np.array([0, 0, 1, 1, 3,
    3])     # rows  
c = np.array([2, 4, 2, 3, 1, 2])     # cols 
csr = csr_matrix((d, (r, c)), shape=(4, 5)) 
print(csr.toarray())    
sk.csr_matrix((d, (r, c)), shape=(4, 5))    
sk.csr_matrix((d, (r, c)), shape=(4, 5)).toarray()