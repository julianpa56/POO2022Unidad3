from ManejadorFlores import ManejadorFlores
from ManejadorRamos import ManejadorRamos

def menu(manF:ManejadorFlores,manR:ManejadorRamos):
    manF.cargarArchivo()
    b=True
    while b:
        op=int(input("Ingrese 1 para cargar ramo | otro numero para salir: "))
        if op==1:
            manR.registrarRamo(manF)
        else:
            b=False
    manR.topFlores(manF)
    tam=int(input("Seleccione tamaño: 1- Chico | 2- Mediano | 3- Grande: "))
    if tam==1:
        manR.mostrarRamos('Chico')
    elif tam==2:
        manR.mostrarRamos('Mediano')
    elif tam==1:
        manR.mostrarRamos('Grande')
    else:
        print("Opcion incorrecta")





if __name__=='__main__':
    manF=ManejadorFlores(3)
    manR=ManejadorRamos()
    menu(manF,manR)