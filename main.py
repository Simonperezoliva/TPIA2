import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from tkinter import *

def calcularKMeans():
    k = int(km_field.get())
    clases = np.array(k)

    # Se lee el dataset
    data = pd.DataFrame()
    data = pd.read_csv('dataset_1.csv', sep= ';', decimal=",") #sep es para indicar mediante qué se separa cada registro del dataset. En este caso se usa ;
    data = data.assign(esCentroide=0) #se agrega columna esCentroide para verificar qué puntos iniciales van ser elegidos como centroides en la primera iteración
    data = data.assign(distancia='NaN') #se agregan columna distancia para verificar la distancia de un punto a su centroide
    print(data)
    
    centroides = np.array(data.sample(n = k)) #se inicializan los k centroides aleatorios
    print(centroides)
    df_centroides = pd.DataFrame(centroides)
    ''''
    for i in range(len(data)): #se calcula la distancia de cada data point a cada centroide
        distancia = np.array([])
        distancia = np.append(distancia, math.sqrt((df_centroides.iloc[0]['X'] - data.iloc[i]['X']) + (df_centroides.iloc[1]['X'] - data.iloc[i]['X']) + (df_centroides.iloc[2]['X'] - data.iloc[i]['X'])))
    '''
    errores = np.array([]) #array con distancias de cada centroide a los puntos
    for centroide in range(df_centroides.shape[0]):
        error = calcularError(df_centroides.iloc[centroide, :2], data.iloc[0,:2])
        errores = np.append(errores, error)
    print(errores)

    #se grafica el dataset
    data.plot(kind = 'scatter', x = 'X', y = 'Y')
    plt.scatter(df_centroides[0], df_centroides[1], c= 'red', s=50)
    plt.title('Algoritmo K-Means')
    plt.show()

#HASTA ACA ANDA

def calcularError(a,b):
    '''
    Given two Numpy Arrays, calculates the root of the sum of squared errores.
    '''
    error = np.square(np.sum((a-b)**2))

    return error    

if __name__=='__main__':
    new = Tk()
    new.resizable(0, 0)
    new.config(background='grey')
    new.title("Algoritmo K-Means")
    new.geometry("300x150")
    km = Label(new, text="Ingresar Cantidad de Clusters",bg='grey',font=("times", 16, "bold"))
    km_field = Entry(new)
    button = Button(new, text="Calcular k-Means",fg='Black',bg='Blue',font=("times", 10, "bold"), command=calcularKMeans)
    #adjusting widgets in position
    km.grid(row=1, column=0)
    km_field.grid(row=2, column=0)
    button.grid(row=3, column=0)
    new.mainloop()
