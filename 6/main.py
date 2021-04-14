import numpy as np

# zadanie1
zadanie1 = np.arange(4, 20*4 + 4, 4)
print(zadanie1)

# zadanie2
zadanie2float = np.arange(7, dtype="float")
print(zadanie2float)
zadanie2int = zadanie2float.astype("int32")
print(zadanie2int)

# zadanie3
def zadanie3(n):
    potega = [2**x for x in range(1, n*n+1)]
    tablica = np.array(potega)
    return tablica
print(zadanie3(5))

# zadanie4
def zadanie4(n, m):
    tablica2 = np.logspace(start=1,num=m, stop=m, base=n, dtype='int')
    return tablica2

# zadanie5
def zadanie5(n):
    diagonalna = np.diag([x for x in range(n, 0, -1)], 2)
    return diagonalna

# zadanie6
zadanie6 = np.array([['W', 'E' ,'L','Y','W'],
                     ['F','D','F','I','J'],
                     ['L','A','M','A','O'],
                     ['E','N','K','B','X'],
                     ['X','E','C','Q','I']])
print(zadanie6)

# zadanie7
def zadanie7(n):
    tablica = [x*2 for x in range(1, n+1)]
    tablica7 = []
    for x in range(0, n):
        for y in range(0, n):
            tablica7.append(tablica[x-y])
    zadanie7 = np.array(tablica7)
    return zadanie7.reshape[(n, n)]
# zadanie9
tablica9 = np.arange(0, 50, 2)
zadanie9 = tablica9.reshape(5, 5)
print(zadanie9)
