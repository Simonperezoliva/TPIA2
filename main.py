import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button #widget para agregar botones a la gráfica de matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import math
from tkinter import *
from tkinter import filedialog

def calcularKMeans():
    k = int(km_field.get())
    #clases = np.array(k)
    

    # Se lee el dataset
    data = pd.DataFrame()
    data = pd.read_csv('dataset_1.csv', sep= ';', decimal=",") #sep es para indicar mediante qué se separa cada registro del dataset. En este caso se usa ;
    data = data.assign(centroide='NaN') #se agrega columna centroide para verificar a qué centroide pertenece cada punto
    centroides = np.array(data.sample(n = k)) #se inicializan los k centroides aleatorios
    print(centroides)
    df_centroides = pd.DataFrame(centroides)
    graficarData(data, df_centroides)
    
    for i in range(len(data)): #se calcula la distancia de cada data point a cada centroide
        distancia = np.array([])
        distancia = np.append(distancia, math.sqrt(math.pow((df_centroides.iloc[0]['X'] - data.iloc[i]['X']),2) + math.pow((df_centroides.iloc[1]['X'] - data.iloc[i]['X']),2) + math.pow((df_centroides.iloc[2]['X'] - data.iloc[i]['X']),2)))
    
    errores = np.array([]) #array con distancias de cada centroide a los puntos
    for centroide in range(len(df_centroides[0])):
        error = calcularError(df_centroides.iloc[centroide, :2], data.iloc[0,:2])
        errores = np.append(errores, error)
    print(errores)
    

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
    #HASTA ACA ANDA



def calcularError(a,b):
    
    #Given two Numpy Arrays, calculates the root of the sum of squared errores.
    
    error = np.square(np.sum((a-b)**2))

    return error    

def buscarDataset():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("CSV Files", "*.csv*")))
    



if __name__=='__main__':
    new = Tk()
    new.resizable(0, 0)
    new.config(background='grey')
    new.title("Algoritmo K-Means")
    new.geometry("400x200")
    km = Label(new, text="Ingresar Cantidad de Clusters",bg='grey',font=("times", 16, "bold"))
    km_field = Entry(new)
    button = Button(new, text="Mostrar Dataset",fg='Black',bg='Blue',font=("times", 10, "bold"), command=calcularKMeans)
    button2 = Button(new, text="Calcular K-Means",fg='Black',bg='Green',font=("times", 10, "bold"), command=calcularKMeans)
    button_explorar = Button(new, text = "Buscar en Archivos", command = buscarDataset)
    #adjusting widgets in position
    km.grid(row=1, column=0)
    km_field.grid(row=2, column=0)
    button.grid(row=3, column=0)
    button2.grid(row=4, column=0)
    button_explorar.grid(row = 2, column = 1)
    new.mainloop()
