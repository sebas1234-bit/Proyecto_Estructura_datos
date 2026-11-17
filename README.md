# Cine Santa Fe 🎬

Sistema de gestión de cine desarrollado como proyecto académico para la
materia **Estructura de Datos**. Es un programa de consola en Python, con
Programación Orientada a Objetos, que aplica las estructuras de datos
fundamentales del curso a un caso real: gestión de películas, asientos y
reservas.

## Integrantes

- Juan José Quinchia
- Nicolle Mazo
- Juan Sebastian Hernandez

## Cómo ejecutarlo

No requiere ninguna librería externa (Python puro, sin `pip install` ni
entorno virtual):

```bash
python main.py
```

## Estructura del proyecto

```
cine-santa-fe/
├── main.py                          # Punto de entrada: menú y bucle principal
├── cine.py                          # Clase Cine: coordina todas las estructuras
├── recomendador.py                  # Clase Recomendador: Gestiona películas por duración y género
├── modelos/
│   ├── persona.py                   # Clase Persona
│   ├── pelicula.py                  # Clase Pelicula
│   ├── operacion.py                 # Clase Operacion
│   ├── asiento.py                   # Clase Asiento
│   └── reserva.py                   # Clase Reserva (une Persona + Pelicula + Asiento)
└── estructuras/
    ├── nodo.py                      # Nodo y NodoDoble
    ├── vector_peliculas.py          # Vector: catálogo de películas
    ├── matriz_asientos.py           # Matriz: distribución de asientos por sala
    ├── lista_simple_reservas.py     # Lista enlazada simple: reservas activas
    ├── lista_doble_historial.py     # Lista enlazada doble: historial de reservas
    ├── pila_operaciones.py          # Pila: gestión de operaciones
    ├── cola_espera.py               # Cola: funciona como lista de espera
    ├── arbol.py                     # Arbol: recomienda películas según tiempo disponible y género 
```

## Estructuras de datos

| Estructura | Estado | Dónde | Uso en el proyecto |
|---|---|---|---|
| **Vector** | ✅ Implementada | `estructuras/vector_peliculas.py` | Catálogo de películas |
| **Matriz** | ✅ Implementada | `estructuras/matriz_asientos.py` | Distribución de asientos de una sala |
| **Lista enlazada simple** | ✅ Implementada | `estructuras/lista_simple_reservas.py` | Reservas activas (inserción por la cabeza, O(1)) |
| **Lista enlazada doble** | ✅ Implementada | `estructuras/lista_doble_historial.py` | Historial de reservas, recorrible en ambos sentidos |
| **Pila** | ✅ Implementada  | `estructuras/pila_operaciones.py` | Registro de las últimas operaciones (agregar, reservar, cancelar), con opción de deshacer la última acción |
| **Cola** | ✅ Implementada  | `estructuras/cola_espera.py` | Fila de espera FIFO para reservar, simulando alta demanda: los clientes se atienden en el mismo orden en que llegaron |
| **Árbol (BST)** | ✅ Implementada  | `estructuras/arbol_reservas.py` | Recomendación de peliculas en cartelera según el tiempo y los gustos del cliente |

*(Grafos: descartado por decisión del equipo.)*

## Funcionalidades del menú

1. Agregar película
2. Mostrar películas
3. Buscar película
4. Actualizar película
5. Eliminar película
6. Reservar asiento
7. Ver reservas
8. Cancelar reserva
9. Ver historial de reservas canceladas
10. Ver últimas operaciones
11. Deshacer última operación
12. Recomendar película
13. Ver árbol de recomendación
14. Salir

## Reparto de trabajo

| Integrante | A cargo de |
|---|---|
| Juan José | Estructura base del proyecto, `agregar_pelicula`, `mostrar_peliculas`, `reservar` |
| Juan Sebastian | `buscar_pelicula`, `mostrar_reservas`, `cancelar_reserva` |
| Nicolle | `actualizar_pelicula`, `eliminar_pelicula`, `mostrar_historial` |
