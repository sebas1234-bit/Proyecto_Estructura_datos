from estructuras.vector_peliculas import VectorPeliculas

class Arbol:
    def nodo(self, info):
        self.info = info
        self.der = None
        self.izq = None

    def __init__(self, info):
        self.raiz = self.nodo()

    def arbol(self):
        self.raiz.info = int(input("Cuanto tiempo tienes: "))
        while True: 
            i = 1
            if self.raiz.info < 100: 
                menos_100 = self.nodo(int(input()))
                self.raiz.izq = menos_100
                print("¿Que género prefieres?: ")
                for self.genero in self.genero_peliculas():
                    print(f"{i}: {self.genero}")
                    i = i+1
                eleccion = input()
                return eleccion
            
            elif self.raiz.info >= 100: 
                mas_100 = self.nodo(int(input()))
                self.raiz.der = mas_100
                print("¿Que género prefieres?: ")
                for self.genero in self.genero_peliculas():
                    print(f"{i}: {self.genero}")
                    i = i+1
                eleccion = input()
                return eleccion

            else: 
                return "No hay peliculas disponibles"
        

    