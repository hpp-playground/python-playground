import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# sns.set("bright")
# sns.set_style("whitegrid")
# sns.set_style("dark")
# sns.set_style("white")
# sns.set_style("ticks")


# limit min and max

plt.xlim(70, 78)


df = pd.read_csv("df.csv")
plot = sns.histplot(
    data=df,
    x="avg",
    hue="name",
    # fill=False,
    # binwidth=0.25,
    bins=25,
    # kde=True,
    # element="poly",
)
plot.figure.savefig("hist.png")

plt.clf()
plt.xlim(70, 78)

plot = sns.kdeplot(
    data=df,
    x="avg",
    hue="name",
    # fill=False,
    # kde=True,
    # element="poly",
)
plot.figure.savefig("kde.png")
