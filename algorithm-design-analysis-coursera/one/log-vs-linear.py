import numpy as np
import matplotlib.pyplot as plt

def linear(x):
    return x

def log2(x):
    return np.log2(x)

x_vals = np.arange(1, 10, 1)
linear_vals = list(map(linear, x_vals))
log2_vals = list(map(log2, x_vals))
plt.scatter(x_vals, linear_vals, color='r')
plt.scatter(x_vals, log2_vals, color='b')
plt.show()
