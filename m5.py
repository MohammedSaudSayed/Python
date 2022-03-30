import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15, 56])
mylabels = ["PHP", "C++", "C", "Java", "Python"]

plt.pie(y, labels = mylabels)
plt.show()