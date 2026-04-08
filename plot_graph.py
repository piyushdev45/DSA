import matplotlib.pyplot as plt
import numpy as np

def plot_graph(x, y, title, xlabel, ylabel):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()

# function call
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plot_graph(x, y, "Sample Graph", "X Axis", "Y Axis")