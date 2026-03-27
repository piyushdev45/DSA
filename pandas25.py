# import pandas as pd
# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# print(df)

# import pandas as pd 
# import numpy as np

# s = pd.Series() 
# print("Pandas Series: ", s) 
# data = np.array(['g', 'e', 'e', 'k', 's']) 
  
# s = pd.Series(data) 
# print("Pandas Series:\n", s)


# import pandas as pd 
   
# df = pd.DataFrame() 
# print(df)
# lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 
  
# df = pd.DataFrame(lst) 
# print(df)
# import pandas as pd
# df = pd.DataFrame()
# print(df)

# import numpy as np
# import pandas as pd

# data = { 'A': np.array([1, 4, 7]),
#          'B': np.array([2, 5, 8]),
#          'C': np.array([3, 6, 9]) }
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data = [
#     {'name': 'yash', 'degree': 'MBA', 'score': 90},
#     {'name': 'jp', 'degree': 'BCA', 'score': 40},
#     {'name': 'piyush', 'degree': 'M.Tech', 'score': 80},
# ]
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd

# data = [1, 2, 3, 4]
 
# ser = pd.Series(data)
# print(ser)

# import pandas as pd
# data = {
#     'name': ['yash', 'jp', 'piyush','aurafarmer','chitransh'],
#     'degree': ['B.COM', 'BCA', 'M.Tech','M.TECH','B.TECH'],
#     'score': [75, 85, 89, 'none', 79],
#     'age': [22, 21, 23, 22, 23],
#     'city': ['GZB', 'GZB', 'GZB', 'MADARA', 'AGRA']  
# }
# df = pd.DataFrame(data)
# print(df)
# print(unique_city := df['city'].unique() )
# print(df.info())
# print(df['score'].isnull())

# finding mising values  
# import pandas as pd
# a1 = pd.Series([1, 2, 3, None, 5])
# print(a1)
# print(a1.isnull())

# import numpy as np
# import pandas as pd

# ser = pd.Series(np.linspace(1, 10, 5))
# print(ser)

# import pandas  as pd 
# df= pd.read_csv('data.csv')
# print(df)

# import pandas as pd 
# df = pd.read_csv('nba.csv')
# print(df.tail(3))
# print(df.head(2))

# import pandas as pd               # wrong code start 
# df = pd.read_csv('nba.csv')
# new_row = {
#     'name': 'chandi',
#     'age': 18,
#     'place': 'GZB',
#     'course': 'B.TECH',         # wrong code 
 #     'salary': 12000
# }

# df.loc[len(df)] = new_row
# print(df)                          # wrong code end 
    
import pandas as pd

df = pd.read_csv('nba.csv')

new_row = {
    'name': 'chandi',
    'age': 18,
    'place': 'GZB',
    'course': 'B.TECH',
    'salary': 12000
}

df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

print(df)