from datetime import date


class Jugador:
    __nombre: str
    __dni:str
    __ciudadNatal: str
    __paisOrigen: str
    __fechaNacimiento: date

    def __init__(self,nom,dni,ciu,pais,fnac) -> None:
        self.__nombre=nom
        self.__dni=dni
        self.__ciudadNatal=ciu
        self.__paisOrigen=pais
        self.__fechaNacimiento=fnac

    def getNombre(self):
        return self.__nombre

    def getDni(self):
        return self.__dni
    

