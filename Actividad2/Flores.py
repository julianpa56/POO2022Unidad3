


class Flores:
    __numero=0
    __nombre=''
    __color=''
    __descripcion=''

    def __init__(self,num,nom,col,des):
        self.__numero=int(num)
        self.__nombre=nom
        self.__color=col
        self.__descripcion=des

    def getNumero(self):
        return self.__numero

    def getNombre(self):
        return self.__nombre

    def getColor(self):
        return self.__color

    def getDescripcion(self):
        return self.__descripcion

    def __str__(self):
        return ("Nro: {} - Nombre: {} - Color: {} - Descripcion: {}".format(self.getNumero(),self.getNombre(),self.getColor(),self.getDescripcion()))