import csv
import numpy as np

from claseEquipo import Equipo




class ManejadorEquipo:
    __arreEquipos=None


    # Atributos numpy
    __cantidad=0
    __dimension=0
    __incremento=1

    def __init__(self):
        self.__arreEquipos=None

    def crearArreglo(self,cantidad):
        self.__arreEquipos= np.empty(cantidad,dtype=Equipo)

    def agregarEquipo(self,unEquipo):
        if self.__dimension==self.__cantidad:
            self.__dimension+=self.__incremento
            self.__arreEquipos.resize(self.__dimension)
        self.__arreEquipos[self.__cantidad]=unEquipo
        self.__cantidad+=1

    def cargarArchivo(self):
        archivo= open('Equipos.csv')
        reader= csv.reader(archivo,delimiter=';')
        cantidad=int(next(reader))
        self.crearArreglo(cantidad)
        b=True
        while b:
            try:
                nuevoEquipo= next(reader)
                self.agregarEquipo(nuevoEquipo)
            except StopIteration:
                b=False
        archivo.close()

    def seleccionarEquipo(self):
        respuesta=None
        for equipo in self.__arreEquipos:
            print(equipo.getNombre())
        b=True
        i=0
        aux=input("Ingrese nombre del equipo a seleccionar")
        while i<len(self.__arreEquipos) and b:
            if self.__arreEquipos[i].getNombre().lower()==aux.lower():
                respuesta= self.__arreEquipos[i]
                b=False
            else:
                i+=1
        return respuesta