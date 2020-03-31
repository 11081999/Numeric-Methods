import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
from matplotlib import pyplot as plt
import sympy
from sympy import *

#GENERAL_PARAMETERS----------------------------------------------------------------------------------------------------#
mathematicaRoot= 0.0118017
es= 0.0001

#Raphson-Newton
# Estimated point root (ONE ROOT ONLY) #
xi= 0.02

#Function
def f(x):
    e= 0.001
    Re= 5000
    D= 0.05
    Sq= sympy.sqrt(x)
    y= (1 / Sq ) + 2.0 * sympy.log( (e / 3.70 * D ) + (2.51 / Re * Sq), 10)
    return y

# Find derivate of the function f(x) at a point xi #
def df(xi):
    x = Symbol('x')
    func = f(x)
    deriv = Derivative(func, x)
    return float(deriv.doit().subs({x: xi}))

#Raphson-Newton method-------------------------------------------------------------------------------------------------#

i= 0
while i <= 50:
    # General Formula #
    xi1 = float(xi - f(xi) / df(xi))

    # Zero check for the function #
    if abs(f( xi + 1 )) < 10**-7:
        print("\nNo. of iterations: " + str(i + 1))
        print(xi1)
        print("\nAccuracy: " + str(abs( 1 - ((abs( mathematicaRoot - xi1) / xi1) * 100))) + " %")
        break

    # Convergence criterion #
    ea = float( abs( (xi1 - xi) / xi1) )
    if ea < es:
        print("\nNo. of iterations: " + str(i + 1))
        print(xi1)
        # Accuracy
        print("\nAccuracy: " + str(abs( 1 - ((abs( mathematicaRoot - xi1) / xi1) * 100))) + " %")
        break

    # Reassignment of the x values #
    xi = xi1

    # Last iteration -> did not converge #
    if i == 50:
        print("\nDid not converge in " + str(i) + " iterations")

    i+= 1