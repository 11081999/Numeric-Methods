import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
import numpy as np

matrix= ([   [0.2,    2,  -5,    6],
             [ 10,    1, -30,    4],
             [  3,-0.18,  15,  -11],
             [  7,  0.3, -20,   15]] )
constants= ([ [10], [-4], [1], [11] ])

#constants= ([[10], [-4], [1], [11] ])

def gauss(matrix, constants):
    n = len(matrix[0])-1
    result= [0, 0, 0, 0]

    for k in range(1, n-1):
        for i in range(k+1, n):
            factor= matrix[i][k]/matrix[k][k]
            for j in range(k+1, n):
                matrix[i][j] -=  factor * matrix[k][j]

            constants[i] -= factor * constants[k]

    result[n]= constants[n]/matrix[n][n]

    for i in range(n -1 , 1, -1):
        sum= constants[i]

        for j in range(i+1, n):
            sum -= matrix[i][j] * result[j]

        result[i]= sum / matrix[i][i]

    return result

print("\nGauss:" + str(gauss(matrix, constants)) )