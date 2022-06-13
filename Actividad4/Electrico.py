


from Calefactor import Calefactor


class Electrico(Calefactor):
    __potenciaMaxima=0

    def __init__(self, mar, mod, pot):
        self.__potenciaMaxima=int(pot)
        super().__init__(mar, mod)

    def calcularConsumo(self,costoKW,cantidad):
        respuesta=(self.__potenciaMaxima/1000)*cantidad*costoKW

        return respuesta

    def getPotencia(self):
        return self.__potenciaMaxima

    def __str__(self):
        
        return ("Calefactor tipo electrico, marca {} - modelo {} - potencia maxima {}".format(super().getMarca(),super().getModelo(),self.getPotencia()))