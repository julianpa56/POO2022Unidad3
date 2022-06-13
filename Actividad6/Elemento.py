from zope.interface import Interface

class IElemento(Interface):

    def insertarElemento(nuevoElemento,posicion):
        pass

    def agregarElemento(nuevoElemento):
        pass

    def mostrarElemento(posicion):
        pass
