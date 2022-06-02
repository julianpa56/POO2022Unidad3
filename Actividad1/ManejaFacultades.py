
import csv
import os

from Facultad import Facultad


class Manejador:
    __listaFacultades=[]


    def cargarArchivo(self):
        archivo= open("Facultades.csv")
        reader= csv.reader(archivo,delimiter=',')
        fila=next(reader)
        bandera=True
        print("Facultad")
        while(bandera):
            print(fila)
            self.__listaFacultades.append(Facultad(fila))
            print("Carreras:")
            filaCarrera=next(reader)
            while bandera and fila[0]==filaCarrera[0]:
                print(filaCarrera)
                nuevaCarrera=filaCarrera[1:]
                print(nuevaCarrera)
                self.__listaFacultades[int(filaCarrera[0])-1].agregarCarrera(nuevaCarrera)
                try:
                    filaCarrera=next(reader)
                except StopIteration:
                    bandera=False
            fila=filaCarrera
        os.system("pause")
        os.system("cls")
        archivo.close()

    def buscarCodigo(self,cod):
        respuesta=False
        b= True
        i=0
        while i<len(self.__listaFacultades) and b:
            if self.__listaFacultades[i].getCodigo()==cod:
                respuesta=True
                b= not b
            else:
                i+=1
        return respuesta

    def listarCarreras(self,codFac):
        print("--- NOMBRE DE FACULTAD: {}".format(self.__listaFacultades[codFac-1].getNombre()))
        self.__listaFacultades[codFac-1].listaCarreras()

    def buscarCarrera(self,carrera):
        b= True
        i=0
        while i<len(self.__listaFacultades) and b:
            aux=self.__listaFacultades[i].buscar(carrera)
            if aux:
                b=False
            else:
                i+=1
        if b:
            print("Carrera no encontrada")