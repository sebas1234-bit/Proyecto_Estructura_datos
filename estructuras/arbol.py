# ============================================================
# ÁRBOL BINARIO
# ============================================================
#
# ¿QUÉ ES UN ÁRBOL BINARIO?
#   Estructura jerárquica donde cada nodo tiene como máximo DOS
#   hijos: uno a la izquierda (izq) y otro a la derecha (der).
#
# CÓMO SE USA EN ESTE PROYECTO (árbol de decisión)
#   Cada nodo interno es una pregunta de sí / no:
#       izquierda (izq)  = respuesta SÍ
#       derecha   (der)  = respuesta NO
#   Cada hoja (nodo sin hijos) guarda el resultado: la lista de
#   películas recomendadas. Bajar desde la raíz hasta una hoja
#   equivale a aplicar filtros, uno por nivel.
#
# TERMINOLOGÍA
#   Raíz:    primer nodo del árbol.
#   Hoja:    nodo sin hijos.
#   Altura:  cantidad de ramas del camino más largo raíz -> hoja.
#
# Esta clase es genérica: no conoce películas. Quien construye el
# árbol (recomendador.py) decide qué preguntas y resultados lleva.
# ============================================================


class NodoArbol:

    def __init__(self, info, resultado=None):
        # info: texto del nodo (la pregunta, o el mensaje de una hoja).
        self.info = info

        # Hijos: None significa que no hay hijo en ese lado.
        self.izq = None
        self.der = None

        # resultado: solo lo usan las hojas (lista de películas).
        self.resultado = resultado

    def es_hoja(self):
        # Una hoja no tiene hijo izquierdo ni derecho.
        return self.izq is None and self.der is None


class Arbol:

    def __init__(self, raiz):
        self.raiz = raiz

    # --------------------------------------------------------
    # Recorrido en PREORDEN: nodo -> izquierda -> derecha.
    # Dibuja el árbol completo con sangría por nivel.
    # Complejidad: O(n), cada nodo se visita una sola vez.
    # --------------------------------------------------------
    def mostrar(self, describir_hoja=None):

        # describir_hoja permite que quien use el árbol decida cómo
        # se imprime un resultado, sin que el árbol conozca su tipo.
        if describir_hoja is None:
            describir_hoja = lambda r: f"{len(r)} resultado(s)"

        self._mostrar(self.raiz, "", 0, describir_hoja)

    def _mostrar(self, nodo, rama, nivel, describir_hoja):

        # Caso base de la recursión: no hay nodo, no se hace nada.
        if nodo is None:
            return

        sangria = "    " * nivel
        prefijo = f"({rama}) " if rama != "" else ""

        if nodo.es_hoja():
            print(f"{sangria}{prefijo}{nodo.info}: [{describir_hoja(nodo.resultado)}]")

        else:
            print(f"{sangria}{prefijo}{nodo.info}")

        # Primero la rama izquierda (Sí) y luego la derecha (No).
        self._mostrar(nodo.izq, "Sí", nivel + 1, describir_hoja)
        self._mostrar(nodo.der, "No", nivel + 1, describir_hoja)

    # --------------------------------------------------------
    # Altura: una hoja vale 0; un nodo interno vale 1 + la mayor
    # de las alturas de sus dos hijos.
    # --------------------------------------------------------
    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):

        if nodo is None or nodo.es_hoja():
            return 0

        altura_izq = self._altura(nodo.izq)
        altura_der = self._altura(nodo.der)

        if altura_izq > altura_der:
            return 1 + altura_izq

        return 1 + altura_der

    # --------------------------------------------------------
    # Cantidad de hojas = cantidad de resultados distintos a los
    # que se puede llegar tomando decisiones.
    # --------------------------------------------------------
    def contar_hojas(self):
        return self._contar_hojas(self.raiz)

    def _contar_hojas(self, nodo):

        if nodo is None:
            return 0

        if nodo.es_hoja():
            return 1

        return self._contar_hojas(nodo.izq) + self._contar_hojas(nodo.der)