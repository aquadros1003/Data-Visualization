import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl
# Zad1
# x = np.arange(1,20,1)
# y = (1/x)
# plt.plot(x,y,label="f(x)")
# plt.ylim(0,1)
# plt.xlim(0,20)
# plt.legend()
# plt.show()

# Zad2
# x = np.arange(1,20,1)
# y = (1/x)
# plt.plot(x,y,":",label="f(x) = 1/x",color="red")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.title("wykres f(x) 1 20")
# plt.ylim(0,1)
# plt.xlim(0,20)
# plt.legend()
# plt.show()

# Zad3

# x = np.arange(0,30,0.1)
# s = np.sin(x)
# c = np.cos(x)
# plt.plot(x,s,label="sin")
# plt.plot(x,c,label="cos")
# plt.legend()
# plt.show()

# Zad4
# s = np.sin(x)
# s2 = np.sin(x+np.pi)
# plt.title("wykres sin")
# plt.ylabel("sin")
# plt.xlabel("x")
# plt.plot(x,s2)
# plt.plot(x,s+2)
# plt.show()

 # Zad5
# df = pd.read_csv("iris.csv", names=["sepal len", "sepal wid", "petal len", "petal wid", "class"])
# df = pd.DataFrame(df)
# df = df[["sepal len", "sepal wid", "class"]]
# plt.xlabel("sepal length")
# plt.ylabel("sepal width")
# data = {"a": df["sepal len"], "b": df["sepal wid"], "c": np.random.randint(0, 150, 150)}
# data["d"] = np.abs(data["a"]-data["b"])
# plt.scatter("a", "b", c="c", s="d", data=data)
# plt.title("Iris sepal length and width")
# plt.show()

# Zad6
# excl = pd.ExcelFile("imiona.xlsx")
# df = pd.read_excel(excl, header=0)
# g1 = df.groupby(["Plec"]).agg({"Liczba":["sum"]})
# w = g1.plot.bar()
# plt.xlabel("plec")
# plt.ylabel("liczba")
# plt.xticks(rotation=0)
# plt.show()
#
# Zad7
# csv = pd.read_csv('zamowienia.csv',sep=';')
# sumy = csv.groupby(['Sprzedawca']).agg({'Utarg':['sum']})
# suma_og = sum(csv['Utarg'])
# sumy = (sumy/suma_og)*100
# sumy = round(sumy)
# plt.show()
