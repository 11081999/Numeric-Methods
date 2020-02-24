import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
from matplotlib import pyplot as plt
import sympy
from sympy import Symbol, Derivative

from timeit import default_timer as timer

# Calculate elapsed time #
start = timer()

#GENERAL_PARAMETERS----------------------------------------------------------------------------------------------------#
graphTitle= "Bisection Calculation"

# Data on the X axis #
x_values = []
x_name= "X"

# Data on the Y axis #
y_values = []
y_name= "Y"

# Limits of the graph and jump between points in the graph#
startLimit= 0
endLimit= 10
jump= 0.01

# Estimated point root (ONE ROOT ONLY) #
es= 0.0001
xl= 0
xu= 100

#Bisection method------------------------------------------------------------------------------------------------------#
def f(x):
    y = x - sympy.exp(-x)
    return y

i= 0
while i <= 50:
    # Middle Point  #
    xr = (xl + xu) / 2

    # Zero check for the function #
    if abs(f(xr)) < 10**-7:
        print("\nNo. of iterations: " + str(i + 1))
        print(xr)
        break

    # Bisection criterion (where is the root?) #
    bisCr= f(xl) * f(xr)

    # The root lies in the lower sub-interval#
    if bisCr < 0:
        xu= xr

    # The root lies in the upper sub-interval#
    if bisCr > 0:
        xl= xr

    # The root equals xr #
    if bisCr == 0:
        print("\nNo. of iterations: " + str(i + 1))
        print(xr)
        break

    # Last iteration -> did not converge #
    if i == 50:
        print("\n Did not converge in any iterations")

    i+= 1

#PLOTTING--------------------------------------------------------------------------------------------------------------
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
