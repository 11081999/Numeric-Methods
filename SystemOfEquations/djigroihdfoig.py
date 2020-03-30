import sys
sys.path.append(r"C:\Users\Roberto\AppData\Local\Programs\Python\Python38-32\Lib\site-packages")
import numpy as np

np.set_printoptions(suppress=True)
def Gauss_Seidel(A, b, error_s):

    [m, n] = np.shape(A)

    U = np.triu(A, 1)
    L = np.tril(A)

    x = np.ones((m ,1))
    err = np.ones((m ,1) ) *100

    while np.max(err) > error_s:

        xn = np.dot(np.linalg.inv(L), (b - np.dot(U, x)))
        err = abs((xn - x ) /xn ) *100
        x = xn

    for i in range(0, m):
        print 'x[%0.0f] = %6.4f --- Error: %0.4f %%' % ( i +1, x[i], err[i])


    # [A]{x} = [b]
A = np.array(np.mat('10, 2,-1;\
	             -3,-6, 2;\
		      1, 2, 5'))

b = np.array(np.mat('27; -61.5;
-21.5'));

# Approximate
% error stop criterion
error_s = 5

Gauss_Seidel(A, b, error_s)

