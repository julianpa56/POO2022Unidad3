


class AparatoElectronico:
    __marca:str
    __modelo:str
    __color:str
    __paisFabricacion:str
    __precioBase:float

    def __init__(self,marca,modelo,color,pFab,preBase):
        self.__marca=marca
        self.__modelo=modelo
        self.__color=color
        self.__paisFabricacion=pFab
        self.__precioBase=preBase