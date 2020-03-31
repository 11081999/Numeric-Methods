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



def gauss(matrix, constants):
    n = len(matrix[0])-1
    print("\nn: "+str(n))

    #operation counter
    opCounter = 0

    #NUMPY ARRAYS CONSIST OF THE SAME DATA TYPES, I WANT THEM TO BE FLOATS!!!!!!!
    result= [0.0, 0.0, 0.0, 0.0, 0.0]

    for k in range(n-1 +1):
        print("\niteration "+str(k)+" matrix a: ")
        print(matrix)
        print("\niteration " + str(k) + " matrix b: ")
        print(constants)
        #PYTHON EXCLUYE EL SEGUNDO PARAMETRO DEL RANGE() POR ESO EL +1 !!!!!!!!
        for i in range(k+1, n +1):
            factor= np.divide(matrix[i][k], matrix[k][k])
            opCounter+= 1
            for j in range(k+1, n +1):
                matrix[i][j]= matrix[i][j] - factor * matrix[k][j]
                opCounter+= 1

            constants[i]= constants[i]- factor * constants[k]
            opCounter+= 1

    result[n]= constants[n]/matrix[n][n]
    opCounter+= 1
    #Aqui no tnego idea de por qué es hasta -2 pero tiene que ver conque range() excluye
    #Su última poscición
    for i in range(n-1, 1 -1-1, -1):
        sum= constants[i]

        for j in range(i+1, n +1):
            sum= sum - matrix[i][j] * result[j]
            opCounter+= 1

        result[i]= np.divide(sum, matrix[i][i])
        opCounter+= 1

    print("\nOperation Count : " + str(opCounter))

    return result

print("\nGauss:" + str(gauss(a, b,)) )