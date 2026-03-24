# view pandas import pandas as pd
# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.head())
import pandas as pd
df = pd.read_csv('data.csv') 
print(df[['Name', 'Age']])