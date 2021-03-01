#zad1
a1 = "zadanie na wd"
b1 = "zadanie ma wizualizacje danych"
c1 = 3
d1 = 7
e1 = 2.4
f1 = 7.6
g1 = 3 + 4j
h1 = 5 + 7j
print(a1,b1,c1,d1,e1,f1,g1,h1)
#zad2
a2 = 7
b2 = 5
suma2 = a2 + b2
roznica2 = a2 - b2
iloczyn2 = a2 * b2
iloraz2 = a2 / b2
print(suma2,roznica2,iloczyn2,iloraz2)
#zad3
print(suma2 + roznica2,iloczyn2 - suma2,suma2 * roznica2, iloraz2 / iloczyn2,suma2 ** roznica2,iloczyn2 % roznica2)
#zad4
from cmath import *
print(exp(10),sqrt(log(5+sin(8)**2,6)),[3,55],[4,80])
#zad5
imie = 'LUKASZ'
nazwisko = 'JANKOWSKI'
print(imie.capitalize() + " " + nazwisko.capitalize())
#zad6
piosenka = 'Idziemy do zoo, zoo, zoo Idziemy do zoo, zoo, zoo Idziemy do zoo zoo, zoo, zoo'
print(piosenka.count('zoo'))
#zad7
lancuch = 'wizualizacja danych'
print(lancuch[1],lancuch[-1])
#zad8
x8 = piosenka.split()
print(x8)
#zad9
a = 'wd'
b = 5.7
c = 57
print(str(a),float(b),hex(c))