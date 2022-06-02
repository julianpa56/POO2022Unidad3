import Flores

class Ramo:
    __tamanio=''
    __listaFlores=[]

    def __init__(self,tam):
        self.__tamanio=tam
    
    def agregarFlores(self,nuevasFlores):
        self.__listaFlores.append(nuevasFlores)