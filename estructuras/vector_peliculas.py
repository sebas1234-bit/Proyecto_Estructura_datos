# ============================================================
# VECTOR DE PELICULAS
# ============================================================

class VectorPeliculas:

    def __init__(self):
        self.peliculas = []

    def agregar(self, pelicula):
        self.peliculas.append(pelicula)

    def obtener_todas(self):
        return self.peliculas

    def buscar_por_id(self, id_pelicula):

        for pelicula in self.peliculas:

            if pelicula.id_pelicula == id_pelicula:
                return pelicula

        return None

    def eliminar_por_id(self, id_pelicula):

        for i in range(len(self.peliculas)):

            if self.peliculas[i].id_pelicula == id_pelicula:
                self.peliculas.pop(i)
                return True

        return False