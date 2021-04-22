import numpy as np

# zadanie1
zadanie1a = np.arange(6).reshape(3,2)
zadanie2b = np.array([x**2 for x in range(1,7)]).reshape(3,2)
print(a1 * b1)

#zadanie2
def zadanie2(v):
    r = 0
    for x in v:
        m = x[0]
        for y in range(1, len(x)):
            if x[y] <= m:
                m = x[y]
        print("Najmniejszą wartością w rzędzie " + str(r) + " jest " + str(m))
        r = r + 1
    v = v.transpose()
    r = 0
    for x in v:
        m = x[0]
        for y in range(1, len(x)):
            if x[y] <= m:
                m = x[y]
        print("Najmniejszą wartością w kolumnie " + str(r) + " jest " + str(m))
        r = r + 1


 a = np.array([[2, 4, 1], [2, 8, 9], [3, 5, 7]])
 b = np.array([[4, 5, 7, 5], [6, 7, 9, 10], [11, 23, 2, 1], [3, 11, 56, 4]])
 zadanie2(b)

# zadanie3
a = np.array([2, 4, 6])
b = np.array([1, 5, 4])
print(a * b)

# zadanie4
a = np.array([2.0, 4.2, 6.5])
b = np.array([1, 5, 4])
print(a.dot(b))

from math import *
# zadanie5
 a = []
c = np.array([[3, 5], [2, 7], [9, 6]])
for x in c:
    for y in range(len(x)):
        a.append(sin(x[y]))
print(a)

#zadanie6
b = []
c = np.array([[3, 5], [2, 7], [9, 6]])
for x in c:
    for y in range(len(x)):
        b.append(cos(x[y]))
print(b)

#zadanie7
a = np.array([[3, 5], [2, 7], [9, 6]])
b = np.array([[2, 4], [5, 6], [3, 5]])
print(a+b)

#zadanie8
a = np.arange(9)
a = a.reshape(3, 3)
for x in a:
    print(x)

# zadanie9
a = np.arange(12).reshape(3, 4)
for x in a.flat:
    print(x)

# zadanie10
a = np.arange(81).reshape(9, 9)
print(a)
(a.reshape(3, 27))
print(a.T)