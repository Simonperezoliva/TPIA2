import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *

def calcularKMeans():
    k = int(km_field.get())
    # Se lee el dataset
    data = pd.DataFrame()
    data = pd.read_csv('dataset_1.csv', sep= ';', decimal=",") #sep es para indicar mediante qué se separa cada registro del dataset. En este caso se usa ;
    data = data.assign(esCentroide=0)
    print(data)
    centroides = np.array(data.sample(n = k)) #se eligen k centroides aleatorios
    print(centroides)
    df_centroides = pd.DataFrame(centroides)
    #se grafica el dataset
    data.plot(kind = 'scatter', x = 'X', y = 'Y')
    plt.scatter(df_centroides[0], df_centroides[1], c= 'red', s=50)
    plt.title('Algoritmo K-Means')
    plt.show()

#HASTA ACA ANDA

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
