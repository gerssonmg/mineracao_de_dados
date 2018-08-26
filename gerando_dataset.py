# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 18:04:22 2018

@author: Gerson
"""
# Pandas é usado para manipulação de dados 
import pandas as pd
from numpy import matrix
from random import randint , uniform
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import time

X1_traning =[]
X2_traning =[]
X1_test = []
X2_test = []

for it_iteretor in range (100):
    X1_traning.append(uniform(0,9))
    X2_traning.append(uniform(0,9))
   
for it_iteretor in range(50):    
    X1_test.append(uniform(0,9))
    X2_test.append(uniform(0,9))
    


raw_data_treino = {'X1': X1_traning[::1],
        'X2': X2_traning[::1]
        }

df_treino = pd.DataFrame(raw_data_treino, columns = ['X1', 'X2'])
df_treino.to_csv('treino.csv')

raw_data_teste = {'X1': X1_test[::1],
        'X2': X2_test[::1]
        }

df_teste = pd.DataFrame(raw_data_teste, columns = ['X1', 'X2'])
df_teste.to_csv('teste.csv')

data_set_test = pd.read_csv('teste.csv')
X1_test = data_set_test['X1']
X2_test = data_set_test['X2']  

# Leia os dados e exiba as primeiras 5 linhas 
#features = pd.read_csv ('e.csv') 
#features.head (5)
#
#print(features['X1'][::2])
#print(features['X2'])