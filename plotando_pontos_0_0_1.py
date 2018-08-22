# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 18:02:37 2018

@author: Gerson
"""

from numpy import matrix
import matplotlib.pyplot as plt
from random import randint
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

"""criando X1 e X2 com valores aleatorios"""
X1 = []
X2 = []
for it_iteretor in range(100):
    X1.append(randint(0,10))
    X2.append(randint(0,10))
"""Plotando o grafico de X1 , X2  / Argumento 'ro' para plotar apenas o pontos """
plt.plot(X1,X2,'ro')

#matrix_X1_X2 = matrix([X1,X2])

"""Calculando a soma dos valores que estão no mesmo quadrante"""
Q1 = 0
cont1 = 0
X1_array = []
X2_array = []
Y_Q1 = []
for n in range(100):
    if X1[n] >= 5  and  X1[n] <= 10 and X2[n]>=5 and X2[n]<=10:
        cont1 = cont1 + 1
        Q1 = X1[n] + X2[n] + Q1
        X1_array.append(X1[n])
        X2_array.append(X2[n])
        Y_Q1.append(X1[n] + X2[n])
print("cont_Q1 " , cont1)
ax.bar(X2_array, Y_Q1 ,X1_array , zdir='y', color='b' , alpha=0.8)

Q2 = 0
cont2 = 0
X1_array = []
X2_array = []
Y_Q2 = []
for n in range(100):
    if X1[n] >= 0  and  X1[n] <= 5 and X2[n]>=5 and X2[n]<=10:
        cont2 = cont2 + 1
        Q2 = X1[n] + X2[n] + Q2
        X1_array.append(X1[n])
        X2_array.append(X2[n])
        Y_Q2.append(X1[n] + X2[n])
print("cont_Q2 " , cont2)
ax.bar(X2_array, Y_Q2 ,X1_array , zdir='y', color='g' , alpha=0.8)

Q3 = 0
cont3 = 0
X1_array = []
X2_array = []
Y_Q3 = []
for n in range(100):
    if X1[n] >= 0  and  X1[n] <= 5 and X2[n]>=0 and X2[n]<=5:
        cont3 = cont3 + 1
        print("X1_",X1[n])
        print("X2_",X2[n])
        Q3 = X1[n] + X2[n] + Q3
        X1_array.append(X1[n])
        X2_array.append(X2[n])
        Y_Q3.append(X1[n]+X2[n])
print("cont_Q3 " , cont3)
ax.bar(X2_array, Y_Q3 ,X1_array , zdir='y', color='r' , alpha=0.8)

Q4 = 0
cont4 = 0
X1_array = []
X2_array = []
Y_Q4 = []
for n in range(100):
    if X1[n] >= 5  and  X1[n] <= 10 and X2[n]>=0 and X2[n]<=5:
        cont4 = cont4 + 1
        Q4 = X1[n] + X2[n] + Q4
        X1_array.append(X1[n])
        X2_array.append(X2[n])
        Y_Q4.append(X1[n] + X2[n])
print("cont_Q4 " , cont4)
ax.bar(X2_array, Y_Q4 ,X1_array , zdir='y', color='y' , alpha=0.8)
            
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Y')

plt.show()
            

