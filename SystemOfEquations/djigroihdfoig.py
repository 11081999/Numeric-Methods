
a=  [[ 0.2,    2,  -5,    6],
     [  10,    1, -30,    4],
     [   3,-0.18,  15,  -11],
     [   7,  0.3, -20,   15],

     [10.0, -4.0,-1.0,-11.0],  ]

def gaussSeidel(a, imax, es, l):
    n = len(a[0])
    print("\nn: " + str(n))
    x = [0.0 for i in range(n)]
    for i in range(1, n):
        dummy = a[i][i]
        for j in range(1, n):
            a[i][j] /= dummy

        a[i][n-1] /= dummy
    for i in range(1, n):
        sum = a[i][n-1]
        for j in range(1, n):
            if i != j:
                sum -= a[i][j] * x[j]

        x[i] = sum

    iter = 1
    sentinel = 0

    print(a)
    while not(sentinel == 1 or iter >= imax):
        sentinel = 1
        for i in range(n):
            old = x[i]
            sum = a[i][n-1]
            for j in range(n):
                if i != j:

                    sum -= a[i][j] * x[j]

            x[i] = l * sum + (1 - l) * old

            if sentinel == 1 and x[i] != 0:
                ea = abs((x[i] - old) / x[i]) * 100
                if ea > es:
                    sentinel = 0
        iter+=1
    print("\nGauss-Seidel:")
    print(x)

gaussSeidel(a, 20, 0.00001, 2)
