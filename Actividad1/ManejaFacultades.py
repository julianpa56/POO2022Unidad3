
import csv

from Facultad import Facultad


class Manejador:
    __listaFacultades=[]


    def cargarArchiv(self):
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
                self.__listaFacultades[int(filaCarrera[0])].agregarCarrera(filaCarrera[1:])
                try:
                    filaCarrera=next(reader)
                except StopIteration:
                    bandera=False
            fila=filaCarrera
        archivo.close()
