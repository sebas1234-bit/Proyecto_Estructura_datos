# ============================================================
# NODOS PARA LAS LISTAS ENLAZADAS
# ============================================================

class Nodo:
    """Nodo para la lista simplemente enlazada."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class NodoDoble:
    """Nodo para la lista doblemente enlazada."""

    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None