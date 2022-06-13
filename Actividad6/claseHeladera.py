
from claseAparatoElectronico import AparatoElectronico


class Heladera(AparatoElectronico):
    __capacidad:int
    __freezer:bool
    __ciclica:bool

    def __init__(self, cap, fre, cic, marca, modelo, color, pFab, preBase):
        self.__capacidad=cap
        self.__freezer=fre
        self.__ciclica=cic
        super().__init__(marca, modelo, color, pFab, preBase)

