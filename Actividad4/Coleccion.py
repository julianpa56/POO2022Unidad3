

import csv
import numpy as np

from Calefactor import Calefactor
from Gas import Gas
from Electrico import Electrico


class Coleccion:
    __arreCalefactores=None

    # Atributos para numpy
    __cantidad=0
    __dimension=0
    __incremento=1

    def __init__(self,cantidad):
        self.__arreCalefactores= np.empty(cantidad,dtype=Calefactor)
        self.__dimension=cantidad

    def agregarCalefactor(self,nuevoCalefactor):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreCalefactores.resize(self.__dimension)
        self.__arreCalefactores[self.__cantidad]=nuevoCalefactor
        self.__cantidad+=1
    
    def cargarArchivos(self):
        archivo1=open('calefactor-electrico.csv')
        reader1= csv.reader(archivo1,delimiter=',')
        archivo2=open('calefactor-a-gas.csv')
        reader2= csv.reader(archivo2,delimiter=',')

        for fila1 in reader1:
            calefactorElectrico= Electrico(fila1[0],fila1[1],int(fila1[2]))
            if isinstance(calefactorElectrico,Calefactor):
                self.agregarCalefactor(calefactorElectrico)
            
        for fila2 in reader2:
            calefactorAGas= Gas(fila2[0],fila2[1],fila2[2],int(fila2[3]))
            if isinstance(calefactorAGas,Calefactor):
                self.agregarCalefactor(calefactorAGas)
        
        archivo1.close()
        archivo2.close()

    def menorConsumoGas(self,costoM3,cantidad):
        menorCosto=None
        i=0
        while(i<len(self.__arreCalefactores)):
            if isinstance(self.__arreCalefactores[i],Gas):
                if menorCosto==None:
                    menorCosto=i
                else:
                    if self.__arreCalefactores[menorCosto].calcularConsumo(costoM3,cantidad)>self.__arreCalefactores[i].calcularConsumo(costoM3,cantidad):
                        menorCosto=i
                    else:
                        i+=1
            else:
                i+=1
        
        print("El calefactor a gas con menor consumo es: MARCA: {} -- MODELO: {}".format(self.__arreCalefactores[menorCosto].getMarca(),self.__arreCalefactores[menorCosto].getModelo()))
        return menorCosto

    def menorConsumoElectrico(self,costoKW,cantidad):
        menorCosto=None
        i=0
        while(i<len(self.__arreCalefactores)):
            if isinstance(self.__arreCalefactores[i],Electrico):
                if menorCosto==None:
                    menorCosto=i
                else:
                    if self.__arreCalefactores[menorCosto].calcularConsumo(costoKW,cantidad)>self.__arreCalefactores[i].calcularConsumo(costoKW,cantidad):
                        menorCosto=i
                    else:
                        i+=1
            else:
                i+=1
        
        print("El calefactor electrico con menor consumo es: MARCA: {} -- MODELO: {}".format(self.__arreCalefactores[menorCosto].getMarca(),self.__arreCalefactores[menorCosto].getModelo()))
        return menorCosto


    def mostrarDatos(self,indice):
        print(self.__arreCalefactores[int(indice)])