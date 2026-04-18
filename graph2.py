# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)
# plt.title("Violin Plot of Total Bill by Day and Gender")
# plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

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

x = ['sun', 'mon', 'fri', 'sat', 'tue', 'wed', 'thu']
y = [5, 6.7, 4, 6, 2, 4.9, 1.8]

ax = sns.stripplot(x=x, y=y)
ax.set(xlabel='Days', ylabel='Amount Spent')
plt.title('Daily Spending (Custom Data)')
plt.show()