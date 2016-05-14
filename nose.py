from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from math import pi
from random import choice

fig = plt.figure()
ax = fig.gca(projection='3d')

U = np.arange(-5, 5, 0.1)
Z = np.arange(-5, 5, 0.1)


U, Z = np.meshgrid(U, Z)
X= 5*np.sqrt(U/Z)*np.cos(Z)
Y=5*np.sqrt(U/Z)*np.sin(Z)



surf = ax.plot_surface(X, Y, Z, cmap=cm.jet)
#ax.set_zlim(-8, 0)
plt.show()
                   
#rstride=2, cstride=2 linewidth=0, antialiased=False