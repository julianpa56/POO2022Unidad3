


class Nodo:
    __aparato=None
    __siguiente=None

    def __init__(self,aparato):
        self.__aparato=aparato
        self.__siguiente=None

    def setSiguiente(self,aparato):
        self.__siguiente=aparato

    def getSiguiente(self):
        return self.__siguiente

    def getAparato(self):
        return self.__aparato