# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 11:53:46 2018

@author: Gerson
Calculando por Media dos vizinhos mais proximos
"""
"""
from random import *
print random()
print uniform(10,20)
print randint(100,1000)
print randrange(100,1000,2)
random() retorna um float x tal que 0 <= x < 1.

uniform(10,20) retorna um float x tal que 10 <= x < 20.

randint(100,1000) retorna um inteiro x tal que 100 <= x < 1000.

randrange(100,1000,2) retorna um inteiro x tal que 100 <= x < 1000 e x é par

"""
from numpy import matrix
from random import randint , uniform
from mpl_toolkits.mplot3d import Axes3D
from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np
import time
import csv
import pandas as pd

def plota_linhas_azuis():
    """Plotando as barras azuis horizontais"""
    X_line_horizontal = [0,9]
    for cont in range(4):
        plt.plot(X_line_horizontal,[cont * 3,cont * 3],color='b') 
        plt.pause(0.5)

    """Plotando as barras azuis horizontais"""
    y_line_vertical = [0,9]
    for cont in range(4):
        plt.plot([cont * 3,cont * 3],y_line_vertical,color='b') 
        plt.pause(0.5)

def treina_matrix(X1,X2):
    MATRIX_SOMA = [0,0,0,0,0,0,0,0,0,0]
    MATRIX_CONT = [0,0,0,0,0,0,0,0,0,0]

    for it_iterator in range(100):
        if X1_traning[it_iterator] < 3:
            if X2_traning[it_iterator] < 3:
                m = 1
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1 
            elif X2_traning[it_iterator] < 6:
                m = 2
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
            elif X2_traning[it_iterator] < 9:
                m = 3
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
    
        elif X1_traning[it_iterator] < 6:
            if X2_traning[it_iterator] < 3:
                m = 4
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
            
            elif X2_traning[it_iterator] < 6:
                m = 5
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
            
            elif X2_traning[it_iterator] < 9:
                m = 6
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
    
        elif X1_traning[it_iterator] < 9:
            if X2_traning[it_iterator] < 3:
                m = 7
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
            
            elif X2_traning[it_iterator] < 6:
                m = 8
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
            
            elif X2_traning[it_iterator] < 9:
                m = 9
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
         
    MATRIX_MEDIA = [0,0,0,0,0,0,0,0,0,0]
    for it_iterator in range(10):
        if MATRIX_CONT[it_iterator] != 0:
            MATRIX_MEDIA[it_iterator] = MATRIX_SOMA[it_iterator] / MATRIX_CONT[it_iterator]  
        
    return MATRIX_MEDIA
    

def testa_matrix(X1,X2):
    MATRIX_SOMA = [0,0,0,0,0,0,0,0,0,0]
    MATRIX_CONT = [0,0,0,0,0,0,0,0,0,0]

    for it_iterator in range(100):
        if X1_traning[it_iterator] < 3:
            if X2_traning[it_iterator] < 3:
                m = 1
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1 
            elif X2_traning[it_iterator] < 6:
                m = 2
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
            elif X2_traning[it_iterator] < 9:
                m = 3
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
    
        elif X1_traning[it_iterator] < 6:
            if X2_traning[it_iterator] < 3:
                m = 4
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
            
            elif X2_traning[it_iterator] < 6:
                m = 5
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
            
            elif X2_traning[it_iterator] < 9:
                m = 6
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
    
        elif X1_traning[it_iterator] < 9:
            if X2_traning[it_iterator] < 3:
                m = 7
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
            
            elif X2_traning[it_iterator] < 6:
                m = 8
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
            
            elif X2_traning[it_iterator] < 9:
                m = 9
                MATRIX_SOMA[m] = MATRIX_SOMA[m] + X1_traning[it_iterator] + X2_traning[it_iterator]
                MATRIX_CONT[m] = MATRIX_CONT[m] + 1
         
    MATRIX_MEDIA = [0,0,0,0,0,0,0,0,0,0]
    for it_iterator in range(10):
        if MATRIX_CONT[it_iterator] != 0:
            MATRIX_MEDIA[it_iterator] = MATRIX_SOMA[it_iterator] / MATRIX_CONT[it_iterator]  
        
    return MATRIX_MEDIA

def testa_X1_X2(X1,X2,MATRIX_MEDIA_LOCAL,ax,plt):
  

    for it_iterator in range(100):
        if X1 < 3:
            if X2 < 3:
                m = 1
                Ymedia = MATRIX_MEDIA_LOCAL[m] + MATRIX_MEDIA_LOCAL[2] + MATRIX_MEDIA_LOCAL[4]
                Ymedia = Ymedia/3
            elif X2 < 6:
                m = 2
                Ymedia = MATRIX_MEDIA_LOCAL[m] + MATRIX_MEDIA_LOCAL[1] + MATRIX_MEDIA_LOCAL[3] + MATRIX_MEDIA_LOCAL[5]
                Ymedia = Ymedia/4
                
            elif X2 < 9:
                m = 3
                Ymedia = MATRIX_MEDIA_LOCAL[m] + MATRIX_MEDIA_LOCAL[2] + MATRIX_MEDIA_LOCAL[6]
                Ymedia = Ymedia/3
                
        elif X1 < 6:
            if X2 < 3:
                m = 4
                Ymedia = MATRIX_MEDIA_LOCAL[m] + MATRIX_MEDIA_LOCAL[1] + MATRIX_MEDIA_LOCAL[5] + MATRIX_MEDIA_LOCAL[6]
                Ymedia = Ymedia/4
                
            elif X2 < 6:
                m = 5
                Ymedia = MATRIX_MEDIA_LOCAL[m] + MATRIX_MEDIA_LOCAL[4] + MATRIX_MEDIA_LOCAL[2] + MATRIX_MEDIA_LOCAL[6] + MATRIX_MEDIA_LOCAL[8]
                Ymedia = Ymedia/5
                
            elif X2 < 9:
                m = 6
                Ymedia = MATRIX_MEDIA_LOCAL[m] + MATRIX_MEDIA_LOCAL[3] + MATRIX_MEDIA_LOCAL[5] + MATRIX_MEDIA_LOCAL[9]
                Ymedia = Ymedia/4
                
        elif X1 < 9:
            if X2 < 3:
                m = 7
                Ymedia = MATRIX_MEDIA_LOCAL[m] + MATRIX_MEDIA_LOCAL[4] + MATRIX_MEDIA_LOCAL[8]
                Ymedia = Ymedia/3
                
            elif X2 < 6:
                m = 8
                Ymedia = MATRIX_MEDIA_LOCAL[m] + MATRIX_MEDIA_LOCAL[5] + MATRIX_MEDIA_LOCAL[7] + MATRIX_MEDIA_LOCAL[9]
                Ymedia = Ymedia/4
                
            elif X2 < 9:
                m = 9
                Ymedia = MATRIX_MEDIA_LOCAL[m] + MATRIX_MEDIA_LOCAL[6] + MATRIX_MEDIA_LOCAL[8]
                Ymedia = Ymedia/3
        
    plot_X1_X2_Ymedia(ax,X1,X2,Ymedia,m,plt)
    return Ymedia

def plot_X1_X2_Ymedia(ax , X1 , X2 , Y,m,plt):
    if m == 1:
        ax.bar([X2], [Y] , [X1] , zdir='y' , color='b' , alpha=0.8)
        plt.pause(0.05)
    elif m == 2:
        ax.bar([X2], [Y] , [X1] , zdir='y' , color='g' , alpha=0.5)
        plt.pause(0.05)
    elif m == 3:
        ax.bar([X2], [Y] , [X1] , zdir='y' , color='r' , alpha=0.8)
        plt.pause(0.05)    
    elif m == 4:
        ax.bar([X2], [Y] , [X1] , zdir='y' , color='c' , alpha=0.8)
        plt.pause(0.05)
    elif m == 5:
        ax.bar([X2], [Y] , [X1] , zdir='y' , color='m' , alpha=0.8)
        plt.pause(0.05)
    elif m == 6:
        ax.bar([X2], [Y] , [X1] , zdir='y' , color='y' , alpha=0.8)
        plt.pause(0.05)
    elif m == 7:
        ax.bar([X2], [Y] , [X1] , zdir='y' , color='k' , alpha=0.8)
        plt.pause(0.05)
    elif m == 8:
        ax.bar([X2], [Y] , [X1] , zdir='y' , color='g' , alpha=1)
        plt.pause(0.05)
    elif m == 9:
        ax.bar([X2], [Y] , [X1] , zdir='y' , color='r' , alpha=0.3)
        plt.pause(0.05)



def plot_pontos(X1,X2,plt):
    for it in range(100):
        x = X1_traning[it]
        y = X2_traning[it]
        plt.plot([x],[y],'ro') 
        plt.pause(0.05)  
    plt.show()

def convert_matrix_point_test(X1, X2, MATRIX_MEDIA_LOCAL , ax,plt):
    for it in range(len(X1)):
        testa_X1_X2(X1[it],X2[it],MATRIX_MEDIA_LOCAL,ax,plt)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X1_traning =[]
X2_traning =[]
X1_test = []
X2_test = []

#    
data_set = pd.read_csv('treino.csv')
X1_traning = data_set['X1']
X2_traning = data_set['X2']    

data_set_test = pd.read_csv('teste.csv')
X1_test = data_set_test['X1']
X2_test = data_set_test['X2']   


    #plt.show()

plt.title("Media dos Vizinhos mais Proximos")

#Plota os pontos    
plot_pontos(X1_traning, X2_traning, plt)

#PLota as linhas
plota_linhas_azuis()

#Matriz com a media de cada região
MATRIX_MEDIA = treina_matrix(X1_traning , X2_traning)

#Plota o quadrante de cada entrada
convert_matrix_point_test(X1_test, X2_test, MATRIX_MEDIA, ax, plt)





