from datetime import date


class Contrato:
    __fechaInicio: date
    __fechaFin: date
    __pagoMensual: float
    __jugador: None
    __equipo: None

    def __init__(self,finicio,ffin,pmen,jugador,equipo):
        self.__fechaInicio=finicio
        self.__fechaFin= ffin
        self.__pagoMensual=pmen
        self.__jugador=jugador
        self.__equipo=equipo

    def getJugador(self):
        return self.__jugador

    def getEquipo(self):
        return self.__equipo

    def getFechaFin(self):
        return self.__fechaFin
    
    def getFechaInicio(self):
        return self.__fechaInicio

    def getPagoMensual(self):
        return self.__pagoMensual