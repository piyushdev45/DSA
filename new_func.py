import seaborn as sns


def new_func(tips):
    sns.countplot(x ='sex', data = tips)