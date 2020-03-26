import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
import numpy as np

#This matrix is U
matrix= np.array([   [0.2,    2,  -5,    6],
                     [ 10,    1, -30,    4],
                     [  3,-0.18,  15,  -11],
                     [  7,  0.3, -20,   15]   ] )

b= np.array([ [1], [4], [-12], [-3]])

print("\nmatrix: ")
print(str(matrix))
print("\nb matrix: ")
print(str(b))


def lu(matrix, b):
    n = len(matrix)
    print("\nlenght: "+ str(n))

    for k in range(0, n-1):
        for i in range(k+1, n):
            factor= matrix[i][k]/matrix[k][k]
            matrix[i][k]= factor
            for j in range(k+1, n):
                matrix[i][j] -=  factor * matrix[k][j]
    print(matrix)

    #Fill L matrix (with diagonal in 1s) (Lower half of gauss
    L = np.array([[0 for i in range(n)] for i in range(n)])
    for i in range(0, n):
        for j in range(0, n):
            if i >= j:
                L[i][j] = matrix[i][j]
        L[i][i] = 1
    print("L: ")
    print(L)
    print(" ")

    # Fill U matrix (upper half of gauss)
    U = np.array([[0 for i in range(n)] for i in range(n)])
    for i in range(0, n):
        for j in range(0, n):
            if i <= j:
                U[i][j] = matrix[i][j]
    print("U: ")
    print(U)
    print(" ")

    # Foward substitution; Ly=B
    d = [1, 4, -12, -3]
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

print("\nFinal result: " + str(lu(matrix, b)))