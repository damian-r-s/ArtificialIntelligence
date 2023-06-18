import numpy as np

def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

# Iterative
x = np.array([200, 17])
w = np.array([[1, -3, 5],
              [-2, 4, -6]])
b = np.array([-1, 1, 2])

def denseIter(a_in, w, b):
    units = w.shape[1]
    a_out = np.zeros(units)
    
    for j in range(units):
        wj = w[:, j]
        z = np.dot(wj, a_in) + b[j]
        a_out[j] = sigmoid(z)
    return a_out

# Vectorized
x = np.array([[200, 17]])
w = np.array([[1, -3, 5],
              [-2, 4, -6]])
b = np.array([[-1, 1, 2]])

def denseVectorized(a_in, w, b):
    z = np.matmul(a_in, w) + b
    return sigmoid(z)