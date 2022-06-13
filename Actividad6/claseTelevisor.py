

from claseAparatoElectronico import AparatoElectronico


class Televisor(AparatoElectronico):
    __tipoPantalla:str
    __pulgadas:float
    __tipoDefinicion:str
    __conexionInternet:bool

    def __init__(self, tPant, pul, tDef, conInt, marca, modelo, color, pFab, preBase):
        self.__tipoPantalla=tPant
        self.__pulgadas=pul
        self.__tipoDefinicion=tDef
        self.__conexionInternet=conInt
        super().__init__(marca, modelo, color, pFab, preBase)