import numpy as np
import matplotlib.pyplot as plt

with open("D:\Workspace\ArtificialIntelligence\DeepLearning\Python\WisconsinDiagnosticBreastCancer\wdbc.data") as f:
    lines = [i[:-1] for i in f.readlines() if i != ""]
    
# cut -d',' -f2 wdbc.data | sort | uniq
n = ["B", "M"]
x = np.array([n.index(i.split(",")[1]) for i in lines], dtype="uint8")
y = np.array([[float(j) for j in i.split(",")[2:]] for i in lines])

i = np.argsort(np.random.random(x.shape[0]))
x = x[i]
y = y[i]
z = (y - y.mean(axis=0))/y.std(axis=0)

np.save("bc_features.npy", y)
np.save("bc_features_standard.npy", z)
np.save("bc_labels.npy", x)

plt.boxplot(z)
plt.show()