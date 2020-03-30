import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
import numpy as np

np.set_printoptions(suppress=True)

matrix= np.array([  [0.2,    2,  -5,    6],
                    [ 10,    1, -30,    4],
                    [  3,-0.18,  15,  -11],
                    [  7,  0.3, -20,   15]   ] )

constants= np.array([ [10.0], [-4.0], [1.0], [-11.0]])

#print("\nmatrix: ")
#print(str(a))
#print("\nb matrix: ")
#print(str(b))

imax= 4
es= 0.0001
lam= 1.2

def sidel(a, b):
    n = len(a[0]) - 1
    print("\nn: " + str(n))
    # NUMPY ARRAYS CONSIST OF THE SAME DATA TYPES, I WANT THEM TO BE FLOATS!!!!!!!
    X = np.array([[0.0 for i in range(n + 1)]])

    for i in range(1, n +1):
        dummy = a[i][i]
        for j in range(1, n +1):
            a[i][j] = a[i][j] / dummy

        b[i] = b[i] / dummy

        for i in range(1, n +1):
            sum = b[i]
            for j in range(1, n +1):
                if i != j:
                    sum = sum - a[i][j] * X[j]
            X[i] = sum

    iter = 1
    sentinel= 1
    while sentinel == 1:
        for i in range(1, n +1):
            old = X[i]
            sum = b[i]
            for j in range(1, n +1):
                if i != j:
                    sum = sum - a[i][j] * X[j]
            X[i] = lam *sum + (1.0 - lam) * old
            if sentinel == 1 and X[i] != 0:
                ea = abs((X[i] - old) / X[i])
                if ea > es:
                    sentinel = 0
            iter = iter + 1
            if sentinel == 1 or iter >= imax:
                break

    print("\nFinal result: ")
    return X

print(str(sidel(matrix, constants)))