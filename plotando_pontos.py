# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 18:02:37 2018

@author: Gerson
"""

from numpy import matrix
import matplotlib.pyplot as plt
from random import randint

 
X1 = []
X2 = []
for it_iteretor in range(100):
    X1.append(randint(0,10))
    X2.append(randint(0,10))
   
X_line_vertical = [0,0]#,200,300,400,500,600]
Y_line_vertical = [0,10]#,200,300,400,500,600]

plt.plot(X1,X2,'ro')

def calc(a , x , b):
    return a * x + b
for cont in range(2):
    plt.plot([cont * 5,cont * 5],Y_line_vertical,color='b') 


X_line_horizontal = [0,500]#,200,300,400,500,600]
Y_line_horizontal = [0,0]#,200,300,400,500,600]

for cont in range(2):
    plt.plot(X_line_horizontal,[cont * 5,cont * 5],color='b') 


Q1 = 0

cont1 = 0
for n in range(100):
    if X1[n] >= 5  and  X1[n] <= 10 and X2[n]>=5 and X2[n]<=10:
        cont1 = cont + 1
        Q1 = X1[n] + X2[n] + Q1
print("cont_Q1 " , cont1)

Q2 = 0
cont2 = 0
for n in range(100):
    if X1[n] >= 0  and  X1[n] <= 5 and X2[n]>=5 and X2[n]<=10:
        cont2 = cont2 + 1
        Q2 = X1[n] + X2[n] + Q2
print("cont_Q2 " , cont2)

Q3 = 0
cont3 = 0
for n in range(100):
    if X1[n] >= 0  and  X1[n] <= 5 and X2[n]>=0 and X2[n]<=5:
        cont3 = cont3 + 1
        Q3 = X1[n] + X2[n] + Q3
print("cont_Q3 " , cont3)

Q4 = 0
cont4 = 0
for n in range(100):
    if X1[n] >= 5  and  X1[n] <= 10 and X2[n]>=0 and X2[n]<=5:
        cont4 = cont4 + 1
        Q4 = X1[n] + X2[n] + Q4
print("cont_Q4 " , cont4)

            
            
print ("Q1med = " , Q1/cont1)
print ("Q2med = " , Q2/cont2)
print ("Q3med = " , Q3/cont3)
print ("Q4med = " , Q4/cont4)

plt.axis([0,10,0,10])
plt.title('Grafico de Pontos', fontsize=12)
plt.xlabel('Eixo X1', fontsize=11)
plt.ylabel('Eixo X2', fontsize=11)
plt.show()

