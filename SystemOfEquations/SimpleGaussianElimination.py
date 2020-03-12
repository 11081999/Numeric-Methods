import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
import numpy as np

matrix= ([   [0.2,    2,  -5,    6],
             [ 10,    1, -30,    4],
             [  3,-0.18,  15,  -11],
             [  7,  0.3, -20,   15]] )
constants= ([10, -4, 1, 11] )

cons= constants.reverse()

z= np.linalg.solve(matrix, constants )

print( "Solutions:\n" + str(z))

def gauss(matrix, constants):
    n = len(matrix[0])-1
    result= [0, 0, 0, 0]

    for k in range(1, n-1):
        for i in range(k+1, n):
            factor= matrix[i][k]/matrix[k][k]
            for j in range(k+1, n):
                matrix[i][j]= matrix[i][j] - factor * matrix[k][j]

            constants[i]= constants[i]-factor * constants[k]

    result[n]= constants[n]/matrix[n][n]

    for i in range(n - 1, -1, -1):
        sum= constants[i]
        for j in range(i+1, n):
            sum= sum - matrix[i][j] * result[j]
        result[i]= sum / matrix[i][i]

    return result

print("\nGauss:" + str(gauss(matrix, constants)) )



def g(A):
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


