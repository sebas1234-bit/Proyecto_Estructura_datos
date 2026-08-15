"""
lista_doble.py
Lista enlazada doble implementada a mano, usada como HistorialVentas:
permite navegar el historial de funciones/ventas hacia adelante y hacia atrás.
"""

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class _Nodo:
    """Nodo interno de la lista enlazada doble."""
    dato: Any
    anterior: Optional["_Nodo"] = None
    siguiente: Optional["_Nodo"] = None


class HistorialVentas:
    """
    Lista enlazada doble que almacena el historial de ventas/funciones.
    Cada nodo apunta al anterior y al siguiente, permitiendo recorrer
    la lista en ambos sentidos mediante un cursor interno.
    """

    def __init__(self):
        self._cabeza: Optional[_Nodo] = None
        self._cola: Optional[_Nodo] = None
        self._cursor: Optional[_Nodo] = None
        self._tamano: int = 0

    def esta_vacia(self) -> bool:
        """Retorna True si el historial no tiene registros."""
        return self._cabeza is None

    def tamano(self) -> int:
        """Retorna la cantidad de registros almacenados."""
        return self._tamano

    def agregar(self, venta: Any) -> None:
        """Agrega un nuevo registro de venta al final del historial. O(1)."""
        nuevo = _Nodo(dato=venta)
        if self.esta_vacia():
            self._cabeza = nuevo
            self._cola = nuevo
        else:
            nuevo.anterior = self._cola
            self._cola.siguiente = nuevo
            self._cola = nuevo
        self._tamano += 1

    def iniciar_recorrido(self) -> Optional[Any]:
        """
        Ubica el cursor al inicio del historial (el primer registro)
        y retorna su dato. Retorna None si el historial está vacío.
        """
        self._cursor = self._cabeza
        return self._cursor.dato if self._cursor else None

    def dato_actual(self) -> Optional[Any]:
        """Retorna el dato en la posición actual del cursor, sin moverlo."""
        return self._cursor.dato if self._cursor else None

    def siguiente(self) -> Optional[Any]:
        """
        Mueve el cursor una posición hacia adelante y retorna su dato.
        Retorna None si ya está en el último registro o no se ha iniciado
        el recorrido.
        """
        if self._cursor is None or self._cursor.siguiente is None:
            return None
        self._cursor = self._cursor.siguiente
        return self._cursor.dato

    def anterior(self) -> Optional[Any]:
        """
        Mueve el cursor una posición hacia atrás y retorna su dato.
        Retorna None si ya está en el primer registro o no se ha iniciado
        el recorrido.
        """
        if self._cursor is None or self._cursor.anterior is None:
            return None
        self._cursor = self._cursor.anterior
        return self._cursor.dato

    def recorrer(self) -> list:
        """Retorna una lista de Python con todos los registros, en orden. O(n)."""
        resultado = []
        actual = self._cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def __len__(self) -> int:
        return self._tamano

    def __str__(self) -> str:
        return " <-> ".join(str(v) for v in self.recorrer()) or "(vacío)"


if __name__ == "__main__":
    historial = HistorialVentas()

    print("¿Está vacío al inicio?", historial.esta_vacia())

    historial.agregar({"funcion": "El último viaje", "hora": "18:00"})
    historial.agregar({"funcion": "Eclipse", "hora": "20:00"})
    historial.agregar({"funcion": "Rescate", "hora": "22:00"})

    print("Historial completo:", historial)
    print("Tamaño:", historial.tamano())

    print("\n--- Navegación con cursor ---")
    print("Inicio:", historial.iniciar_recorrido())
    print("Actual:", historial.dato_actual())
    print("Siguiente:", historial.siguiente())
    print("Siguiente:", historial.siguiente())
    print("Anterior:", historial.anterior())
    print("Siguiente (fuera de rango):", end=" ")
    historial.siguiente()
    print(historial.siguiente())  # ya no hay más, debe dar None