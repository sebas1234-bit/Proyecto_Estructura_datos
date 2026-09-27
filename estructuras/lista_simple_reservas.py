# ============================================================
# LISTA SIMPLEMENTE ENLAZADA
# RESERVAS ACTIVAS
# ============================================================

from estructuras.nodo import Nodo


class ListaSimpleReservas:

    def __init__(self):
        self.cabeza = None

    def agregar(self, reserva):

        nuevo = Nodo(reserva)

        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def mostrar(self):

        actual = self.cabeza

        if actual is None:
            print("\nNo hay reservas activas.")
            return

        while actual is not None:

            actual.dato.mostrar_reserva()
            actual = actual.siguiente

    def buscar_por_documento(self, documento):

        actual = self.cabeza

        while actual is not None:

            if actual.dato.persona.documento == documento:
                return actual.dato

            actual = actual.siguiente

        return None

    def eliminar(self, reserva):

        actual = self.cabeza
        anterior = None

        while actual is not None:

            if actual.dato == reserva:

                if anterior is None:
                    self.cabeza = actual.siguiente

                else:
                    anterior.siguiente = actual.siguiente

                return True

            anterior = actual
            actual = actual.siguiente

        return False