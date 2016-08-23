# original gist, without opt for sys input
# https://gist.github.com/horacepan/cb5ba61e621e1636fcc538ea1bdcfdec

import numpy as np
import matplotlib.pyplot as plt
import sys

def sigmoid(x, c=1):
    return 1 / (1 +  np.exp(-x * c))

c = int(sys.argv[1])
x_vals = np.arange(-10, 10, 0.1)
sigmoid_vals = map(lambda x: sigmoid(x, c), x_vals)
plt.scatter(x_vals, sigmoid_vals)
plt.show()
