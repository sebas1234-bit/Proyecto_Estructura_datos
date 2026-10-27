# ============================================================
# PILA (LIFO) - HISTORIAL DE OPERACIONES
# Guarda las últimas compras y cancelaciones
# ============================================================

from estructuras.nodo import Nodo


class PilaOperaciones:

    def __init__(self):
        self.tope = None
        self.cantidad = 0

    def push(self, operacion):
        """Apila una operación (queda en el tope)."""
        nuevo = Nodo(operacion)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.cantidad += 1

    def pop(self):
        """Desapila y devuelve la última operación. None si está vacía."""
        if self.esta_vacia():
            return None

        nodo = self.tope
        self.tope = nodo.siguiente
        self.cantidad -= 1

        return nodo.dato

    def peek(self):
        """Devuelve la última operación sin quitarla. None si está vacía."""
        if self.esta_vacia():
            return None

        return self.tope.dato

    def esta_vacia(self):
        return self.tope is None

    def mostrar(self, limite=None):
        """Recorre desde el tope (más reciente) sin modificar la pila."""
        actual = self.tope
        contador = 0

        while actual is not None:

            if limite is not None and contador >= limite:
                break

            contador += 1
            print(f"\n#{contador}")
            actual.dato.mostrar()

            actual = actual.siguiente