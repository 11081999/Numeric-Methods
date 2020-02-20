import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
from matplotlib import pyplot as plt
import sympy
from sympy import Symbol, Derivative

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
xi= 15.158907921376873

#FUNCTION-------------------------------------------------------------------------------------------------------------#
def f(x):
    #i.e
    #y= x+1
    #y= pow(x, 2)
    #y= 4*pow(x, 2) +  7*x + 8

    #Write known funcion
    y= g*m*(1-sympy.exp(-x*t/m))/x-40

    return y
#DERIVATIVE OF THE FUNCTION AT A POINT XI
def df(xi):
    x = Symbol('x')
    func = f(x)
    deriv = Derivative(func, x)
    return float(deriv.doit().subs({x: xi}))

#XI
def xi1():
    return float(xi - ( f(xi)  / df(xi) ))

#"ERROR"
def error():
    return float((xi1() - xi) / xi1())

#ASSIGN X & Y VALUES
while startLimit < endLimit:
    x_values.append(startLimit)
    y_values.append(f(startLimit))
    startLimit = startLimit + jump

def printResult():
    print("")
    print("F(xi)")
    print(f(xi))
    print("derivative at xi")
    print(df(xi))
    print("xi_1")
    print(xi1())
    print("-Error-")
    print(error())

printResult()

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
plt.show()
