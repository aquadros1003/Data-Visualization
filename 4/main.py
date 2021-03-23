from Klasy import *
#zad1
zad1 = [0+x for x in range(1,31,1)]
zad1x2 = [str(x*2) for x in zad1]
plik1 = open("zad1_plik.txt", "w")
plik1.writelines(zad1x2)
#zad2
plik1 = open("zad1_plik.txt", "r")
plik2 = plik1.readlines()
print(plik2)
#zad3
with open("tekst.txt", "w") as zadanie3:
     for newLine in range(20) :
         zadanie3.write("linijka\n")
with open("tekst.txt", "r") as zadanie3:
    for line in zadanie3:
         print(line, end="")
#zad5
zad5 = ciagi_arytmetyczne.ciagi_arytmetyczne()
zad5.pobierz_parametry(7, 7, 7)
zad5.policz_elementy()
zad5.pobierz_elementy(7, 7, 7)
zad5.policz_sume()
zad5.wyswietl_dane()
#zad6
robaczek = Robaczek.Robaczek()
robaczek.idz_w_gore(4)
robaczek.w_lewo(7)
robaczek.do_dolu(7)
robaczek.w_prawo(8)
robaczek.gdzie_jestes()


