"""
vector_funciones.py
Vector (arreglo dinámico) implementado como wrapper simple.
Uso en el proyecto: funciones/horarios disponibles para reservar
(distinto del catálogo de películas — este es el "cartel" de horarios).
"""

from typing import Any, List


class VectorFunciones:
    def __init__(self):
        self._datos: List[Any] = []

    def agregar(self, funcion: dict) -> None:
        """Agrega una función/horario disponible. O(1) amortizado."""
        self._datos.append(funcion)

    def obtener(self, indice: int) -> Any:
        """Acceso directo por posición. O(1)."""
        return self._datos[indice]

    def tamano(self) -> int:
        return len(self._datos)

    def a_lista(self) -> List[Any]:
        return list(self._datos)

    def __len__(self) -> int:
        return len(self._datos)

    def __str__(self) -> str:
        return str(self._datos)


if __name__ == "__main__":
    funciones = VectorFunciones()
    funciones.agregar({"pelicula": "Dune 2", "hora": "19:00", "sala": 1})
    funciones.agregar({"pelicula": "Coco", "hora": "16:00", "sala": 2})
    funciones.agregar({"pelicula": "Oppenheimer", "hora": "21:00", "sala": 1})

    print("Funciones disponibles:", funciones)
    print("Tamaño:", funciones.tamano())
    print("Función en posición 1:", funciones.obtener(1))