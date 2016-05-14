from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
#vars
X = np.arange(-5, 5, 0.05)
B = np.arange(-5, 5, 0.05)
X, B = np.meshgrid(X, B)
V=np.sqrt(X**2 + B**2)
C = np.arange(-5, 5, 0.05)
D = np.arange(-5, 5, 0.05)
C, D = np.meshgrid(C, D)
U=np.sqrt(C**2 + D**2)
#torus
#X=np.cos(V)*np.cos(U)
Y=np.cos(V)*np.sin(U)
Z=np.sin(V)



#actually graphing
surf = ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap=cm.jet,
                       linewidth=0, antialiased=False)
#ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()