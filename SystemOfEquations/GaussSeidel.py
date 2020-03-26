import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
import numpy as np

P= 400
A= 6
E= 100

a=  np.array([[  0.3369,     -0.128,   0.096,    -0.008899,  -0.05332],
              [       1,    -2.9832, 0.00884,            0,    1.7361],
              [       1,    -0.0118,  3.7146,            0,         0],
              [-0.00889,    -0.2222,  0.3541,            0,    0.1204],
              [       1,    -2.2585, -6.6864,            0,         0]] )

#This needs to be a column array?
b=  np.array([ [P/E*A, 0, 0, P/E*A, 0] ])

n = len(a[0])

es= 0.0001

print("Matrix size: " + str(n))

for i in range(1, n):
    dummy= a[i][i]
    for j in range(1, n):
        a[i][j]= a[i][j] / dummy
    b[i] = b[i] / dummy
    for i in range (1, n):
        sum= b[i]
        for j in range(1, n):
            if i != j:
                sum= sum - a[i][j]*X[j]
        X[i]= sum

iter= 1
sentinel= 1

for i in range(1, n):
    old= X[i]
    sum= b[i]
    for j in range(1, n):
        if i != j:
            sum= sum - a[i][j] * X[j]
    X[i]= lambda*sum + (1.0-lambda)*old
    if sentinel == 1 and X[i] != 0:
        ea= abs((X[i]-old)/X[i])*100
        if ea > es:
            sentinel= 0
    iter= iter + 1
    if sentinel == 1 or iter >= imax:
        break