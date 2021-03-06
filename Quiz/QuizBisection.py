import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
from matplotlib import pyplot as plt
import sympy
from sympy import Symbol, Derivative

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
xu= 5

mathematicaRoot= 1
#mathematicaRoot= 0.34997

#Bisection method------------------------------------------------------------------------------------------------------#
def f(x):
    y= x**8 - 1
    return y

i= 0
while i <= 50:
    # Middle Point  #
    xr = (xl + xu) / 2

    # Zero check for the function #
    if abs(f(xr)) < 10**-7:
        print("\nNo. of iterations: " + str(i + 1))
        print(xr)
        print("\nAccuracy: " + str(abs(1 - ((abs(mathematicaRoot - xr) / xr) * 100))) + " %")
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
        print("\nAccuracy: " + str(abs(1 - ((abs(mathematicaRoot - xr) / xr) * 100))) + " %")
        break

    # Last iteration -> did not converge #
    if i == 50:
        print("\nDid not converge in " + str(i) + " iterations")

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


# Highlight Axes#
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
ax.spines['left'].set_smart_bounds(True)
ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Values #
plt.plot(x_values, y_values, label='Python')

# Plott data #
#plt.show()