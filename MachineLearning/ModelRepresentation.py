import numpy as np
import matplotlib.pyplot as plt

def computeModelOutput(x, w, b):    
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b        
    return f_wb

x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])

print(f"x_train={x_train}")
print(f"y_train={y_train}")
print(f"x_train.shape={x_train.shape}")
m = x_train.shape[0]
print(f"Number of training examples is: {m}")

i = 0
x_i = x_train[i]
y_i = y_train[i]
print(f"(x^({i}), y^({i})) = ({x_i}, {y_i})")

w = 200
b = 100
print(f"w: {w}")
print(f"b: {b}")

tmp_f_wb = computeModelOutput(x_train, w, b)
plt.plot(x_train, tmp_f_wb, c='b', label='Predictions')
plt.scatter(x_train, y_train, marker='x', c='r', label='Actual values')
plt.title("Housing Prices")
plt.ylabel('Price (in 1000s of dollars)')
plt.xlabel('Size (1000 sqft)')
plt.show()

x_i = 1.2
cost = w * x_i + b

print(f"Cost 1200sqft={cost} thousand dollars")