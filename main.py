import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib.widgets import Button #widget para agregar botones a la gráfica de matplotlib
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
#from matplotlib.figure import Figure
#import math
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import ttk
import os

def calcularKMeans():
    k = int(kmField.get())
    #clases = np.array(k)

    # Se lee el dataset
    data = pd.DataFrame()
    data = pd.read_csv(v.get(), sep= ';', decimal=",") #sep es para indicar mediante qué se separa cada registro del dataset. En este caso se usa ;
    data = data.assign(centroide='NaN') #se agrega columna centroide para verificar a qué centroide pertenece cada punto
    centroides = np.array(data.sample(n = k)) #se inicializan los k centroides aleatorios
    print(centroides)
    df_centroides = pd.DataFrame(centroides)
    graficarData(data, df_centroides)

    #EN EL CORE SE DEBERÍA HACER UNA ITERACIÓN Y ESPERAR EL EVENT DEL BOTON DE AVANZAR UNA ITERACIÓN
    #EN CASO DEL BOTÓN AVANZAR HASTA EL FINAL, EJECUTAR TODO EL ALGORITMO Y RECIÉN AHÍ MOSTRAR
    #DENTRO DE CADA ITERACIÓN ACTUALIZAR LA POSICIÓN DE LOS CENTROIDES (LISTA DE CENTROIDES) Y LA COLUMNA DE LOS CLUSTERS A LOS QUE PERTENECE CADA DATO

def graficarData(data, df_centroides):  
    #se grafica el dataset
    plt.ion() #indica que los graficos son interactivos. Es decir, no se debe especificar un plot.show() para mostrarse
    data.plot(kind = 'scatter', x = 'X', y = 'Y')
    plt.scatter(df_centroides[0], df_centroides[1], c= 'red', s=50)
    plt.subplots_adjust(bottom=0.2)
    plt.title('Algoritmo K-Means')
    plt.show()

def importarDataset():
    global v
    csv_file_path = askopenfilename(filetypes= (('CSV files', '*.csv'), ('all files', '*.all')))
    v.set(csv_file_path)
    df = pd.read_csv(csv_file_path, sep= ';', decimal=",")
    df.plot(kind='scatter', x= 'X', y= 'Y')
    plt.title('Dataset')
    plt.show()


if __name__=='__main__':
    new = Tk()
    new.resizable(0, 0)
    new.config(background='grey')
    new.title("TP Inteligencia Artificial II - Algoritmo K-Means")
    new.geometry("850x400")

    km = Label(new, text="Ingrese la Cantidad de Clusters",bg='grey',font=("times", 18, "bold"),justify='center')
    kmField = Entry(new)
    buttonCalcularKMeansA = Button(new, text="Calcular K-Means\n Aleatorio",fg='White',bg='#001A33',font=("times", 12, "bold"), command=calcularKMeans)
    buttonCalcularKMeansH = Button(new, text="Calcular K-Means\n Heurístico",fg='White',bg='#001A33',font=("times", 12, "bold"), command=calcularKMeans)
    lbDataset = Label(new, text='Seleccione el Dataset a Utilizar',bg='grey',font=("times", 18, "bold"),justify='center')
    v = StringVar()
    entryDataset = Entry(new, textvariable=v)
    buttonImportar = Button(new, text='Buscar Dataset \n y Mostrar',fg='White',bg='#001A33', font=("times", 12, "bold"), justify='center', command=importarDataset)
    buttonCerrar = Button(new, text='Cerrar', fg='White',bg='#2F2F2F', font=("times", 12, "bold"), command=new.destroy)

    #adjusting widgets in position
    lbDataset.place(x=20, y=50)
    entryDataset.place(x=65,y=90, width=225,height=25)
    buttonImportar.place(x=110,y=130, height=50)
    km.place(x=450, y=50)
    kmField.place(x=525,y=90, width=150, height=25)
    buttonCalcularKMeansA.place(x=460,y=130,width=150, height=50)
    buttonCalcularKMeansH.place(x=650,y=130,width=150, height=50)
    buttonCerrar.place(x=350,y=260, width=100, height=50)
    new.mainloop()