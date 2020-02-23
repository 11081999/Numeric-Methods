import sys
sys.path.append(r"C:\Users\rober\AppData\Local\Programs\Python\Python38\Lib\site-packages")
from matplotlib import pyplot as plt
import sympy
from sympy import Symbol, Derivative

from timeit import default_timer as timer

#Calculate elapsed time
start = timer()

#GENERAL_PARAMETERS----------------------------------------------------------------------------------------------------#
graphTitle= "Raphson-Newton Iterations Calculation"

#Data on the X axis
x_values = []
x_name= "X"

#Data on the Y axis
y_values = []
y_name= "Y"

#Limits
startLimit= 14
endLimit= 16
jump= 0.01

#GENERAL
g= 9.81
m= 70
t= 10

#Estimated point root (ONE ROOT ONLY)
xi= 2
xim1= 3

#
es= 0.0001

#FUNCTIONS-------------------------------------------------------------------------------------------------------------#
def f(x):
    #i.e
    #y= x+1
    #y= pow(x, 2)
    #y= 4*pow(x, 2) +  7*x + 8

    #Write known funcion
    #y= g*m*(1-sympy.exp(-x*t/m))/x-40
    y = (x - sympy.exp(-x))

    return y

#XI
def xi1():
    return float(xi - ( f(xi)*(xim1-xi) / (f(xim1)-f(xi)) ))

#"ERROR"
def ea():
    return abs( float((xi1() - xi) / xi1()) )

#Print elapsed Time
def time():
    end = timer()
    print("")
    print("Time elapsed: ")
    print(float(end - start))

#SECANT METHOD OF INTERPOLATING----------------------------------------------------------------------------------------#
i= 0
while i <= 50:
    if abs(f(xi1())) < 10**-7:
        print("i: " + str(i))
        print(xi1())

    if ea() < es:
        print("i: " + str(i))
        print(xi1())

    xim1= xi
    xi = xi1()

    if i == 50:
        print("\n Did not converge in any iterations")

    i+= 1


#PLOTTING--------------------------------------------------------------------------------------------------------------#
#Styles
#plt.xkcd()

#Names & Tags
fig, ax = plt.subplots()
ax.set(xlabel= x_name, ylabel= y_name, title=graphTitle)

#Grid
ax.grid()

#Values
plt.plot(x_values, y_values, label='Python')

#Plott
#plt.show()
