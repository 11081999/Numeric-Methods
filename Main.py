import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
from matplotlib import pyplot as plt
from sympy import Symbol, Derivative

#GENERAL_PARAMETERS----------------------------------------------------------------------------------------------------#
graphTitle= "Title"

#Data on the X axis
x_values = []
x_name= "X"

#Data on the Y axis
y_values = []
y_name= "Y"

#Limits
startLimit= 0
endLimit= 100
jump= 0.01

#FUNCTION-------------------------------------------------------------------------------------------------------------#
def f(x):
    #y= x+1

    #y= pow(x, 2)

    #y= 4*pow(x, 2) +  7*x + 8

    y= x**3 - 5*x - 9

    return y

#ASSIGN X & Y VALUES
while startLimit < endLimit:
    x_values.append(startLimit)
    y_values.append(f(startLimit))
    startLimit = startLimit + jump

#FIND DERIVATIVE-------------------------------------------------------------------------------------------------------#
x= Symbol('x')
func= f(x)
deriv= Derivative(func, x)
#Calculate derivative at specific point: deriv.doit().subs({x:4})
print("")
print(deriv.doit())

#SECANT METHOD OF INTERPOLATING----------------------------------------------------------------------------------------#
"""
def secant(x0, x1, e, N):
    print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            print('Not Convergent!')
            break

        condition = abs(f(x2)) > e
    print('\n Required root is: %0.8f' % x2)

# Input Section
x0 = input('Enter First Guess: ')
x1 = input('Enter Second Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')

# Converting x0 and e to float
x0 = float(x0)
x1 = float(x1)
e = float(e)

# Converting N to integer
N = int(N)

# Note: You can combine above three section like this
# x0 = float(input('Enter First Guess: '))
# x1 = float(input('Enter Second Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Secant Method
secant(x0, x1, e, N)
"""
#CALCULATION OF THE NEWTON-RAPHSON ITERATIONS--------------------------------------------------------------------------#


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
