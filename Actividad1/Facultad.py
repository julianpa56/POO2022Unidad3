import numpy as np

from Carrera import Carrera

class Facultad:
    # atributos para arreglo numpy
    __dimension=0
    __incremento=1
    __cantidad=0
    __listaCarreras=None
    # atributos de instancia
    __codigo=0
    __nombre=''
    __direccion=''
    __localidad=''
    __telefono=''
    

    def __init__(self,datos:list):
        self.__codigo=int(datos[0])
        self.__nombre=datos[1]
        self.__direccion=datos[2]
        self.__localidad=datos[3]
        self.__telefono=datos[4]
        self.__listaCarreras= np.empty(0,dtype=Carrera)

    def agregarCarrera(self,datosCarrera:list):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__listaCarreras.resize(self.__dimension)
        self.__listaCarreras[self.__cantidad]=Carrera(datosCarrera)
        self.__cantidad+=1

    def getCodigo(self):
        return self.__codigo
