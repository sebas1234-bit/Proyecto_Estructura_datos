# ============================================================
# CLASE PELICULA
# ============================================================

class Pelicula:

    def __init__(self, id_pelicula, titulo, genero, duracion, es_preestreno=False, cupo_maximo=30):
        # Campos originales de tu clase
        self.id_pelicula = id_pelicula
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion

        # Nuevos campos para la lógica del Preestreno y la Cola (FIFO)
        self.es_preestreno = es_preestreno
        self.cupo_maximo = cupo_maximo
        self.reservas_actuales = 0

    def tiene_cupo(self):
        """Verifica si la película aún tiene cupos disponibles."""
        return self.reservas_actuales < self.cupo_maximo

    def mostrar_informacion(self):
        """Muestra los datos básicos y los cupos si es un preestreno."""
        tipo = " [PREESTRENO EXCLUSIVO]" if self.es_preestreno else ""
        print(f"ID: {self.id_pelicula}{tipo}")
        print(f"Título: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"Duración: {self.duracion} minutos")

        # Muestra la disponibilidad de cupos solo si es preestreno
        if self.es_preestreno:
            cupos_disponibles = self.cupo_maximo - self.reservas_actuales
            print(f"Cupos disponibles: {cupos_disponibles}/{self.cupo_maximo}")
