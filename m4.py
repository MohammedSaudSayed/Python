import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 2, 4, 6])
ypoints = np.array([0, 100, 200, 250])

plt.plot(xpoints, ypoints, linestyle = 'dotted')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()