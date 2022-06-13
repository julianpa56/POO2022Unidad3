import csv
import numpy as np

from Flores import Flores

class ManejadorFlores:
    __arreFlores=None

    # variables arreglo numpy
    __cantidad=0
    __incremento=1
    __dimension=0

    def __init__(self,tam):
        self.__arreFlores=np.empty(tam,dtype=Flores)

    def agregarFlor(self,nuevaFlor):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreFlores.resize(self.__dimension)
        self.__arreFlores[self.__cantidad]=nuevaFlor
        self.__cantidad+=1

    def cargarArchivo(self):
        archivo= open('flores.csv')
        reader = csv.reader(archivo,delimiter=';')
        for flor in reader:
            nuevaFlor= Flores(flor[0],flor[1],flor[2],flor[3])
            self.agregarFlor(nuevaFlor)
        archivo.close()

    def buscarFlor(self,num:int):
        respuesta=-1
        i=0
        b=True
        while i<len(self.__arreFlores) and b:
            print("num flor {} - num {}".format(self.__arreFlores[i],num))
            if self.__arreFlores[i].getNumero()==num:
                respuesta=i
                b=False
            else:
                i+=1
        return respuesta

    def elegirFlor(self):
        respuesta=False
        print("Ingrese el numero de la flor para incluirla al ramo ---")
        for flor in self.__arreFlores:
            print(flor)
        numero=int(input("--Ingrese numero de flor: "))
        aux=self.buscarFlor(numero)
        if aux!= -1:
            respuesta=self.__arreFlores[aux]
        return respuesta
    
    def cantidadFlores(self):
        return len(self.__arreFlores)

    def obtenerFlor(self,indice):
        return self.__arreFlores[indice]

