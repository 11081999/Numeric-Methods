import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
from matplotlib import pyplot as plt
import sympy
from sympy import *

#GENERAL_PARAMETERS----------------------------------------------------------------------------------------------------#
mathematicaRoot= 0.0118017
es= 0.0001

# Estimated point root (ONE ROOT ONLY) #
xl= 0.0000000001
xu= 1

#function
def f(x):
    e= 0.001
    Re= 5000
    D= 0.05
    Sq= sympy.sqrt(x)
    y= (1 / Sq ) + 2.0 * sympy.log( (e / 3.70 * D ) + (2.51 / Re * Sq), 10)
    return y

#Bisection method------------------------------------------------------------------------------------------------------#

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