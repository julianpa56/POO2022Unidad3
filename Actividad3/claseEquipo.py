


class Equipo:
    __nombre: str
    __ciudad: str

    def __init__(self,nom,ciu):
        self.__nombre=nom
        self.__ciudad=ciu

    def getNombre(self):
        return self.__nombre

    def getCiudad(self):
        return self.__ciudad