from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from math import pi
from random import choice

fig = plt.figure()
ax = fig.gca(projection='3d')

U = np.arange(-15, 15, .5)
Z = np.arange(-15, 105, .5)


U, Z = np.meshgrid(U, Z)
X= 4*np.sqrt(Z/10)*np.cos(U)
Y=10*np.sqrt(Z/10)*np.sin(U)



surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
#ax.set_zlim(-8, 0)
plt.show()
                   
#rstride=2, cstride=2 linewidth=0, antialiased=False