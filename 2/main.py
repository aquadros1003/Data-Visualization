#zad1
filmy = ['ulubiony_film1','ulubiony_film2','ulubiony_film3','ulubiony_film4','ulubiony_film5']
filmy=filmy[::-1]
filmy=filmy + ['ulubiony_film6','ulubiony_film7','ulubiony_film8','ulubiony_film9','ulubiony_film10']
#zad2
slownik_filmy = {'klucz1':filmy[0],'klucz2':filmy[1],'klucz3':filmy[2],'klucz4':filmy[3],'klucz5':filmy[4],
'klucz6':filmy[5],'klucz7':filmy[6],'klucz8':filmy[7],'klucz9':filmy[8],'klucz10':filmy[9]}
#zad3
przedmioty = {'Matematyka_dyskretna':'ME','Analiza_matematyczna':'AM','Wizualizacja_danych':'WD','Programowanie_strukturalne':'PS'}
ilosc_przedmiotow = len(przedmioty)
#zad4
liczba4 = float(input("Podaj liczbe: "))
potega4 = liczba4**liczba4
#zad5
ciag_znakow5 = open("zadanie5.txt", "a")
ciag_znakow5.write(str(input("Podaj ciag znaków: ")))
ciag_znakow5.close()
ciag_znakow5 = open("zadanie5.txt", "r")
ilosc_a = (ciag_znakow5.readline().count("a"))
#zad6
a6 = int(input("Podaj a: "))
b6 = int(input("Podaj b: "))
c6 = int(input("Podaj c: "))

if a6%2 == 0 and b6 > c6:
    print ("a jest parzyste oraz b > c");
#zad7
zadanie7 = [4.0,6.4,6,3,7,7.77,4,9,1]
for x in zadanie7:
    print (x+(x-1))
#zad8
lista_parzyste = []
zad8 = 0
while zad8<=9:
    x = int(input("Podaj liczbe: "))
    if x % 2 == 0:
        lista_parzyste.append(x)
    zad8=zad8+1
#zad9
import sys as system
rysunek = [1,2,3,4,5,6]
for zad8a in rysunek:
    if (zad8a) == 1 | (zad8a) == 6:
        for zad9b in rysunek:
            system.stdout.write("O")
            system.stdout.write("\n")
    else:
        system.stdout.write("O")
        for zad9c in range(4):
            system.stdout.write(" ")
        system.stdout.write("O")
        system.stdout.write("\n")
#zad10
try:
    zad10 = float(input("Podaj cyfrę: "))
except ValueError:
    print("Podany został inny znak niż cyfra")






