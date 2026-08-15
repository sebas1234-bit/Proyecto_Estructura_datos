"""
lista_simple.py
Lista enlazada simple implementada a mano, usada como ListaEntradas:
representa las entradas (tickets) compradas por un cliente del cine.
"""

from dataclasses import dataclass
from typing import Any, Callable, Optional


@dataclass
class _Nodo:
    """Nodo interno de la lista enlazada simple."""
    dato: Any
    siguiente: Optional["_Nodo"] = None


class ListaEntradas:
    """
    Lista enlazada simple que almacena las entradas (tickets) de un cliente.
    Cada nodo apunta únicamente al siguiente nodo (estructura unidireccional).
    """

    def __init__(self):
        self._cabeza: Optional[_Nodo] = None
        self._tamano: int = 0

    def esta_vacia(self) -> bool:
        """Retorna True si la lista no tiene entradas."""
        return self._cabeza is None

    def tamano(self) -> int:
        """Retorna la cantidad de entradas almacenadas."""
        return self._tamano

    def agregar(self, entrada: Any) -> None:
        """Agrega una nueva entrada al final de la lista. O(n)."""
        nuevo = _Nodo(dato=entrada)
        if self.esta_vacia():
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._tamano += 1

    def eliminar(self, entrada: Any) -> bool:
        """
        Elimina la primera ocurrencia de una entrada que sea igual al valor dado.
        Retorna True si se eliminó, False si no se encontró. O(n).
        """
        anterior = None
        actual = self._cabeza
        while actual is not None:
            if actual.dato == entrada:
                if anterior is None:
                    self._cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._tamano -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar(self, condicion: Callable[[Any], bool]) -> Optional[Any]:
        """
        Retorna la primera entrada que cumpla la función 'condicion',
        sin eliminarla de la lista. Si ninguna cumple, retorna None. O(n).

        Ejemplo:
            entrada = lista.buscar(lambda e: e["pelicula"] == "El último viaje")
        """
        actual = self._cabeza
        while actual is not None:
            if condicion(actual.dato):
                return actual.dato
            actual = actual.siguiente
        return None

    def recorrer(self) -> list:
        """Retorna una lista de Python con todas las entradas, en orden. O(n)."""
        resultado = []
        actual = self._cabeza
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def __len__(self) -> int:
        return self._tamano

    def __str__(self) -> str:
        return " -> ".join(str(e) for e in self.recorrer()) or "(vacía)"


if __name__ == "__main__":
    lista = ListaEntradas()

    print("¿Está vacía al inicio?", lista.esta_vacia())

    lista.agregar({"id": 1, "pelicula": "El último viaje", "asiento": "A1"})
    lista.agregar({"id": 2, "pelicula": "Eclipse", "asiento": "B2"})
    lista.agregar({"id": 3, "pelicula": "Rescate", "asiento": "C3"})

    print("Entradas del cliente:", lista)
    print("Tamaño:", lista.tamano())

    encontrada = lista.buscar(lambda e: e["pelicula"] == "Eclipse")
    print("Entrada encontrada (Eclipse):", encontrada)

    eliminado = lista.eliminar({"id": 1, "pelicula": "El último viaje", "asiento": "A1"})
    print("¿Se eliminó la entrada 1?", eliminado)
    print("Entradas restantes:", lista)