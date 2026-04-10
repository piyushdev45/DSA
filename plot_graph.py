# import matplotlib.pyplot as plt
# import numpy as np

# def plot_graph(x, y, title, xlabel, ylabel):
#     plt.figure(figsize=(10, 5))
#     plt.plot(x, y, marker='o')
#     plt.title(title)
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.grid()
#     plt.show()

# # function call
# x = [1, 2, 3, 4]
# y = [10, 20, 15, 25]

# plot_graph(x, y, "Sample Graph", "X Axis", "Y Axis")

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y1 = [1, 4, 9, 16, 25]
# y2 = [25, 20, 15, 10, 5]

# plt.plot(x, y1, label='y = x^2', color='green', linestyle='--', marker='o')
# plt.plot(x, y2, label='y = 30 - x^2', color='red', linestyle='-', marker='x')

# plt.grid(True)

# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Customized Line Plot with Multiple Series')

# plt.legend()
# plt.savefig('all_features_plot.png')
# plt.show()

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.scatter(x, y, color='blue', marker='x')

# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Simple Scatter Plot')

# plt.show()

# import matplotlib.pyplot as plt 
# import numpy as np      
# days = np.array(['mon', 'tue', 'wed', 'thu', 'fri'])
# temperature = np.array([30, 32, 28, 35, 31])        
# plt.plot(days, temperature, marker='o', linestyle='-', color='b')
# plt.title('Temperature Over 5 Days')        
# plt.xlabel('Day')
# plt.ylabel('Temperature (°C)')  
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([1, 2, 3, 4])   
# y = x * 2                

# plt.plot(x, y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np  
# x = np.array([1, 2, 3, 4])
# y= np.array([2, 4, 6, 8])
# plt.plot(x, y, marker='o', linestyle='-', color='purple')   
# plt.title('Line Plot Example')
# plt.xlabel('X-axis')    
# plt.ylabel('Y-axis')
# plt.grid()  
# plt.show() 

# circle graph 
# import matplotlib.pyplot as plt     
# labels = ['A', 'B', 'C', 'D']
# sizes = [15, 30, 45, 10]    
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
# plt.axis('equal')
# plt.title('Sample Pie Chart')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np  
# fruits = ['Apple', 'Banana', 'Cherry', 'Date']
# quantities = [10, 15, 7, 12]    
# plt.bar(fruits, quantities, color=['red', 'yellow', 'pink', 'brown'])
# plt.title('Fruit Quantities')       
# plt.xlabel('Fruits')
# plt.ylabel('Quantities')    
# plt.show()
 

# import matplotlib.pyplot as plt
# import numpy as np  
# digital_coins = ['Bitcoin', 'Ethereum', 'Ripple', 'Litecoin','Ruppe']
# values = [50000, 3000, 1, 2000, 500]  
# plt.bar(digital_coins, values, color=['orange', 'blue', 'green', 'gray','brown'])
# plt.title('Digital Coin Values')        
# plt.xlabel('Digital Coins')
# plt.ylabel('Values (USD)')  
# plt.show()

# import numpy as np 
# import matplotlib.pyplot as plt 

# barWidth = 0.25
# fig = plt.subplots(figsize =(12, 8)) 

# IT = [12, 30, 1, 8, 22] 
# ECE = [28, 6, 16, 5, 10] 
# CSE = [29, 3, 24, 25, 17] 

# br1 = np.arange(len(IT)) 
# br2 = [x + barWidth for x in br1] 
# br3 = [x + barWidth for x in br2] 

# plt.bar(br1, IT, color ='r', width = barWidth, 
#         edgecolor ='grey', label ='IT') 
# plt.bar(br2, ECE, color ='g', width = barWidth, 
#         edgecolor ='grey', label ='ECE') 
# plt.bar(br3, CSE, color ='b', width = barWidth, 
#         edgecolor ='grey', label ='CSE') 

# plt.xlabel('Branch', fontweight ='bold', fontsize = 15) 
# plt.ylabel('Students passed', fontweight ='bold', fontsize = 15) 
# plt.xticks([r + barWidth for r in range(len(IT))], 
#         ['2015', '2016', '2017', '2018', '2019'])

# plt.legend()
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
x= np.array([1, 2, 3, 4, 5])
y= np.array([2, 4, 6, 8, 10])
plt.scatter(x, y, color='blue', marker='x')
plt.xlabel('X-axis')    
plt.ylabel('Y-axis')
plt.title('Simple Scatter Plot')    
plt.grid()
plt.show()