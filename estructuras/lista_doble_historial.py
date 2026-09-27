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