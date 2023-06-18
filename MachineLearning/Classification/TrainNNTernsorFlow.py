import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import BinaryCrossentropy

model = Sequential([
    Dense(units=25, activation='sigmoid'),
    Dense(units=15, activation='sigmoid'),
    Dense(units=1, activation='sigmoid')
])


model.compile(loss = BinaryCrossentropy())

X = np.array([
    [200.0, 17.0],
    [120.0, 5.0],
    [425.0, 20.0],
    [212.0, 18.0]
])

Y = np.array([1, 0, 0, 1])
model.fit(X, Y, epochs=100)