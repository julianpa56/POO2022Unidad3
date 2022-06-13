from zope.interface import implementer

from Elemento import IElemento
from claseNodo import Nodo

@implementer(IElemento)
class ManejadorAparatos:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0

    def __init__(self):
        self.__comienzo=None
        self.__actual=None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__actual==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getAparato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def agregarElemento(self, nuevoAparato):
        nodo= Nodo(nuevoAparato)
        nodo.setSiguiente(self.__comienzo)
        if self.__comienzo is None:
            self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1

    def insertarElemento(self,nuevoAparato,posicion):
        aux=self.__comienzo
        b=True
        contador=0
        if posicion <= self.__tope and posicion>=0:
            if contador== posicion: # Al principio
                nodo= Nodo(nuevoAparato)
                nodo.setSiguiente(self.__comienzo)
                self.__comienzo=nodo
                self.__actual=nodo
                self.__tope+=1
            else: 
                anterior=aux
                aux=aux.getSiguiente()
                while (aux is not None) and b:
                    if contador== posicion:
                        b=False
                    else:
                        contador+=1
                        anterior=aux
                        aux=aux.getSiguiente()
                nodo= Nodo(nuevoAparato)
                nodo.setSiguiente(aux)
                anterior.setSiguiente(nodo)
                self.__tope+=1
