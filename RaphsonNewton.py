import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
from matplotlib import pyplot as plt
import sympy
from sympy import Symbol, Derivative

from timeit import default_timer as timer

# Calculate elapsed time #
start = timer()

#GENERAL_PARAMETERS----------------------------------------------------------------------------------------------------#
graphTitle= "Raphson-Newton Calculation"

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
es= 0.001

#Raphson-Newton method-------------------------------------------------------------------------------------------------#
def f(x):
    y = (x - sympy.exp(-x))
    return y

# Find derivate of the function f(x) at a point xi #
def df(xi):
    x = Symbol('x')
    func = f(x)
    deriv = Derivative(func, x)
    return float(deriv.doit().subs({x: xi}))

i= 0
while i <= 50:
    # General Formula #
    xi1 = float(xi - f(xi) / df(xi))

    # Zero check for the function #
    if abs(f( xi + 1 )) < 10**-7:
        print("No. of iterations: " + str(i + 1))
        print(xi1)
        break

    # Convergence criterion #
    ea = float( abs( (xi1 - xi) / xi1) )

    if ea < es:
        print("No. of iterations: " + str(i + 1))
        print(xi1)
        break

    # Reassignment of the x values #
    xi = xi1

    # Last iteration -> did not converge #
    if i == 50:
        print("\n Did not converge in" + " n " + " iterations")

    i+= 1

#PLOTTING--------------------------------------------------------------------------------------------------------------#
# Assign X and  Y values to axis #
while startLimit < endLimit:
    x_values.append(startLimit)
    y_values.append(f(startLimit))
    startLimit = startLimit + jump

# Styles #
"""plt.xkcd()"""

# Add names and tags #
fig, ax = plt.subplots()
ax.set(xlabel= x_name, ylabel= y_name, title=graphTitle)

# Add a grid #
ax.grid()

# Values #
plt.plot(x_values, y_values, label='Python')

# Plott data #
plt.show()
