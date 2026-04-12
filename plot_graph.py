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

# import matplotlib.pyplot as plt
# import numpy as np
# x= np.array([1, 2, 3, 4, 5])
# y= np.array([2, 4, 6, 8, 10])
# plt.scatter(x, y, color='blue', marker='x')
# plt.xlabel('X-axis')    
# plt.ylabel('Y-axis')
# plt.title('Simple Scatter Plot')    
# plt.grid()
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np  
# x1 = np.array([1, 2, 3, 4, 5])
# y1 = np.array([2, 4, 6, 8, 10])
# x2 = np.array([1, 2, 3, 4, 5    ])
# y2 = np.array([10, 8, 6, 4, 2])
# plt.plot(x1, y1, label='y = 2x', color='blue', linestyle='-', marker='o')
# plt.plot(x2, y2, label='y = 12 - 2x', color='red', linestyle='--', marker='x')
# plt.grid(True)  
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')    
# plt.title('Customized Line Plot with Multiple Series')  
# plt.scatter(x1, y1, color='blue', marker='o')
# plt.scatter(x2, y2, color='red', marker='x')      
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np  
# # Generate random data for the histogram
# data = np.random.randn(1000)

# # Plotting a basic histogram
# plt.hist(data, bins=30, color='skyblue', edgecolor='black')
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Basic Histogram')
# plt.show()

# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np

# # Generate random data for the histogram
# data = np.random.randn(1000)

# # Creating a customized histogram with a density plot
# sns.histplot(data, bins=30, kde=True, color='lightgreen', edgecolor='red')

# # Adding labels and title
# plt.xlabel('Values')
# plt.ylabel('Density')
# plt.title('Customized Histogram with Density Plot')

# # Display the plot
# plt.show()

# # Import libraries
# from matplotlib import pyplot as plt
# import numpy as np


# # Creating dataset
# cars = ['AUDI', 'BMW', 'FORD',
#         'TESLA', 'JAGUAR', 'MERCEDES']

# data = [23, 17, 35, 29, 12, 41]

# # Creating plot
# fig = plt.figure(figsize=(10, 7))
# plt.pie(data, labels=cars)

# # show plot
# plt.show()

# import matplotlib.pyplot as plt

# x = range(1, 11)
# markers = ['o', 's', '^', 'v', 'D', '*', '+', 'x']

# for i, marker in enumerate(markers):
#     plt.plot(x, [i*2]*10, marker=marker, linestyle='')

# plt.title('Different Matplotlib Markers')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()

# import matplotlib.pyplot as plt

# x = [4,1,7,5,8]
# plt.plot(x,'o-r')  # Red circles with a solid line

# plt.title('Plot with fmt')
# plt.xlabel('X-axis')

# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x1 = np.linspace(0, 5, 100)
# y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)

# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# ax1.plot(x1, y1)
# ax1.set_title('Plot without grid')

# ax2.plot(x1, y1)
# ax2.set_title("Plot with grid")
# ax2.grid(True)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 2 * np.pi, 400)
# y = np.sin(x ** 2)

# plt.plot(x, y, 'green')
# plt.title("Plot with custom grid lines")
# plt.grid(True, color='grey', linewidth=1.4, linestyle='-.')

# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # Creating subplots
# fig, ax = plt.subplots(3, 3)

# # Plot random data in each subplot
# for row in ax:
#     for col in row:
#         col.plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))

# plt.show()

# import numpy as np 
# import matplotlib.pyplot as plt 
# from matplotlib import style 
# data = np.random.randn(50) 
# plt.style.use('Solarize_Light2') 
# plt.plot(data) 
# plt.show()

import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import style 
data = np.random.randn(50) 
plt.style.use('dark_background') 
plt.plot(data) 
plt.show()