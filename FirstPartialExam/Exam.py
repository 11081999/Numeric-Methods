import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
from matplotlib import pyplot as plt
import sympy
from sympy import Symbol, Derivative

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
jump= 0.001

#GENERAL_PARAMETERS----------------------------------------------------------------------------------------------------#

mathematicaRoot= 0.011
es= 0.0001

#Raphson-Newton--------------------------------------------------------
# Estimated point root (ONE ROOT ONLY) #
xi= 0.01

#Secant--------------------------------------------------------
# Estimated point root (ONE ROOT ONLY) #
xim1= 0.1
xi= 0.01

#Bisection--------------------------------------------------------
# Estimated point root (ONE ROOT ONLY) #
xl= 0.00001
xu= 1

#f(t) values
K= 40000
po= 30
r= 0.1

def f(x):
    e= 0.001
    Re= 5000
    D= 0.05
    Sq= sympy.sqrt(x)
    y= (1 / Sq ) + 2.0 * sympy.log( (e / 3.70 * D ) + (2.51 / Re * Sq), 10)
    return float(y)


#Secant method---------------------------------------------------------------------------------------------------------#

i= 0
while i <= 50:
    # General Formula #
    xi1 = float(xi - (f(xi) * (xim1 - xi) / (f(xim1) - f(xi))))

    # Zero check for the function #
    if abs(f(xi1)) < 10**-7:
        print("\nNo. of iterations Secant: " + str(i + 1))
        print(xi1)
        print("\nAccuracy: " + str(abs( 1 - ((abs( mathematicaRoot - xi1) / xi1) * 100))) + " %")
        break

    # Convergence criterion #
    ea = abs(float((xi1 - xi) / xi1))
    if ea < es:
        print("\nNo. of iterations Secant: " + str(i + 1))
        print(xi1)
        print("\nAccuracy: " + str(abs( 1 - ((abs( mathematicaRoot - xi1) / xi1) * 100))) + " %")
        break

    # Reassignment of the x values #
    xim1= xi
    xi = xi1

    # Last iteration -> did not converge #
    if i == 50:
        print("\nDid not converge in " + str(i) + " iterations")

    i+= 1