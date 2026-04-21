# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)
# plt.title("Violin Plot of Total Bill by Day and Gender")
# plt.show()
# import seaborn as sns
# import matplotlib.pyplot as plt

# fmri = sns.load_dataset("fmri")
# sns.lineplot(x="timepoint", y="signal", hue="region", data=fmri)
# plt.show()

# tips = sns.load_dataset("tips")

# sns.scatterplot(x="total_bill", y="tip", hue="day", data=tips)
# plt.show()
# import seaborn as sns
# import matplotlib.pyplot as plt

# tips = sns.load_dataset("tips")

# sns.barplot(x="day", y="total_bill", data=tips)
# # plt.show()
# next
# import seaborn as sns
# import matplotlib.pyplot as plt

# tips = sns.load_dataset("tips")

# sns.boxplot(x="day", y="total_bill", data=tips)
# plt.show()
# import seaborn as sns
# import matplotlib.pyplot as plt

# tips = sns.load_dataset("tips")

# sns.histplot(tips["total_bill"], kde=True)
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt

# iris = sns.load_dataset("iris")
# sns.pairplot(iris, hue="species")
# plt.show()

# import matplotlib.pyplot as plt
# import seaborn as sns

# x = ['sun', 'mon', 'fri', 'sat', 'tue', 'wed', 'thu']
# y = [5, 6.7, 4, 6, 2, 4.9, 1.8]

# ax = sns.stripplot(x=x, y=y)
# ax.set(xlabel='Days', ylabel='Amount Spent')
# plt.title('Daily Spending (Custom Data)')
# plt.show()

# sns.set(style="whitegrid")
# iris = sns.load_dataset("iris")
# sns.swarmplot(x="species", y="sepal_length", data=iris)
# plt.title("Swarm Plot of Sepal Length by Species")
# plt.show()

# import matplotlib.pyplot as plt

# plt.plot([0, 1], [10, 11], label='Line 1')
# plt.plot([0, 1], [11, 10], label='Line 2')
# plt.scatter([0, 1], [10.5, 10.5], color='blue', marker='o', label='Dots')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Simple Line and Dot Plot')
# plt.legend()
# plt.show()

# import matplotlib.pyplot as plt
# import seaborn as sns

# # Apply Seaborn theme
# sns.set_theme(style="darkgrid")

# # Creating a simple Matplotlib plot
# x = [1, 2, 3, 4, 5]
# y = [10, 12, 15, 18, 22]

# plt.plot(x, y, marker='o', linestyle='-', color='blue', label="Trend")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Matplotlib Plot with Seaborn Theme")
# plt.legend()
# plt.show()


# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd

# data = pd.DataFrame({
#     'Year': [2018, 2019, 2020, 2021, 2022],
#     'Sales': [100, 150, 200, 250, 300]
# })

# plt.figure(figsize=(8, 5))
# sns.lineplot(x='Year', y='Sales', data=data, marker='o')

# # Customizing using Matplotlib
# plt.title("Yearly Sales Growth", fontsize=14, fontweight='bold')
# plt.xlabel("Year", fontsize=12)
# plt.ylabel("Total Sales", fontsize=12)
# plt.xticks(rotation=45)
# plt.grid(True, linestyle='--')

# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# x = np.linspace(0, 10, 20)
# y = np.sin(x)
# plt.figure(figsize=(8, 5))
# sns.lineplot(x=x, y=y, color='blue', label='Sine Wave')
# plt.scatter(x, y, color='red', marker='o', label="Data Points")

# plt.title("Seaborn Line Plot with Matplotlib Scatter Overlay")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.legend()
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt

# # Set a Seaborn color palette
# sns.set_palette("Set2")

# # Create some example data
# data = [3, 5, 7, 9, 2, 4, 6, 8]

# # Create a simple bar plot using the set color palette
# sns.barplot(x=range(len(data)), y=data)

# plt.show()


# from matplotlib import pyplot as plt
# import seaborn as sns

# cp = sns.color_palette()
# sns.palplot(cp)
# plt.show()


# from matplotlib import pyplot as plt
# import seaborn as sns

# sns.palplot(sns.color_palette("Greys"))
# plt.show()

import seaborn as sns
import matplotlib.pyplot as plt


sns.set(style ="ticks") 
tips = sns.load_dataset('tips')

sns.relplot(x ="total_bill",
            y ="tip",
            kind ="line",
            data = tips)
plt.show()
