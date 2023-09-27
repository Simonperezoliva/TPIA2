import sys
import csv
import math
import random
import matplotlib.pyplot as plt
from ventana3 import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QGridLayout,QLineEdit,QPushButton, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
from math import sqrt,pow

class dataPoint:
    def __init__(self,valorX, valorY, punto, cantidadCentroide,cantidadX,cantidadY,centroide):
        self.valorX = valorX
        self.valorY = valorY
        self.punto = punto
        self.cantidadCentroide = cantidadCentroide
        self.cantidadX = cantidadX
        self.cantidadY = cantidadY
        self.centroide = centroide

class distCentroide:
    def __init__(self,distancia, punto):
        self.distancia = distancia
        self.punto=punto

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyQt File Dialog')
        self.setGeometry(100, 100, 400, 100)

        layout = QGridLayout()
        self.setLayout(layout)

        # file selection
        file_browse = QPushButton('Browse')
        file_browse.clicked.connect(self.open_file_dialog)
        self.filename_edit = QLineEdit()

        layout.addWidget(QLabel('File:'), 0, 0)
        layout.addWidget(self.filename_edit, 0, 1)
        layout.addWidget(file_browse, 0 ,2)

      
        self.show()


class interfazGUIa(QtWidgets.QWidget):
    cantidadKs=2
    rutaArchivo=" "
    def __init__(self, parent=None):    
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.botonBuscarArchivo.clicked.connect(self.open_file_dialog)
        self.ui.botonAleatorio.clicked.connect(self.aleatorio)
        self.ui.botonHeuristica.clicked.connect(self.heuristica)
        self.ui.kSlider.valueChanged.connect(self.update)
    
    def update(self):
        self.ui.valoresK.setText(f'Valor actual: {self.ui.kSlider.value()}')
    
    def open_file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File", 
            "D:\\icons\\avatar\\", 
            "Files (*.csv)"
        )
        
        if filename:
            path = Path(filename)
            self.ui.archivoBuscado.setText(str(path))
            
            print("path:",path)
            
            self.rutaArchivo = path
            

    def aleatorio(self):
        listaPuntos=[]
        if self.rutaArchivo!=" ":
            with open(self.rutaArchivo, "r") as archivo:
                lector = csv.reader(archivo, delimiter=";")
                cantidad=1
                # Omitir el encabezado
                next(lector, None)
                for fila in lector:
                    # Tenemos la lista. En la 0 tenemos el nombre, en la 1 la calificación y en la 2 el precio
                    datoX = float(fila[0].replace(",","."))
                    datoY = float(fila[1].replace(",","."))
                    punto=dataPoint(datoX,datoY,cantidad,0,0,0,0)
                    listaPuntos.append(punto)
                    cantidad+=1
                cantidad-=1
                
                listaCentroides=[]
        
                cantidadK=self.ui.kSlider.value()
                numsAux=[]
                while len(listaCentroides)<cantidadK:
                
                    numRandom=random.randint(1,cantidad)
                    bandera=0
                    for k in numsAux:
                        if numRandom==k:
                            bandera=1
                    
                    if bandera==0:
                        for j in listaPuntos:
                            if j.punto==numRandom:
                                centroideCreado=dataPoint(j.valorX,j.valorY,j.punto,0,0,0,0)
                                listaCentroides.append(centroideCreado)
                                listaPuntos.remove(j)
                    
                
                print("Seteo de centroides")
                for j in listaCentroides:  
                    print(j.valorX," ",j.valorY,"  ", j.punto," ")

                bandera1=True
                bandera2=True
                listaCentroidesActu=[]
                listaCentroidesAux=[]
                listaDistancias=[]
                while bandera1==True and bandera2==True:
                    bandera1=False
                    bandera2=False
                    listaCentroidesAux.clear()
                    listaCentroidesAux.extend(listaCentroides.copy())
                    
                    print("lista de PUNTOS INICIO")
                    for j in listaPuntos:
                        print(j.valorX,"\t",j.valorY,"\t", j.punto,"\t",j.centroide)

                    for j in listaPuntos:
                        listaDistancias.clear()
                        """ Asignacion de distancias a centroides """
                        for k in listaCentroides:
                            resta1=j.valorX-k.valorX
                            resta2=j.valorY-k.valorY
                            valor1= math.sqrt(math.pow(resta1,2)+math.pow(resta2,2))
                            objeto=distCentroide(valor1,k.punto)
                            listaDistancias.append(objeto)
                        
                        """ Obtencion de la menor distancia """
                        menorDistancia=listaDistancias.__getitem__(0)
                        for k in listaDistancias:
                            if menorDistancia.distancia>k.distancia:
                                menorDistancia=k
                        
                        if j.centroide!=menorDistancia.punto:
                            bandera1=True
                            j.centroide=menorDistancia.punto
                        
                        
                        for k in listaCentroides:
                            if k.punto == menorDistancia.punto:
                                centroideActu=k
                        
                        listaCentroides.remove(centroideActu)
                        cantidadCentroide2=centroideActu.cantidadCentroide+1
                        cantidadX2=centroideActu.cantidadX+j.valorX
                        cantidadY2=centroideActu.cantidadY+j.valorY
                        valorX2=centroideActu.valorX
                        valorY2=centroideActu.valorY
                        punto2=centroideActu.punto
                        listaCentroides.append(dataPoint(valorX2,valorY2,punto2,cantidadCentroide2,cantidadX2,cantidadY2,0))
                    
                    print("lista de centroides sin actu 1")
                    for j in listaCentroidesAux:
                        print(j.valorX," ",j.valorY,"  ", j.punto," ")
                    listaCentroidesActu.clear()
                    
                    print("lista de PUNTOS ")
                    for j in listaPuntos:
                        print(j.valorX,"\t",j.valorY,"\t", j.punto,"\t",j.centroide)
                    listaCentroidesActu.clear()

                    for j in listaCentroides:
                        if(j.cantidadCentroide!=0):
                            mediaX=j.cantidadX/j.cantidadCentroide
                            mediaY=j.cantidadY/j.cantidadCentroide
                            punto1=j.punto
                            cantidadCentroide1=0
                            cantidadX1=0
                            cantidadY1=0
                            centroide1=0
                            listaCentroidesActu.append(dataPoint(mediaX,mediaY,punto1,cantidadCentroide1,cantidadX1,cantidadY1,centroide1))
                        else:
                            mediaX=j.valorX
                            mediaY=j.valorY
                            punto1=j.punto
                            cantidadCentroide1=0
                            cantidadX1=0
                            cantidadY1=0
                            centroide1=0
                            listaCentroidesActu.append(dataPoint(mediaX,mediaY,punto1,cantidadCentroide1,cantidadX1,cantidadY1,centroide1))

                    print("lista de centroides sin actu 2")
                    for j in listaCentroidesAux:
                        print(j.valorX," ",j.valorY,"  ", j.punto," ")
                    
                    
                    print("lista de centroides actulizado")
                    for j in listaCentroidesActu:
                        print(j.valorX," ",j.valorY,"  ", j.punto," ")
                    for j in listaCentroidesAux:
                        for k in listaCentroidesActu:
                            if j.punto==k.punto:
                                if j.valorX!=k.valorX or j.valorY!=k.valorY:
                                    bandera2=True

                    listaCentroides.clear()
                    listaCentroides.extend(listaCentroidesActu.copy())
                    print(bandera1,bandera2)
                    print("Actualizacion de Centroides")
                    for j in listaCentroides:
                        print(j.valorX," ",j.valorY,"  ", j.punto," ")
                
                print("********FINALLLLL*******")
                
                colores=["red","blue","#00FF40","#D7DF01","#FF8000","#00FFFF"]
                contador=0
                listaPuntosGraficaX=[]
                listaPuntosGraficaY=[]
                listaColores=[]
                for j in listaCentroides:
                    for k in listaPuntos:
                        if j.punto==k.centroide:
                            listaPuntosGraficaX.append(k.valorX)
                            listaPuntosGraficaY.append(k.valorY)
                            listaColores.append(colores[contador])
                    listaPuntosGraficaX.append(j.valorX)
                    listaPuntosGraficaY.append(j.valorY)
                    listaColores.append("#FE2EF7")
                    contador+=1

                print("long X:",len(listaPuntosGraficaX))
                print("long Y:",len(listaPuntosGraficaY))
                print("long colores:",len(listaColores))
                plt.scatter(listaPuntosGraficaX,listaPuntosGraficaY,color=listaColores)
                """ plt.xlabel("Eje X")
                plt.ylabel("Eje Y")
                plt.title("grafico") """
                plt.show()

    def heuristica(self):
        listaPuntos=[]
        listaPuntosMedia=[]
        listaCentroides=[]
        if self.rutaArchivo!=" ":
            with open(self.rutaArchivo, "r") as archivo:
                lector = csv.reader(archivo, delimiter=";")
                cantidad=1
                # Omitir el encabezado
                next(lector, None)
                for fila in lector:
                    # Tenemos la lista. En la 0 tenemos el nombre, en la 1 la calificación y en la 2 el precio
                    datoX = float(fila[0].replace(",","."))
                    datoY = float(fila[1].replace(",","."))
                    punto=dataPoint(datoX,datoY,cantidad,0,0,0,0)
                    listaPuntos.append(punto)
                    cantidad+=1
                cantidad-=1
                
                listaCentroides.clear()
        
                cantidadK=self.ui.kSlider.value()
                numsAux=[]



                mediaXTotal=0
                mediaYTotal=0
                cantidadPuntosTotal=0
                for j in listaPuntos:
                    mediaXTotal+=j.valorX
                    mediaYTotal+=j.valorY
                    cantidadPuntosTotal+=1

                mediaXTotal=mediaXTotal/cantidadPuntosTotal
                mediaYTotal=mediaYTotal/cantidadPuntosTotal
                listaPuntosMedia.clear()
                listaPuntosMedia.append(dataPoint(mediaXTotal,mediaYTotal,0,0,0,0,0))
                
                bandera3=0
                contador=0
                
                while len(listaCentroides)<cantidadK:
                    mayorDistancia=0
                    posLista=-1
                    for k in listaPuntos:
                        posLista+=1
                        contador+=1
                        distanciaTotal=0
                        for j in listaPuntosMedia:
                            resta1=k.valorX-j.valorX
                            resta2=k.valorY-j.valorY
                            distanciaPunto=math.sqrt(math.pow(resta1,2)+math.pow(resta2,2))
                            distanciaTotal+=distanciaPunto
                        if mayorDistancia<distanciaTotal:
                            mayorDistancia=distanciaTotal
                            puntoMayor=dataPoint(k.valorX,k.valorY,k.punto,0,0,0,0)
                            puntoMayorSacar=posLista
                    
                    if bandera3==0 and contador==cantidadPuntosTotal:
                        listaPuntosMedia.clear()
                        bandera3=1

                    listaPuntosMedia.append(puntoMayor)
                    listaCentroides.append(puntoMayor)
                    listaPuntos.pop(puntoMayorSacar)
                    cantidadPuntosTotal-=1


                    
                
                print("Seteo de centroides")
                for j in listaCentroides:  
                    print(j.valorX," ",j.valorY,"  ", j.punto," ")
                
                bandera1=True
                bandera2=True
                listaCentroidesActu=[]
                listaCentroidesAux=[]
                listaDistancias=[]
                while bandera1==True and bandera2==True:
                    bandera1=False
                    bandera2=False
                    listaCentroidesAux.clear()
                    listaCentroidesAux.extend(listaCentroides.copy())
                    
                    print("lista de PUNTOS INICIO")
                    for j in listaPuntos:
                        print(j.valorX,"\t",j.valorY,"\t", j.punto,"\t",j.centroide)

                    for j in listaPuntos:
                        listaDistancias.clear()
                        """ Asignacion de distancias a centroides """
                        for k in listaCentroides:
                            resta1=j.valorX-k.valorX
                            resta2=j.valorY-k.valorY
                            valor1= math.sqrt(math.pow(resta1,2)+math.pow(resta2,2))
                            objeto=distCentroide(valor1,k.punto)
                            listaDistancias.append(objeto)
                        
                        """ Obtencion de la menor distancia """
                        menorDistancia=listaDistancias.__getitem__(0)
                        for k in listaDistancias:
                            if menorDistancia.distancia>k.distancia:
                                menorDistancia=k
                        
                        if j.centroide!=menorDistancia.punto:
                            bandera1=True
                            j.centroide=menorDistancia.punto
                        
                        
                        for k in listaCentroides:
                            if k.punto == menorDistancia.punto:
                                centroideActu=k
                        
                        listaCentroides.remove(centroideActu)
                        cantidadCentroide2=centroideActu.cantidadCentroide+1
                        cantidadX2=centroideActu.cantidadX+j.valorX
                        cantidadY2=centroideActu.cantidadY+j.valorY
                        valorX2=centroideActu.valorX
                        valorY2=centroideActu.valorY
                        punto2=centroideActu.punto
                        listaCentroides.append(dataPoint(valorX2,valorY2,punto2,cantidadCentroide2,cantidadX2,cantidadY2,0))
                    
                    print("lista de centroides sin actu 1")
                    for j in listaCentroidesAux:
                        print(j.valorX," ",j.valorY,"  ", j.punto," ")
                    listaCentroidesActu.clear()
                    
                    print("lista de PUNTOS ")
                    for j in listaPuntos:
                        print(j.valorX,"\t",j.valorY,"\t", j.punto,"\t",j.centroide)
                    listaCentroidesActu.clear()

                    for j in listaCentroides:
                        if(j.cantidadCentroide!=0):
                            mediaX=j.cantidadX/j.cantidadCentroide
                            mediaY=j.cantidadY/j.cantidadCentroide
                            punto1=j.punto
                            cantidadCentroide1=0
                            cantidadX1=0
                            cantidadY1=0
                            centroide1=0
                            listaCentroidesActu.append(dataPoint(mediaX,mediaY,punto1,cantidadCentroide1,cantidadX1,cantidadY1,centroide1))
                        else:
                            mediaX=j.valorX
                            mediaY=j.valorY
                            punto1=j.punto
                            cantidadCentroide1=0
                            cantidadX1=0
                            cantidadY1=0
                            centroide1=0
                            listaCentroidesActu.append(dataPoint(mediaX,mediaY,punto1,cantidadCentroide1,cantidadX1,cantidadY1,centroide1))

                    print("lista de centroides sin actu 2")
                    for j in listaCentroidesAux:
                        print(j.valorX," ",j.valorY,"  ", j.punto," ")
                    
                    
                    print("lista de centroides actulizado")
                    for j in listaCentroidesActu:
                        print(j.valorX," ",j.valorY,"  ", j.punto," ")
                    for j in listaCentroidesAux:
                        for k in listaCentroidesActu:
                            if j.punto==k.punto:
                                if j.valorX!=k.valorX or j.valorY!=k.valorY:
                                    bandera2=True

                    listaCentroides.clear()
                    listaCentroides.extend(listaCentroidesActu.copy())
                    print(bandera1,bandera2)
                    print("Actualizacion de Centroides")
                    for j in listaCentroides:
                        print(j.valorX," ",j.valorY,"  ", j.punto," ")
                
                print("********FINALLLLL*******")
                
                colores=["red","blue","#00FF40","#D7DF01","#FF8000","#00FFFF"]
                contador=0
                listaPuntosGraficaX=[]
                listaPuntosGraficaY=[]
                listaColores=[]
                for j in listaCentroides:
                    for k in listaPuntos:
                        if j.punto==k.centroide:
                            listaPuntosGraficaX.append(k.valorX)
                            listaPuntosGraficaY.append(k.valorY)
                            listaColores.append(colores[contador])
                    listaPuntosGraficaX.append(j.valorX)
                    listaPuntosGraficaY.append(j.valorY)
                    listaColores.append("#FE2EF7")
                    contador+=1

                print("long X:",len(listaPuntosGraficaX))
                print("long Y:",len(listaPuntosGraficaY))
                print("long colores:",len(listaColores))
                plt.scatter(listaPuntosGraficaX,listaPuntosGraficaY,color=listaColores)
                """ plt.xlabel("Eje X")
                plt.ylabel("Eje Y")
                plt.title("grafico") """
                plt.show()



                



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mi_app = interfazGUIa()
    mi_app.show()
    """ window = MainWindow() """
    sys.exit(app.exec())