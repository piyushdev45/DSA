from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = plt.axes(projection='3d')

# z = np.linspace(0, 1, 100)
# x = z * np.sin(25 * z)
# y = z * np.cos(25 * z)

# ax.plot3D(x, y, z, 'purple')
# ax.set_title('3D Line Plot')
# plt.show()

# fig = plt.figure()
# ax = plt.axes(projection='3d')

# z = np.linspace(0, 1, 100)
# x = z * np.sin(25 * z)
# y = z * np.cos(25 * z)
# c = x + y  # Color array based on x and y

# ax.scatter(x, y, z, c=c)
# ax.set_title('3D Scatter Plot')
# plt.show()

x = np.outer(np.linspace(-2, 2, 10), np.ones(10))
y = x.copy().T
z = np.cos(x**2 + y**3)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='green')
ax.set_title('Surface Plot')
plt.show()