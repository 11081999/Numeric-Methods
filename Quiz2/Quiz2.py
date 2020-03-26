import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
from matplotlib import pyplot as plt
import sympy
from sympy import Symbol, Derivative

#GENERAL_PARAMETERS----------------------------------------------------------------------------------------------------#

mathematicaRoot= 82.93
es= 0.0001

#Raphson-Newton--------------------------------------------------------
# Estimated point root (ONE ROOT ONLY) #
xi= 84

#Secant--------------------------------------------------------
# Estimated point root (ONE ROOT ONLY) #
xim1= 2
xi= 84

#Bisection--------------------------------------------------------
# Estimated point root (ONE ROOT ONLY) #
xl= 50
xu= 100

#f(t) values
K= 40000
po= 30
r= 0.1

def f(x):
    y= ((K * po * sympy.exp(r * x) / (K + po * (sympy.exp(r* x) - 1) )) - 30000 )
    return y


#Bisection method------------------------------------------------------------------------------------------------------#
i= 0
while i <= 50:
    # Middle Point  #
    xr = (xl + xu) / 2

    # Zero check for the function #
    if abs(f(xr)) < 10**-7:
        print("\nNo. of iterations Bisection: " + str(i + 1))
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
        print("\nNo. of iterations Bisection: " + str(i + 1))
        print(xr)
        print("\nAccuracy: " + str(abs(1 - ((abs(mathematicaRoot - xr) / xr) * 100))) + " %")
        break

    # Last iteration -> did not converge #
    if i == 50:
        print("\nDid not converge in " + str(i) + " iterations")

    i+= 1

#Raphson-Newton method-------------------------------------------------------------------------------------------------#

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
        print("\nNo. of iterations Raphson-Newton: " + str(i + 1))
        print(xi1)
        print("\nAccuracy: " + str(abs( 1 - ((abs( mathematicaRoot - xi1) / xi1) * 100))) + " %")
        break

    # Convergence criterion #
    ea = float( abs( (xi1 - xi) / xi1) )
    if ea < es:
        print("\nNo. of iterations Raphson-Newton: " + str(i + 1))
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
