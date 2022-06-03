


from Calefactor import Calefactor


class Electrico(Calefactor):
    __potenciaMaxima=0

    def __init__(self, mar, mod, pot):
        self.__potenciaMaxima=int(pot)
        super().__init__(mar, mod)

    def calcularConsumo(self):
        pass