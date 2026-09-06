class VectorPeliculas:
    def __init__(self):
        self.catalogo = [
            {"titulo": "El Despertar de la Fuerza", "genero": "Ciencia Ficción", "duracion": "135 min"},
            {"titulo": "Misión Imposible", "genero": "Acción", "duracion": "147 min"},
            {"titulo": "Intensamente 2", "genero": "Animación", "duracion": "96 min"}
        ]

    def obtener_todas(self):
        return self.catalogo

    def agregar(self, pelicula: dict):
        self.catalogo.append(pelicula)
        return True

    def eliminar(self, titulo: str):
        for i, p in enumerate(self.catalogo):
            if p["titulo"].lower() == titulo.lower():
                self.catalogo.pop(i)
                return True
        return False
