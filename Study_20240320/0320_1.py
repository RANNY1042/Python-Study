
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19920613)

x= np.arange(0.0, 100.0, 5.0)
y = (x*15)+np.random.rand(20)*50


plt.scatter(x,y, c='b', alpha=0.5, label="scatter point")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='upper left')
plt.title('Scatter plot')
plt.show()