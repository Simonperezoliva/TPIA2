import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import math
from tkinter import *
from tkinter.filedialog import askopenfilename

def calcularKMeans():
    k = int(kmField.get())
    if k > 1  and k < 6:
        # Se lee el dataset
        data = pd.DataFrame()
        data = pd.read_csv(v.get(), sep= ';', decimal=",") #sep es para indicar mediante qué se separa cada registro del dataset. En este caso se usa ;
        data = data.assign(centroide='NaN') #se agrega columna centroide para verificar a qué centroide pertenece cada punto
        centroides = np.array(data.sample(n = k)) #se inicializan los k centroides aleatorios
        print(centroides)
        df_centroides = pd.DataFrame(centroides)
        graficarData(data, df_centroides)
    else:
        errorClusters()

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
    plt.title('Dataset sin Aplicar K-Means')
    plt.show()

def errorClusters():
    new2 = Tk()
    new2.resizable(0, 0)
    new2.config(background='grey')
    new2.title("Error de Clusters")
    new2.geometry("300x150")
    error1 = Label(new2, text="Error:",bg='grey',font=("times", 18, "bold"),justify='center')
    error2 = Label(new2, text="Cantidad de Clusters no Válida.\nIngrese entre 2 y 5 Clusters",bg='grey',font=("times", 14, "bold"),justify='center')
    error1.place(x=120, y=25)
    error2.place(x=25, y=75)


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

    #se ajustan los widgets en su posición 
    lbDataset.place(x=20, y=50)
    entryDataset.place(x=65,y=90, width=225,height=25)
    buttonImportar.place(x=110,y=130, height=50)
    km.place(x=450, y=50)
    kmField.place(x=525,y=90, width=150, height=25)
    buttonCalcularKMeansA.place(x=460,y=130,width=150, height=50)
    buttonCalcularKMeansH.place(x=650,y=130,width=150, height=50)
    buttonCerrar.place(x=350,y=260, width=100, height=50)
    new.mainloop()