class Robaczek:
    wspolrzedna_x = 0
    wspolrzedna_y = 0
    ruch = 1

    def __int__(self, x, y, krok):
        self.wspolrzedna_x = x
        self.wspolrzedna_y = y
        self.ruch = krok

    def idz_w_gore(self,ile_krokow):
        self.wspolrzedna_y += (ile_krokow * krok)
    def do_dolu(self,ile_krokow):
        self.wspolrzedna_y -= (ile_krokow * krok)
    def w_prawo(self, ile_krokow):
        self.wspolrzedna_x += (ile_krokow * krok)
    def w_lewo(self, ile_krokow):
        self.wspolrzedna_x -= (ile_krokow * krok)
    def gdzie_jestes(self):
        print("X = " + str(self.wspolrzedna_x) + "Y = " + str(self.wspolrzedna_y))