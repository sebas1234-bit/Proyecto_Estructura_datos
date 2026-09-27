# ============================================================
# MATRIZ DE ASIENTOS
# ============================================================

from modelos.asiento import Asiento


class MatrizAsientos:

    def __init__(self, filas=5, columnas=6):

        self.filas = filas
        self.columnas = columnas

        self.asientos = []

        for fila in range(filas):

            fila_asientos = []

            for columna in range(columnas):

                asiento = Asiento(fila + 1, columna + 1)
                fila_asientos.append(asiento)

            self.asientos.append(fila_asientos)

    def mostrar(self):

        print("\n========== ASIENTOS ==========")

        for fila in self.asientos:

            for asiento in fila:

                if asiento.esta_disponible():
                    simbolo = "O"
                else:
                    simbolo = "X"

                print(
                    f"[{asiento.fila},{asiento.columna}] {simbolo}",
                    end="  "
                )

            print()

        print("O = Disponible")
        print("X = Ocupado")

    def obtener_asiento(self, fila, columna):

        if (
            fila < 1
            or fila > self.filas
            or columna < 1
            or columna > self.columnas
        ):
            return None

        return self.asientos[fila - 1][columna - 1]