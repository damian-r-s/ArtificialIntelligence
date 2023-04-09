import numpy as np
import matplotlib.pyplot as plt

with open("D:\Workspace\ArtificialIntelligence\DeepLearning\Python\Iris\iris.data") as f:
    lines = [i[:-1] for i in f.readlines() if i != ""]
    
# cat iris.data  | cut -d',' -f 5 | sort | uniq
n = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

# assign classes
x = [n.index(i.split(",")[-1]) for i in lines if i != ""] 
x = np.array(x, dtype="uint8")

y = [[float(j) for j in i.split(",")[:-1]] for i in lines if i != ""]
y = np.array(y)

i = np.argsort(np.random.random(x.shape[0]))
x = x[i]
y = y[i]

np.save("iris_features.npy", y)
np.save("iris_labels.npy", x)

plt.boxplot(y)
plt.show()