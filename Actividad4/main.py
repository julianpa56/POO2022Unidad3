import numpy as np

from Coleccion import Coleccion


if __name__=='__main__':

    cantidad=int(input("Ingrese una cantidad para el tamaño del arreglo: "))

    coleccion= Coleccion(cantidad)
    coleccion.cargarArchivos()

    print ("Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo")
    costoM3=int(input("Ingrese costo por m3: "))
    cantidad1=int(input("Ingrese cantidad de m3: "))
    resultado1= coleccion.menorConsumoGas(costoM3,cantidad1)

    print("- Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.")
    costoKW=int(input("Ingrese costo de kilowatt/h : "))
    cantidad2=int(input("Ingrese cantidad que se estima a consumir por hora: "))
    resultado2= coleccion.menorConsumoElectrico(costoKW,cantidad2)

    