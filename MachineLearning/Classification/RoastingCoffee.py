import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([Dense(units=3, activation="sigmoid"), 
                    Dense(units=1, activation="sigmoid")])

x = np.array([
    [200.0, 17.0],
    [120.0, 5.0],
    [425.0, 20.0],
    [212.0, 18.0]
])

y = np.array([1, 0, 0, 1])

model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(0.001)
)
model.fit(x, y, epochs = 20)