# Complejidad computacional (Big O) — Sistema de Gestión de Cine

Este documento reúne el análisis de complejidad de cada estructura que
vamos implementando, en la misma notación Big O que vimos en clase. Cada
uno agrega la fila de lo que implementó, con una explicación corta de por
qué tiene esa complejidad — así queda listo para explicárselo al profesor.

| Estructura | Autor | Operación | Complejidad | Por qué |
|---|---|---|---|---|
| Pila | Sebas | `apilar` / `desapilar` | O(1) | Solo se toca el nodo del tope, sin recorrer el resto de la pila |
| Pila | Sebas | `a_lista` | O(n) | Recorre todos los nodos, del tope hasta la base |
| Vector (funciones/horarios) | Sebas | `agregar` | O(1) amortizado | Agregar al final de un arreglo dinámico no requiere desplazar nada, salvo cuando el arreglo interno necesita crecer |
| Vector (funciones/horarios) | Sebas | `obtener(indice)` | O(1) | Acceso directo por posición de memoria, sin recorrer nada |
| Lista enlazada simple | *(Juan José, completar)* | | | |
| Lista enlazada doble | *(Juan José, completar)* | | | |
| Vector (catálogo de películas) | *(Juan José, completar)* | | | |
| Matriz de asientos | *(Nicolle, completar)* | | | |
| Bubble Sort | *(Sebas, pendiente de implementar)* | `ordenar` | O(n²) peor caso, O(n) mejor caso con bandera de "hubo intercambio" | Compara cada par adyacente en cada una de las n pasadas; si la lista ya viene ordenada, una sola pasada sin intercambios basta para detenerse |

## Notas

- "Peor caso" = la situación más desfavorable posible (ej. lista al revés).
- "Mejor caso" = la situación más favorable (ej. lista ya ordenada).
- No es necesario que todas las estructuras tengan complejidad O(1) — la
  idea es entender POR QUÉ cada una tiene la complejidad que tiene, no que
  todas sean rápidas.