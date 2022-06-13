import numpy as np
from datetime import date, timedelta
import csv


from claseEquipo import Equipo
from claseManejadorEquipo import ManejadorEquipo
from claseJugador import Jugador
from claseManejadorJugador import ManejadorJugador
from claseContrato import Contrato

class ManejadorContrato:
    __arreContratos:None

    # Atributos numpy
    __dimension=0
    __cantidad=0
    __incremento=1

    def __init__(self):
        self.__arreContratos= np.empty(0,dtype=Contrato)

    def agregarContrato(self,nuevoContrato):
        if self.__dimension==self.__cantidad:
            self.__dimension+=self.__incremento
            self.__arreContratos.resize(self.__dimension)
        self.__arreContratos[self.__cantidad]=nuevoContrato
        self.__cantidad+=1
    
    def crearContrato(self,mJugador:ManejadorJugador,mEquipo:ManejadorEquipo):
        fechaInicio=input("Ingrese fecha de inicio del contrato: ")
        fechaFin=input("Ingrese fecha de finalizacion del contrato: ")
        pagoMensual=float(input("Ingrese pago mensual: "))
        jugador= mJugador.seleccionarJugador()
        equipo= mEquipo.seleccionarEquipo()
        if jugador!=None and equipo != None:
            nuevoContrato= Contrato(fechaInicio,fechaFin,pagoMensual,jugador,equipo)
            self.agregarContrato(nuevoContrato)
            print("Contrato creado y agregado con exito")
        elif jugador == None:
            print("Jugador no encontrado")
        else:
            print("Equipo no encontrado")

    def consultaPorDni(self,dni):
        b=True
        i=0
        while i<len(self.__arreContratos) and b:
            if self.__arreContratos[i].getJugador().getDni()==dni:
                equipo=self.__arreContratos[i].getEquipo().getNombre()
                fecha=self.__arreContratos[i].getFechaFin()
                print("Nombre de equipo: {} - Fecha de finalizacion del contrato: {}".format(equipo,fecha))
                b=False
            else: 
                i+=1
        if b:
            print("No se encontro contrato con jugador con DNI {}".format(dni))

    def consultarContratos(self,idEquipo):
        hoy= date.today()
        for contrato in self.__arreContratos:
            if contrato.getEquipo().getNombre()== idEquipo:
                ffin=contrato.getFechaFin()
                tiempoRestante= ffin - hoy
                tiempoRestante= tiempoRestante // timedelta(days=30)
                print("JUGADOR: {} - EQUIPO: {} - MESES RESTANTES: {}".format(contrato.getJugador().getNombre(),contrato.getEquipo().getNombre(),tiempoRestante))

    def importeContratos(self,nomEquipo):
        respuesta=0
        for contrato in self.__arreContratos:
            if nomEquipo.lower()==contrato.getEquipo().getNombre().lower():
                respuesta+=contrato.getPagoMensual()
        return respuesta

    def escribirArchivo(self):
        archivo= open('Contratos.csv','w',newline='')
        writer= csv.writer(archivo, dialect= 'excel', delimiter=';')
        for contrato in self.__arreContratos:
            writer.writerow({contrato.getJugador().getDni():1, contrato.getEquipo().getNombre():2, contrato.getFechaInicio():3,contrato.getFechaFin():4, contrato.getPagoMensual():5})