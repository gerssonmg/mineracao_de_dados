# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:57:44 2018

@author: Gerson
"""

from numpy import matrix
import matplotlib.pyplot as plt


X = matrix([[1.1,1],
            [1.3,1],
            [1.5,1],
            [2.0,1],
            [2.2,1],
            [2.9,1],
            [3.0,1],
            [3.2,1],
            [3.7,1],
            [3.9,1],
            [4.0,1],
            [4.0,1],
            [4.1,1]
        ])

Y = matrix([[39343],
            [46205],
            [37731],
            [43525],
            [39891],
            [56642],
            [60150],
            [54445],
            [57189],
            [63218],
            [55794],
            [56957],
            [57081]
        ])

plt.plot(X[1::],Y[1::],'ro')

def calc(a , x , b):
    return a * x + b

theta = (X.T*X).I*X.T*Y
print("a = ", theta[1])
print("b = ", theta[0])

print(calc(theta[1] , 1.1 ,theta[0] ))





