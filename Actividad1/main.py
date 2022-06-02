from ManejaFacultades import Manejador


def menu(manejador: Manejador):
    op=int(input("1- Listar carreras por codigo de facultad\n2- Buscar carrera y mostrar detalles\n -- OTRA OPCION PARA SALIR: "))
    while (op==1 or op==2):
        if op==1:
            aux=int(input("Ingrese codigo de facultad: "))
            existe=manejador.buscarCodigo(aux)
            if existe:
                manejador.listarCarreras(aux)
            else:
                print("Codigo de facultad inexistente")
        if op==2:
            aux2=input("Ingrese nombre de carrera a buscar: ")
            manejador.buscarCarrera(aux2)
        
        op=int(input("1- Listar carreras por codigo de facultad\n2- Buscar carrera y mostrar detalles\n -- OTRA OPCION PARA SALIR: "))




if __name__=='__main__':
    manejador= Manejador()
    manejador.cargarArchivo()
    menu(manejador)
    del(manejador)