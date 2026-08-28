"""
matriz.py
Matriz de asientos implementada como estructura independiente.
Uso en el proyecto: representar la distribución de asientos de una sala.
"""

from typing import List, Optional


class MatrizAsientos:
    def __init__(self, filas: int, columnas: int):
        self.filas = filas
        self.columnas = columnas
        self._matriz: List[List[Optional[str]]] = [
            [None for _ in range(columnas)] for _ in range(filas)
        ]

    def esta_libre(self, fila: int, columna: int) -> bool:
        self._validar_posicion(fila, columna)
        return self._matriz[fila][columna] is None

    def reservar(self, fila: int, columna: int, usuario: str) -> bool:
        self._validar_posicion(fila, columna)
        if not self.esta_libre(fila, columna):
            return False
        self._matriz[fila][columna] = usuario
        return True

    def liberar(self, fila: int, columna: int) -> None:
        self._validar_posicion(fila, columna)
        self._matriz[fila][columna] = None

    def ocupado_por(self, fila: int, columna: int) -> Optional[str]:
        self._validar_posicion(fila, columna)
        return self._matriz[fila][columna]

    def a_estructura_json(self) -> List[List[Optional[str]]]:
        return self._matriz

    def _validar_posicion(self, fila: int, columna: int) -> None:
        if not (0 <= fila < self.filas) or not (0 <= columna < self.columnas):
            raise IndexError(
                f"Posición ({fila}, {columna}) fuera de rango para una sala "
                f"de {self.filas}x{self.columnas}"
            )


if __name__ == "__main__":
    sala = MatrizAsientos(filas=5, columnas=8)
    print("¿B4 libre?", sala.esta_libre(1, 3))
    sala.reservar(1, 3, "Ana")
    print("¿B4 libre ahora?", sala.esta_libre(1, 3))
    print("Ocupado por:", sala.ocupado_por(1, 3))
    print("Intento de reservar ya ocupado:", sala.reservar(1, 3, "Luis"))
