import seaborn as sns
import pandas as pd

# Load the example planets dataset
#dataset = sns.load_dataset("") # Mettre entre guillement le nom du fichier du dataset
#ou remplacer par dataset = pd.read_csv()
dataset = pd.read_pickle("../dumps/df.pkl")

cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
graph = sns.relplot(
    data=dataset,
    x="date", y="positivity",
    palette=cmap, sizes=(10, 200),
)
graph.set(xscale="log", yscale="log")
graph.ax.xaxis.grid(True, "minor", linewidth=.25)
graph.ax.yaxis.grid(True, "minor", linewidth=.25)
graph.despine(left=True, bottom=True)
