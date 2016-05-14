from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from math import pi
from random import choice

fig = plt.figure()
ax = fig.gca(projection='3d')

U = np.arange(-2*pi, 0, .01)
V = np.arange(-2*pi, 0, .01)


U, V = np.meshgrid(U, V)
X=(4+2*np.cos(V))*np.cos(U)
Y=(4+2*np.cos(V))*np.sin(U)

Z=2*np.sin(V)



surf = ax.plot_surface(X, Y, Z, cmap=cm.autumn)
#ax.set_zlim(-8, 0)
plt.show()
                   
#rstride=2, cstride=2 linewidth=0, antialiased=False