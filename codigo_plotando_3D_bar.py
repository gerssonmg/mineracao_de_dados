# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 00:20:44 2018

@author: Gerson
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xs = [7,6]
ys = [0.9 , 8.7]
zs = 10
ax.bar(xs , ys , zs , zdir='y', color='b', alpha=1)

xs = [6 , 8]
ys = [0.7 , 0.6]
zs = 9
ax.bar(xs , ys , zs , zdir='y', color='b', alpha=1)

xs = [5 , 3]
ys = [0.6 , 0.5]
zs = 8
ax.bar(xs , ys , zs , zdir='y', color='b', alpha=1)


ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Y')


plt.show()