# 5 diff subjects, diff students and make pychart

import matplotlib.pyplot as plt
import numpy as np

for i in range(5):
    y = int(input("Enter students: "))
    np.array([y])
    
mylabels = ["Laravel", "C++", "Python", "Java", "Data Structures"]
plt.pie(y.append(mylabels))
plt.pie(y, labels = mylabels)

plt.show() 