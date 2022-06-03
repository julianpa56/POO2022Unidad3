


from Calefactor import Calefactor


class Gas(Calefactor):
    __matricula=''
    __calorias=0

    def __init__(self, mar, mod, matr, cal):
        self.__matricula=matr
        self.__calorias=int(cal)
        super().__init__(mar, mod)

    def calcularConsumo(self,costoM3:int,cantidad:int):
        
        respuesta=(self.__calorias/1000)*cantidad*costoM3

        return respuesta