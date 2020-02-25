import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
from matplotlib import pyplot as plt
import sympy
from sympy import Symbol, Derivative

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import numpy as np


#GENERAL_PARAMETERS----------------------------------------------------------------------------------------------------#
graphTitle= "System of Equiations"

# Jacobian of a matrix #

# Data on the X axis #
x_values = []
x_name= "X"

# Data on the Y axis #
y_values = []
y_name= "Y"

# Limits of the graph #
startLimit= 0
endLimit= 10
jump= 0.01

# Estimated point root (ONE ROOT ONLY) #
xi= 2
es= 0.0001

#Raphson-Newton method-------------------------------------------------------------------------------------------------#
def fun(x, y):
    z= x**2 + y
    return float(z)

#PLOTTING--------------------------------------------------------------------------------------------------------------#
# Assign X and  Y values to axis #
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(-5, 5, 0.05)
X, Y = np.meshgrid(x, y)
zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)
#ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='winter', edgecolor='none')

ax.set_xlabel(x_name)
ax.set_ylabel(y_name)
ax.set_zlabel('Z Label')

plt.show()