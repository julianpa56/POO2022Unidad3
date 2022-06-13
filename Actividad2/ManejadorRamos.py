from ManejadorFlores import ManejadorFlores
from Ramo import Ramo


class ManejadorRamos:
    __listaRamos=[]

    def registrarRamo(self,manejadorF:ManejadorFlores):
        b=True
        tam=int(input("Seleccione tamaño del ramo: 1- Chico | 2- Mediano | 3- Grande \n Opcion: "))
        if tam==1 or tam==2 or tam==3:
            if tam==1:
                tam='Chico'
            elif tam==2:
                tam='Mediano'
            else:
                tam='Grande'
        try:
            assert type(tam)==str
        
        except AssertionError:
            print("Se ingreso una opcion incorrecta de tamaño")

        nuevoRamo=Ramo(tam)
        while b:
            florElegida=manejadorF.elegirFlor()
            if florElegida!=False:
                nuevoRamo.agregarFlores(florElegida)
                op=int(input("Flor agregada al ramo - ingrese 1 para continuar sino otro numero para termiar"))
                if op!=1:
                    b=False
            else:
                op=int(input("Flor no encontrada - si desea reintentar ingrese 1 u otro numero para terminar"))
                if op!=1:
                    b=False
        
        self.__listaRamos.append(nuevoRamo)
        print("Ramo registrado")

    def topFlores(self,manejadorF:ManejadorFlores):
        cantidad=manejadorF.cantidadFlores()
        contadorFlores=[0 for i in range(cantidad)]
        floresYCantidad=[]
        for ramo in self.__listaRamos:
            ramo.contarFlores(contadorFlores)
        for i in range(len(contadorFlores)):
            flor=manejadorF.obtenerFlor(i)
            floresYCantidad.append([flor,contadorFlores[i]])
        print("5 Flores mas vendidas -------------")
        for i in range(5):
            aux=floresYCantidad.index(max(floresYCantidad,key=lambda item: item[1]))
            print("Nombre: {} - Cantidad: {}".format(floresYCantidad[aux][0].getNombre(),floresYCantidad[aux][1]))
            floresYCantidad.pop(aux)
        print("-----------------------------------")

    def mostrarRamos(self,tam):

        for ramo in self.__listaRamos:
            if(ramo.getTamanio().lower()==tam.lower()):
                ramo.listaFlores()
