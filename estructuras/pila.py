"""
Pila (LIFO) implementada desde cero con un nodo enlazado.
Uso en el proyecto: registro de últimas operaciones (compras/cancelaciones)
y funcionalidad de "deshacer última operación" en el panel de personal.
"""

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class _Nodo:
    dato: Any
    siguiente: Optional["_Nodo"] = None


class Pila:
    def __init__(self):
        self._tope: Optional[_Nodo] = None
        self._tamano: int = 0

    def apilar(self, dato: Any) -> None:
        """Agrega un elemento al tope de la pila. O(1)."""
        nuevo = _Nodo(dato=dato, siguiente=self._tope)
        self._tope = nuevo
        self._tamano += 1

    def desapilar(self) -> Any:
        """Quita y retorna el elemento del tope. O(1)."""
        if self.esta_vacia():
            raise IndexError("No se puede desapilar: la pila está vacía")
        nodo = self._tope
        self._tope = nodo.siguiente
        self._tamano -= 1
        return nodo.dato

    def ver_tope(self) -> Any:
        """Retorna el elemento del tope sin quitarlo."""
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self._tope.dato

    def esta_vacia(self) -> bool:
        return self._tope is None

    def __len__(self) -> int:
        return self._tamano

    def a_lista(self, limite: Optional[int] = None) -> list:
        """Retorna los elementos del tope hacia la base, útil para mostrar
        el historial de operaciones más recientes en el panel de personal."""
        resultado = []
        actual = self._tope
        while actual is not None and (limite is None or len(resultado) < limite):
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado


if __name__ == "__main__":
    # Prueba rápida
    historial = Pila()
    historial.apilar({"operacion": "compra", "cliente": "Ana", "asiento": "B4"})
    historial.apilar({"operacion": "compra", "cliente": "Luis", "asiento": "B5"})
    historial.apilar({"operacion": "cancelacion", "cliente": "Ana", "asiento": "B4"})

    print("Historial (más reciente primero):")
    for op in historial.a_lista():
        print(" -", op)

    print("Deshacer última operación:", historial.desapilar())
    print("Tamaño actual:", len(historial))
