import tensorflow as tf
import numpy as np
import pickle
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
    ])
model.compile(optimizer='sgd', loss='mse')
xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
ys = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5], dtype=float)
model.fit(xs, ys, epochs=10)


filename = "model.pkl"

pickle.dump(model, open(filename, 'wb'))