import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
import numpy as np

np.set_printoptions(suppress=True)

#This matrix is U
a= np.array([   [  6.0,  0.0, -1.0,    0,     0],
                [ -3.0,  3.0,    0,    0,     0],
                [  0.0, -1.0,    9,    0,     0],
                [  0.0,   -1,   -8,   11,    -2],
                [ -3.0, -1.0,    0,    0,     4] ] )

b= np.array([ [50.0], [0.0], [160.0], [0.0], [0.0]])

#print("\nmatrix: ")
#print(str(a))
#print("\nb matrix: ")
#print(str(b))


def lu(matrix, constants):
    n = len(matrix[0])-1
    print("\nn: "+str(n))

    # operation counter
    opCounter = 0

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
            opCounter += 1
            matrix[i][k]= factor
            for j in range(k+1, n +1):
                matrix[i][j]= matrix[i][j] - factor * matrix[k][j]
                opCounter += 1

    print("\nMtrix Deconstructed: ")
    print(matrix)

    L = np.array([[0.0 for i in range(n +1)] for i in range(n +1)])
    for i in range(0, n +1):
        for j in range(0, n +1):
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
            opCounter += 1

        constants[i]= sum

    print(constants)

    #Backward substitution
    X[n] = constants[n]/U[n][n]
    for i in range(n - 1, 1 - 1-1, -1):
        sum = 0
        for j in range(i + 1, n +1):
            sum = sum + U[i][j] * X[j]
            opCounter += 1

        X[i] = (constants[i] - sum)/ U[i][i]
        opCounter += 1

    print("\nOperation Count : " + str(opCounter))

    print("\nFinal result: ")

    return X

print(str(lu(a, b)))