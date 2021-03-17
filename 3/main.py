#zad1
a = [ 1 -x for x in  range(1, 11, 1)]
print(a)

b = [ 4**y for y in range(8)]
print(b)

c = [x for x in b if x % 2 == 0]
print(c)

#zad2
lista_zadanie2a = [randint(0, 100) for x in range(10)]
lista_zadanie2.sort()
print(lista_zadanie2)
lista_zadanie2b = [x for x in randList if x%2==0]
print(lista_zadanie2b)

#zad3
produkty_zadanie3 = {"cytryny":"Kg", "maslo":"kostka", "chleb":"szt","łosoś":"kg"}
print(produkty_zadanie3)
produkty_sztuki = [produkt for produkt in produkty_zadanie3.keys() if produkty_zadanie3[produkt] =="szt"]
print(produkty_sztuki)
#zad4
a = float(input("Podaj dlugosc pierwszego boku trojkata: \n"))
b = float(input("Podaj dlugosc drugiego boku trojkata: \n"))
c = float(input("Podaj dlugosc trzeciego boku trojkata\n"))
    if (str(a).isdigit() == False) | (str(b).isdigit() == False) | (str(c).isdigit() == False):
            print ("Podano bledne wartosci")
    if (a<=0)|(b<=0)|(c<=0):
            print("Podano bledne wartosci")
        elif (a > b) & (a > c):
            check = b**2 + c**2
    if a**2 == check:
                print("Trojkat jest prostokatny")
        else:
                print("Trojkat nie jest prostokatny")
        elif (b > a) & (b > c):
                check = a**2 + c**2
                if b**2 == check:
                    print( "Trojkat jest prostokatny")
                else:
                    print("Trojkat nie jest prostokatny")
            else :
                check = b ** 2 + a ** 2
                if c ** 2 == check:
                    print("Trojkat jest prostokatny")
                else:
                    print( "Trojkat nie jest prostokatny")

#zad5
a = input("Podaj dlugosc pierwszej podstawy trapezu\n")
a = float(input())
b = input("Podaj dlugosc drugiej podstawy trapezu\n")
b = float(input())
h = input("Podaj wysokosc trapezu\n")
h = float(input())
  if (str(a).isdigit() == False) | (str(b).isdigit() == False) | (str(h).isdigit() == False):
        print("Podano bledne wartosci")
    else:
        if (a<=0)|(b<=0)|(h<=0):
            print ("Podano bledne wartosci")
        else:
            P = (a+b)*h/2
            print(P)

#zad6
def iloczyn_elementow_ciagu(a1=1, q=4, n=10):
    an = a1*q
    elementy_ciagu = []
    elementy_ciagu.append(a1)
    elementy_ciagu.append(an)
    iloczyn = a1*an
    for x in range (3, n+1, 1):
        anp1 = an * q
        elementy_ciagu.insert(x, anp1)
        an = anp1
        iloczyn *= anp1

    return iloczyn, elementy_ciagu
print(iloczyn_elementow_ciagu(1, 2, 6))

#zad7
def zadanie7(* elementy):
    if(len(elementy) != 0):
        iloczyn = 1
        for x in range(len(elementy)):
            iloczyn*=elementy[x]
        return iloczyn
    else:
        return 0
print(zadanie7(1, 2, 3, 4, 5, 6))

#zad8
def zakupy(**koszyk):
    przedmioty = len(koszyk)
    if przedmioty != 0:
        suma = 0
        ceny = [cena for cena in koszyk.values() if isinstance(cena, float) == True or isinstance(cena, int) == True]
        print(ceny)
        for x in range (len(ceny)):
            suma+=float(ceny[x])

    else:
        return "Brak zakupów"
    return suma