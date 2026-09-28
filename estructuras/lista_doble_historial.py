# ============================================================
# LISTA DOBLEMENTE ENLAZADA
# HISTORIAL (recorrible en ambos sentidos)
# ============================================================

from estructuras.nodo import NodoDoble


class ListaDobleHistorial:

    def __init__(self):

        self.cabeza = None
        self.cola = None

    def agregar(self, reserva):

        nuevo = NodoDoble(reserva)

        if self.cabeza is None:

            self.cabeza = nuevo
            self.cola = nuevo

        else:

            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo
        def esta_vacia(self):

        return self.cabeza is None

    def mostrar_inicio_fin(self):

        actual = self.cabeza

        while actual is not None:

            actual.dato.mostrar_reserva()
            actual = actual.siguiente

    def mostrar_fin_inicio(self):

        actual = self.cola

        while actual is not None:

            actual.dato.mostrar_reserva()
            actual = actual.anterior
