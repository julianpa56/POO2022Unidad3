

class Carrera:
    __codigo=0
    __nombre=''
    __fechaInicio=''
    __duracion=''
    __titulo=''

    def __init__(self,datos:list):
        self.__codigo=int(datos[0])
        self.__nombre=datos[1]
        self.__fechaInicio=datos[2]
        self.__duracion=datos[3]
        self.__titulo=datos[4]

    def getNombre(self):
        return self.__nombre
        
    def getDuracion(self):
        return self.__duracion

    def getCodigo(self):
        return self.__codigo