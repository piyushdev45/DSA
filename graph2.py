# import seaborn as sns
# import matplotlib.pyplot as plt
# tips = sns.load_dataset("tips")
# sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)
# plt.title("Violin Plot of Total Bill by Day and Gender")
# plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

fmri = sns.load_dataset("fmri")
sns.lineplot(x="timepoint", y="signal", hue="region", data=fmri)
plt.show()