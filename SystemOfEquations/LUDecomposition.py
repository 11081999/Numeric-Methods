import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
import numpy as np

np.set_printoptions(suppress=True)

#This matrix is U
a= np.array([   [0.2,    2,  -5,    6],
                [ 10,    1, -30,    4],
                [  3,-0.18,  15,  -11],
                [  7,  0.3, -20,   15]   ] )

b= np.array([ [10.0], [-4.0], [1.0], [-11.0]])

#print("\nmatrix: ")
#print(str(a))
#print("\nb matrix: ")
#print(str(b))


def lu(matrix, constants):
    n = len(matrix[0])-1
    print("\nn: "+str(n))
    #NUMPY ARRAYS CONSIST OF THE SAME DATA TYPES, I WANT THEM TO BE FLOATS!!!!!!!
    X= np.array([[0.0 for i in range(n +1)] for i in range(n +1)])

    for k in range(n-1 +1):
        print("\niteration "+str(k)+" matrix a: ")
        print(matrix)
        print("\niteration " + str(k) + " matrix b: ")
        print(constants)
        #PYTHON EXCLUYE EL SEGUNDO PARAMETRO DEL RANGE() POR ESO EL +1 !!!!!!!!
        for i in range(k+1, n+1):
            factor= np.divide(matrix[i][k], matrix[k][k])
            matrix[i][k]= factor
            for j in range(k+1, n +1):
                matrix[i][j]= matrix[i][j] - factor * matrix[k][j]

    print("\nMtrix Deconstructed: ")
    print(matrix)

    L = np.array([[0.0 for i in range(n +1)] for i in range(n +1)])
    for i in range(0, n +1):
        for j in range(0, n +1):
            if i >= j:
                L[i][j] = matrix[i][j]
        L[i][i] = 1

    L = np.array([[0.0 for i in range(n +1)] for i in range(n +1)])
    for i in range(0, n + 1):
        for j in range(0, n + 1):
            if i >= j:
                L[i][j] = matrix[i][j]
        L[i][i] = 1

    U = np.array([[0.0 for i in range(n +1)] for i in range(n +1)])
    for i in range(0, n + 1):
        for j in range(0, n + 1):
            if i <= j:
                U[i][j] = matrix[i][j]

    print("\nMtrix L : ")
    print(L)
    print("\nMtrix U : ")
    print(U)

    #Foward substitution
    for i in range(0, n +1):
        sum= constants[i]
        for j in range(0, i-1 +1):
            sum= sum - L[i][j] * constants[j]
        constants[i]= sum

    print(constants)

    #Backward substitution
    X[n] = constants[n]/U[n][n]
    for i in range(n - 1, 1 - 1-1, -1):
        sum = 0
        for j in range(i + 1, n +1):
            sum = sum + U[i][j] * X[j]

        X[i] = (constants[i] - sum)/ U[i][i]

    print("\nFinal result: ")

    return X

print(str(lu(a, b)))

"""
    # Foward substitution; Ly=B
    d = [10, -4, 1, -11]
    y1 = d[0]
    y2 = (d[1] - L[1][0] * y1)
    y3 = d[2] - L[2][0] * y1 - L[2][1] * y2
    y4 = d[3] - L[3][0] * y1 - L[3][1] * y2 - L[3][2] * y3

    print(" ")
    # Back substitution: Ux = y
    x4 = y4 / U[3][3]
    print("x4=", x4)
    x3 = (y3 - U[2][3] * x4) / U[2][2]
    print("x3=", x3)
    x2 = (y2 - U[1][2] * x3 - U[1][3] * x4) / U[1][1]
    print("x2=", x2)
    x1 = (y1 - U[0][1] * x2 - U[0][2] * x3 - U[0][3] * x4) / U[0][0]
    print("x1=", x1)
"""