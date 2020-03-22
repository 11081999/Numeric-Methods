import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
import numpy as np

matrix= np.array([   [0.2,    2,  -5,    6],
             [ 10,    1, -30,    4],
             [  3,-0.18,  15,  -11],
             [  7,  0.3, -20,   15]] )

b= np.array([ [1], [4], [-20], [15]])

print("\nmatrix: "+ str(matrix))
print("\nb matrix: "+ str(b))


def lu(matrix):
    n = len(matrix)
    print("\nlenght: "+ str(n))

    #Fill L matrix and its diagonal with 1
    L = np.array([[0 for i in range(n)] for i in range(n)])
    for i in range(0, n):
        L[i][i] = 1
    print("\nL matrix: ")
    print(L)

    #Fill U matrix
    U = np.array([[0 for i in range(n)] for i in range(n)])
    for i in range(0, n):
        for j in range(0, n):
            U[i][j] = matrix[i][j]

    print("\nU matrix: " + str(U))
    n = len(U)
    print("\nlenght: " + str(n))

    # (4) Find both U and L matrices
    for i in range(0, n):  # for i in [0,1,2,..,n]
        # (4.1) Find the maximun value in a column in order to change lines
        maxElem = abs(U[i][i])
        maxRow = i
        for k in range(i + 1, n):  # Interacting over the next line
            if (abs(U[k][i]) > maxElem):
                maxElem = abs(U[k][i])  # Next line on the diagonal
                maxRow = k

        # (4.2) Swap the rows pivoting the maxRow, i is the current row
        for k in range(i, n):  # Interacting column by column
            tmp = U[maxRow][k]
            U[maxRow][k] = U[i][k]
            U[i][k] = tmp

        # (4.3) Subtract lines
        for k in range(i + 1, n):
            c = -U[k][i] / float(U[i][i])
            L[k][i] = c  # (4.4) Store the multiplier
            for j in range(i, n):
                U[k][j] += c * U[i][j]  # Multiply with the pivot line and subtract

        # (4.5) Make the rows bellow this one zero in the current column
        for k in range(i + 1, n):
            U[k][i] = 0



    n = len(L)

    # (5) Perform substitutioan Ly=b
    y = np.array([0 for i in range(n)])
    for i in range(0, n, 1):
        y[i] =  b[i] /  float(L[i][i])
        for k in range(0, i, 1):
            y[i] -= y[k] * L[i][k]

    print("\nY array: " + str(y))
    n = len(U)

    # (6) Perform substitution Ux=y
    x = np.array([0 in range(n)])
    for i in range(n - 1, -1, -1):
        x[i] = y[i] / float(U[i][i])
        for k in range(i - 1, -1, -1):
            U[i] -= x[i] * U[i][k]

    return x
"""
    for k in range(1, n):
        for i in range(k+1, n):
            factor= matrix[i][k]/matrix[k][k]
            matrix[i][k]= factor
            for j in range(k+1, n):
                matrix[i][j] -=  factor * matrix[k][j]

    #print("\nb Final matrix: "+ str(matrix))
"""

print("\nFinal result: " + str(lu(matrix)))