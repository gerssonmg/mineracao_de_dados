# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 18:02:37 2018

@author: Gerson
"""

from numpy import matrix
import matplotlib.pyplot as plt
from random import randint

#n = 0
#for n in range(10):
#    n = n + 1
#    plt.plot(n , n+1 , 'ro')

#for n in range(1000):
#    plt.plot(randint(0,500), randint(0,500),'ro')    
#    plt.axis(0,100,0,100)
    
X = []
Y = []
for it_iteretor in range(1000):
    X.append(randint(0,500))
    Y.append(randint(0,500))
    
X_line_vertical = [0,0]#,200,300,400,500,600]
Y_line_vertical = [0,500]#,200,300,400,500,600]

plt.plot(X,Y,'ro')
for cont in range(18):
    plt.plot([cont * 30,cont * 30],Y_line_vertical,color='b') 


X_line_horizontal = [0,500]#,200,300,400,500,600]
Y_line_horizontal = [0,0]#,200,300,400,500,600]

plt.plot(X,Y,'ro')
for cont in range(18):
    plt.plot(X_line_horizontal,[cont * 30,cont * 30],color='b') 
     
    
plt.axis([0,510,0,510])
plt.title('Grafico de Pontos', fontsize=12)
plt.xlabel('Eixo X1', fontsize=11)
plt.ylabel('Eixo X2', fontsize=11)
plt.show()
    
