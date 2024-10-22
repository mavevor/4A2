
import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(0,2* np.pi,100)
y_vals = np.sin(x_vals)

plt.plot(x_vals, y_vals)

plt.show()
