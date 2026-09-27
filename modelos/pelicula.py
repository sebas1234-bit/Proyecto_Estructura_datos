# ============================================================
# CLASE PELICULA
# ============================================================

class Pelicula:

    def __init__(self, id_pelicula, titulo, genero, duracion):
        self.id_pelicula = id_pelicula
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion

    def mostrar_informacion(self):
        print(f"ID: {self.id_pelicula}")
        print(f"Título: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"Duración: {self.duracion} minutos")