import csv
import numpy as np

import Flores

class ManejadorFlores:
    __arreFlores=None

    # variables arreglo numpy
    __cantidad=0
    __incremento=1
    __dimension=0

    def __init__(self):
        self.__arreFlores=np.empty(0,dtype=Flores)

    def agregarFlor(self,nuevaFlor):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreFlores.resize(self.__dimension)
        self.__arreFlores[self.__cantidad]=nuevaFlor
        self.__cantidad+=1

    def cargarArchivo(self):
        archivo= open('flores.csv')
        reader = csv.reader(archivo,delimiter=';')
        