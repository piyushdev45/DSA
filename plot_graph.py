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

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.scatter(x, y, color='blue', marker='x')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Scatter Plot')

plt.show()