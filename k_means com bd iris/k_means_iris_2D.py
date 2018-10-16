# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:40:21 2018

@author: Gerson
"""

"""
Exemplo de iniciar:
    1- Compilar
    2- print_centroides()
    3- plot_agrupamento_dados()
    4- plot_all()
"""

import pandas as pd
from numpy import matrix
import numpy as np
from sklearn.cluster import KMeans
from scipy import spatial
import matplotlib.pyplot as plt


iris = pd.read_csv("iris_2D.csv")
iris.head()

X = iris.iloc[:, 0:2].values

"""
PLOTANDO TODOS OS PONTOS
"""
plt.figure()
plt.plot(X[:,0],X[:,1],'ro',color='b')


"""
Inicializando kmeans
Definindo o numero de clusters
Definindo qual algoritmo usar no caso random
"""
K = 5

kmeans = KMeans(n_clusters = K, init = 'random')

"""
O método fit() recebe como
 parâmetro os dados a serem
 agrupados, nesse caso será
 a variável X que declaramos
 anteriormente
"""
kmeans.fit(X)


"""
Neste momento já temos
os dados agrupados e
vamos verificar os 
centroides gerados 
através do atributo 
cluster_centers_
"""

print("kmeans3 = " , kmeans.cluster_centers_)


def print_centroides():
    plt.plot(kmeans.cluster_centers_[0][0],
                 kmeans.cluster_centers_[0][1],'ro',color='r')
    
    plt.plot(kmeans.cluster_centers_[1][0],
                 kmeans.cluster_centers_[1][1],'ro',color='m')
    
    plt.plot(kmeans.cluster_centers_[2][0],
                 kmeans.cluster_centers_[2][1],'ro',color='y')
    
    plt.plot(kmeans.cluster_centers_[3][0],
                 kmeans.cluster_centers_[3][1],'ro',color='g')
    
    plt.plot(kmeans.cluster_centers_[4][0],
                 kmeans.cluster_centers_[4][1],'ro',color='k')


def plot_agrupamento_dados():
    
    for i in range(X.size):
        array_a = np.array([X[i][0],X[i][1]])
        r = classifica(array_a)
        print_grupos(r , array_a)
        print("ARRAY = ",array_a)
        print("GRUPO = ",r)
        
def classifica_um_dado(array_b):
    #np.array(1,1)     
    r = classifica(array_b)
    print_grupos(r , array_b)
        
def print_grupos(grupo , array_a):
    if grupo == 0:
        plt.plot(array_a[0],array_a[1],'ro',color='r')
    
    elif grupo == 1:
        plt.plot(array_a[0],array_a[1],'ro',color='m')
    
    elif grupo == 2:
        plt.plot(array_a[0],array_a[1],'ro',color='y')
    
    elif grupo == 3:
        plt.plot(array_a[0],array_a[1],'ro',color='g')
    
    elif grupo == 4:
        plt.plot(array_a[0],array_a[1],'ro',color='k')
        


def classifica(a):
    
    aux = 0
    similaridade = 1000000
    grupo = -1
    for i in range(kmeans.n_clusters):
        #print ("i=",i,"k=",kmeans.cluster_centers_[i]) 
        #print("SIMILARIDADE = ", spatial.distance.euclidean(  a, kmeans.cluster_centers_[i]))
        if spatial.distance.euclidean(  a, kmeans.cluster_centers_[i]) < similaridade:
            
            similaridade = spatial.distance.euclidean(  a, kmeans.cluster_centers_[i])
            grupo = i
        
    return grupo


def plot_all():
    for i in range(40,80):
        for j in range(20,45):
            
            #array_a = np.array([j/10,i/10])
            array_a = np.array([i/10,j/10])
            classifica_um_dado(array_a)
            
           
            plt.pause(0.000001)
            plt.show()

"""
Codigos A baixo, apenas para testes
"""

def ComputeDistance_classifica(a, b):
    aux = 0
    similaridade = 1000000
    grupo = -1
    for i in range(kmeans.n_clusters):
        print ("i=",i,"k=",kmeans.cluster_centers_[i]) 
        print("SIMILARIDADE = ", spatial.distance.euclidean(  kmeans.cluster_centers_[aux], kmeans.cluster_centers_[i]))
        if spatial.distance.euclidean(  kmeans.cluster_centers_[aux], kmeans.cluster_centers_[i]) < similaridade:
            
            similaridade = spatial.distance.euclidean(  kmeans.cluster_centers_[aux], kmeans.cluster_centers_[i])
            grupo = i  

    return grupo

def teste():
    result = ComputeDistance_classifica(1,1)


    if result == 0:
        plt.plot(kmeans.cluster_centers_[result][0],
                 kmeans.cluster_centers_[result][1],'ro',color='r')

    print("RESULT =",result)

