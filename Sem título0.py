# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 23:59:02 2018

@author: Gerson
"""

"""
========================================
Create 2D bar graphs in different planes
========================================

Demonstrates making a 3D plot which has 2D bar graphs projected onto
planes y=0, y=1, etc.
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for c, z in zip(['r', 'g', 'b', 'y'], [30, 20, 10, 0]): 

#Vai iterar onde
#c faz referencia ao primeiro conjunto []
#z faz referecnai ao segundo conjunto 

    
    xs = np.arange(20) 
#    Retorna um Array iniciando de 0 a 20
#    de 1 em 1 
    
    print("xs",xs)
    ys = np.random.rand(20)
    print("ys",ys)
    print("c" , c)
    print("z" , z)

    # You can provide either a single color or an array. To demonstrate this,
    # the first bar of each set will be colored cyan.
    cs = [c] * len(xs)
    print("cs",cs)
    cs[0] = 'c'
    print("c",cs[0])
    ax.bar(xs, 0.9, zs=z, zdir='y', color=cs, alpha=1)
    #(array.length = 20 , array.length = 20 , posicao "z" , direcao , cor , opacidade)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
