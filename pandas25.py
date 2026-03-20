import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df)

import pandas as pd 
import numpy as np

s = pd.Series() 
print("Pandas Series: ", s) 
data = np.array(['g', 'e', 'e', 'k', 's']) 
  
s = pd.Series(data) 
print("Pandas Series:\n", s)