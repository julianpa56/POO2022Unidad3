

class Ramo:
    __tamanio=''
    __listaFlores=[]

    def __init__(self,tam):
        self.__tamanio=tam
    
    def agregarFlores(self,nuevasFlores):
        self.__listaFlores.append(nuevasFlores)

    def contarFlores(self,contador:list):
        for flor in self.__listaFlores:
            indice=flor.getNumero()
            contador[indice-1]+=1

    def listaFlores(self):
        print("Lista de flores -------")
        for flor in self.__listaFlores:
            print(flor)
        print("-----------------------")

    def getTamanio(self):
        return self.__tamanio