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


def gauss(matrix, constants):
    n = len(matrix[0])-1
    print("\nn: "+str(n))
    #NUMPY ARRAYS CONSIST OF THE SAME DATA TYPES, I WANT THEM TO BE FLOATS!!!!!!!
    result= [0.0, 0.0, 0.0, 0.0]

    for k in range(n-1 +1):
        print("\niteration "+str(k)+" matrix a: ")
        print(matrix)
        print("\niteration " + str(k) + " matrix b: ")
        print(constants)
        #PYTHON EXCLUYE EL SEGUNDO PARAMETRO DEL RANGE() POR ESO EL +1 !!!!!!!!
        for i in range(k+1, n +1):
            factor= np.divide(matrix[i][k], matrix[k][k])
            for j in range(k+1, n +1):
                matrix[i][j]= matrix[i][j] - factor * matrix[k][j]

            constants[i]= constants[i]- factor * constants[k]

    result[n]= constants[n]/matrix[n][n]
    #Aqui no tnego idea de por qué es hasta -2 pero tiene que ver conque range() excluye
    #Su última poscición
    for i in range(n-1, 1 -1-1, -1):
        sum= constants[i]

        for j in range(i+1, n +1):
            sum= sum - matrix[i][j] * result[j]

        result[i]= np.divide(sum, matrix[i][i])

    return result

print("\nGauss:" + str(gauss(a, b)) )