from math import *
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
pierwsza_liczba = input("Podaj pierwszą liczbę: ")
znak = input("Podaj znak działania: ")
druga_liczba = input("Podaj drugą liczbę: ")
if znak == "+":
    suma = int(pierwsza_liczba) + int(druga_liczba)
    print(suma)
elif znak == "-":
    roznica = int(pierwsza_liczba) - int(druga_liczba)
    print(roznica)
elif znak == "*":
    iloczyn = int(pierwsza_liczba) * int(druga_liczba)
    print(iloczyn)
elif znak == "/":
    iloraz = int(pierwsza_liczba) / int(druga_liczba)
    print(iloraz)
else:
    print("error")
#zad3
print(suma2 + roznica2,iloczyn2 - suma2,suma2 * roznica2, iloraz2 / iloczyn2,suma2 ** roznica2,iloczyn2 % roznica2)
#zad4
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
napis2 = "Jest dziś poniedziałek"
print("Jaki mamy dziś dzień? %s " %  (napis2))
liczba = 5.677
print("twoja liczba to: %(z1).2f" % {'z1': liczba})
liczba_szesnastkowo = 0xf351
print(liczba_szesnastkowo)
print("%x" % (liczba_szesnastkowo))