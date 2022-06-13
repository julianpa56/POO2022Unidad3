

from claseAparatoElectronico import AparatoElectronico


class Lavarropas(AparatoElectronico):
    __capacidad:int
    __velocidad:int
    __cantidadProgramas:int
    __tipoCarga:str

    def __init__(self, cap, vel, cantProg, tCar, marca, modelo, color, pFab, preBase):
        self.__capacidad=cap
        self.__velocidad=vel
        self.__cantidadProgramas=cantProg
        self.__tipoCarga=tCar
        super().__init__(marca, modelo, color, pFab, preBase)