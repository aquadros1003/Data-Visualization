import numpy as np
import math as m
import pandas as pd
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt


#ZADANIE 1
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# t = np.linspace(0, 2 * np.pi, 100)
# z = t
# x = np.sin(t)
# y = 2 * np.cos(t)
# ax.plot(x, y, z)
# plt.show()

#ZADANIE 2
# np.random.seed(19680801)
# def randrange(n, vmin, vmax):
#     return (vmax - vmin) * np.random.rand(n) + vmin
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# x1 = randrange(10, 32, 32)
# y1 = randrange(10, 32, 42)
# z1 = randrange(10, 46, 45)
# x2 = randrange(10, 42, 72)
# y2 = randrange(10, 13, 3)
# z2 = randrange(10, 45, 131)
# x3 = randrange(10, 13, 53)
# y3 = randrange(10, 51, 14)
# z3 = randrange(10, 53, 53)
# x4 = randrange(10, 23, 15)
# y4 = randrange(10, 76, 34)
# z4 = randrange(10, 23, 151)
# x5 = randrange(10, 41, 151)
# y5 = randrange(10, 42, 105)
# z5 = randrange(10, 86, 53)
# ax.scatter(x1, y1, z1, c='b', marker='X')
# ax.scatter(x2, y2, z2, c='r', marker='p')
# ax.scatter(x3, y3, z3, c='c', marker='*')
# ax.scatter(x4, y4, z4, c='k', marker='+')
# ax.scatter(x5, y5, z5, c='y', marker='o')
# plt.show()

#ZADANIE 4
# fig = plt.figure(figsize=(12, 10))
# ax1 = fig.add_subplot(1, 5, 1, projection='3d')
# ax2 = fig.add_subplot(1, 5, 2, projection='3d')
# ax3 = fig.add_subplot(1, 5, 3, projection='3d')
# ax4 = fig.add_subplot(1, 5, 4, projection='3d')
# ax5 = fig.add_subplot(1, 5, 5, projection='3d')
# _x = np.arange(4)
# _y = np.arange(5)
# _xx, _yy = np.meshgrid(_x, _y)
# x, y = _xx.ravel(), _yy.ravel()
# top = x + y
# bottom = np.zeros_like(top)
# width = depth = 1
# ax1.bar3d(x, y, bottom, width, depth, top, color='g')
# ax2.bar3d(x, y, bottom, width, depth, top, color='k', shade=False)
# ax3.bar3d(x, y, bottom, width, depth, top, color='c')
# ax4.bar3d(x, y, bottom, width, depth, top, color='y', )
# ax5.bar3d(x, y, bottom, width, depth, top, color='b', shade=True)
# plt.show()

#ZADANIE 3
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# surface = ax.plot_surface(X, Y, Z, cmap=plt.get_cmap(), linewidth=0, antialiased=True)
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
# fig.colorbar(surface, shrink=1, aspect=5)
# plt.show()
