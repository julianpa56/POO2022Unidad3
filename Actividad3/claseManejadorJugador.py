


from claseJugador import Jugador


class ManejadorJugador:
    __listaJugadores:list

    def __init__(self):
        self.__listaJugadores=[]

    def agregarJugador(self):
        nom=input("Ingrese nombre de jugador: ")
        dni=input("Ingrese dni: ")
        ciu=input("Ingrese ciudad: ")
        pais=input("Ingrese pais: ")
        fnac=input("Ingrese fecha de nacimiento: ")
        nuevoJugador= Jugador(nom,dni,ciu,pais,fnac)

    def seleccionarJugador(self):
        respuesta=None
        for jugador in self.__listaJugadores:
            print(jugador.getNombre())
        b=True
        i=0
        aux=input("Ingrese nombre del jugador a seleccionar")
        while i<len(self.__listaJugadores) and b:
            if self.__listaJugadores[i].getNombre().lower()==aux.lower():
                respuesta= self.__listaJugadores[i]
                b=False
            else:
                i+=1
        return respuesta

