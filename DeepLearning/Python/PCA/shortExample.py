import numpy as np
from sklearn.decomposition import PCA

X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

pca = PCA(n_components=2)

pca.fit(X)

X_pca = pca.transform(X)

# Wyświetlenie wyników
print("Oryginalne dane:")
print(X)
print("\nSkładowe główne:")
print(X_pca)