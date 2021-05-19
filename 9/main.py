import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
from pathlib import Path

# ts = pd.Series(np.random.randn(1000), index = pd.date_range('1/1/2015',periods=1000))
#
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia','Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#         'Populacja': [11190846, 13031711035, 38676567, 38675467]}
#
# df = pd.DataFrame(data)
# print(df)
#
# grupa = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})
# print(grupa)
#
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Kontynent')
# wykres.set_ylabel('Mld')
# wykres.legend()
# plt.xticks(rotation = 0)
# plt.savefig('wykres.png')
# plt.title('Populacja z podzialem na kontynenty')
# plt.show()

# df = pd.read_csv('dane.csv',header = 0, sep = ';', decimal = '.')
# print (df)
# grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia':['sum']})
# print(grupa)
# wykres = grupa.plot.pie(subplots = True, autopct = '%.2f %%', fontsize = 20, figsize = (6, 6), legend = (0,0))
# plt.legend()
# plt.legend(loc = 'lower right')
# plt.title('Suma zamówienia dla sprzedawcy')
# plt.show()

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2015', periods=1000))
#
# ts = ts.cumsum()
#
# df = pd.DataFrame(ts)
#
# df['MA'] = df.rolling(window=50).mean()
# df.plot()
# plt.show()

# #ZADANIA
# #1
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# grupa1 = df.groupby(['Rok']).agg({'Liczba': ['sum']})
# wykres1 = grupa1.plot()
# wykres1.set_ylabel("Liczba urodzeń")
# wykres1.set_xlabel("Rok")
# wykres1.legend()
# plt.title("Liczba urodzonych dzieci w poszczególnych latach")
# plt.show()
# #2
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
#
# grupa2 = df.groupby(['Plec']).agg({'Liczba': ['sum']})
# wykres2 = grupa2.plot.bar()
# wykres2.set_ylabel("Liczba urodzeń")
# wykres2.set_xlabel("Płeć")
# wykres2.legend()
# plt.title("Liczba urodzonych dzieci ze względu na płeć")
# plt.xticks(rotation=0)
# plt.show()
#
# #3
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# df = df[(df['Rok'] >= 2013) & (df['Rok'] <= 2017)]
# grupa3 = df.groupby(['Plec']).agg({'Liczba': ['sum']})
# wykres3 = grupa3.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6), legend=(0, 0))
# plt.legend(loc="lower right")
# plt.title("Stosunek urodzeń ze względu na płeć")
# plt.show()
#
# #4
# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal=',')
# grupa4 = df.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})
# wykres4 = grupa4.plot.bar()
# wykres4.set_ylabel("Ilosc zamowien")
# wykres4.set_xlabel("Sprzedawcy")
# wykres4.legend()
# plt.title("Ilość zamówień na poszczegolnych sprzedawcow")
# plt.xticks(rotation=0)
# plt.show()
