# ============================================================
# RECOMENDADOR DE PELÍCULAS
# Construye el árbol binario de decisión con el catálogo actual.
# ============================================================
#
# ESTRUCTURA DEL ÁRBOL GENERADO  (izquierda = Sí, derecha = No)
#
#                  ¿Tienes menos de 100 minutos?
#                   /                          \
#                 Sí                            No
#                 /                              \
#     ¿Quieres ver Animación?          ¿Quieres ver Acción?
#        /            \                    /            \
#      Sí              No                Sí              No
#   [películas]   ¿Quieres ver Acción?  [películas]   ...
#                      ...
#
#   Nivel 1: el tiempo disponible separa películas cortas (izq)
#            de largas (der).
#   Nivel 2 en adelante: una pregunta por cada género presente.
#            "Sí" lleva a las películas de ese género; "No" pasa al
#            siguiente género. Si se rechazan todos, la última hoja
#            muestra todas las películas del rango.
#
# DECISIONES DE DISEÑO
#   - El árbol se construye desde los datos, no está escrito a mano:
#     al agregar o eliminar películas, el árbol se ajusta solo.
#   - Si un género es el único del rango, no se pregunta.
#   - Si un lado no tiene películas, su hoja avisa que no hay.
# ============================================================

from estructuras.arbol import NodoArbol, Arbol

# Umbral en minutos que separa "corta" de "larga". Está en un solo
# lugar: cambiarlo no obliga a buscar números sueltos por el código.
UMBRAL_MINUTOS = 100


def _hoja(mensaje, peliculas):
    """Crea una hoja: un nodo sin hijos que guarda el resultado."""
    return NodoArbol(mensaje, resultado=peliculas)


def _generos_distintos(grupo):
    """Géneros sin repetir, ignorando mayúsculas y espacios."""

    generos = []

    for pelicula in grupo:
        genero = pelicula.genero.strip().lower()

        if genero not in generos:
            generos.append(genero)

    return generos


def _pregunta_genero(grupo, generos, posicion):
    """Nodo con la pregunta del género `posicion` y sus dos ramas."""

    genero = generos[posicion]

    coincidencias = [
        p for p in grupo if p.genero.strip().lower() == genero
    ]

    nodo = NodoArbol(f"¿Quieres ver {genero.capitalize()}?")

    # Izquierda (Sí): películas de ese género.
    nodo.izq = _hoja(f"Películas de {genero.capitalize()}", coincidencias)

    # Derecha (No): se pregunta por el siguiente género (recursión).
    # Si ya no quedan géneros, todos fueron rechazados y se ofrecen
    # todas las películas del rango.
    if posicion == len(generos) - 1:
        nodo.der = _hoja("Ningún género elegido, estas son todas las de este rango", grupo)

    else:
        nodo.der = _pregunta_genero(grupo, generos, posicion + 1)

    return nodo


def _subarbol_generos(grupo):
    """Subárbol que filtra por género un grupo ya filtrado por duración."""

    # Caso 1: no hay películas de esta duración.
    if len(grupo) == 0:
        return _hoja("No hay películas en este rango de duración", [])

    generos = _generos_distintos(grupo)

    # Caso 2: un solo género, no hay nada que elegir.
    if len(generos) == 1:
        return _hoja("Película disponible en este rango", grupo)

    # Caso 3: varios géneros, se arma la cadena de preguntas.
    return _pregunta_genero(grupo, generos, 0)


def construir_arbol_recomendacion(peliculas):
    """Devuelve un Arbol construido con el catálogo recibido."""

    # Primer filtro: separar por duración.
    cortas = [p for p in peliculas if p.duracion < UMBRAL_MINUTOS]
    largas = [p for p in peliculas if p.duracion >= UMBRAL_MINUTOS]

    raiz = NodoArbol(f"¿Tienes menos de {UMBRAL_MINUTOS} minutos?")

    raiz.izq = _subarbol_generos(cortas)   # Sí: tiene poco tiempo
    raiz.der = _subarbol_generos(largas)   # No: tiene tiempo de sobra

    return Arbol(raiz)