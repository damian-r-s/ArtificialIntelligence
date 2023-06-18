import numpy as np

X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [10, 11, 12],
     [13, 14, 15]]

mu = np.mean(X, axis=0)

X_centred = X - mu

C = np.cov(X_centred.T)

eigenvalues, eigenvectors = np.linalg.eig(C)

                                          
sorted_indices = np.argsort(eigenvalues)[::-1]
sorted_eigenvalues = eigenvalues[sorted_indices]
sorted_eigenvectors = eigenvectors[:, sorted_indices]


k = 2  # liczba składowych głównych do wyboru
selected_eigenvectors = sorted_eigenvectors[:, :k]


# Krok 7: Transformacja danych
Y = X_centred @ selected_eigenvectors

# Wyświetlenie wyników
print("Oryginalne dane:")
print(X)
print("\nSkładowe główne:")
print(Y)