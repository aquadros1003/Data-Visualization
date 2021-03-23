class ciagi_arytmetyczne:
    a1 = 0
    roznica = 0
    ile_elementow = 0
    wyrazy_ciagu = [a1]

    def wyswietl_dane(self):
        print(self.wyrazy_ciagu)
    def pobierz_elementy(self, *n):
        pobrane_elementy = []
        for x in n:
            pobrane_elementy.append(self.wyrazy_ciagu[x-1])
        print(pobrane_elementy)
    def pobierz_parametry(self, a1, roznica,  ile_elementow):
        self.a1 = a1
        self.roznica = roznica
        self. ile_elementow = ile_elementow
    def policz_sume(self):
        suma = 0
        for x in self.wyrazy_ciagu:
            suma += x
        print(suma)
    def policz_elementy(self):
        if self.roznica != 0:
            a1 = self.a1
            for x in range(self.ile_elementow):
                an = a1 + self.roznica
                self.wyrazy_ciagu.append(an)
                a1 = an
